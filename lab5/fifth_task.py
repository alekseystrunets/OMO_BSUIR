
nums = [0, 1234, 5, 30, 8, 15, 12, 1]
print("Изначальный список:", nums)
for i in range(len(nums)):
    if nums[i] < 15:
        nums[i] *= 2

print("Новый список:", nums)