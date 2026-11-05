
import pytest
from playwright.sync_api import Page
from pages.booking_form_page import BookingFormPage


@pytest.mark.parametrize(
    "guest_name, room, expected_status",
    [
        ("Swetha", "deluxe", "Booking Confirmed"),
        ("Arjun", "standard", "Booking Confirmed"),
        ("Rahul", "suite", "Booking Confirmed"),
        ("", "deluxe", "Guest Name Required"),
        ("Priya", "", "Room Selection Required"),
    ]
)
def test_booking_scenarios(
    hotel_booking_form: Page,
    guest_name,
    room,
    expected_status
):
    booking = BookingFormPage(hotel_booking_form)

    booking.enter_guest_name(guest_name)
    booking.select_room(room)
    booking.confirm_booking()

    booking.verify_status(expected_status)
