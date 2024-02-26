# LED Effects for RaspberryPi via network message

Welcome to the LED Controller System, designed to enhance your applications with vibrant LED lighting effects. This system enables you to control RGB LEDs connected to a Raspberry Pi, offering various animations like breathing, blinking, and fading to enrich user experiences.
## Components
### led_server.py

- **Main Feature**: Controls RGB LEDs through the RGBLEDController class, allowing for dynamic lighting effects.
- **Initialization**: Requires GPIO pin configuration for the RGB LEDs. 
- **Functionalities**:
  - Animation configurations (fade speed, breath speed, blink times). 
  - Direct LED color setting and animation control (looping, activation, interruption). S
- **Server Integration**: Utilizes the ServerThread class to listen for external commands, enabling dynamic control over LED animations.

### minidisplay.py

**Purpose**: Displays console logs remotely, facilitating debugging and monitoring of the LED Controller system from any location.

### client.py

**Functionality**: Sends commands to the LED server (led_server.py), allowing users to remotely control LED animations and settings.

## Getting Started

1. Ensure your Raspberry Pi is set up with RGB LEDs connected to the specified GPIO pins.
1. Incorporate the led_server.py in your application to control LED animations based on your needs.
1. Use minidisplay.py to monitor system logs remotely for easier troubleshooting and monitoring.
1. Utilize client.py to send custom LED commands to the server, offering flexibility in controlling the LED effects dynamically.

## Example Usage
1. start led_server.py to ensure listening to new LED effect Commands
    ```sh
    python3 led_server.py
    ```

2. a) Set the color to green via keyboard input:
   ```sh
   python3 client.py
   ```
   1. Type in "color 255 0 0" and hit enter

       
2. b) Set the color to green via a python skript:

```python
import socket

def send_msg_to_LED(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((LED_HOST, LED_PORT))
        client_socket.sendall(command.encode('utf-8'))

LED_HOST = 'localhost'
LED_PORT = 12345
        
send_msg_to_LED("color 255 0 0")
```
## Tips

- Use calming breathing effects during idle times for ambiance.
- Employ bright blinks to indicate key actions like photo capture or payment confirmation.
- Align LED color themes with your application or event branding for cohesive experiences.