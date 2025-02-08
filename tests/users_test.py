from core.models.users import User

def test_user_creation(create_test_user):
    """Test if the user is created successfully."""
    user = create_test_user
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.created_at is not None
    assert user.updated_at is not None

def test_get_by_id(create_test_user):
    """Test if get_by_id retrieves the correct user."""
    user = User.get_by_id(create_test_user.id)
    assert user is not None
    assert user.username == "testuser"

def test_get_by_email(create_test_user):
    """Test if get_by_email retrieves the correct user."""
    user = User.get_by_email("testuser@example.com")
    assert user is not None
    assert user.username == "testuser"

def test_filter(create_test_user):
    """Test if filter method returns the correct user."""
    user = User.filter(User.username == "testuser").first()
    assert user is not None
    assert user.username == "testuser"
