
nums = [12, 34, 2, 6, 7896]

count = 0

for num in nums:
    if len(str(num)) % 2 == 0:
        count = count + 1
print(count)
