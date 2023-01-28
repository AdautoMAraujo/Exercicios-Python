import sketchpy
from sketchpy import canvas
obj = sketchpy.canvas.sketch_from_image('186993.jpg')
obj.draw(threshold=155)
