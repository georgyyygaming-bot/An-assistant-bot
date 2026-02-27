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


