print("Exit the loop when number is 5")
number = 0
while True:
    print(number)
    if number == 5:
        break
    number += 1
print("\n")


print("Exit the loop when i is 3")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("\n")


num = 0
while True:
    print(num)
    num += 1
    if num == 5:
        print("Breaking out of loop")
        break
print("\n")


print("Question1: shopping cart")

while True:
    item = input("Enter an item to add: ")
    if item == "done":
        break
    print(f"Successfully added: {item}")
print("\n")


print("Question2: build a list of items")

items = []

while True:
    item1 = input("Enter an item: ")

    if item1 == "done":
        break

    items.append(item1)

    print(f"{item1} has been added to the list.")

print(f"The the complete list of items is: {items}")