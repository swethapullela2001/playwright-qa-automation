
from playwright.sync_api import Page
from pages.booking_form_page import BookingFormPage


def test_valid_booking(hotel_booking_form: Page):
    booking = BookingFormPage(hotel_booking_form)

    booking.enter_guest_name("QA Tester")
    booking.select_room("deluxe")
    booking.confirm_booking()

    booking.verify_status("Booking Confirmed")
def test_missing_guest_name(hotel_booking_form: Page):
    booking = BookingFormPage(hotel_booking_form)

    booking.enter_guest_name("")
    booking.select_room("standard")
    booking.confirm_booking()

    booking.verify_status("Guest Name Required")
def test_missing_room_selection(hotel_booking_form: Page):
    booking = BookingFormPage(hotel_booking_form)

    booking.enter_guest_name("QA Tester")
    booking.confirm_booking()

    booking.verify_status("Room Selection Required")