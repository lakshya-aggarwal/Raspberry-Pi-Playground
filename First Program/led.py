from gpiozero import LED

led = LED(17)

while True:
    # Get input from user for LED control (0 for off, 1 for on)
    user_input = input("Enter 0 to turn LED off or 1 to turn it on: ")

    if user_input == '1':
        led.on()
    elif user_input == '0':
        led.off()
    else:
        print("Invalid input. Exiting program.")
        break
