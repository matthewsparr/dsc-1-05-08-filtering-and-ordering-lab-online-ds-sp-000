def select_all_female_dogs_name_and_breed():
    return "SELECT name, breed FROM dogs2 WHERE gender = "F""

def select_all_dogs_names_in_alphabetical_order():
    return "SELECT name FROM dogs2 ORDER BY name"

def select_nameless_dog():
    return "SELECT * FROM dogs2 WHERE name is NULL"

def select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest():
    return "SELECT name, breed FROM dogs2 WHERE hungry = 1 ORDER BY age"

def select_name_age_and_temperament_of_oldest_dog():
    return "SELECT name, age, temperament FROM dogs2 ORDER BY age DESC LIMIT 1"

def select_name_and_age_of_three_youngest_dogs():
    return "SELECT name, age FROM dogs2 ORDER BY age LIMIT 3"

def select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest():
    return "SELECT name, breed FROM dogs2 WHERE age BETWEEN 5 AND 10"

def select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order():
    return "SELECT name, age, hungry FROM dogs2 WHERE age BETWEEN 2 AND 7 AND hungry = 1 ORDER BY name"
