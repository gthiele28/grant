#3.1
def say_goodbye(name):
    print("Goodbye " + name)

#3.2
def circle_area(radius):
    print((radius ** 2) * 3.14)

#4.1
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#5.1
def temp_range(lst):
    return (min(lst), max(lst))

#5.2
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False
    
#5.3
def get_mpg(distance, fuel):
    return distance/fuel

#5.4
def encrypt_data(data):
    return int(str(data)[-1] + str(data)[0:-1])

#6.1
def new_pow(x, y):
    total = 1
    for i in range(y):
        total *= x
    return total

#6.2.1
def find_min(lst):
    save = lst[0]
    for i in lst:
        if i < save:
            save = i
    return save


def find_max(lst):
    save = lst[0]
    for i in lst:
        if i > save:
            save = i
    return save

#6.2.2
def while_min(lst):
    i = 1
    save = lst[0]
    while i < len(lst):
        if lst[i] < save:
            save = lst[i]
        i+=1
    return save

def while_max(lst):
    i = 1
    save = lst[0]
    while i < len(lst):
        if lst[i] > save:
            save = lst[i]
        i+=1
    return save

#6.3
def digit_sum(val):
    dsum = 0
    while val:
        dsum += val % 10
        val //=10
    return dsum

test = int(input("Number to compute digit sum: "))
print("The sum of the digits in " + str(test) + " is " + str(digit_sum(test)))