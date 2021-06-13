# put your python code here
first_event = [int(input()) for i in range(3)]
second_event = [int(input()) for i in range(3)]

first_seconds = first_event[0] * 3600 + first_event[1] * 60 + first_event[2]
second_seconds = second_event[0] * 3600 + second_event[1] * 60 + second_event[2]

print(second_seconds - first_seconds)
