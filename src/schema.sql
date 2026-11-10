-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Store application users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) UNIQUE NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    password_hash TEXT NOT NULL,
    monthly_budget REAL NOT NULL DEFAULT 0 CHECK (monthly_budget >= 0)
);

-- Store predefined expense categories
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    name_en VARCHAR(50) NOT NULL
);

-- Store user expenses
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    description VARCHAR(150) NOT NULL,
    amount REAL NOT NULL CHECK (amount > 0),
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT
);

-- Insert default predefined categories
INSERT OR IGNORE INTO categories (id, name, name_en) VALUES
    (1, 'Alimentation', 'Food'),
    (2, 'Logement', 'Housing'),
    (3, 'Transport', 'Transport'),
    (4, 'Loisirs', 'Leisure'),
    (5, 'Santé', 'Health'),
    (6, 'Abonnements', 'Subscriptions'),
    (7, 'Autre', 'Other');
