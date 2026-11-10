import math
import re
from datetime import date, datetime
from auth import login_required
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from models import (
    create_expense, delete_expense, get_all_categories, get_category_by_id,
    get_expense_by_id, get_expense_history_by_month, get_expenses_by_user, get_monthly_category_totals,
    get_monthly_total_by_user, set_user_budget, update_expense,
)

expenses_bp = Blueprint("expenses", __name__)


def validate_expense_form(form):
    """Validate and normalize expense form values before a database write."""
    description = form.get("description", "").strip()
    amount_raw = form.get("amount", "").strip()
    expense_date = form.get("expense_date", "").strip()
    category_raw = form.get("category_id", "").strip()
    if not description or not amount_raw or not expense_date or not category_raw:
        return None, None, None, None, "Tous les champs de la dépense sont obligatoires."
    if len(description) > 150:
        return None, None, None, None, "La description ne doit pas dépasser 150 caractères."
    try:
        amount = float(amount_raw)
        if not 0 < amount < 100000000:
            raise ValueError
    except ValueError:
        return None, None, None, None, "Le montant doit être un nombre supérieur à 0."
    try:
        datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError:
        return None, None, None, None, "La date saisie est invalide."
    try:
        category_id = int(category_raw)
        if get_category_by_id(category_id) is None:
            raise ValueError
    except ValueError:
        return None, None, None, None, "La catégorie sélectionnée est invalide."
    return category_id, description, amount, expense_date, None


def page_data(user_id, edit_expense=None, filters=None):
    """Build shared values used by the expense list and edit templates."""
    filters = filters or {"category": None, "month": "", "q": ""}
    month = date.today().strftime("%Y-%m")
    expenses = get_expenses_by_user(user_id, filters["category"], filters["month"] or None, filters["q"])
    budget = float(g.user["monthly_budget"] or 0)
    spent = float(get_monthly_total_by_user(user_id, month) or 0)
    remaining = budget - spent
    progress = min(100, round((spent / budget) * 100)) if budget > 0 else 0
    history = get_expense_history_by_month(user_id, 22)
    return dict(
        expenses=expenses, categories=get_all_categories(), edit_expense=edit_expense,
        today=date.today().isoformat(), budget=budget, spent=spent,
        remaining=remaining, progress=progress, filters=filters,
        history=history, history_max=max((item["total"] for item in history), default=0),
    )


@expenses_bp.route("/expenses")
@login_required
def list_expenses():
    """Display the current user's expenses and requested filter state."""
    category_raw = request.args.get("category", "").strip()
    category_id = None
    if category_raw:
        try:
            category_id = int(category_raw)
            if get_category_by_id(category_id) is None:
                category_id = None
        except ValueError:
            category_id = None
    month = request.args.get("month", "")
    if month and not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", month):
        month = ""
    filters = {"category": category_id, "month": month, "q": request.args.get("q", "").strip()[:100]}
    return render_template("expenses.html", **page_data(g.user["id"], filters=filters))


@expenses_bp.route("/expenses/add", methods=("POST",))
@login_required
def add_expense():
    """Validate and persist a new expense for the current user."""
    category_id, description, amount, expense_date, error = validate_expense_form(request.form)
    if error:
        flash(error, "error")
    else:
        create_expense(g.user["id"], category_id, description, amount, expense_date)
        flash("Dépense ajoutée avec succès.", "success")
    return redirect(url_for("expenses.list_expenses"))


@expenses_bp.route("/expenses/<int:expense_id>/edit", methods=("GET", "POST"))
@login_required
def edit_expense(expense_id):
    """Display or save changes to an expense owned by the current user."""
    expense = get_expense_by_id(expense_id, g.user["id"])
    if expense is None:
        flash("Dépense introuvable ou accès non autorisé.", "error")
        return redirect(url_for("expenses.list_expenses"))
    if request.method == "POST":
        category_id, description, amount, expense_date, error = validate_expense_form(request.form)
        if error:
            flash(error, "error")
        else:
            update_expense(expense_id, g.user["id"], category_id, description, amount, expense_date)
            flash("Dépense modifiée avec succès.", "success")
            return redirect(url_for("expenses.list_expenses"))
    return render_template("expenses.html", **page_data(g.user["id"], edit_expense=expense))


@expenses_bp.route("/expenses/<int:expense_id>/delete", methods=("POST",))
@login_required
def remove_expense(expense_id):
    """Delete an expense when it belongs to the current user."""
    if delete_expense(expense_id, g.user["id"]):
        flash("Dépense supprimée.", "success")
    else:
        flash("Impossible de supprimer cette dépense.", "error")
    return redirect(url_for("expenses.list_expenses"))


@expenses_bp.route("/dashboard")
@login_required
def dashboard():
    """Display the monthly budget summary and recent expenses."""
    month = request.args.get("month", date.today().strftime("%Y-%m"))
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", month):
        month = date.today().strftime("%Y-%m")
    budget = float(g.user["monthly_budget"] or 0)
    spent = float(get_monthly_total_by_user(g.user["id"], month) or 0)
    categories = get_monthly_category_totals(g.user["id"], month)
    history = get_expense_history_by_month(g.user["id"], 22)
    history_max = max((item["total"] for item in history), default=0)
    recent = get_expenses_by_user(g.user["id"], month=month)[:5]
    return render_template(
        "dashboard.html", month=month, budget=budget, spent=spent,
        remaining=budget-spent,
        progress=min(100, round(spent / budget * 100)) if budget else 0,
        category_totals=categories, recent=recent, history=history, history_max=history_max,
    )


@expenses_bp.route("/budget", methods=("POST",))
@login_required
def update_budget():
    """Validate and save the current user's monthly budget."""
    try:
        amount = float(request.form.get("monthly_budget", ""))
        if amount < 0 or amount >= 100000000:
            raise ValueError
    except ValueError:
        flash("Saisissez un budget valide supérieur ou égal à zéro.", "error")
        return redirect(url_for("expenses.dashboard"))
    set_user_budget(g.user["id"], amount)
    flash("Budget mensuel mis à jour.", "success")
    return redirect(url_for("expenses.dashboard"))
