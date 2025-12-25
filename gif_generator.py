import imageio.v3 as iio

filenames = ['golf-old_225x302.png','golf-new_225x302.png']

images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('golf.gif', images, duration=500, loop=0)
