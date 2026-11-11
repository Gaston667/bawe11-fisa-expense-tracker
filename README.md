# Expense Tracker

Application web de suivi de dépenses personnelles développée avec Python, Flask, SQLite, HTML, CSS et JavaScript.

## Lancement sur une VM Linux vierge

Python 3.10+ est nécessaire. SQLite est inclus dans Python.

### 1. Installer Python si nécessaire

```bash
sudo apt update
```

```bash
sudo apt install -y python3 python3-venv python3-pip
```

### 2. Extraire l'archive et entrer dans le projet

```bash
tar -xzf diallo_algassimou_pellel_flask.tar.gz
```

```bash
cd diallo_algassimou_pellel_flask
```

### 3. Installer Flask

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

### 4. Lancer le site

```bash
python src/app.py
```

Ouvrir ensuite `http://127.0.0.1:5000`.

Au premier démarrage, la base SQLite (`instance/expense_tracker.db`), ses trois tables et les catégories initiales sont créées automatiquement à partir du fichier `src/schema.sql`.

### Données de démonstration, optionnel

Arrêter le serveur avec `Ctrl + C`, puis exécuter :

```bash
python src/seed_demo_data.py
```

Relancer ensuite le serveur. Compte créé : `alga.diallo@test.fr` / `test@1234`.

## Windows

Exécuter chaque commande séparément, dans cet ordre :

```powershell
py -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
python -m pip install -r requirements.txt
```

```powershell
python src\app.py
```
