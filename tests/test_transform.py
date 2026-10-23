from src.transform import clean_amount


def test_clean_amount():
    assert clean_amount("$1,200.50") == 1200.50