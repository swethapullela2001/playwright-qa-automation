from playwright.sync_api import Playwright
def test_get_post(playwright:Playwright):
    api = playwright.request.new_context()
    try:
        payload = {
            "title": "New Hotel Booking",
            "body": "Standard Room",   
            "userId": 2
        }
        response = api.post("https://jsonplaceholder.typicode.com/posts", data=payload)
        assert response.status == 201
        data = response.json()
        assert data["title"] == "New Hotel Booking"
        assert data["body"] == "Standard Room"
        assert data["userId"] == 2
        assert data["id"] == 101
    finally:
        api.dispose()