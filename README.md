# Student Assignment Tracker

A beginner-friendly assignment tracker built with **Python, Flask, HTML, pytest, GitHub Actions, and Docker**.

## Five user stories

1. **Add an assignment** — As a student, I want to add an assignment title so that I can remember work I need to complete.  
   *Acceptance criteria:* A non-empty title is added and shown in the assignment list; blank titles are ignored.
2. **View assignments** — As a student, I want to see all my assignments so that I can track my workload.  
   *Acceptance criteria:* The home page lists saved assignments and shows a helpful empty state when there are none.
3. **Mark work complete** — As a student, I want to mark an assignment complete so that I can distinguish finished work from pending work.  
   *Acceptance criteria:* A pending assignment can be marked complete and its completed status is displayed.
4. **Validate input** — As a student, I want blank assignment titles rejected so that my list does not contain empty tasks.  
   *Acceptance criteria:* Whitespace-only titles are not saved.
5. **Check service health** — As a maintainer, I want a health endpoint so that I can quickly check whether the app is responding.  
   *Acceptance criteria:* `GET /health` returns HTTP 200 and JSON `{"status":"ok"}`.

## Implemented feature

The assignment-management feature supports adding, viewing, and completing assignments. The sample stores assignments in memory, so data resets when the application restarts; it is intended as a small practical-task demonstration, not a production database.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Run automated tests

```bash
pytest -q
```

GitHub Actions runs the pytest suite on pushes to `main` and `feature/**`, and on pull requests targeting `main`.

## Run with Docker

```bash
docker build -t student-assignment-tracker .
docker run --rm -p 5000:5000 student-assignment-tracker
```

Open http://localhost:5000.

## Git branching workflow

The feature was developed on `feature/assignment-management`, created from `main`. The feature branch is submitted to `main` through a pull request.

```bash
git checkout main
git pull origin main
git checkout -b feature/assignment-management
# implement and test the feature
git add .
git commit -m "feat: add assignment management"
git push -u origin feature/assignment-management
```
