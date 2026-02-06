items = []

while True:
    item = input("Enter an item: ")
    
    if item.lower() == "done":
        break
    
    items.append(item)
    
    print(f"'{item}' has been added to the list.")

print("\nYour complete list:")
if items:
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
else:
    print("No items were added.")