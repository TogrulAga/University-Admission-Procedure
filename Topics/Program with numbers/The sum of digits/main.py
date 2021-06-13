# put your python code here
number = int(input())
sum_ = 0
for i in range(1, len(str(number)) + 1):
    sum_ += number % (10**i) / 10 ** (i - 1)
    number -= number % (10 ** i)
print(int(sum_))
