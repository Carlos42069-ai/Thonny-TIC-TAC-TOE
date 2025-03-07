odd_counter = 0

for i in range(10):
    num = int(input(f"Enter a number {i+1}:"))
    if num % 2 != 0:
        odd_counter +=1
print("Total odd numbers: ", odd_counter)

    