firstname = input("Please enter your first name")
surname = input("Please enter your surname")
age = input("Please enter your age")
dateofbirth = input("Please enter your birthday(Just Year)")
list = [firstname, surname, age, dateofbirth]
for i in list:
    print(i)

if list[2] < '18':
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
