#WAP function to remove a given word from a list ad strip it at the same time.
def rem(l, word):
    for item in l:
        l.remove(word)
        return l
l = ["akshat","Amit","Ayush","Amitabh"]

print(rem(l, "Ayush"))