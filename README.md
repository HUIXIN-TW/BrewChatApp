# CITS5505-WebChat

_UWA CITS5505 Project2 (22922504, 22926143)_

## Create an environment

Refer to: https://flask.palletsprojects.com/en/2.2.x/installation/#create-an-environment
Create a project folder and a venv folder within:

```bash
% python3 -m venv venv
```

## Activate the environment

Before you work on your project, activate the corresponding environment:

```bash
% . venv/bin/activate
```

## Install Flask

```bash
% pip install Flask
```

A minimal Flask application looks something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
