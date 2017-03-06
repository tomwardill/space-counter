# python imports
import time

# micropython imports
import urequests
import machine


# pin mappings

top_pin = 5 # D5
left_top_pin = 4 # D7
right_top_pin = 16 # D1
centre_pin = 0 # D0
left_lower_pin = 13 # D6
right_lower_pin = 14 # D2
bottom_pin = 12 # D3

# function mappings
numerical_maps = {
    1: [right_top_pin, right_lower_pin],
    2: [top_pin, right_top_pin, centre_pin, left_top_pin, bottom_pin],
    3: [top_pin, right_top_pin, centre_pin, right_lower_pin, bottom_pin],
    4: [left_top_pin, centre_pin, right_top_pin, right_lower_pin],
    5: [top_pin, left_top_pin, centre_pin, right_lower_pin, bottom_pin],
    6: [top_pin, left_top_pin, centre_pin, left_lower_pin, right_lower_pin, bottom_pin],
    7: [top_pin, right_top_pin, right_lower_pin],
    8: [top_pin, left_top_pin, right_top_pin, centre_pin, left_lower_pin, right_lower_pin, bottom_pin],
    9: [top_pin, left_top_pin, right_top_pin, centre_pin, right_lower_pin],
    'e': [top_pin, left_top_pin, centre_pin, left_lower_pin, bottom_pin]
}

pin_maps = {}
for key, value in numerical_maps.items():
    pin_maps[key] = [machine.Pin(x, machine.Pin.OUT) for x in value]

def all_off():
    for pin in pin_maps[8]:
        pin.high()

def display(value):
    all_off()
    for pin in pin_maps[value]:
        pin.low()

all_off()

while True:
    try:
        print("Making request")
        response = urequests.get('http://api.open-notify.org/astros.json')
        number = response.json()['number']
        print(number)
        display(number)
        time.sleep(3600)
    except Exception as e:
        print(e)
        display('e')
        time.sleep(3600)
