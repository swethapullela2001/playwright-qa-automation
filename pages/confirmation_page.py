
from playwright.sync_api import Page, expect


class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_confirmation_heading(self):
        expect(
            self.page.get_by_role(
                "heading", name="Booking Successful"
            )
        ).to_be_visible()

    def verify_booking_id(self):
        expect(
            self.page.locator("#booking-id")
        ).to_have_text("Booking ID: 1001")

