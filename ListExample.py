numbers = [23, 45, 56, 23, 234, 89]

numbers.append(34)
numbers.insert(2, 45)
numbers.remove(23)
temp = numbers[3]
# temp_not_legal = numbers[10] - illegal command - index out of range

for number in numbers:
    add = number + 10
    print(add)


cities = ["Rome", "London", "Paris", "Jerusalem", "Acre"]
city = "London"
if "London" in cities:
    print("yes")
