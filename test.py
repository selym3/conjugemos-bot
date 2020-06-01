from conjug_wrapper import Conjug

conjug = Conjug()

while True:
    word = input("english word: ")
    if word == ".":
        break
    print(conjug.get_all(word))
