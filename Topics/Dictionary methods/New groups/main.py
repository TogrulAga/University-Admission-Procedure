# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
classes = dict.fromkeys(groups, None)
n_groups = int(input())

for g in range(n_groups):
    classes[list(classes.keys())[g]] = int(input())

print(classes)
