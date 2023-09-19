

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

#Declaring starting and ending states
s0 = input("Which of these states is the starting state? :")

sf = input("Which of these states is the ending state? : ")
sf = states.index(sf)

#Re-declaring done as false so we can now check symbols
done = False

while (not done): 
    option = input("Please enter in all the symbols, or type 'done' if you've finished typing symbols: ")

    if option.lower() == "done":
        done = True
    else:
        symbols.append(option)

print("List of states: ") 
print(states)

print("List of symbols: ")
print(symbols)
print("Now we'll ask you how the states transition with symbols")

for i in range(len(states)):
    transitionsToAdd = []
    for j in range(len(symbols)):
        nextState = input("If we are in state " + states[i] + " and we see symbol " + symbols[j] + " , what is the next state we go to: ")
        transitionsToAdd.append(nextState)
    
    transitions.append(transitionsToAdd)

#Printing the matrix for output
print("Matrix of state transitions: ")
for i in range(len(transitions)):
    print(transitions[i])


#Checking if the input is read by the automata
print("Now we'll check if your input is accepted by this automaton...")

userString = input("Enter in your string: ")
userArray = list(userString)

currentState = s0

for i in range(len(userArray)):
    currentState = states.index(currentState)

    currentState = transitions[int(currentState)][int(symbols.index(userArray[i]))]

if states.index(currentState) != sf:
    print("The user's input was not accepted :(")
else:
    print("The user's input was accepted! :)")


