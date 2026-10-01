print('Введите числа: ')
threshold = float(input())
n = int(input())

total = n
errors = 0
pr_count = 0
max_temp = None
sum_temp = 0.0
v_count = 0

for _ in range(n):
    line = input().strip()
    
    if line == "error":
        errors += 1
    else:
        temp = float(line)
        v_count += 1
        sum_temp += temp
        
        if temp > threshold:
            pr_count += 1

        if max_temp is None or temp > max_temp:
            max_temp = temp

average_temp = sum_temp / v_count if v_count > 0 else 0.0
print('Вывод: ')
print(total)
print(errors)
print(pr_count)
print(f"{max_temp:.1f}")
print(f"{average_temp:.1f}")
