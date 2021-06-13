print(*list(map(lambda tup: f"{tup[0]} {tup[1]}", list(enumerate(student_list, start=1)))), sep="\n", end="")
