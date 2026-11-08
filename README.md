# Mini Feedback Board

A tiny Flask web app for practicing a whole-project code review. Visitors can leave a name and a short comment, then see the feedback on the home page.

This is an intern-level exercise. Read the brief and inspect the whole project before changing anything. The code is intentionally small; the review is about checking behavior and explaining impact, not spotting clever tricks.

## Intended behavior

- The home page shows feedback entries and a form to add one.
- Name and comment are required. Whitespace-only values are invalid.
- Names are at most 40 characters; comments are at most 500 characters.
- Invalid submissions are not saved and show a helpful message.
- New feedback appears first.
- Submitted text is displayed as text, not interpreted as HTML.
- Feedback is kept in memory while the app is running. It is okay for the list to reset after restart.

## Run locally

Requires Python 3.10 or newer.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

## Review exercise

Review the full project against the brief. Try a normal submission, empty fields, whitespace, and values longer than the limits. Also inspect how submitted text gets from the form to the page.

For each finding, write:

1. **Where** it is.
2. **What a user can do** to trigger it.
3. **What happens** and why it matters.
4. **A small improvement** you would suggest.

Start with behavior and user impact. Style preferences can wait. Aim for three clear findings, then we can review your notes together.

