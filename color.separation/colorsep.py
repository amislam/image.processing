#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# read the image.
x = plt.imread("./images.jpeg")
print (x.shape)
# rows * columns * 3 bytes for each pixcel RGB

# create 3 copies of the image -- xr=x will create a referece not a copy!
xr= np.copy(x)
xg= np.copy(x)
xb= np.copy(x)

xr_= np.copy(x)
xg_= np.copy(x)
xb_= np.copy(x)


# set zeros in Grean and Blue
xr[:,:,1:]=0
xr_[:,:,0]=0

# set zeros in Red and Blue
xg[:,:,0]=0
xg[:,:,2]=0
xg_[:,:,1]=0

# set zeros in Red and Grean
xb[:,:,0]=0
xb[:,:,1]=0
xb_[:,:,2]=0

plt.imsave("./red.jpeg",    xr)
plt.imsave("./_red.jpeg",   xr_)
plt.imsave("./green.jpeg",  xg)
plt.imsave("./_green.jpeg", xg_)
plt.imsave("./blue.jpeg",   xb)
plt.imsave("./_blue.jpeg",  xb_)

