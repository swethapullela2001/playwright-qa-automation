
import json
import pytest


from playwright.sync_api import Page
from pages.hotel_booking_page import HotelBookingPage

with open("test_data/booking_data.json", "r") as file:
    booking_data = json.load(file)

@pytest.mark.parametrize("guest", booking_data)
def test_booking_guest_data(hotel_page: Page, guest):
    booking_page = HotelBookingPage(hotel_page)
    booking_page.enter_guest_name(guest["name"])
    booking_page.verify_guest_name(guest["name"])
