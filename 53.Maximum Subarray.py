nums = [1, 2, 3, 4, 5]

max_sum = 0
for start in range(len(nums)):  # Start index of subarray
    current_sum = 0
    for end in range(start, len(nums)):  # End index of subarray
        current_sum += nums[end]
        max_sum = max(max_sum, current_sum)
print("Maximum subarray sum:", max_sum)
