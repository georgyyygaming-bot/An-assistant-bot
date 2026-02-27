# Bot Backend (Flask)

Simple Flask server that proxies messages to the DeepSeek API.

## Setup

```bash
python -m venv venv
. venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Create a `.env` file containing:

```
DEEPSEEK_API_KEY=sk-...
```

## Running

```bash
flask run   # or python app.py
```

The server listens on port 5000 by default. POST JSON to `/chat`:

```json
{ "message": "Hello" }
```

Response:

```json
{ "reply": "..." }
```

### Running tests

Install dev dependencies and run pytest:

```bash
pip install -r requirements.txt
pytest
```

## Notes

- Adapt system prompt or context as needed.

## Publishing to GitHub

This project can be pushed to a public or private repository. A simple example:

```bash
cd "c:\Users\Georgyyyy\Documents\backend for bot"
git init
git add .
git commit -m "Initial bot backend"
# optionally add remote
# git remote add origin https://github.com/<username>/<repo>.git
# git push -u origin main
```

Include the `assistant_bot.html` file in the same repo or a separate `frontend` directory. GitHub Pages or any static host can serve the HTML, while the Flask app runs on a server (Heroku, VPS, etc.).

You may also want to update `.gitignore` to exclude `.env` and virtual environments (already handled).

d.
- This is intended as a minimal starting point.
