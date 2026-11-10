"""Populate the local demo account with expenses spread across 22 months.

Run from the project root with: python src/seed_demo_data.py
"""

import hashlib
import os
import sqlite3
from datetime import date
from pathlib import Path


DEMO_EMAIL = "alga.diallo@test.fr"
DEMO_PASSWORD = "test@1234"


def month_before(year, month, offset):
    """Return the year and month located a number of months in the past."""
    month -= offset
    while month <= 0:
        year -= 1
        month += 12
    return year, month


def seed():
    """Create or refresh the demo account and its 22-month expense history."""
    project_root = Path(__file__).resolve().parent.parent
    database_path = os.environ.get("EXPENSE_TRACKER_DATABASE", project_root / "instance" / "expense_tracker.db")
    db = sqlite3.connect(database_path)
    db.row_factory = sqlite3.Row
    user = db.execute("SELECT id FROM users WHERE email = ?", (DEMO_EMAIL,)).fetchone()
    if user is None:
        salt = "expense-tracker-demo"
        digest = hashlib.pbkdf2_hmac("sha256", DEMO_PASSWORD.encode(), salt.encode(), 1_000_000).hex()
        password_hash = f"pbkdf2:sha256:1000000${salt}${digest}"
        cursor = db.execute(
            """INSERT INTO users (email, nom, prenom, password_hash, monthly_budget)
               VALUES (?, ?, ?, ?, ?)""",
            (DEMO_EMAIL, "Demo", "Expense Tracker", password_hash, 850),
        )
        user_id = cursor.lastrowid
    else:
        user_id = user["id"]
        db.execute("UPDATE users SET monthly_budget = ? WHERE id = ?", (850, user_id))

    db.execute("DELETE FROM expenses WHERE user_id = ?", (user_id,))
    today = date.today()
    entries = [
        (1, "Courses", 96.50, 5), (3, "Transport", 42.00, 12),
        (6, "Abonnement", 14.99, 20), (4, "Sortie", 38.00, 25),
    ]
    for offset in range(22):
        year, month = month_before(today.year, today.month, offset)
        for index, (category_id, label, base_amount, day) in enumerate(entries):
            amount = base_amount + ((offset * 13 + index * 7) % 45)
            db.execute(
                """INSERT INTO expenses (user_id, category_id, description, amount, expense_date)
                   VALUES (?, ?, ?, ?, ?)""",
                (user_id, category_id, f"{label} {month:02d}/{year}", amount, f"{year:04d}-{month:02d}-{day:02d}"),
            )
    db.commit()
    db.close()
    print("Demo data added for 22 months.")


if __name__ == "__main__":
    seed()
