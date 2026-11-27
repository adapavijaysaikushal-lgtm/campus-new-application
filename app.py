from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
assignments = []
_next_id = 1


@app.get("/")
def home():
    return render_template("index.html", assignments=assignments)


@app.post("/assignments")
def add_assignment():
    global _next_id
    title = request.form.get("title", "").strip()
    if title:
        assignments.append({"id": _next_id, "title": title, "completed": False})
        _next_id += 1
    return redirect(url_for("home"))


@app.post("/assignments/<int:assignment_id>/complete")
def complete_assignment(assignment_id):
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            assignment["completed"] = True
            break
    return redirect(url_for("home"))


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
