from playwright.sync_api import Playwright
def test_get_post(playwright:Playwright):
    api = playwright.request.new_context()
    try:
        response = api.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        data = response.json()
        assert data["id"] == 1
    finally:
        api.dispose()