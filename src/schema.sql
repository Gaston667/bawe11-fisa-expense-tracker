-- Enable foreign key
PRAGMA Foreign_key  = ON;

-- Store application user
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email UNIQUE VARCHAR(100) NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    password_hash TEXT NOT NULL,
    monthly_budget REAL NOT NULL DEFAULT 0
);