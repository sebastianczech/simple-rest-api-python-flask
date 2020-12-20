import people


def test_people_add_and_read_all():
    person = {
        "fname": "Test Name",
        "lname": "Test Lastname",
        "timestamp": people.get_timestamp(),
    }
    list = people.create(person)
    assert 4 == len(list)


def test_people_read_all():
    list_of_people = people.read_all()
    assert 3 == len(list_of_people)
