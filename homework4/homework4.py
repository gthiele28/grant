#3.  Lists

#3.1
foods = ["salmon", "french fries", "pancakes", "eggs", "hash browns"]

print(foods[1])
print(foods[-1])
foods.append("shrimp")
foods.insert(0,"apple")
del(foods[2])
print(len(foods))

for i in foods:
    print(i.upper())

new_foods = foods[0::5]

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

#3.2

#bug 1: I struggled to get numbers to store the output of the range function and not just the function itself at first
#Using the list caster ultimately solved the issue
numbers = list(range(21))

def get_first_15(nums):
    return nums[:15] #Bug 3 - this wasn't working at first, I had to go back and change the number because I forgot one wouldn't work properly

def get_every_fifth(lst):
    return lst[::5]

def reverse_and_stride(lst):
    lst.reverse()
    return lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_fifth(step1)
step3 = reverse_and_stride(step2)

#3.3
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(nums):
    sum = 0
    
    for i in nums:
        for j in i:
            sum += j
    
    return sum

#3.4
def make_5x5():
    all = []
    for i in range(5):
        all.append([])
        for j in range(5):
            all[i].append(i*5 + j + 1)
    return all

grid = make_5x5()

def replace_3s(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] % 3 == 0:
                nums[i][j] = "?"
    return nums

new_grid = replace_3s(grid)

def sum_valid(nums):
    sum = 0
    for i in nums:
        for j in i:
            if j != "?":
                sum += j
    return sum

new_sum = sum_valid(new_grid)

#4
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mariam"] = 100
ages["Milana"] = 52
del(ages["Mariam"])

for i in ages:
    print(i + ": " + str(ages[i])) #Bug 2: syntax error first tieme writing, forgot a + to concatenate string and to cast the age to a string

grid = make_5x5()
print(replace_3s(grid))