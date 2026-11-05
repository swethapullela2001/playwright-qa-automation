
from playwright.sync_api import Page, expect


def test_booking_failure_demo(page: Page):
    page.set_content("""
        <h2>Hotel Booking</h2>
        <p id="status">Booking Pending</p>
    """)

    expect(page.locator("#status")).to_have_text(
        "Booking Confirmed",
        timeout=2000
    )
