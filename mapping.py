import machine

pins = [
    14,
    13,
    5,
    16,
    12,
    4,
    0
]


def run_pin_test():
    for pin in pins:
        print("Current pin: {}".format(str(pin)))
        m = machine.Pin(pin, machine.Pin.OUT)
        m.low()
        input('Next...')
