from http import HTTPStatus
from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.apis.teachers.schema import TeacherSchema
from core.models.assignments import Assignment, AssignmentStateEnum, Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teachers_list = Teacher.get_teachers_by_principal()
    teachers_list_dump = TeacherSchema().dump(teachers_list, many=True)
    return APIResponse.respond(data=teachers_list_dump)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principals_assignments = Assignment.get_assignments_by_principal()
    principals_assignments_dump = AssignmentSchema().dump(principals_assignments, many=True)
    return APIResponse.respond(data=principals_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    assignment = Assignment.get_by_id(grade_assignment_payload.id)
    if assignment.state == AssignmentStateEnum.DRAFT.value:
        return APIResponse.respond_error(message='Assignment is in Draft state and cannot be graded', error='FyleError', status_code=HTTPStatus.BAD_REQUEST)
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
