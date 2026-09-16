from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"task": "Test Task"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Task" in response.data