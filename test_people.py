import people
import connexion
import pytest


app = connexion.App(__name__, specification_dir='specification')
app.add_api('swagger.yml')


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_people_add_and_read_all(client):
    with app.app.app_context():
        person = {
            "fname": "Test Name",
            "lname": "Test Lastname",
            "timestamp": people.get_timestamp(),
        }
        people.create(person)
        list_of_people = people.read_all()
        assert 4 == len(list_of_people)

        lname = "Test Lastname"
        people.delete(lname)
        list_of_people = people.read_all()
        assert 3 == len(list_of_people)


def test_people_read_all(client):
    with app.app.app_context():
        list_of_people = people.read_all()
        assert 3 == len(list_of_people)
