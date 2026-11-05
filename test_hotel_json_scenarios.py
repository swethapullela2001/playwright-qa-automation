
import json
import pytest

from pathlib import Path
from playwright.sync_api import Page
from pages.booking_form_page import BookingFormPage


DATA_FILE = (
    Path(__file__).resolve().parent
    / "test_data"
    / "booking_scenarios.json"
)

with DATA_FILE.open(encoding="utf-8") as file:
    booking_scenarios = json.load(file)


@pytest.mark.parametrize("scenario", booking_scenarios)
def test_booking_from_json(
    hotel_booking_form: Page,
    scenario
):
    booking = BookingFormPage(hotel_booking_form)

    booking.enter_guest_name(scenario["guest_name"])
    booking.select_room(scenario["room"])
    booking.confirm_booking()

    booking.verify_status(scenario["expected_status"])
