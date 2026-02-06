print("***password entry***")
password = ""
while password != "secret123":
    password = input("enter password: ")
    if password != "secret123":
        print("Wrong password, please try again")
print("Access granted")
print("\n")


print("shopping cart = panier d'achat")
item = ""
while item != "done":
    item = input("Add item: ")
    if item != "done":
        print(f"Added {item}")