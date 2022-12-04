# write your code here

# First part
favorite_animals = ["dog" , "cat" , "monkey" , "rabbit"]

print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove("monkey")
print(favorite_animals)

# Second part

favorite_animals.append("monkey")

for animal in favorite_animals:
    print(f"I Love {animal}")


# Third part

numbers = [5 , 4 , 3 , 2 , 1]
numbers_sum = 0

for number in numbers:
    numbers_sum = numbers_sum + number
print(numbers_sum)