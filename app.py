from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
feedback_entries = []


@app.get("/")
def home():
    return render_template("home.html", feedback_entries=feedback_entries)


@app.post("/feedback")
def add_feedback():
    name = request.form.get("name", "")
    message = request.form.get("message", "")
    feedback_entries.append({"name": name, "message": message})
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

