import bmi as bmi
def test_bmi_normal_weight() :
    weight = 72
    height = 1.75
    result = bmi.calculate_bmi(height, weight)
    assert(result == 0)
def test_bmi_over_weight():
    weight = 90
    height = 1.70
    result = bmi.calculate_bmi(height, weight)
    assert(result == 1)
def test_bmi_under_weigh():
    weight = 50
    height = 1.80
    result = bmi.calculate_bmi(height, weight)
    assert(result == -1)