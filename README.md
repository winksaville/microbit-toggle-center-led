# toggle-center-led

When button a is pressed turn on the center LED, pixel[2,2].

```
# Turn on the center display LED when Button A is pressed
from microbit import *

PIXEL_LEVEL_MAX_ON: int = 9
PIXEL_LEVEL_MIN_ON: int = 1
PIXEL_LEVEL_OFF: int = 0

PIXEL_ON: int = PIXEL_LEVEL_MAX_ON
PIXEL_OFF: int = PIXEL_LEVEL_OFF

# Center Pixel
PIXEL_X: int = 2
PIXEL_Y: int = 2

# Set initial conditions
print("Starting with pixel off");
display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_OFF)
prev_pixel_state: int = PIXEL_OFF

# Loop changing pixel state when button is pressed or released
while True:
    if button_a.is_pressed():
        display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_ON)
        if prev_pixel_state == PIXEL_OFF:
            print("Pixel is on")
            prev_pixel_state = PIXEL_ON
    else:
        display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_OFF)
        if prev_pixel_state == PIXEL_ON:
            print("Pixel is off")
            prev_pixel_state = PIXEL_OFF
```

## Build and Run

On one terminal start `minicom` or other app capable of
using the serial port:
```
minicom -D /dev/ttyACM0
```

Now in the other terminal be sure you've got a
`venv enabled` activated with `uflash` then run
`uflash toggle-center-led.py`
```
(micro-bit-uflash) wink@fwlaptop 24-01-05T20:33:07.923Z:~/prgs/micro-bit/MicroPython/button_a-led22 (main)
$ uflash button_a-led22.py 
Flashing button_a-led22.py to: /run/media/wink/MICROBIT/micropython.hex
(micro-bit-uflash) wink@fwlaptop 24-01-05T20:33:27.137Z:~/prgs/micro-bit/MicroPython/button_a-led22 (main)
$
```

In the other terminal you'll see `Starting with pixel off`,
where X is the `loop_number`.
```
Starting with pixel off
```

If you press and hold button A `Pixel is on` is added:
```
Starting with pixel off
Pixel is on
```

When you release button A `Pixel is off` is added:
```
Starting with pixel off
Pixel is on
Pixel is off
```

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http:
```
or what I do is `ls /dev/tty*` and 
Plug in the microbit into the computers USB port.
```
uflash print.py
```

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.

