word = ["Red", "Green", "Blue"]
myWords = iter(word)

for i in word:
    print(next(myWords))

ban = "Banana"
print("\n")
banexecute = iter(ban)
for b in ban:
    print(next(banexecute))