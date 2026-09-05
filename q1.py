def sum(nums):
    total = 0
    for num in nums:
        total += num
    return(total)
n = int(input("Enter how many numbers you want in the list: "))
nums = []
for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)
print(nums)
print("Sum: ",sum(nums))