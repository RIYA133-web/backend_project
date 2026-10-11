# Flask REST API Backend

A beginner-friendly REST API built using Python, Flask, and Flask-SQLAlchemy. This project demonstrates CRUD-related API functionality, database relationships, input validation, and automated testing.

## Features

- Retrieve users
- Retrieve posts belonging to a user
- Create posts with input validation
- Retrieve a post by its ID
- Handle missing fields and invalid JSON
- Validate user IDs before creating posts
- Automated tests using pytest
- GitHub Actions workflow for automated checks

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest
- GitHub Actions

## Project Structure

```text
backend_project/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── __init__.py
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
├── run.py
└── README.md
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/RIYA133-web/backend_project.git
   cd backend_project
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install Flask Flask-SQLAlchemy pytest
   ```

4. Run the application:

   ```bash
   python run.py
   ```

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

Check Python syntax:

```bash
python -m compileall -q app run.py
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/users` | Retrieve users |
| GET | `/users/<user_id>/posts` | Retrieve a user's posts |
| POST | `/posts` | Create a post |
| GET | `/posts/<post_id>` | Retrieve a post by ID |

## Error Handling

The API validates required fields, rejects empty titles and content, checks user IDs, and returns appropriate HTTP error responses for invalid requests.

## Learning Goals

This project helped me practise REST API development, database models and relationships, request validation, automated testing, and continuous integration using GitHub Actions.
