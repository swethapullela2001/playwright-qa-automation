
from playwright.sync_api import Page, expect


class HotelBookingPage:

    def __init__(self, page: Page):
        self.page = page

    def enter_guest_name(self, name):
        self.page.get_by_label("Guest Name").fill(name)

    def verify_guest_name(self, name):
        expect(
            self.page.get_by_label("Guest Name")
        ).to_have_value(name)

    def confirm_booking(self):
        self.page.get_by_role(
            "button", name="Confirm Booking"
        ).click()

    def verify_booking_confirmation(self):
        expect(
            self.page.locator("#status")
        ).to_have_text("Booking Confirmed")
