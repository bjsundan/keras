"""
author: Akshay Chawla (https://github.com/akshaychawla)
TEST:rs
Test convert.py's ability to handle Deconvolution and Crop laye
by converting voc-fcn8s .prototxt and .caffemodel present in the caffe/models/segmentation folder
"""
import os
import inspect
import numpy as np
import keras.caffe.convert as convert
from scipy import misc
import matplotlib.pyplot as plt
from subprocess import call

# check whether files are present in folder
"""
path = os.path.dirname(inspect.getfile(inspect.currentframe()))
assert os.path.exists(path + "/deploy.prototxt"), "Err. Couldn't find the debug.prototxt file"
assert os.path.exists(path + "/horse.png"), "Err. Couldn't find the horse.png image file"
if not os.path.exists(path + "/fcn8s-heavy-pascal.caffemodel"):
    call(["wget http://dl.caffe.berkeleyvision.org/fcn8s-heavy-pascal.caffemodel -O "
          + "./" + path + "/fcn8s-heavy-pascal.caffemodel"],
         shell=True)
assert os.path.exists(path + "/fcn8s-heavy-pascal.caffemodel"), "Err. Cannot find .caffemodel file.	\
please download file using command : wget http://dl.caffe.berkeleyvision.org/fcn8s-heavy-pascal.caffemodel "

model = convert.caffe_to_keras(path + "/deploy.prototxt", path + "/fcn8s-heavy-pascal.caffemodel", debug=1)

print ("Yay!")

# 1. load image
img = misc.imread(path + "/horse.png")

# modify it
img = np.rollaxis(img, 2)
img = np.expand_dims(img, 0)

# 2. run forward pass
op = model.predict(img)

# 3. reshape output
op = op[0]
op = op.reshape((500, 500, 21))
op_arg = np.argmax(op, axis=2)

# 4. plot output
plt.imshow(op_arg)
plt.show()

print ("..done")
"""
