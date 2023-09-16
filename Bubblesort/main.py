
def bubblesort(*args):
    print(args)
    numbers = list(args)
    for i in range (len(numbers)):
        for x in range(0, len(numbers)-1):
            if numbers[x] > numbers [x+1]:
                numbers [x], numbers [x+1] = numbers [x+1], numbers[x]
                print(numbers)
    return(numbers)

print(bubblesort(1,55,11,77,8,5,1,23,9,87,458,48,45,45964,89,489,489,4))


