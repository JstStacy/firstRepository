def test_remove_name(user):
    user.name = ''
    assert user.name == ''

def test_name(user):
    assert user.name == 'Anastasiia'

def test_second_name(user):
    assert user.second_name == 'Taran'
