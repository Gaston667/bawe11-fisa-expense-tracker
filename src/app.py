import os

from flask import Flask
from db import close_db, init_db

def create_app():
    """ Create and configure the flask application."""
    app = Flask(__name__)

    #Get the absolute path of th project
    project_root = os.path.dirname(
        os.path.dirname.os.path.abspath(__file__)
    )

    #Config the database connexion 
    app.config["DATABASE"] = os.path.join(
        project_root,
        "instance",
        "expense_tracker.db"
    )

    # Register the clean up fonction
    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()
    return app


app = create_app()

if __name__ = "__main__"
    app.run(debug=true);
