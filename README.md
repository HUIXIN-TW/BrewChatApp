# CITS5505-JustChat-Instruction

_UWA CITS5505 Project2 (22922504, 22926143) contributing equally_

## Introduction

The app should allow users to create an account, and begin a chat (or game, or session etc) with someone specific (or someone random, or some bot service etc). They should be able to access some amount of the history of their chats, and the application should provide some kind of unique service or context that is not available in generic applications like Facebook Messenger. Examples might include tutoring, dating, gaming, counselling, etc. The application should be written using HTML, CSS, Flask, AJAX, JQuery, and Bootstrap. (Any additional technologies not mentioned in lectures will require special approval from the unit coordinator).

The web application should be styled to be interesting and engaging for a user in the selected context. It should offer several views including:

An opening view, describing the context and purpose of the application, and allowing the user to create an account or log in.
A chat view, allowing the user to interact with the application or other users via text (or similar).
A search view, allowing the user to review their history and previous interactions..

### Functionalities

-   [ ] Register/ Log in/ Log out/ Account Information / Change Password
-   [ ] Opening View
-   [ ] Chat View
-   [ ] Search View
-   [ ] Set up Final GitHub README
    -   [ ] the purpose of the web application, explaining the its design and use.
    -   [ ] the architecture of the web application. (front, back, API, db, deployment)
    -   [ ] describe how to launch the web application.
    -   [ ] describe some unit tests for the web application, and how to run them.
    -   [ ] Include commit logs, showing contributions and review from both contributing students

### Criteria

[Marking Criterion](https://teaching.csse.uwa.edu.au/units/CITS3403/projects/Project2Criterion.pdf) is available

#### Front-end

Criteria: Front-end (50%)

-   [ ] The web application must be functional so that the user can easily access the application.
-   [ ] The webpage must be implemented using HTML5, CSS and Javascript (or a subset thereof).
-   [ ] All resources used (including pictures, javascript libraries, css) must be full referenced.
-   [ ] The website must use HTML5, and CSS. The HTML and CSS must pass this validator.
-   [ ] The website must work on Chrome, Firefox and Microsoft Edge, and render well on mobile devices.
-   [ ] The website should have at least three pages/views:
-   [ ] one explaining the context to users, and allowing account creation or log in;
-   [ ] one presenting the interactive chat;
-   [ ] one page allowing a user to search their previous interactions.
-   [ ] There must be a consistent style (via css file) for all pages yet each page should be easily identifiable.

#### Back-end

Criteria: Backend functionality (50%)
The second part of the project criteria is the back end functionality of web application. The web application should be implmented using Flask (any additional libraries/modules require unit coordinator approval), and provide at least the following functionality:

-   [ ] A user account and tracking feature.
-   [ ] A method to store interactions and results.
-   [ ] A method to search previous interactions.

## Submission and Presentation Instructions

Discussion when the project complete 75% or a week before the presentation

# CITS5505-JustChat-Project-README

## Create an environment

Refer to: https://flask.palletsprojects.com/en/2.2.x/installation/#create-an-environment

Create a project folder and a venv folder within:

```bash
python3 -m venv venv
```

## Activate the environment

Before you work on your project, activate the corresponding environment:

```bash
. venv/bin/activate
```

## Install all requirements

```bash
pip3 install -r requirements.txt
```

A minimal Flask application looks something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

```bash
pip3 install -r requirements.txt
```

```bash
flask --app app.py --debug run
```

Get you all requirements (every time when you install new module)

```bash
python3 -m pip freeze > requirements.txt
```

Check file tree for a Flask project with a basic structure:

```bash
tree -I 'venv|__pycache__|pytest_cache' > tree.txt
```
