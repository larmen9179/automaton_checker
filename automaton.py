print("Welcome to the Automaton checker!")
print("First, we'll ask for all the states and symbols and how they work together...")
print("Then you can enter in characters and check if your automaton accepts it!!")
print()

states = []
symbols = []

#Matrix to assign states to states with symbols
transitions = []

done = False

while (not done):
    option = input("Please enter in your state, or type 'done' if you've finished typing states: ")

    if option.lower() == "done":
        done = True
    else:
        states.append(option)


#Re-declaring done as false so we can now check symbols
done = False

while (not done): 
    option = input("Please enter in all the symbols, or type 'done' if you've finished typing symbols: ")

    if option.lower() == "done":
        done = True
    else:
        symbols.append(option)

print(states)
print(symbols)

print("Now we'll ask you how the states transition with symbols")

for i in range(len(states)):
    transitionsToAdd = []
    for j in range(len(symbols)):
        nextState = input("If we are on state " + states[i] " and we see symbol " + symbols[i] + " , what is the next states we go to: ")
        transitionsToAdd.append(nextState)
    
    transitions.append(transitionsToAdd)

