# Second Approach
#  --------------------------------------Kadane's Algorithm--------------------------------------------
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = nums[0]
current_sum = 0

for num in nums:
    current_sum += num
    max_sum = max(max_sum, current_sum)
    if current_sum < 0:
        current_sum = 0

print("Maximum subarray sum:", max_sum)


# First Approach
#  --------------------------------------Brute Force Approach--------------------------------------------
# nums = [1, 2, 3, 4, 5]

# max_sum = 0
# for start in range(len(nums)):  # Start index of subarray
#     current_sum = 0
#     for end in range(start, len(nums)):  # End index of subarray
#         current_sum += nums[end]
#         max_sum = max(max_sum, current_sum)
# print("Maximum subarray sum:", max_sum)
