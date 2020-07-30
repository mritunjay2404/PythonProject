name,char = input("Type your name and character :").split(",")
length = len(name)
print(f"The length of your name is {length}")
print(f"Character count: {name.strip().lower().count(char.strip().lower())}")

