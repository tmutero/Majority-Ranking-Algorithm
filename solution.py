def find_majority_of_contains(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > len(nums) // 2:
        return candidate
    else:
        return "No majority element"

input1 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
input2 = [3, 3, 4, 2, 4, 2, 2]

output1 = find_majority_of_contains(input1)
output2 = find_majority_of_contains(input2)

print("Output 1:", output1)
print("Output 2:", output2)
