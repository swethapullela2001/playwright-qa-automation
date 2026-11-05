
from playwright.sync_api import Page, expect


class BookingFormPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_guest_name(self, name):
        self.page.get_by_label("Guest Name").fill(name)

    def select_room(self, room):
        self.page.get_by_label("Room Type").select_option(room)

    def confirm_booking(self):
        self.page.get_by_role(
            "button", name="Confirm Booking"
        ).click()

    def verify_status(self, expected_status):
        expect(
            self.page.locator("#status")
        ).to_have_text(expected_status)
