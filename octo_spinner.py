from keyboard import on_release_key, on_press_key
from mouse import move
from util import get_position, Value
from time import sleep

# Adjust these for your screen resolution, use calibrate_center.py
CENTER_X, CENTER_Y = 959.5, 539.5

RADIUS = 300

# Progress increments, per SLEEP_DURATION seconds
ROTATE_LEFT = 0.00044
ROTATE_NONE = 0.00054
ROTATE_RIGHT = 0.00064

SLEEP_DURATION = 0.0001

if __name__ == '__main__':
    enabled = Value(False)
    progress_inc = Value(ROTATE_NONE)
    progress = Value(0)

    def rotate_left(_):
        progress_inc(ROTATE_LEFT)
    
    def rotate_right(_):
        progress_inc(ROTATE_RIGHT)
    
    def rotate_none(_):
        progress_inc(ROTATE_NONE)

    def toggle(_):
        if enabled(not enabled()):
            print("Toggled OFF")
        else:
            print("Toggled ON")

    on_press_key(',', rotate_left)
    on_press_key('.', rotate_right)
    on_release_key('\'', toggle)

    on_release_key(',', rotate_none)
    on_release_key('.', rotate_none)

    print("Ready.")
    print("Press ['] to toggle.")
    print("Hold [<] to rotate counter-clockwise.")
    print("Hold [>] to rotate clockwise.")

    try:
        while True:
            if enabled():
                x, y = get_position(RADIUS, progress())

                x += CENTER_X
                y += CENTER_Y

                move(x, y)

                progress(progress() + progress_inc())
                sleep(SLEEP_DURATION)
    except KeyboardInterrupt:
        print("Exiting.")