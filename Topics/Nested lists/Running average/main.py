number = list(input())

running_avg = []

for i in range(len(number)-1):
    running_avg.append((int(number[i]) + int(number[i+1])) / 2)

print(running_avg)
