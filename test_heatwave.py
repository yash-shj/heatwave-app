from heatwave import check_heatwave, classify_regions

def test_check_heatwave_true():
    assert check_heatwave('Nagpur', 42.0) is True

def test_check_heatwave_false():
    assert check_heatwave('Pune', 36.0) is False

def test_check_heatwave_boundary():
    assert check_heatwave('Nashik', 40.0) is True

def test_classify_regions():
    readings = {'Mumbai': 38.5, 'Nagpur': 42.0}
    result = classify_regions(readings)
    assert result == {'Mumbai': 'NORMAL', 'Nagpur': 'ALERT'}