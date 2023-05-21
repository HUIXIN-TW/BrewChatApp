# CITS5505-BrewChat

_UWA CITS5505 Project2 (22922504, 22926143) contributing equally_

## Table of contents
* [Purpose](#general-info)
* [Architecture](#architecture)
* [Technologies](#technologies)
* [Launch](#launch)
* [Test](#test)
* [Commit Log](#commit)
* [Source](#source)


## Purpose of the Web Application <a name = "general-info"></a>

BrewChat is a Flask-based chat application designed for coffee lovers. It connects users with a shared passion for coffee, allowing them to engage in conversations, share stories, and explore various coffee topics. The daily matching system pairs users with a random conversation partner each day, fostering diverse interactions. With Eliza, a 24/7 chatbot, users can ask coffee-related questions and receive insightful responses. BrewChat aims to recreate the serendipitous encounters of a coffee shop setting, providing companionship and knowledge exchange for coffee enthusiasts.

## Architecture of the web application<a name = "architecture"></a>

BrewChat is built using HTML, CSS, Flask, AJAX, jQuery, and the SQLAlchemy database framework, with the chat function powered by Socket.IO. Here's an overview of the application's architecture:

- Client-side (Frontend): The client-side of BrewChat encompasses the user interface developed using HTML, CSS, and JavaScript. It provides an intuitive and visually appealing experience to users, allowing them to interact with the application. AJAX and jQuery are utilized for asynchronous requests and dynamic UI updates, enhancing the user experience.

- Server-side (Backend): The server-side of BrewChat is built using the Flask web framework, which handles the server-side logic and serves the application's routes. Flask enables the processing of client requests, performs business logic, and communicates with databases and other services. Flask-SocketIO facilitates real-time bidirectional communication between clients and the server for chat functionality.

- Chatbot (Backend): BrewChat incorporates the Eliza Chatbot as part of the backend functionality. The Eliza Chatbot, implemented using the Natural Language Toolkit (NLTK), enables chat-based conversations with users. It processes user input, performs natural language processing, generates appropriate responses, and communicates with the client-side interface.

- Database: BrewChat utilizes the SQLAlchemy database framework to interact with the SQLite database. The SQLite database stores user information, conversation pairings, and relevant chat logs. SQLAlchemy provides an Object-Relational Mapping (ORM) tool, simplifying database operations within the application.

The BrewChat web application combines Flask, SocketIO, and SQLAlchemy for smooth real-time communication in the chat feature. Additionally, the integration of the Eliza chatbot enhances user engagement, replicating the serendipity of coffee shop encounters.

## Technologies <a name = "technologies"></a>
- Python version: 3.8.2 or 3.9.6
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

- macOS user:

```bash
. venv/bin/activate
```

- Microsoft Windows user:

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
```

### Run Web App

```bash
flask --app brewchat.py --debug run
```
If not work, try `export FLASK_APP=brewchat.py`

## Test <a name = "test"></a>
The BrewChat application includes a suite of unit tests to ensure the correctness and functionality of the various components. These tests are designed to cover different aspects of the application and help identify any potential issues or bugs.
The application also includes a suite of Selenium tests to verify the end-to-end functionality and user experience. These tests simulate user interactions with the application in a browser environment.

### Set up Test

Change to the project directory
```
cd tests
```
### How to run

Run the unit test and selenium tests using the following command
```
python3 -m unittest test_authUser.py
python3 -m unittest test_unauthUser.py
python3 -m unittest test_validate.py
python3 -m unittest test_db.py
python3 test_selenium.py # need to flask run in the background
```
#### Unit Tests

The unit tests in the BrewChat application focus on testing individual components and functionalities in isolation. They help ensure that each component behaves as expected and that the application as a whole functions correctly. These tests cover various scenarios and edge cases to validate the behavior of the code.

Below are a few examples of unit tests implemented for the BrewChat application:

- **Example Unit Test: Login functionality**
    This test suite for testing the login functionality of the BrewChat web application. It includes test cases for validating the login process with different scenarios:

    1. `test_valid_login`: This test case verifies that a user can successfully log in with the correct username and password. It creates a test user, sets their password, performs a login request with the correct credentials, and checks if the login is successful.

    2. `test_invalid_login_wrong_password`: This test case checks the behavior when an incorrect password is provided during the login process. It creates a test user, sets their password, performs a login request with an incorrect password, and verifies that the login fails.

    3. `test_invalid_login_nonexisting_user`: This test case validates the behavior when a non-existing user attempts to log in. It performs a login request with incorrect credentials and checks that the login fails.

    These tests help ensure that the login functionality of the BrewChat application behaves as expected and handles different scenarios correctly.

#### Selenium Tests

The Selenium tests in BrewChat are designed to verify the end-to-end functionality and user experience of the application. These tests simulate user interactions with the application in a browser environment, allowing us to test the application's behavior from a user's perspective. They help identify potential issues related to user workflows, page navigation, form submissions, and more.

Below are a examples of Selenium tests implemented for the BrewChat application:

- **Example Selenium Test: First Time to Use BrewChat**

  This test simulates a user's first visit to BrewChat and performs the following steps:

  1. User visits the register page
  2. User inputs username and password
  3. User clicks the register button
  4. Asserts that the page redirects to the login page
  5. User inputs username and password on the login page
  6. User clicks the login button
  7. Asserts that the page redirects to the index page

  This test verifies the registration and login functionality, ensuring that a user can successfully register, login, and access the main index page.

These tests, combined with the unit tests, help maintain the quality and reliability of the BrewChat application by catching potential issues early in the development process.

## Commit log <a name = "commit"></a>

The following commit logs show contributions and reviews from both contributing students:

Run Author summary
```shell
git log --format='%an' | sort -u
```
HUIXIN / HUIXIN-TW : Hui-Xin Yang 22922504
Yunchuan / remykung : Yun-Chuan Kung 22926143

Review Process:
All pull request must be reviewed by the other student, it helps ensure code quality and fosters collaboration among team members.

```shell
* commit 2eb7f33acc42d177ec4151829c0deb6c26e6e606 (origin/updated-ReadMe-Testing--YunChuan)
| Author: Yunchuan <leisyun@gmail.com>
| Date:   Mon May 22 06:14:01 2023 +0800
| 
|     updated-readme-testing
|   
*   commit 9ed8838d27cde772ad0231e5cf8d0f496d5c3a17 (origin/master, origin/HEAD)
|\  Merge: e1ba53d 1c7b988
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Sun May 21 06:20:05 2023 +0800
| | 
| |     Merge pull request #22 from HUIXIN-TW/overall-review-minor-fix
| |     
| |     minor fix
| | 
| * commit 1c7b98886b30cae37515cbc8397428b94e416238 (HEAD -> overall-review-minor-fix, origin/overall-review-minor-fix, test-page-function)
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Sun May 21 06:17:20 2023 +0800
|   
|       minor fix
|   
*   commit e1ba53d662ff18752b1c5851edfbe30580865170
|\  Merge: d7c6c57 bc65c65
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Sun May 21 05:10:10 2023 +0800
| | 
| |     Merge pull request #21 from HUIXIN-TW/Check-all-pages-style-and-comment--YunChuan
| |     
| |     all page style check and comment
| |   
| *   commit bc65c654e9737f08ad3220b4a77c0b60251a3e40 (origin/Check-all-pages-style-and-comment--YunChuan)
| |\  Merge: 22d76b8 d7c6c57
| |/  Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
|/|   Date:   Sun May 21 05:07:57 2023 +0800
| |   
| |       Merge branch 'master' into Check-all-pages-style-and-comment--YunChuan
| |   
* |   commit d7c6c57516c7a345a000c7df0ae5c3f8651492d4
|\ \  Merge: ae8bbdb 58d0124
| | | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | | Date:   Sun May 21 04:56:24 2023 +0800
| | | 
| | |     Merge pull request #18 from HUIXIN-TW/updated-README--YunChuan
| | |     
| | |     updated the layout of readme
| | |   
| * |   commit 58d012473dd8bcac3038af501838341beb199ec4 (origin/updated-README--YunChuan)
| |\ \  Merge: d182e0d ae8bbdb
| |/ /  Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
|/| |   Date:   Sun May 21 04:56:00 2023 +0800
| | |   
| | |       Merge branch 'master' into updated-README--YunChuan
| | |   
* | |   commit ae8bbdbbafeca23fd844a1929dddfff930e527e4
|\ \ \  Merge: ea8040b d7d9b52
| | | | Author: remykung <75251932+remykung@users.noreply.github.com>
| | | | Date:   Sun May 21 04:53:31 2023 +0800
| | | | 
| | | |     Merge pull request #20 from HUIXIN-TW/test-page-function
| | | |     
| | | |     Test page function
| | | | 
| * | | commit d7d9b527410bb074dd13361783a8d15457ea92b5 (origin/test-page-function)
| | | | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | | | Date:   Sun May 21 04:50:42 2023 +0800
| | | | 
| | | |     update readme
| | | | 
| * | | commit 85ed86d161c624aa4e9d3ee71488e36a2f19cf7d
| | | | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | | | Date:   Sun May 21 04:45:31 2023 +0800
| | | | 
| | | |     test-page-function-selenium
| | | | 
| * | | commit 937cff1a14b1563effa830b3d8eb430e0bea56fe
| | | | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | | | Date:   Sat May 20 23:43:41 2023 +0800
| | | | 
| | | |     test-page-function-unittest
| | | | 
| * | | commit fc1454a29b35b90869195e341e931cabcd626eff
| | | | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | | | Date:   Sat May 20 19:25:29 2023 +0800
| | | | 
| | | |     test-page-function
| | | |   
| | * |   commit d182e0d28656c287150f75d5a19ebc5be3edcf17
| | |\ \  Merge: 1d02e95 58cc6e8
| | | | | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | | | | Date:   Sun May 21 04:55:14 2023 +0800
| | | | | 
| | | | |     Merge pull request #19 from HUIXIN-TW/Update-README.md----typo-fix
| | | | |     
| | | | |     Update README.md -- typo fix
| | | | | 
| | | * | commit 58cc6e87b5273c7d96d2845845b8022c86763d56 (origin/Update-README.md----typo-fix)
| | | | | Author: remykung <75251932+remykung@users.noreply.github.com>
| | | | | Date:   Sun May 21 02:16:53 2023 +0800
| | | | | 
| | | | |     Update README.md -- typo fix
| | | | |     
| | | | |     Update README.md -- typo fix
| | | | | 
| | * | | commit 1d02e957d9388e31eec6965f1405d13e762468ad
| | |/ /  Author: remykung <75251932+remykung@users.noreply.github.com>
| | | |   Date:   Sun May 21 02:15:43 2023 +0800
| | | |   
| | | |       Update README.md -- typo fix
| | | | 
| | | * commit 22d76b8bb1b6bab507f86273d1137a4939442aef
| | |/  Author: Yunchuan <leisyun@gmail.com>
| | |   Date:   Sun May 21 04:58:45 2023 +0800
| | |   
| | |       all page style check and comment
| | | 
| | * commit eb1579cb34a3446c39c77dceb6c45817816fddcb
| |/  Author: Yunchuan <leisyun@gmail.com>
|/|   Date:   Sat May 20 22:28:11 2023 +0800
| |   
| |       updated the layout of readme
| | 
* | commit ea8040b78453d3ecacb2d32d3591f5127cc87211
|\| Merge: f39d085 96343a0
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Sat May 20 13:48:35 2023 +0800
| | 
| |     Merge pull request #17 from HUIXIN-TW/update-routes--huixin
| |     
| |     update routes
| | 
| * commit 96343a00093ed395333d99c35a3b128d2f3d69d7 (origin/update-routes--huixin, update-routes--huixin)
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Sat May 20 13:45:38 2023 +0800
|   
|       update routes
|   
*   commit f39d085bf90e3c0509740b575ad7063161481d89 (master)
|\  Merge: 760ddf9 4412859
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Fri May 19 18:49:35 2023 +0800
| | 
| |     Merge pull request #16 from HUIXIN-TW/chat-eliza-memory-page-style--YunChuan
| |     
| |     style chat, eliza and memory pages, fix search.js
| | 
| * commit 441285985a08b5379d8273a6f595fe266933d90c (origin/chat-eliza-memory-page-style--YunChuan)
|/  Author: Yunchuan <leisyun@gmail.com>
|   Date:   Fri May 19 18:41:43 2023 +0800
|   
|       style chat, eliza and memory pages, fix search.js
|   
*   commit 760ddf9b26db2d486266ad4d1713f4f9b47289d3
|\  Merge: 689222d 1052105
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Fri May 19 03:38:12 2023 +0800
| | 
| |     Merge pull request #15 from HUIXIN-TW/minor-fix-universally
| |     
| |     chech minor bugs
| | 
| * commit 1052105ddf3881e3b21738d8d9d543da5c14209c (origin/minor-fix-universally, minor-fix-universally)
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Fri May 19 03:36:01 2023 +0800
|   
|       chech minor bugs
|   
*   commit 689222d6726a3c6e8fbc691093f55acb997189fe (training-eliza)
|\  Merge: 5c0a830 182dd36
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Fri May 19 02:24:04 2023 +0800
| | 
| |     Merge pull request #14 from HUIXIN-TW/chat-style-sheet-modify--YunChuan
| |     
| |     chat style sheet modify
| | 
| * commit 182dd368debc91ec95ddb7933656537302f86e45 (origin/chat-style-sheet-modify--YunChuan)
| | Author: Yunchuan <leisyun@gmail.com>
| | Date:   Fri May 19 02:15:42 2023 +0800
| | 
| |     chat style sheet modify
| |   
* |   commit 5c0a830deb10c3ae3c36b0a04b5f95b6215b4a5a
|\ \  Merge: bbc47f9 7f50efb
| |/  Author: remykung <75251932+remykung@users.noreply.github.com>
|/|   Date:   Fri May 19 01:59:16 2023 +0800
| |   
| |       Merge pull request #13 from HUIXIN-TW/training-eliza
| |       
| |       train eliza
| | 
| * commit 7f50efb4e4f59f507ef52a3de1a58c2c4222bc29 (origin/training-eliza)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Fri May 19 01:56:21 2023 +0800
| | 
| |     train eliza
| |   
* |   commit bbc47f90d36ae41ff7f17ba73b607a4e9b87cd48
|\ \  Merge: 16690e9 ab21786
| | | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | | Date:   Thu May 18 22:21:16 2023 +0800
| | | 
| | |     Merge pull request #12 from HUIXIN-TW/add-AboutMe-page-modify-account-page--YunChuan
| | |     
| | |     add about me page and modify the some style
| | | 
| * | commit ab2178676c6a53af28e5c1d1ef63f1aa093f0394 (origin/add-AboutMe-page-modify-account-page--YunChuan)
| | | Author: Yunchuan <leisyun@gmail.com>
| | | Date:   Thu May 18 22:09:51 2023 +0800
| | | 
| | |     add about me page and modify the some style
| | |   
* | |   commit 16690e9ede6815985577cd6b2d44c2865875a35c
|\ \ \  Merge: 16abc58 86fb610
| |/ /  Author: remykung <75251932+remykung@users.noreply.github.com>
|/| /   Date:   Thu May 18 21:43:54 2023 +0800
| |/    
| |         Merge pull request #11 from HUIXIN-TW/real-time-chat
| |         
| |         add real-time-chat function
| | 
| * commit 86fb6107126b4335d8c9566f3d6a3b900f174b5e (origin/real-time-chat, real-time-chat)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Thu May 18 21:41:00 2023 +0800
| | 
| |     add real-time-chat function
| | 
* | commit 16abc589c0017b870f698325fb040ea884ff3f04
|\| Merge: d5a8a2c 5ff2e45
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Thu May 18 13:58:57 2023 +0800
| | 
| |     Merge pull request #10 from HUIXIN-TW/accinfo-into-DB-and-dynamic-page-style
| |     
| |     add info into Db and customised page based on dif db info
| | 
| * commit 5ff2e459e03c6ca133c7411080b19ce1e991db62 (origin/accinfo-into-DB-and-dynamic-page-style, accinfo-into-DB-and-dynamic-page-style)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Thu May 18 06:38:47 2023 +0800
| | 
| |     get random user
| | 
| * commit 1c060c4722b9baf9f95eea66f7e888a17fcd6faf
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Thu May 18 04:47:03 2023 +0800
|   
|       add info into Db and customised page based on dif db info
|   
*   commit d5a8a2c9afa49ee3690c3530b97df97d95d36cc6
|\  Merge: 7827252 8a82a06
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Wed May 17 14:27:55 2023 +0800
| | 
| |     Merge pull request #9 from HUIXIN-TW/register-server-side-validation-and-memory-page-style--YunChuan
| |     
| |     register sever-side validation, memory pg update
| | 
| * commit 8a82a0646cb862549460822c051fcf837233d2b8 (origin/register-server-side-validation-and-memory-page-style--YunChuan)
|/  Author: Yunchuan <leisyun@gmail.com>
|   Date:   Wed May 17 14:20:16 2023 +0800
|   
|       register sever-side validation, memory pg update
|   
*   commit 782725291f2ac87b677af98321b1cb6e51b07a59
|\  Merge: 2efce5b 3bdfd16
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Mon May 15 03:03:20 2023 +0800
| | 
| |     Merge pull request #7 from HUIXIN-TW/adj-time-zone
| |     
| |     adj to perth timezone
| | 
| * commit 3bdfd166708d456ba594dfbc5363384262c6b529 (origin/adj-time-zone, adj-time-zone)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Mon May 15 02:57:07 2023 +0800
| | 
| |     adj to perth timezone
| |   
* |   commit 2efce5b42dd522453b5fc72e5b28a750d60e6ae7
|\ \  Merge: 7a29e19 6566737
| |/  Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
|/|   Date:   Mon May 15 03:02:54 2023 +0800
| |   
| |       Merge pull request #8 from HUIXIN-TW/chat-window-style--YunChuan
| |       
| |       chat page - chat window style
| | 
| * commit 6566737eb47fab86222759a8a8c3292b48a1c1f4 (origin/chat-window-style--YunChuan)
|/  Author: Yunchuan <leisyun@gmail.com>
|   Date:   Mon May 15 03:00:00 2023 +0800
|   
|       chat page - chat window style
|   
*   commit 7a29e1937d6c92f3883c5882b1687800ce436ba5
|\  Merge: 2a7f6bb e552c7c
| | Author: remykung <75251932+remykung@users.noreply.github.com>
| | Date:   Mon May 15 02:27:34 2023 +0800
| | 
| |     Merge pull request #6 from HUIXIN-TW/chatbot-function-connected-db--Huixin
| |     
| |     add chatbot related function and store data in db
| |   
| *   commit e552c7c7fb36c8c1a32d9e9c87c9391ea4229f1c (origin/chatbot-function-connected-db--Huixin)
| |\  Merge: ecb32e8 2a7f6bb
| |/  Author: remykung <75251932+remykung@users.noreply.github.com>
|/|   Date:   Mon May 15 02:27:19 2023 +0800
| |   
| |       Merge branch 'master' into chatbot-function-connected-db--Huixin
| |   
* |   commit 2a7f6bb0ce32b251536b67b2ded2e7fa0ad191d4
|\ \  Merge: 8005e87 ee1e649
| | | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | | Date:   Mon May 15 02:07:30 2023 +0800
| | | 
| | |     Merge pull request #5 from HUIXIN-TW/add-html-pages-index-memory--YunChuan
| | |     
| | |     adding pages and style
| | | 
| * | commit ee1e64909a032f83975335fcbd87de9f170f1b72 (origin/add-html-pages-index-memory--YunChuan)
| | | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | | Date:   Sun May 14 18:05:34 2023 +0000
| | | 
| | |     minor
| | | 
| * | commit 9bca927227f33502093101e358ec11164108ff38
|/ /  Author: Yunchuan <leisyun@gmail.com>
| |   Date:   Mon May 15 01:29:41 2023 +0800
| |   
| |       adding pages and style
| |   
* |   commit 8005e87d329adfd6f4fddb4a2236ee550178ad9f
|\ \  Merge: 44c6992 7961eac
| | | Author: remykung <75251932+remykung@users.noreply.github.com>
| | | Date:   Wed May 10 23:33:13 2023 +0800
| | | 
| | |     Merge pull request #4 from HUIXIN-TW/new-structure-new-db-setting
| | |     
| | |     New structure and new db setting - Add login, register and logout function
| | | 
| | * commit ecb32e8365d79b320150d07cba285b28f52286ae
| |/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| |   Date:   Mon May 15 02:09:54 2023 +0800
| |   
| |       add chatbot related function and store data in db
| | 
| * commit 7961eacdbf7dae095e177f9922c8221be6219f54 (origin/new-structure-new-db-setting)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Wed May 10 23:10:55 2023 +0800
| | 
| |     complete new structure and DB setting
| | 
| * commit b291440ed606966ce597c1d566c08ea512c1a77a
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Sun May 7 18:52:36 2023 +0800
| | 
| |     new structure new db setting. NOT WORKING LOGIN YET
| | 
| * commit 60e60617f6b094a05069d3ea1edd0073d6c2d085 (origin/set-up-db-and-login-function-Huixin)
| | Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| | Date:   Sun May 7 17:14:15 2023 +0800
| | 
| |     Update README
| | 
| * commit d3dc8fdfaa09f48308be3518285d91646bfca52c
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Sun May 7 17:01:35 2023 +0800
|   
|       set DB. Add login and register function
|   
*   commit 44c6992011e9bb10fb7b37d23ab391c070d5184e
|\  Merge: 1cbfbbe 1025327
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Sun May 7 15:50:00 2023 +0800
| | 
| |     Merge pull request #2 from HUIXIN-TW/login-related-pages--YunChuan
| |     
| |     add login, register, account pages--frontend
| | 
| * commit 1025327f8e479ff7e3feeb622e5476b241874de0 (origin/login-related-pages--YunChuan)
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Sun May 7 07:42:18 2023 +0000
| | 
| |     fix minor bugs
| | 
| * commit 49438edad800bcba5700fe1f37546d81390bcfdd
| | Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| | Date:   Sun May 7 07:33:04 2023 +0000
| | 
| |     update page design
| | 
| * commit 16cbad1536115c5044fefb304d89ee6ef307a3da
| | Author: Yunchuan <leisyun@gmail.com>
| | Date:   Sun May 7 03:16:25 2023 +0800
| | 
| |     add login, register, account pages--frontend
| | 
* | commit 1cbfbbe2753f5b6a0bddea70e54778419642ef55
|/  Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
|   Date:   Sun May 7 15:44:55 2023 +0800
|   
|       update README
| 
* commit 218bde0f061a7d200bdca1386c42ce200ab325bd
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Sun May 7 02:27:49 2023 +0800
| 
|     init justchat app
| 
* commit 0d0c63fc27030aef1278f89fd3d77a904d640d5d (origin/workshop-practice)
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Sun May 7 00:56:26 2023 +0800
| 
|     w9 workshop css, log conf
| 
* commit 3784f21ca24285be91e2b94030df8ec3059eff68
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed May 3 20:14:34 2023 +0800
| 
|     practice flask lab
| 
* commit 8d5947c8b193fd9aa7b0a922fa7e78edfdcdbd79
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed May 3 20:06:57 2023 +0800
| 
|     add style.css sheet dotenv
| 
* commit fbe1630f606761a8e83ba2839d8ddf4f4e8ed019
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed May 3 15:50:11 2023 +0800
| 
|     finish test
| 
* commit 8d40ed34563d1ca2286f4c0cc77ec259c9bda1c0
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed May 3 04:06:00 2023 +0800
| 
|     WIP TEST topics
| 
* commit 4318373166ef79157d3092b5a104275c62ac550d
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Fri Apr 28 23:40:33 2023 +0800
| 
|     server validate
| 
* commit 5e2f847996d76d9399200356e9f887544c51fdd0
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Fri Apr 28 03:19:39 2023 +0800
| 
|     add route
| 
* commit 3b6e6a0198ab74a673b5910acfabc8e92f70e128
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed Apr 26 16:33:45 2023 +0800
| 
|     updated gitignore
| 
* commit 93f142048092da9d4cd12b8ed34c9c21939edd4a
| Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
| Date:   Wed Apr 26 02:59:21 2023 +0800
| 
|     Delete .DS_Store
| 
* commit 5e61a3817731f384d6986a785c6ea9328f271838
| Author: HUIXIN-TW <huixin.yang.tw@gmail.com>
| Date:   Wed Apr 26 02:57:44 2023 +0800
| 
|     setting, init mini flask
| 
* commit 875851425112aa992cde975a2feee0225be7f598
  Author: HUIXIN <75252053+HUIXIN-TW@users.noreply.github.com>
  Date:   Wed Apr 26 00:32:47 2023 +0800
  
      Initial commit
```
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