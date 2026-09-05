def sum(nums):
    total = 0
    for num in nums:
        total += num
    return(total)
def even(nums):
    even = 0
    odd = 0
    for num in nums:
        if num%2 == 0:
            even+=1
        else:
            odd+=1
    return(even,odd)
n = int(input("Enter how many numbers you want in the list: "))
nums = []
for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)
print(nums)
print("Even Count: ",even(nums)[0])
print("Odd Count: ",even(nums)[1])
# print("Sum: ",sum(nums))