# put your python code here
duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

print(duration * food_cost + (duration - 1) * hotel_cost + 2 * flight_cost)
