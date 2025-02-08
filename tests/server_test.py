def test_server_startup(client):
    """Test if the server starts up correctly."""
    response = client.get('/')  # Assuming a health-check endpoint exists
    assert response.status_code == 200
