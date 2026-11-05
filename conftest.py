import pytest
from playwright.sync_api import Page


@pytest.fixture
def hotel_page(page: Page):
    page.set_content("""
        <h2>Hotel Booking</h2>

        <label for="guest">Guest Name</label>
        <input id="guest" type="text">

        <button onclick="
            document.getElementById('status').textContent =
                'Booking Confirmed';
        ">
            Confirm Booking
        </button>

        <p id="status"></p>
    """)

    return page


@pytest.fixture
def multi_page_hotel(page: Page):
    page.set_content("""
        <h2>Hotel Booking</h2>

        <label for="guest">Guest Name</label>
        <input id="guest" type="text">

        <button onclick="
            document.body.innerHTML =
                '<h2>Booking Successful</h2>' +
                '<p id=&quot;booking-id&quot;>Booking ID: 1001</p>';
        ">
            Confirm Booking
        </button>
    """)

    return page


@pytest.fixture
def hotel_booking_form(page: Page):
    page.set_content("""
        <h2>Hotel Booking Form</h2>

        <label for="guest">Guest Name</label>
        <input id="guest" type="text">

        <label for="room">Room Type</label>
        <select id="room">
            <option value="">Select Room</option>
            <option value="standard">Standard</option>
            <option value="deluxe">Deluxe</option>
            <option value="suite">Suite</option>
        </select>

        <button onclick="
            const guest = document.getElementById('guest').value;
            const room = document.getElementById('room').value;
            const status = document.getElementById('status');

            if (!guest.trim()) {
                status.textContent = 'Guest Name Required';
            } else if (!room) {
                status.textContent = 'Room Selection Required';
            } else {
                status.textContent = 'Booking Confirmed';
            }
        ">
            Confirm Booking
        </button>

        <p id="status"></p>
    """)

    return page


import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def api_context(playwright: Playwright):
    api = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Accept": "application/json"
        }
    )

    yield api

    api.dispose()



import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def authenticated_api(playwright: Playwright):
    api = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Authorization": "Bearer demo-token",
            "Accept": "application/json"
        }
    )

    yield api

    api.dispose()
