# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
new_dict = {}

new_dict.update(first_family)
new_dict.update(second_family)

print(new_dict)
