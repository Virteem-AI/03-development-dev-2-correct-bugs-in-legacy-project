import pytest
from buggy_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def clear_tasks():
    from buggy_app import tasks
    tasks.clear()


def test_create_task_returns_201(client):
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201


def test_create_task_has_id(client):
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201
    assert "id" in response.get_json()


def test_update_task_changes_title(client):
    response = client.post("/tasks", json={"title": "Original"})
    assert response.status_code == 201
    task_id = response.get_json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated"


def test_delete_returns_204(client):
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201
    task_id = response.get_json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204


def test_app_runs():
    import buggy_app
    source = open(buggy_app.__file__, encoding="utf-8").read()
    assert "app.run" in source
