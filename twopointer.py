# def two_sum_sorted(arr, target):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target:
#             return [left, right]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return None

# a = two_sum_sorted([1,2,3,4,5],6)
# print(a)

def method(nums1,nums2):
    nums = sorted(nums1+nums2)
    left,right = 0, len(nums) -1
    while left<right:
        left+=1
        right-=1
        if left+1 == right:
            return float(nums[left]+nums[right])/2.0
    return float(nums[left]) if len(nums)%2!=0 else sum(nums)/2


a = method([1,3],[2])
print(a)



