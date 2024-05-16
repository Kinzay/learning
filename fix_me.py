def calculate_average(nums_list: list):
    total = sum(nums_list)
    count = len(nums_list)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
