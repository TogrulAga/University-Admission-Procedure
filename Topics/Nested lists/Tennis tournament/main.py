n = int(input())
players = [input().split() for line in range(n)]
winners = list(filter(lambda x: x[1] == "win", players))
names = list(map(lambda x: x[0], winners))
print(names, len(names), sep='\n')
