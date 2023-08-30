import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database 


# Create class User
class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Anastasiia'
        self.second_name = 'Taran'

    def remove(self):
        self.name = ''
        self.second_name = ''

# Create fixture for User()
@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

# Create fixture for GitHub()
@pytest.fixture
def github_api():
    api = GitHub()
    yield api
    
# Create fixture for Database()
@pytest.fixture
def database():
    db = Database()
    yield db


    