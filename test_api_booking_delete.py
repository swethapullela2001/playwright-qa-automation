
from playwright.sync_api import Playwright


def test_delete_booking(playwright: Playwright):
    api = playwright.request.new_context()

    try:
        response = api.delete(
            "https://jsonplaceholder.typicode.com/posts/2"
        )

        assert response.status == 200
        assert response.ok == True
    finally:
        api.dispose()
