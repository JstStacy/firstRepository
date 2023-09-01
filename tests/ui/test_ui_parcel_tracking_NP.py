from modules.ui.page_objects.parcel_tracking_NP import ParcelTracking
import pytest
import random
import string

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


@pytest.mark.ui_NP
def test_check_incorrect_tth():
    # Create page object
    find_parcel = ParcelTracking()

    # Open https://track.ukrposhta.ua/tracking_UA.html?barcode=
    find_parcel.go_to()

    # Generate a random string of length 15
    random_tth = random_string(15)

    # Try to enter the random TTH
    find_parcel.try_to_find_parcel(random_tth)

    # Check that page name meets expectations
    assert find_parcel.check_title('Трекінг відправлень | Укрпошта')

    # Close the browser
    find_parcel.close()