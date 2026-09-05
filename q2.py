def process_list(numbers):
    copy = numbers.copy()
    test=[]
    for num in copy:
        if num<0:
            test.append(num)
    for num in test:
        copy.remove(num)
    copy.append(0)
    copy.sort()
    return(copy)

n = int(input("Enter how many numbers you want in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
print("Original:", numbers)
print("Result:", process_list(numbers))
