from src.pricing import apply_coupon, calc_total


def test_calc_total_adds_tax_to_every_line():
    assert calc_total([(10.0, 2), (5.0, 1)]) == 30.0


def test_calc_total_with_an_explicit_tax():
    assert calc_total([(10.0, 2)], 0.0) == 20.0
    assert calc_total([(10.0, 2)], 0.5) == 30.0


def test_calc_total_rounds_to_cents():
    assert calc_total([(0.333, 1)], 0.0) == 0.33


def test_calc_total_of_an_empty_cart():
    assert calc_total([]) == 0


def test_apply_coupon():
    assert apply_coupon(100.0, 25) == 75.0
