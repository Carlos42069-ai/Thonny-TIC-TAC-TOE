even_counter = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_counter += 1
    
print("The total even numbers are: ", even_counter)