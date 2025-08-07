# def missing_number(nums):
#     n = len(nums)
#     return n * (n + 1) // 2 - sum(nums)

# print(missing_number([3, 0, 1]))  # 2

def missing_number(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    missing = expected_sum - actual_sum
# checks if the number provided have a missing number or not 
    if missing in numbers or missing > n:    
        return "No missing number"
    else:
        return missing


print(missing_number([3, 0, 1]))       # 2
print(missing_number([0, 1, 2, 3]))    # No missing number
