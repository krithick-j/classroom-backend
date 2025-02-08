import pytest
import json
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.students import Student
from core.models.teachers import Teacher
from core.models.users import User
from tests import app
from core import db


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers

@pytest.fixture
def teacher():
    return Teacher(id=1, user_id=5)

@pytest.fixture
def student():
    return Student(id=1, user_id=10)

@pytest.fixture
def create_test_user():
    """Fixture to create a test user and clean up after the test."""
    db.session.query(User).filter_by(username="testuser").delete()  # Ensure no duplicates
    db.session.commit()

    user = User(username="testuser", email="testuser@example.com")
    db.session.add(user)
    db.session.commit()

    yield user

    db.session.delete(user)
    db.session.commit()
    
