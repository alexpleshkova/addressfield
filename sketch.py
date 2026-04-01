import py5
import random
import py5_tools

images_files = ['26rn260.jpg', '32rn291-copy.jpg', '32rn292.jpg','33rn300-01.jpg', '39rn330.jpg', '40rn334-01.jpg', '73rn-01-copy.jpg', '73rn-02-copy.jpg']
images = []


def setup():
    py5.size(3500, 2480)
    py5.background("#B5B5B5")  
    py5.image_mode(py5.CENTER)
    for filename in images_files:
        img = py5.load_image(filename)
        print(f"Loaded {filename} with size: {img.width}x{img.height}")
        images.append(img)

def draw():
    
    img = random.choice(images)
    if img:
        py5.image(
                img, 
                py5.random(-500, 3500), #x
                py5.random(-500, 2480), #y
                py5.random(1000), #width
                py5.random(1000), #height /not random == img too big on screen
                py5.random_int(1, 5000), #x upleft c /why 10000?
                py5.random_int(1, 5000), #y upleft c /upleft vals shd be smaller
                py5.random_int(5000, 10000), #x lowright c
                py5.random_int(5000, 10000)  #y lowright c
        ) 
    else:
        print('no img loaded')
    #if 100 <= py5.frame_count <= 110:
        #py5.save_frame("output/frame###.jpg")
    
py5.run_sketch() #python sketch.py (to run), 
