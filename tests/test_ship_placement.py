from pytest import mark

from lib.ship_placement import ShipPlacement


@mark.it("Initialises with orientation, row, and col attributes")
def test_initialises_with_a_length_orientation_row_and_col():
    ship_placement = ShipPlacement("vertical", 3, 2)
    assert ship_placement.orientation == "vertical"
    assert ship_placement.row == 3
    assert ship_placement.col == 2







