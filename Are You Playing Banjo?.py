def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return (name+" "+"plays banjo")
    else:
        return (name+" "+"does not play banjo")
name=input("enter the name: ")
print(are_you_playing_banjo(name))
