"""
Basic image augmentation using the Augmentor lib for Python. 
Have to transform the label if changing the shape or orientation.

References:
- https://github.com/mdbloice/Augmentor
"""
import os 

import Augmentor

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
IMAGE_PATH = os.path.join(ROOT_PATH, "images")

p = Augmentor.Pipeline(IMAGE_PATH)

# Here you will define the pipeline of transformations etc.

p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.sample(10)