def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/height**2
    print(bmi)
    rslt=-2
    if bmi<18.5:
        rslt = -1

    elif 18.5<=bmi<=25.0:
        rslt = 0

    elif bmi>=25.0:
        rslt = 1

    print(rslt)
    return rslt


calculate_bmi(weight=57, height=1.73)
