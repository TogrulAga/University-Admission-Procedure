# the following line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
print(*[f"{password} {len(password)}" for password in sorted(passwords, key=len)], sep='\n')
