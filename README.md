# Flask REST API Backend

A beginner-friendly REST API project built with Python, Flask, and Flask-SQLAlchemy. This project demonstrates API development, database relationships, request validation, error handling, automated testing, and continuous integration with GitHub Actions.

## Project Overview

This project provides REST API endpoints to retrieve users, create posts, retrieve individual posts, and fetch posts belonging to a specific user. It uses SQLite for data storage and SQLAlchemy to manage database models and relationships.

The project also includes input validation and automated tests to help ensure that the API handles valid and invalid requests correctly.

## Features

- Retrieve users through a REST API endpoint
- Retrieve posts associated with a specific user
- Create posts with request validation
- Retrieve individual posts by ID
- Validate required fields and reject empty titles or content
- Handle invalid JSON requests
- Check whether a user exists before creating a post
- Return appropriate HTTP status codes and error messages
- Run automated tests using pytest
- Check Python syntax using compileall
- Automate checks with GitHub Actions

## Tech Stack

- **Language:** Python
- **Web Framework:** Flask
- **ORM:** Flask-SQLAlchemy
- **Database:** SQLite
- **Testing:** pytest
- **Continuous Integration:** GitHub Actions
- **Version Control:** Git and GitHub

## Project Structure

```text
backend_project/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── app/
│   ├── models/
│   │   ├── user.py
│   │   └── post.py
│   ├── routes/
│   │   ├── user.py
│   │   └── post.py
│   ├── services/
│   │   ├── user_services.py
│   │   └── post_services.py
│   └── __init__.py
├── tests/
│   └── test_api.py
├── run.py
└── README.md
```

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure Python and Git are installed on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/RIYA133-web/backend_project.git
cd backend_project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**

```bat
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install Flask Flask-SQLAlchemy pytest
```

### 5. Run the Application

```bash
python run.py
```

The development server should start. Check the terminal for the local URL provided by Flask.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users` | Retrieve the list of users |
| GET | `/users/<user_id>/posts` | Retrieve posts belonging to a user |
| POST | `/posts` | Create a new post |
| GET | `/posts/<post_id>` | Retrieve a post by its ID |

## Creating a Post

Send a `POST` request to `/posts` with a JSON body like this:

```json
{
  "title": "My First Post",
  "content": "This is my first post.",
  "user_id": 1
}
```

A successful request returns HTTP status `201 Created` with a confirmation message and the new post's ID.

The specified user must already exist in the database.

## Validation and Error Handling

The API checks incoming requests and handles common errors, including:

- Invalid or malformed JSON
- Missing required fields
- Empty or whitespace-only titles
- Empty or whitespace-only content
- Invalid user ID types
- User IDs that do not exist

The API returns appropriate HTTP error status codes for invalid requests and missing resources.

## Running Tests

Run the automated test suite from the project root:

```bash
python -m pytest -v
```

To check Python syntax:

```bash
python -m compileall -q app run.py
```

## Continuous Integration

This repository uses GitHub Actions to automate project checks when changes are pushed to GitHub or a pull request is opened, according to the configured workflow.

The workflow helps identify syntax errors and test failures before changes are considered complete.

## Learning Outcomes

Through this project, I practised:

- Building REST API endpoints with Flask
- Organising code into models, routes, and service layers
- Creating database models and relationships
- Validating request data and handling errors
- Writing automated tests with pytest
- Running automated checks with GitHub Actions
- Using Git and GitHub to manage a software project

## Future Improvements

- Add endpoints to update and delete posts
- Add more tests for edge cases
- Improve API documentation
- Add pagination and filtering
- Introduce authentication and authorisation

## Author

**Riya**

GitHub: [RIYA133-web](https://github.com/RIYA133-web)

---

This project was created for learning and practising backend development with Python
