from playwright.sync_api import Page,expect
def test_guest_name(page):
    page.set_content("""
        
<h2>Hotel Booking</h2>

<label for="guest">Guest Name</label>
<input id="guest" type="text">

<button onclick="
    document.getElementById('status').textContent =
        'Booking Confirmed';
">
    Confirm Booking
</button>

<p id="status"></p>

    """)
    page.get_by_label("Guest Name").fill("QA Tester")
    expect(page.get_by_label("Guest Name")).to_have_value("QA Tester")
def test_booking_confirmation(page)	:
    page.set_content("""
            
    <h2>Hotel Booking</h2>
    
    <label for="guest">Guest Name</label>
    <input id="guest" type="text">
    
    <button onclick="
        document.getElementById('status').textContent =
            'Booking Confirmed';
    ">
        Confirm Booking
    </button>
    
    <p id="status"></p>
    
        """)
    page.get_by_role("button",name="Confirm Booking").click()
    expect(page.locator("#status")).to_have_text("Booking Confirmed")