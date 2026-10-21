from src.legacy_export import export_rows
from src.promotions import seasonal_price
from src.reports import quarterly_revenue


def test_quarterly_revenue_looks_calc_total_up_by_name_and_excludes_tax():
    assert quarterly_revenue([[(10.0, 2)], [(5.0, 1)]]) == 25.0


def test_export_rows_totals_each_order_with_tax():
    assert export_rows([[(10.0, 2)], [(5.0, 1)]]) == [{"total": 24.0}, {"total": 6.0}]


def test_seasonal_price_takes_ten_percent_off():
    assert seasonal_price(100.0) == 90.0
