import time
from graphics import draw_pixel
from ray_tracer import ray_trace

while True:
    ray_trace(draw_pixel)
    time.sleep(0.1)
