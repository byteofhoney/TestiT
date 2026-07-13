# Contributing to TesiT

TesiT is a small open source project. If you found a bug, have a feature idea or want to fix something, you are welcome here.

This is not a big open source org with a committee. If your change makes the project better and the code is clean, it will get merged.

---

## Before you start

Check the open issues first. If something is already being worked on, leave a comment rather than opening a duplicate. If you have a new idea, open an issue before writing code so we can agree it is worth building. 

---

## How to run it locally

Fork the repo, then clone your fork:

```bash
git clone https://github.com/byteofhoney/testit.git
cd testit
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac or Linux
pip install -r backend/requirements.txt
```

Create a `.env` file inside the `backend/` folder:

MONGO_URI=mongodb_atlas_connection_string
SECRET_KEY=enter-a-random-string

Run the backend:

```bash
cd backend
python app.py
```

Open `frontend/index.html` or `frontend/dashboard.html` directly in your browser.
No build step, no npm, no bundler.

---

## Branch naming

Branch off `main` and use this format:

feat/short-description
fix/short-description
docs/short-description

-> Examples:
feat/api-key-auth
fix/duplicate-events
docs/update-readme

---

## Making a pull request

- Keep the PR focused on one thing. A PR that fixes a bug and adds a feature is two PRs.
- Write a short description of what you changed and why.
- If your PR closes an issue, add `Closes #issue number` in the description. <-
- Do not send a PR with unrelated file changes or formatting rewrites.

---

## Code style

Follow what is already there. The backend is plain Flask with no extra layers.
The frontend is plain html, css and JavaScript with no frameworks. Keep it
that way unless there is a strong reason not to.

---

## Questions

Open an issue and tag it `question`. 