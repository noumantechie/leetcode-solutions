# First Approach
#  --------------------------------------Using Direct Integer Division--------------------------------------------
nums = [12, 34, 2, 6, 7896]


def count_digits(n):
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return digits


count = 0
for num in nums:
    if count_digits(num) % 2 == 0:
        count += 1

print(count)


# Second Approach
# -------------------------------------Using String Conversion ----------------------------------------------

# count = 0

# for num in nums:
#     if len(str(num)) % 2 == 0:
#         count = count + 1
# print(count)
