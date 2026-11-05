from playwright.sync_api import Page,expect
def test_guest_name(hotel_page:Page):
    hotel_page.get_by_label("Guest Name").fill("QA Tester")
    expect(hotel_page.get_by_label("Guest Name")).to_have_value("QA Tester")
def test_booking_confirmation(hotel_page:Page):
    hotel_page.get_by_role("button",name="Confirm Booking").click()
    expect(hotel_page.locator("#status")).to_have_text("Booking Confirmed")