import math
from functools import wraps

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from models import create_user, get_user_by_email, get_user_by_id

auth_bp = Blueprint("auth", __name__)


@auth_bp.before_app_request
def load_logged_in_user():
    """Load the logged-in user from the session before each request."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)


def login_required(view):
    """Redirect anonymous users to the login page."""
    @wraps(view)
    def wrapped_view(**kwargs):
        """Run the protected view only when a current user is available."""
        if g.user is None:
            flash("Veuillez vous connecter pour accéder à cette page.", "error")
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view


@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    """Handle user registration and validation."""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        username = request.form.get("username", "").strip()
        nom = request.form.get("nom", "").strip() or username
        prenom = request.form.get("prenom", "").strip()
        password = request.form.get("password", "")
        budget_raw = request.form.get("monthly_budget", "0").strip()

        error = None

        # Validate required fields
        if not email or not nom or not password:
            error = "Tous les champs obligatoires doivent être remplis."
        elif "@" not in email:
            error = "L'adresse email est invalide."
        elif len(password) < 4:
            error = "Le mot de passe doit contenir au moins 4 caractères."

        # Validate monthly budget
        monthly_budget = 0.0
        if error is None:
            try:
                monthly_budget = float(budget_raw) if budget_raw else 0.0
                if monthly_budget < 0:
                    error = "Le budget mensuel ne peut pas être négatif."
            except ValueError:
                error = "Le budget mensuel doit être un nombre valide."

        # Check whether the email is already registered
        if error is None and get_user_by_email(email) is not None:
            error = "Cet email est déjà utilisé par un autre compte."

        # Insert the user with a hashed password
        if error is None:
            password_hash = generate_password_hash(password)
            create_user(email, nom, prenom, password_hash, monthly_budget)
            flash("Compte créé avec succès ! Vous pouvez vous connecter.", "success")
            return redirect(url_for("auth.login"))

        flash(error, "error")

    return render_template("register.html")


@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    """Authenticate an existing user and open a session."""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        error = None
        user = get_user_by_email(email)

        if user is None or not check_password_hash(user["password_hash"], password):
            error = "Email ou mot de passe incorrect."

        if error is None:
            session.clear()
            session.permanent = True
            session["user_id"] = user["id"]
            flash("Connexion réussie.", "success")
            return redirect(url_for("expenses.dashboard"))

        flash(error, "error")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    """Clear the current session and log the user out."""
    session.clear()
    flash("Vous avez été déconnecté.", "success")
    return redirect(url_for("auth.login"))
