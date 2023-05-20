# CITS5505-BrewChat

_UWA CITS5505 Project2 (22922504, 22926143) contributing equally_

## Table of contents
* [Purpose of the Web Application](#general-info)
* [Architecture of the web application](#architecture)
* [Technologies](#technologies)
* [Launch](#launch)
* [Test](#test)
* [Source](#source)


## Purpose of the Web Application <a name = "general-info"></a>

BrewChat is a Flask-based chat application designed for coffee lovers. It connects users with a shared passion for coffee, allowing them to engage in conversations, share stories, and explore various coffee topics. The daily matching system pairs users with a random conversation partner each day, fostering diverse interactions. With Eliza, a 24/7 chatbot, users can ask coffee-related questions and receive insightful responses. BrewChat aims to recreate the serendipitous encounters of a coffee shop setting, providing companionship and knowledge exchange for coffee enthusiasts.

## Architecture of the web application<a name = "architecture"></a>

BrewChat is built using HTML, CSS, Flask, AJAX, jQuery, and the SQLAlchemy database framework, with the chat function powered by Socket.IO. Here's an overview of the application's architecture:

- Client-side (Frontend): The client-side of BrewChat encompasses the user interface developed using HTML, CSS, and JavaScript. It provides an intuitive and visually appealing experience to users, allowing them to interact with the application. AJAX and jQuery are utilized for asynchronous requests and dynamic UI updates, enhancing the user experience.

- Server-side (Backend): The server-side of BrewChat is built using the Flask web framework, which handles the server-side logic and serves the application's routes. Flask enables the processing of client requests, performs business logic, and communicates with databases and other services. Flask-SocketIO facilitates real-time bidirectional communication between clients and the server for chat functionality.

- Chatbot (Backend): BrewChat incorporates the Eliza Chatbot as part of the backend functionality. The Eliza Chatbot, implemented using the Natural Language Toolkit (NLTK), enables chat-based conversations with users. It processes user input, performs natural language processing, generates appropriate responses, and communicates with the client-side interface.

- Database: BrewChat utilizes the SQLAlchemy database framework to interact with the SQLite database. The SQLite database stores user information, conversation pairings, and relevant chat logs. SQLAlchemy provides an Object-Relational Mapping (ORM) tool, simplifying database operations within the application

The BrewChat web application combines Flask, SocketIO, and SQLAlchemy for smooth real-time communication in the chat feature. Additionally, the integration of the Eliza chatbot enhances user engagement, replicating the serendipity of coffee shop encounters.

## Technologies <a name = "technologies"></a>
- Python version: 3.8.2 or 
- Flask version: 2.3.1
- Werkzeug version: 2.3.1
- SQLAlchemy version: 2.0.12

## Launch <a name = "launch"></a>

### Create an environment

Create a project folder and a venv folder within:

```bash
python3 -m venv venv
```

### Activate the environment

Before you work on your project, activate the corresponding environment:

macOS User:

```bash
. venv/bin/activate
```

Microsoft Windows user:

```bash
. venv\Scripts\activate
```

### Install all requirements

```bash
pip3 install -r requirements.txt
```

### Database setting

Initialize database

```bash
flask db init
flask db migrate -m "build tables"
flask db upgrade
flask shell
```

### Run Web App

```bash
flask --app brewchat.py --debug run
```
if not work, try `export FLASK_APP=brewchat.py`

### Others

Get you all requirements (every time when you install new module)

```bash
python3 -m pip freeze > requirements.txt
```

Check file tree for a Flask project with a basic structure:

```bash
tree -I 'venv|__pycache__|pytest_cache' > tree.txt
```

## Unit test <a name = "test"></a>

## Commit log

## Source <a name = "source"></a>
This app is inspired by the Flask Mega-Tutorial  by [@Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


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

## Git Version

To push a new branch to a remote repository in Git, you can follow these steps:

First, create a new branch locally using the following command:

```
git checkout -b <new-branch-name>
```

Make some changes to the new branch and commit them:

```
git add .
git commit -m "commit message"
```

Push the new branch to the remote repository:

```
git push -u <remote-name> <new-branch-name>
```

Note: Replace <remote-name> with the name of your remote repository, for example, origin. Replace <new-branch-name> with the name of the new branch you created.

After pushing the branch, you should be able to see it in the remote repository on the website or by running the following command:

```
git branch -r
```

That's it! Your new branch has been pushed to the remote repository.

Template

```md
What I did:
-   [ ]

Unsolved problems:
-   [ ]

Next steps:
-   [ ]
```

## Submission and Presentation Instructions

Discussion when the project complete 75% or a week before the presentation

# CITS5505-BrewChat-Project-README

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

## Run Web App

A minimal Flask application looks something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

```bash
flask --app brewchat.py --debug run
```
if not work, try `export FLASK_APP=brewchat.py`

## Others

Get you all requirements (every time when you install new module)

```bash
python3 -m pip freeze > requirements.txt
```

Check file tree for a Flask project with a basic structure:

```bash
tree -I 'venv|__pycache__|pytest_cache' > tree.txt
```

## Database setting

Initialize database

```bash
flask db init
flask db migrate -m "build tables"
flask db upgrade
flask shell
```

Play with DB
Type `python` in Terminal to get into python playground

```python
>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')
>>> u
<User susan>
```

Activate shell

```
(venv) huixinyang@Damons-MacBook-Air CITS5505-BrewChat % flask shell
Python 3.9.6 (default, Oct 18 2022, 12:41:40) 
[Clang 14.0.0 (clang-1400.0.29.202)] on darwin
App: app
Instance: /Users/huixinyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/ObsidianSync/000 UWA/UWA Materials/2023s1/CITS5505/CITS5505-BrewChat/instance
>>> app
<Flask 'app'>
>>> db
<SQLAlchemy sqlite:////Users/huixinyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/ObsidianSync/000 UWA/UWA Materials/2023s1/CITS5505/CITS5505-BrewChat/app.db>
>>> User
<class 'app.models.User'>
>>> Chat
<class 'app.models.Chat'>
>>> 
```