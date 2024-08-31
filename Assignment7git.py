num_list : list = []
user_name : str = input ("what is your name: ")

for x in range(1,4):
    num : int = int(input(f"Write your {x} favorite number : "))
    num_list.append(num)
   
print(f"\nHello, {user_name} lets explore your favorite numbers:")

print(num_list)

for items in num_list:
if item % 2 == 0:
    print (f"{item} is even number")
else:
    print(f"{item} is odd number")

for item in num_list:
    print(f"{item} and its square:({item},{item**2})")
sum_of_num : int =sum(num_list)
print(f"Amazing! the sum of your favorite numbers is: {sum_of_num}")

is_prime = True
if sum_of_num <=1:
    is_prime = False
if x in range (2,sum_of_num)
if sum_of_num % x == 0:
    is_prime = False