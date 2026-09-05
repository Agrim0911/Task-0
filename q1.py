''' Outputs sum of elements of input array '''
def sum(nums):
    total = 0
    for num in nums:
        total += num
    return(total)

''' Outputs the number of even and odd elements in the input array '''
def even(nums):
    even = 0
    odd = 0
    for num in nums:
        if num%2 == 0:
            even+=1
        else:
            odd+=1
    return(even,odd)

''' Outputs a sorted array using merge sort '''
def merge_sort(nums):
    sorted_list=[]
    if len(nums) > 1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                sorted_list.append(left[i])
                i+=1
            else:
                sorted_list.append(right[j])
                j+=1
        while i<len(left):
            sorted_list.append(left[i])
            i+=1
        while j<len(right):
            sorted_list.append(right[j])
            j+=1
    return(sorted_list)



n = int(input("Enter how many numbers you want in the list: "))
nums = []
for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)
sorted_list = merge_sort(nums)

print("Largest: ",sorted_list[-1])
print("Smallest: ",sorted_list[0])
print("Sum: ",sum(nums))
print("Even Count: ",even(nums)[0])
print("Odd Count: ",even(nums)[1])
print("Reversed: ",nums[::-1])
