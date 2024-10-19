import math

WIDTH = 320
HEIGHT = 240

sphere_pos = (160, 120, 50)  
light_pos = (100, 50) 

def shade(normal, light_direction):
    intensity = max(0, normal[0] * light_direction[0] + normal[1] * light_direction[1])
    return int(255 * intensity)

def ray_trace(draw_pixel):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            ray_dir = (x - WIDTH / 2, y - HEIGHT / 2)
            ray_length = math.sqrt(ray_dir[0]**2 + ray_dir[1]**2)

            if ray_length > 0:
                ray_dir = (ray_dir[0] / ray_length, ray_dir[1] / ray_length)

            dx = x - sphere_pos[0]
            dy = y - sphere_pos[1]
            if dx**2 + dy**2 <= sphere_pos[2]**2:
                normal = (dx / sphere_pos[2], dy / sphere_pos[2])
                light_direction = (light_pos[0] - x, light_pos[1] - y)
                light_length = math.sqrt(light_direction[0]**2 + light_direction[1]**2)

                if light_length > 0:
                    light_direction = (light_direction[0] / light_length, light_direction[1] / light_length)

                color = shade(normal, light_direction)

                draw_pixel(x, y, color)
