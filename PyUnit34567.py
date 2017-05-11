#Unit 3: PygLatin - part 10
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
    
#Unit 4: Taking a Vacation - part 7
def hotel_cost(nights):
    return 140*nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost
        
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)

#Unit 5: A Day at the Supermarket - part 12
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] = stock[item] -1
    return total
#Unit 6: Student Becomes the Teacher - part 9
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    average = float(total)/len(numbers)
    return average
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * average(student["homework"]) + 0.3 * average(student["quizzes"]) + 0.6 * average(student["tests"]);
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score:
        return "B"
    elif 70 <= score:
        return "C"
    elif 60 <= score:
        return "D"
    else: 
        return "F"
    return get_letter_grade(get_average(lloyd))
    
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
print get_class_average(students)
print get_letter_grade(get_class_average(students))
