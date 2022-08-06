#! python3
# resizeAndAddLogo.py - Resizes all iamges in current working ceratory to fit
# in a 300x300 square, and adds catlogo.pnt to the lower-right coner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withlogo', exist_ok=True)

# Loop over all file in the working direcoty.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue    # skip on-image file and the logo file teself
    
    im = Image.open(filename)
    width, height = im.size


    # Check if image need to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # Resize the image.
        print('Resizing %s ..' % (filename))
        im = im.resize((width, height))

        # Add the logo.
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)


        # Save changes.
        im.save(os.path.join('withlogo', filename))

