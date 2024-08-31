user_name : str = input ("write your name: ")
for x in range(1,4):S
    num1 : int = int(input(f"Write your {x} favorite name : "))

print(f"\nHello, {user_name} lets explore your favorite name:")







#Three Favorite Numbers
for x in range(1,4):
    num = int(input(f"enter your{x} favorite number: "))
    num-list.append(num)



#check if the Number even or odd
print(f"\nHello, {user_name}!Lets enjoy your favorite numbers:\n")
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")

#Display each number and its square
print()
for num in num-list:
    print (f"The number {num} and its square: ({num}, {num **2})")

#Calculate and Display the Sum of the numbers
sum_numbers = sum(num_list)
print(f"\nAmazing! the sum of your favorite numbers is: {sum_numbers}\n")