
def test_authenticated_get(authenticated_api):
    response = authenticated_api.get("/posts/1")

    assert response.status == 200

    data = response.json()
    assert data["id"] == 1

def test_authenticated_post(authenticated_api):
    payload = {
        "title": "Authenticated Booking",
        "body": "Suite Room",
        "userId": 3
    }

    response = authenticated_api.post(
        "/posts",
        data=payload
    )

    assert response.status == 201

    data = response.json()
    assert data["title"] == "Authenticated Booking"
    assert data["userId"] == 3
