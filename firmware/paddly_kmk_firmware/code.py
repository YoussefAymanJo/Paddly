print("Starting")

import board
import busio
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB 
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306



keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (board.GP3,board.GP5,board.GP7)
keyboard.row_pins = (board.GP2,board.GP4,board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

i2c_bus = busio.I2C(board.GP21, board.GP20)
driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)
display = Display(
    display=display_driver,
    entries=[
            ImageEntry(image="D:\Paddly\Paddly\images\vert_cat.bmp", x=0, y=0),
    ],
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=3,
)
keyboard.extensions.append(display)

rgb = RGB(pixel_pin=board.GP09,
        num_pixels=2,
        val_limit=255,
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=0.5,
        animation_mode=AnimationModes.RAINBOW,
        refresh_rate=144,
        )
keyboard.extensions.append(rgb)

encoder_handler.pins = ((board.GP14, board.GP15,None,False),(board.GP18,board.GP19,None,False))

layer_1 = KC.TG(1)

keyboard.keymap = [
	# 0 layer
	[
		layer_1,KC.NO,KC.MUTE,
        KC.LCTL(KC.C),KC.LCTL(KC.X),KC.LCTL(KC.V),
        KC.LCTL(KC.Z),KC.LGUI(KC.PSCR),KC.LGUI(KC.L)
	],
	# 1 Layer
	[
		layer_1,KC.NO,KC.MPLY,
        KC.F11,KC.TRNS,KC.TRNS,
        rgb.off(),rgb.show(),KC.TRNS
	],
]
encoder_handler.map = [
    #encoder_1
    [
    (KC.BRID,KC.BRIU,KC.NO),(KC.VOLD,KC.VOLU,KC.NO)
    ]
    #encoder_2
    [
        ((KC.LCTRL(KC.KP_MINUS),KC.LCTRL(KC.KP_PLUS)),KC.No),(KC.MPRV,KC.MNXT,KC.NO)
    ]
 ]


if __name__ == '__main__':
    keyboard.go()