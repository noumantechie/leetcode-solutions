# ThirdApproach
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

# Time Compexity O(n)


# Second Approach
#  --------------------------------------Brute Force Approach--------------------------------------------
# nums = [1, 2, 3, 4, 5]

# max_sum = 0
# for start in range(len(nums)):  # Start index of subarray
#     current_sum = 0
#     for end in range(start, len(nums)):  # End index of subarray
#         current_sum += nums[end]
#         max_sum = max(max_sum, current_sum)
# print("Maximum subarray sum:", max_sum)

# Time Complexity = O(n2)


# First Approach
# --------------------------------------Brute force Dynamic calculate sum--------------------------------------------        max_sum = nums[0]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum = nums[0]
# for start in range(len(nums)):  # Start index of subarray
#     for end in range(start, len(nums)):  # End index of subarray
#         subarray_sum = sum(nums[start:end+1])  # Compute sum of subarray
#         max_sum = max(max_sum, subarray_sum)  # Update max sum if larger

# print("Maximum subarray sum:", max_sum)
# Time Complexity O(n3)
