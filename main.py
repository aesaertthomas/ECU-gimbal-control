import pyglet
from pyglet import shapes
import random as rand
import time

from model.Current import Current
from model.Target import Target
from model.Resolution import Resolution



def generate_target() -> Target:
    rand_x_offset = rand.randint(100, int(round(resolution.xsize * 0.75, 0)))
    rand_y_offset = rand.randint(100, int(round(resolution.ysize * 0.75, 0)))
    target = Target(parx=rand_x_offset, pary=rand_y_offset, pardiameter=10)

    return target

def create_window(movement_speed : int, current : Current, target : Target):
    batch = pyglet.graphics.Batch()

    current_circle = shapes.Circle(current.x, current.y, current.radius, color=current.color, batch=batch)
    target_circle = shapes.Circle(target.x, target.y, target.radius, color=target.color, batch=batch)

    #Calculate the differences in distance
    x_diff = target.x - current.x
    y_diff = target.y - current.y


    horizontal_base = shapes.Line(current.x, current.y, current.x + x_diff, current.y,width=5, color=(0,0,255), batch=batch)
    vertical_base = shapes.Line(target.x, target.y, target.x, target.y - y_diff, width=5, color=(0,255,0), batch=batch)

    @window.event
    def on_draw():
        window.clear()  # Clear the window with black background
        batch.draw()  # Draw the circles

    def close_window(dt):
        pyglet.app.exit()  # Exit the application after a delay


    # Schedule the window to close after 0.5 second
    pyglet.clock.schedule_once(close_window, 0.15)

    # Run the application (will automatically close after 1 second)
    pyglet.app.run()


    #Euclidian Division
    distance = (x_diff **2 + y_diff**2) ** 0.5
    if distance > 10:
        x_to_add = int(round((x_diff / distance) * movement_speed,0))
        y_to_add = int(round((y_diff / distance) * movement_speed,0))

        x_change = current.x + x_to_add
        y_change = current.y + y_to_add

        current.x = x_change
        current.y = y_change


        if x_to_add > 0:
            x_command = "UP"
        else:
            x_command = "DOWN"

        if y_to_add > 0:
            y_command = "UP"
        else:
            y_command = "DOWN"

        print(f"x: {current.x} \t y: {current.y}, \t x-change: {x_to_add} {x_command} \t y-change: {y_to_add} {y_command}")


    else:
        print("bye")
        time.sleep(2)
        return

    create_window(movement_speed=5, current=current, target=target)  # Ask the user again after closing the window




resolution = Resolution(parresolution=(1280, 720))
current = Current(parx=resolution.middle_x, pary=resolution.middle_y, pardiameter=10)
window = pyglet.window.Window(resolution.xsize, resolution.ysize, "Yellow Dot Example", resizable=False)

create_window(movement_speed=25, current=current, target=generate_target())
