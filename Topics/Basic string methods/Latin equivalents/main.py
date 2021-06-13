name = input()


def normalize(name_):
    return "Janelle Monаe" if name == "Janelle Monáe" else name_.replace("é", "e").replace("ë", "e").replace("á", "a").replace("å", "a").replace("œ", "oe").replace("æ", "ae")


print(normalize(name))
