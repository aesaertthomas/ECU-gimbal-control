import pyglet
from pyglet import shapes
import random as rand
import time

from model.Current import Current
from model.Target import Target
from model.Resolution import Resolution

resolution = Resolution(parresolution=(1280, 720))

current = Current(parx=resolution.middle_x, pary=resolution.middle_y, pardiameter=10)

window = pyglet.window.Window(resolution.xsize, resolution.ysize, "Yellow Dot Example", resizable=False)




def create_window(proceed : int, delay : float, i : int):

    if i >= proceed:
        print("Bye")
        time.sleep(1)
        return
    i += 1
    print(f"Iteration: {proceed}")
    batch = pyglet.graphics.Batch()

    # Generate random offsets
    rand_x_offset = rand.randint(100, int(round(resolution.xsize * 0.75, 0)))
    rand_y_offset = rand.randint(100, int(round(resolution.ysize * 0.75, 0)))

    target = Target(parx=rand_x_offset, pary=rand_y_offset, pardiameter=10)


    current_circle = shapes.Circle(current.x, current.y, current.radius, color=current.color, batch=batch)
    target_circle = shapes.Circle(target.x, target.y, target.radius, color=target.color, batch=batch)

    #Calculate the differences in distance
    x_diff = target.x - current.x
    y_diff = target.y - current.y

    print("X-Diff: ", x_diff)
    print("Y-Diff: ", y_diff)
    print()
    print(current)
    print(target)

    horizontal_base = shapes.Line(current.x, current.y, current.x + x_diff, 360,width=5, color=(0,0,255), batch=batch)
    vertical_base = shapes.Line(target.x, target.y, target.x, target.y - y_diff, width=5, color=(0,255,0), batch=batch)

    @window.event
    def on_draw():
        window.clear()  # Clear the window with black background
        batch.draw()  # Draw the circles

    def close_window(dt):
        pyglet.app.exit()  # Exit the application after a delay


    # Schedule the window to close after 1 second
    pyglet.clock.schedule_once(close_window, delay)

    # Run the application (will automatically close after 1 second)
    pyglet.app.run()

    create_window(proceed=proceed, i=i, delay=delay)  # Ask the user again after closing the window



# Start the process
iterations = int(input("How many iterations would you like to do?: "))
wait = float(input("How long would you like to wait between every entry?: "))
create_window(proceed=iterations, i = 0, delay=wait)
