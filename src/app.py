import os
from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, url_for

from auth import auth_bp
from db import close_db, init_db
from expenses import expenses_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Get the absolute path of the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    instance_path = os.path.join(project_root, "instance")

    # Ensure the instance directory exists for the SQLite database
    os.makedirs(instance_path, exist_ok=True)

    # Configure session secret key and database path
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "dev-secret-key-expense-tracker"
    )
    app.config["DATABASE"] = os.environ.get("EXPENSE_TRACKER_DATABASE", os.path.join(instance_path, "expense_tracker.db"))
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)
    app.config["SESSION_REFRESH_EACH_REQUEST"] = True

    # Register database cleanup at the end of each request
    app.teardown_appcontext(close_db)

    # Initialize database tables and default categories
    with app.app_context():
        init_db()

    # Register authentication and expense blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)

    @app.route("/")
    def index():
        """Redirect visitors to the dashboard entry point."""
        return redirect(url_for("expenses.dashboard"))

    @app.route("/contact", methods=("GET", "POST"))
    def contact():
        """Display contact information and validate contact form fields."""
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            subject = request.form.get("subject", "").strip()
            message = request.form.get("message", "").strip()

            if not name or not email or not subject or not message:
                flash("Veuillez remplir tous les champs du formulaire de contact.", "error")
            elif "@" not in email:
                flash("Veuillez saisir une adresse email valide.", "error")
            else:
                flash("Le formulaire n'est pas relié à une messagerie. Utilisez l'adresse email affichée ci-dessous.", "error")
                return redirect(url_for("contact"))

        return render_template("contact.html")

    @app.errorhandler(404)
    def page_not_found(error):
        """Display a clear page when the requested route does not exist."""
        return render_template("404.html"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        debug=os.environ.get("FLASK_DEBUG") == "1",
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
    )
