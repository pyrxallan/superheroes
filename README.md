# Superheroes API

A Flask-based REST API for managing superheroes, their powers, and hero-power relationships.

## Features

- Manage heroes with their real names and super names
- Manage powers with descriptions
- Associate heroes with powers and strength levels
- RESTful API endpoints
- Database migrations with Flask-Migrate
- Seeding script for sample data

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Seed the database:
   ```bash
   python seed.py
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

- `GET /` - Welcome message
- `GET /heroes` - Get all heroes
- `GET /heroes/<id>` - Get hero by ID
- `GET /powers` - Get all powers
- `GET /powers/<id>` - Get power by ID
- `PATCH /powers/<id>` - Update power
- `POST /hero_powers` - Create hero-power association

## Testing

Run tests with:
```bash
pytest
```

## Database

Uses SQLite database stored in `instance/app.db`.
