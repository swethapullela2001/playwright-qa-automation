import pytest
from playwright.sync_api import Page
from pages.confirmation_page import ConfirmationPage
from pages.hotel_booking_page import HotelBookingPage
@pytest.mark.parametrize("guest_name", ["Swetha", "Rahul", "Priya", "Arjun"])
def test_hotel_guest_names(hotel_page: Page, guest_name):
    booking = HotelBookingPage(hotel_page)
    booking.enter_guest_name(guest_name)
    booking.verify_guest_name(guest_name)