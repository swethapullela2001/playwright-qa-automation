
from playwright.sync_api import Page
from pages.hotel_booking_page import HotelBookingPage


def test_guest_name_pom(hotel_page: Page):
    booking = HotelBookingPage(hotel_page)

    booking.enter_guest_name("QA Tester")

    booking.verify_guest_name("QA Tester")


def test_booking_confirmation_pom(hotel_page: Page):
    booking = HotelBookingPage(hotel_page)

    booking.enter_guest_name("QA Tester")

    booking.confirm_booking()

    booking.verify_booking_confirmation()
