# Space Counter

This is mostly a toy project that will use the [Open Notify API](http://open-notify.org/) to display the number of people in a 7 segment display, using micropython on an ESP8266
Depressingly, a single 7 digit display is adequate to count the number of people in space at this point in time (early 2017).

## Usage

1. Alter `boot.py` to contain your WiFi access point name and password
2. Upload `boot.py` and `mapping.py` to your ESP board
3. Use `mapping.py` to figure out the pin values for `main.py`
4. Update and upload `main.py`
5. Reboot your ESP
6. Check it actually works

## Using mapping.py

On a terminal to your ESP do:
```python
import mapping
mapping.run_pin_test()
```

At this point, it will output what pin it thinks it is lighting up, drop this number into the correct place in `main.py`

## Caveats

* Only tested on a WeMos D1 Mini ESP8266 board.
* You may want to check what pins I've soldered to before running `run_pin_test`, or update that with the pins you've actually used.
