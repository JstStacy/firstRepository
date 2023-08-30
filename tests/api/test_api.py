import pytest


# Name removal test. The mark 'change' was used
@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

# The test check that username is Anastasiia
@pytest.mark.check
def test_name(user):
    assert user.name == 'Anastasiia'

# The test check that second name is Taran
@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Taran'
