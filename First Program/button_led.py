from gpiozero import LED, Button
from time import sleep

# Initialize LED and Button
led = LED(4)
button = Button(17)  # Connect push button to GPIO 18

# LED state tracking
led_state = False

print("LED Control with Push Button")
print("Press the button to toggle LED on/off")
print("Or type '0' to turn off, '1' to turn on, 'q' to quit")

while True:
    # Check if button is pressed
    if button.is_pressed:
        led_state = not led_state  # Toggle LED state
        if led_state:
            led.on()
            print("LED turned ON")
        else:
            led.off()
            print("LED turned OFF")
        sleep(0.3)  # Debounce delay to prevent multiple triggers
    
    # Check for keyboard input (non-blocking)
    try:
        import sys
        import select
        
        # Check if there's input available (non-blocking)
        if select.select([sys.stdin], [], [], 0.1)[0]:
            user_input = input().strip()
            
            if user_input == '1':
                led.on()
                led_state = True
                print("LED turned ON")
            elif user_input == '0':
                led.off()
                led_state = False
                print("LED turned OFF")
            elif user_input.lower() == 'q':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Use '0', '1', or 'q' to quit.")
    except:
        pass  # No input available, continue with button monitoring
    
    sleep(0.1)  # Small delay to prevent excessive CPU usage
