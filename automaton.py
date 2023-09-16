print("Welcome to the Automaton checker!")
print("First, we'll ask for all the states and symbols and how they work together...")
print("Then you can enter in characters and check if your automaton accepts it!!")
print()

states = []
symbols = []

done = False

while (not done):
    option = input("Please enter in your state, or type 'done' if you've finished typing states: ")

    if option.lower() == "done":
        done = True
    else:
        states.append(option)

print(states)
print(symbols)

#Re-declaring done as false so we can now check symbols
done = False