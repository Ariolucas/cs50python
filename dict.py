
words = set()

def check(word):
    if word in words:
        return True
    else:
        return False

def size():
    return len(words)

def load(dictionary):
    file = open(dictionary, "r")
    word = line.rstrp()
    for line in file:
        words.add(word)
    close(file)
    return True


def unload():
    return True
