def find_fibonacci(number, mem = {}):
    if number in mem:
        return mem[number]

    if number in [0, 1]:
        mem[number] = number
        return number
        
    fibo =  find_fibonacci(number-1, mem) + find_fibonacci(number-2, mem)
    mem[number] = fibo
    return fibo

print(find_fibonacci(99)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
