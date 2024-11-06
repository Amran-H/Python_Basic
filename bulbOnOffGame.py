is_bulb_on=False

def display_bulb_state():
    if is_bulb_on:
        print("The bulb is ON")
    else:
        print("The bulb is OFF")

def toggle_bulb():
    global is_bulb_on
    is_bulb_on = not is_bulb_on
    display_bulb_state()

for i in range(1, 1000):
    command=str(input("Enter command (on/off/exit): ").strip().lower())
    
    if command == "on":
        if not is_bulb_on:
            toggle_bulb()
        else:
            print("The bulb already is ON")
                   
    elif command == "off":
        if  is_bulb_on:
            toggle_bulb()
        else:
            print("The bulb is already OFF")           
    elif command == "exit":
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid command. Please enter on, off, or exit ")