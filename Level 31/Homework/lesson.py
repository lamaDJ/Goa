# my_surname = "Molashvili"  

# user_surname = input("Enter your surname: ")

# if my_surname.lower() == user_surname.lower():
#     print("Our surnames are similar.")
# else:
#     print("We have different surnames.")

# ----------------------------------------------------------------------------------------------------------------------------------

# food = ["burger", "fries", "soda", "pizza"]
# food.pop()
# food.append("broccoli")
# print(food)

# -----------------------------------------------------------------------------------------------------------------------------------

my_name = "Andria"

user_name = input("Enter your name: ")

first_match = my_name[0].lower() == user_name[0].lower()
last_match = my_name[-1].lower() == user_name[-1].lower()

if first_match and last_match:
    print(2)
elif first_match or last_match:
    print(1)
else:
    print(0)