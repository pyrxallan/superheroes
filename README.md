# Superheroes API

A Flask REST API for managing superheroes and their superpowers.

**Author:** Allan Ratemo 
**GitHub:** [@pyrxallan](https://github.com/pyrxallan)  
**Repository:** [https://github.com/pyrxallan/superheroes](https://github.com/pyrxallan/superheroes)

## Description

This is a Flask-based REST API that allows you to manage superheroes, their powers, and the relationships between them. The API supports full CRUD operations with proper validation and error handling. Built as part of Phase 4 code challenge to demonstrate backend development skills with Python, Flask, and SQLAlchemy.

## Features

- Manage superheroes with their real names and superhero aliases
- Track superpowers with detailed descriptions
- Create associations between heroes and powers with strength ratings
- Full CRUD operations with RESTful endpoints
- Input validation for data integrity
- Proper error handling with appropriate HTTP status codes
- JSON responses for all endpoints
- Pre-seeded database with popular superheroes

## Technologies Used

- Python 3.12
- Flask - Web framework
- Flask-SQLAlchemy - Database ORM
- Flask-Migrate - Database migrations
- SQLite - Database
- SQLAlchemy-serializer - JSON serialization

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip
- Virtual environment

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pyrxallan/superheroes.git
cd superheroes
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
# Option 1: Using migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Option 2: Direct creation (simpler)
python create_db.py
```

5. Seed the database:
```bash
python seed.py
```

6. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5555`

## Database Schema

**Heroes**
- id (Primary Key)
- name (String)
- super_name (String)

**Powers**
- id (Primary Key)
- name (String)
- description (String, min 20 characters)

**HeroPowers** (Join Table)
- id (Primary Key)
- strength (String: 'Strong', 'Weak', or 'Average')
- hero_id (Foreign Key)
- power_id (Foreign Key)

## API Endpoints

### GET /heroes
Get all heroes.

Response:
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

### GET /heroes/:id
Get a specific hero with their powers.

Success Response (200):
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

Error Response (404):
```json
{
  "error": "Hero not found"
}
```

### GET /powers
Get all powers.

Response:
```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
```

### GET /powers/:id
Get a specific power.

Success Response (200):
```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

Error Response (404):
```json
{
  "error": "Power not found"
}
```

### PATCH /powers/:id
Update a power's description.

Request Body:
```json
{
  "description": "Updated description with at least 20 characters"
}
```

Success Response (200):
```json
{
  "id": 1,
  "name": "super strength",
  "description": "Updated description with at least 20 characters"
}
```

Error Responses:
- 404: `{"error": "Power not found"}`
- 400: `{"errors": ["validation errors"]}`

### POST /hero_powers
Create a new hero-power association.

Request Body:
```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

Success Response (201):
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

Error Response (400):
```json
{
  "errors": ["validation errors"]
}
```

## Testing

Run the automated test suite:

```bash
# Make sure the server is running
python app.py

# In another terminal
python test_api.py
```

Or use pytest:
```bash
pytest
```

Expected output: `10 passed`

### Postman Testing

1. Import `challenge-2-superheroes.postman_collection.json` into Postman
2. Run the collection to test all endpoints
3. Verify all requests return correct status codes

## Validation Rules

**Power:**
- description must be at least 20 characters

**HeroPower:**
- strength must be 'Strong', 'Weak', or 'Average'

## Usage Examples

Get all heroes:
```bash
curl http://localhost:5555/heroes
```

Create a hero-power association:
```bash
curl -X POST http://localhost:5555/hero_powers \
  -H "Content-Type: application/json" \
  -d '{"strength": "Strong", "power_id": 1, "hero_id": 2}'
```

Update a power:
```bash
curl -X PATCH http://localhost:5555/powers/1 \
  -H "Content-Type: application/json" \
  -d '{"description": "Updated description with more than 20 characters"}'
```

## Project Structure

```
superheroes/
├── app.py                  # Main application file
├── models.py              # Database models
├── seed.py                # Database seeding
├── create_db.py           # Database creation
├── test_api.py            # Test suite
├── requirements.txt       # Dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── instance/
    └── app.db            # SQLite database
```

## Support

For issues or questions:
- Create an issue: [GitHub Issues](https://github.com/pyrxallan/superheroes/issues)
- Contact: Through GitHub profile [@pyrxallan](https://github.com/pyrxallan)

## License

MIT License

Copyright (c) 2025  Allan Ratemo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

Created as part of Phase 4 code challenge for Flatiron School curriculum.

---

**Repository:** [https://github.com/pyrxallan/superheroes](https://github.com/pyrxallan/superheroes)  
**Author:** Allan Ratemo [@pyrxallan](https://github.com/pyrxallan)