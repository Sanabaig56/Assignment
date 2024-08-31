num_list: list = []
user_name: str = input("What is your name: ")

# Collecting three favorite numbers from the user
for x in range(1, 4):
    num: int = int(input(f"Write your {x} favorite number: "))
    num_list.append(num)

# Greeting the user and showing their favorite numbers
print(f"\nHello, {user_name}, let's explore your favorite numbers:")
print(num_list)

# Checking if each number in the list is even or odd
for item in num_list:
    if item % 2 == 0:
        print(f"{item} is an even number")
    else:
        print(f"{item} is an odd number")

# Printing each number and its square
for item in num_list:
    print(f"{item} and its square: ({item}, {item**2})")

# Calculating the sum of the numbers
sum_of_num: int = sum(num_list)
print(f"Amazing! The sum of your favorite numbers is: {sum_of_num}")

# Checking if the sum is a prime number
is_prime = True
if sum_of_num <= 1:
    is_prime = False
else:
    for x in range(2, sum_of_num):
        if sum_of_num % x == 0:
            is_prime = False
            break

if is_prime:
    print(f"The sum {sum_of_num} is a prime number!")
else:
    print(f"The sum {sum_of_num} is not a prime number.")
