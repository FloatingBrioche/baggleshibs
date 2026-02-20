from pytest import mark

from lib.ship import Ship


@mark.it("Initialises with .length attr as passed int")
def test_initialises_with_a_given_length():
    ship = Ship(length=5)
    assert ship.length == 5

@mark.it("Initialises with .health attr equal to .length")
def test_initialises_with_a_health_attr_eq_length():
    ship = Ship(length=5)
    assert ship.health == 5

@mark.it("Initialises with a .body attr of type list")
def test_initialises_with_a_body_attr_of_list_type():
    ship = Ship(length=5)
    assert isinstance(ship.body, list)

@mark.it(".body is a list of 'S' of length equal to .length")
def test_len_body_attr_list_eq_length():
    ship = Ship(length=5)
    assert ship.body == ["S", "S", "S", "S", "S"]