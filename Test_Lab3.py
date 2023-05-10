import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
def test_bubble_sort_more_than_ten():
    result = []
    input_arr = [23, 33, 45, 65, 54, 78, 12, 24, 43, 95, 67]
    result = len(input_arr)

    if result > 10 :
        x = 1
        print(x)
    assert(x==1)
    return x
def test_bubble_sort_zero():
    result = []
    input_arr = []
    result = len(input_arr)

    assert(result ==0)
    return result
def test_bubble_sort_not_integers():
    result = []
    input_arr = [10.5, 6, 7, 8, 15, 16]
    result=(type(input_arr))
    if result != int:
        z = 2
        print(z)
    assert(z==2)
    return z
