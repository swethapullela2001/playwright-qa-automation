
from playwright.sync_api import Playwright


def test_update_booking_put(playwright: Playwright):
    api = playwright.request.new_context()

    try:
        payload = {
        "id": 2,
        "title": "Hotel Booking Updated",
        "body": "Deluxe Room",
        "userId": 1
    }

        response = api.put(
            "https://jsonplaceholder.typicode.com/posts/2",
            data=payload
        )

        assert response.status == 200

        data = response.json()

        assert data["title"] == "Hotel Booking Updated"
        assert data["body"] == "Deluxe Room"
        assert data["userId"] == 1
        assert data["id"] == 2
    finally:
        api.dispose()



def test_update_booking_patch(playwright: Playwright):
    api = playwright.request.new_context()

    try:
        payload = {
            "title": "Hotel Booking Modified"
        }

        response = api.patch(
            "https://jsonplaceholder.typicode.com/posts/2",
            data=payload
        )

        assert response.status == 200

        data = response.json()

        assert data["title"] == "Hotel Booking Modified"

    finally:
        api.dispose()
