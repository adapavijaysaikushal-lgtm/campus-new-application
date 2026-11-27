import pytest
from app import app, assignments


@pytest.fixture()
def client():
    assignments.clear()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client
    assignments.clear()


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Assignment Tracker" in response.data


def test_add_assignment(client):
    response = client.post("/assignments", data={"title": "Finish lab record"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Finish lab record" in response.data
    assert len(assignments) == 1


def test_blank_assignment_is_not_added(client):
    client.post("/assignments", data={"title": "   "})
    assert assignments == []


def test_mark_assignment_complete(client):
    client.post("/assignments", data={"title": "Submit project"})
    assignment_id = assignments[0]["id"]
    response = client.post(f"/assignments/{assignment_id}/complete", follow_redirects=True)
    assert response.status_code == 200
    assert assignments[0]["completed"] is True
    assert b"Completed" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
