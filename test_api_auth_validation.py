
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def protected_api():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            token = self.headers.get("Authorization")

            if token == "Bearer valid-test-token":
                self.send_response(200)
                message = b'{"message": "Access Granted"}'
            else:
                self.send_response(401)
                message = b'{"message": "Unauthorized"}'

            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(message)))
            self.end_headers()
            self.wfile.write(message)

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield f"http://127.0.0.1:{server.server_port}"

    server.shutdown()
    server.server_close()
    thread.join()


def test_valid_token(playwright: Playwright, protected_api):
    api = playwright.request.new_context()

    try:
        response = api.get(
            protected_api,
            headers={
                "Authorization": "Bearer valid-test-token"
            }
        )

        assert response.status == 200

    finally:
        api.dispose()


def test_invalid_token(playwright: Playwright, protected_api):
    api = playwright.request.new_context()

    try:
        response = api.get(
            protected_api,
            headers={
                "Authorization": "Bearer wrong-token"
            }
        )

        assert response.status == 401

    finally:
        api.dispose()

def test_missing_token(playwright: Playwright, protected_api):
    api = playwright.request.new_context()

    try:
        response = api.get(protected_api)

        assert response.status == 401
        assert response.json()["message"] == "Unauthorized"
    finally:
        api.dispose()