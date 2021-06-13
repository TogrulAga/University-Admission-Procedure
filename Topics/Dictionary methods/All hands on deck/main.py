deck = {str(key): key for key in range(2, 11)}
deck.update(Jack=11)
deck.update(Queen=12)
deck.update(King=13)
deck.update(Ace=14)

print(sum(deck[input()] for i in range(6)) / 6)
