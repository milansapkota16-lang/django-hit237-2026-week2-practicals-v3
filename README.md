# django-hit237-2026-week2-practicals-v3
HIT237 Week 2 practical sessions

Installation and development
----------------------------

1. Create a virtual environment (recommended name: `.venv`):

```powershell
python -m venv .venv
```

2. Install dependencies (from the venv):

```powershell
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt
```

3. Initialize the database:

```powershell
.venv\Scripts\python manage.py migrate
```

4. Run the development server:

```powershell
.venv\Scripts\python manage.py runserver
```

Notes:
- If `requirements.txt` is missing you can install Django directly: `.venv\\Scripts\\python -m pip install Django`.
- The project package is named `project_blog` and lives in the repository root.

