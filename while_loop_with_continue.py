print("Continue to the next iteration if i is 3:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("\n")


print("Odd numbers")
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(f"Odd number: {counter}")
