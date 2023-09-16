numbers = [40, 24, 60, 15, 52, 98, 46, 7, 27, 40, -5, -2, 69]

for i in range (len(numbers)):
    for x in range(0, len(numbers)-1):
        if numbers[x] > numbers [x+1]:
            numbers [x], numbers [x+1] = numbers [x+1], numbers[x]
            print(numbers)



print("Sorted Numbers: " + str(numbers))
