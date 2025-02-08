from core.models.assignments import Assignment, AssignmentStateEnum
import pytest
from core.models.assignments import Assignment
from core.libs import assertions
from core import db


def test_assignment_repr():
    """Test string representation of the Assignment model."""
    assignment = Assignment(id=1, content="Test Assignment", student_id=1, state="DRAFT")
    assert repr(assignment) == "<Assignment 1>"
