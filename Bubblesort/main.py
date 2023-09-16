
def bubblesort(order,numbers):
    #numbers = list(args)
    #print(numbers)
    for i in range (len(numbers)):
        for x in range(0, len(numbers)-1):
            if order == 0:
                if numbers[x] > numbers[x + 1]:
                    numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
                    #print(numbers)
            if order == 1:
                if numbers[x] < numbers [x+1]:
                    numbers [x], numbers [x+1] = numbers [x+1], numbers[x]
                    #print(numbers)
    return(numbers)



select_order = int(input("Write 0 to sort by ascending order and 1 otherwise: "))

user_numbers = input("Enter your numbers separated by commas: ").split(",")
user_numbers = [int(x) for x in user_numbers]


print(bubblesort(select_order,user_numbers))

