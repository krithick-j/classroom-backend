# Classroom Backend - Flask

This project is a backend service for a classroom management system. It provides APIs for managing users, assignments, and grading. The system supports different roles such as Principal, Teacher, and Student, each with specific permissions and capabilities.

## Features

- **Principal**: Can view all teachers, view all assignments, and re-grade assignments.
- **Teacher**: Can view assignments submitted to them and grade those assignments.
- **Student**: Can create, edit, and submit assignments, as well as view their own assignments.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/krithick-j-classroom-backend.git
   cd krithick-j-classroom-backend

2. **Set up a virtual environment**:
   ```bash
   virtualenv env --python=python3.8
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Reset the database**:
   ```bash
   export FLASK_APP=core/server.py
   rm core/store.sqlite3
   flask db upgrade -d core/migrations/
   ```

5. **Run the server**:
   ```bash
   bash run.sh
   ```

## Running Tests

To run the tests, use the following command:

```bash
pytest -vvv -s tests/
```

To generate a test coverage report(94% till now):

```bash
pytest --cov
open htmlcov/index.html
```

## API Documentation

### Authentication
- **Header**: `X-Principal`
- **Value**: JSON object containing user details (e.g., `{"user_id": 1, "student_id": 1}`)

### Endpoints

#### Student
- **GET /student/assignments**: List all assignments created by the student.
- **POST /student/assignments**: Create or edit an assignment.
- **POST /student/assignments/submit**: Submit an assignment to a teacher.

#### Teacher
- **GET /teacher/assignments**: List all assignments submitted to the teacher.
- **POST /teacher/assignments/grade**: Grade an assignment.

#### Principal
- **GET /principal/assignments**: List all submitted and graded assignments.
- **POST /principal/assignments/grade**: Grade or re-grade an assignment.
- **GET /principal/teachers**: List all teachers.

## Database Migrations

The project uses Alembic for database migrations. To create a new migration:

```bash
flask db migrate -m "Your migration message" -d core/migrations/
```

To apply the migration:

```bash
flask db upgrade -d core/migrations/
```

## Docker

The project can be run using Docker. To build and run the Docker container:

```bash
docker compose up -d
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

This README provides a comprehensive overview of the project, including installation instructions, API documentation, and details on running tests and migrations. It also includes information on how to contribute and contact details for further inquiries.
