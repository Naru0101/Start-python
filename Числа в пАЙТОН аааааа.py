start = int(input('input start range:'))
end = int(input('input end range:'))
prime_numbers = []
for num in range(start,end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
print("Prime numbers in the range from", start, "in", end, ":", prime_numbers)                