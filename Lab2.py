
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    z = get_user_input()
    calc_average_temperature(z)
    calc_min_max_temperature(z)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def get_user_input():
    print("Enter multiple decimal number with spacing in between : ")
    x = input()
    y = x.split(",")
    z = [float(w) for w in y]
    return z
def calc_average_temperature(z):

    average = sum(z)/len(z)
    print("The average temperature of all the temperature is " +str(average))
    return average
def calc_min_max_temperature(z):
    p = [min(z),max(z)]
    print("The minimum temperature is "+str(p[0]))
    print("The maximum temperature is "+str(p[1]))
main()