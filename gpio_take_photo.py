from signal import pause
from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime

button = Button(18)
red_led = LED(21)
camera = PiCamera()

def button_pressed():
    print("Button pressed.")
    print('taking photo')
    timestamp = datetime.now().isoformat()
    camera.capture('/home/wilson/Pictures%s.jpg' % timestamp)
    red_led.on()

def button_released():
    print("Button released.")
    red_led.off()

red_led.off()
button.when_pressed = button_pressed
button.when_released = button_released
print("Press CTRL-C to exit.")
pause()
