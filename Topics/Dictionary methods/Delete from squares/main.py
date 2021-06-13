key = int(input())
print(squares[key] if key in squares else "There is no such key")
if key in squares:
    del squares[key]
print(squares)
