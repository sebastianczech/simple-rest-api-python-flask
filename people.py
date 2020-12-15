from flask import make_response, abort
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


people = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return [people[key] for key in sorted(people.keys())]


def read_one(lname):
    if lname in people:
        person = people.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    return person


def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    if lname not in people and lname is not None:
        people[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    if lname in people:
        people[lname]["fname"] = person.get("fname")
        people[lname]["timestamp"] = get_timestamp()
        return people[lname]
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    if lname in people:
        del people[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
