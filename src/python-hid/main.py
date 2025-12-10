import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Press, Release, Tap, Macros

# Instantiate KMK and all modules
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
encoderh = EncoderHandler()
keyboard.modules.append(encoderh)
keyboard.modules.append(Layers)
keyboard.extensions.append(MediaKeys())

# PINDEFS
# see /graphics/kicad-schematic.png or the kicad schematic files
## 4x3 matrix - 12 keys
keyboard.row_pins = [board.D26, board.D27, board.D38, board.D29] # Pads 1-4 GPIO26-29
keyboard.col_pins = [board.D0, board.D2, board.D1]               # Pads 7,8,9 GPIO0-2
keyboard.diode_orientation = DiodeOrientation.COL2ROW            # Diodes have dir COLUMN to ROW
## Rotary encoder
encoderh.pins = ((board.D3, board.D4))                           # Pads 11,10 GPIO3-4
# FIXME: When I have physical prototype figure out all the correct parameters for the encoder
# encoderh.divisor = 4
## I2C display
SDA = board.D6
SCL = board.D7
# TODO: Figure out if and what to do with the display on the HID version


# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.P1, KC.P2, KC.P3, KC.P0,
     KC.P4, KC.P5, KC.P6, KC.MO(1),
     KC.P7, KC.P8, KC.P9, KC.KP_ENTER],
    
    # TODO: Make a 2nd layer; consult Tomko
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS]
]
encoderh.map = [ # NOTE: The press function is not wired as all pins are used
    [KC.VOLD, KC.VOLU, None],
    [KC.BRID, KC.BRIU, None]
]

if __name__ == '__main__':
    keyboard.go()