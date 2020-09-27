def crash_course(dltr):
    result = 0
    temp = 1

    for i in range(1, dltr):
        temp = temp * i
        for k in range(i):
            result += temp
    return result

print(crash_course(4))