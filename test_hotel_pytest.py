def test_booking_id():
    booking_id = 1001
    assert booking_id == 1001
def test_hotel_city():
    city = "Hyderabad"
    assert city == "Hyderabad"
def test_total_amount():
    room_price = 2000
    nights = 3
    total_amount = room_price * nights
    assert total_amount == 6000