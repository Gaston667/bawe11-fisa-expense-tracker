from datetime import date

from db import get_db


def create_user(email, nom, prenom, password_hash, monthly_budget=0.0):
    """Create a user and return the generated database identifier."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO users(email, nom, prenom, password_hash, monthly_budget) VALUES (?, ?, ?, ?, ?)",
        (email, nom, prenom, password_hash, monthly_budget),
    )
    db.commit()
    return cursor.lastrowid


def get_user_by_email(email):
    """Return the user associated with an email address, if it exists."""
    return get_db().execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def get_user_by_id(user_id):
    """Return a user by primary key, or None when it does not exist."""
    return get_db().execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()


def get_all_categories():
    """Return the predefined expense categories in their display order."""
    return get_db().execute("SELECT * FROM categories ORDER BY id ASC").fetchall()


def get_category_by_id(category_id):
    """Return one predefined category by identifier."""
    return get_db().execute("SELECT * FROM categories WHERE id = ?", (category_id,)).fetchone()


def get_expenses_by_user(user_id, category_id=None, month=None, search=None):
    """Return user-owned expenses, optionally narrowed by category, month, or text."""
    query = """
        SELECT e.id, e.user_id, e.category_id, e.description, e.amount,
               e.expense_date, e.created_at,
               c.name AS category_name, c.name_en AS category_name_en
        FROM expenses e JOIN categories c ON e.category_id = c.id
        WHERE e.user_id = ?
    """
    params = [user_id]
    if category_id:
        query += " AND e.category_id = ?"
        params.append(category_id)
    if month:
        query += " AND strftime('%Y-%m', e.expense_date) = ?"
        params.append(month)
    if search:
        query += " AND e.description LIKE ? COLLATE NOCASE"
        params.append(f"%{search}%")
    query += " ORDER BY e.expense_date DESC, e.id DESC"
    return get_db().execute(query, params).fetchall()


def get_monthly_total_by_user(user_id, month):
    """Return the total amount spent by one user during a YYYY-MM period."""
    row = get_db().execute(
        "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE user_id = ? AND strftime('%Y-%m', expense_date) = ?",
        (user_id, month),
    ).fetchone()
    return row["total"]


def get_monthly_category_totals(user_id, month):
    """Return the selected month's totals grouped by predefined category."""
    return get_db().execute(
        """
        SELECT c.id, c.name, c.name_en, COALESCE(SUM(e.amount), 0) AS total
        FROM categories c LEFT JOIN expenses e ON e.category_id = c.id
          AND e.user_id = ? AND strftime('%Y-%m', e.expense_date) = ?
        GROUP BY c.id ORDER BY total DESC, c.id
        """,
        (user_id, month),
    ).fetchall()


def get_expense_history_by_month(user_id, months=22):
    """Return the total spending for each of the most recent calendar months."""
    rows = get_db().execute(
        """
        SELECT strftime('%Y-%m', expense_date) AS month, SUM(amount) AS total
        FROM expenses
        WHERE user_id = ?
        GROUP BY strftime('%Y-%m', expense_date)
        """,
        (user_id,),
    ).fetchall()
    totals = {row["month"]: float(row["total"]) for row in rows}

    today = date.today()
    year, month = today.year, today.month
    history = []
    for _ in range(months):
        key = f"{year:04d}-{month:02d}"
        history.append({"month": key, "total": totals.get(key, 0)})
        month -= 1
        if month == 0:
            year -= 1
            month = 12
    history.reverse()
    return history


def create_expense(user_id, category_id, description, amount, expense_date):
    """Create an expense for a user and return its generated identifier."""
    cursor = get_db().execute(
        "INSERT INTO expenses (user_id, category_id, description, amount, expense_date) VALUES (?, ?, ?, ?, ?)",
        (user_id, category_id, description, amount, expense_date),
    )
    get_db().commit()
    return cursor.lastrowid


def get_expense_by_id(expense_id, user_id):
    """Return an expense only when it belongs to the supplied user."""
    return get_db().execute(
        """SELECT e.*, c.name AS category_name, c.name_en AS category_name_en
           FROM expenses e JOIN categories c ON e.category_id = c.id
           WHERE e.id = ? AND e.user_id = ?""",
        (expense_id, user_id),
    ).fetchone()


def update_expense(expense_id, user_id, category_id, description, amount, expense_date):
    """Update a user-owned expense and report whether a row was changed."""
    cursor = get_db().execute(
        """UPDATE expenses SET category_id = ?, description = ?, amount = ?, expense_date = ?
           WHERE id = ? AND user_id = ?""",
        (category_id, description, amount, expense_date, expense_id, user_id),
    )
    get_db().commit()
    return cursor.rowcount > 0


def delete_expense(expense_id, user_id):
    """Delete a user-owned expense and report whether a row was removed."""
    cursor = get_db().execute(
        "DELETE FROM expenses WHERE id = ? AND user_id = ?",
        (expense_id, user_id),
    )
    get_db().commit()
    return cursor.rowcount > 0


def set_user_budget(user_id, amount):
    """Store a new monthly budget for the supplied user."""
    cursor = get_db().execute("UPDATE users SET monthly_budget = ? WHERE id = ?", (amount, user_id))
    get_db().commit()
    return cursor.rowcount > 0
