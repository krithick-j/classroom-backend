from core.libs.exceptions import FyleError


def test_fyle_error():
    error_message = "This is a FyleError"
    status_code = 403  # Example status code

    error = FyleError(status_code, error_message)

    assert error.message == error_message
    assert error.status_code == status_code
    assert error.to_dict() == {"message": error_message}