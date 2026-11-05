from playwright.sync_api import Page
from pages.confirmation_page import ConfirmationPage
from pages.hotel_booking_page import HotelBookingPage
def test_complete_hotel_booking(multi_page_hotel: Page):
    booking = HotelBookingPage(multi_page_hotel)
    booking.enter_guest_name("QA Tester")
    booking.confirm_booking()
    confirmation = ConfirmationPage(multi_page_hotel)
    confirmation.verify_confirmation_heading()
    confirmation.verify_booking_id()