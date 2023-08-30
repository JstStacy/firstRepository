import pytest

# Create a group of tests that check user name. The mark 'check' was used

@pytest.mark.check
def test_check_name(user):
    assert user.name == 'Anastasiia'
   

@pytest.mark.check
def test_check_second_name(user):
    assert user.second_name == 'Taran'