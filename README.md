# Handwritten To Text Output (HTTO)
## Authors: Armando Cabrera & Jaime Andrade
This is a still-in-work prototype for the course CS4361 at The University of Texas at El Paso.


## Required Libraries
- pip install Flask
- pip install tensorflow
- pip install numpy
- pip install Image
- pip install BytesIO
- pip install jsonify

## Download files from Repository
- server_test -> app.py
- server_test -> templates -> index.html
- server_test -> static -> script.js, style.css
- models -> handwritten_character_model_enhanced.h5
  #
(OPTIONAL)
- handwritten_test_images
- dataset

# User Interface

Once you have downloaded all required files, in your preferred coding environment run this command in the terminal:
- python .\server_test\app.py

You will be prompted with tensorflow activation routine, amongst in there will be a line:
- 'Running on http://127.0.0.1:0000'
## Cntrl + Click on that link
You will then be prompted with a screen similar to the one below

<img width="1280" alt="image" src="https://github.com/mando34/HTTO/assets/89607986/11a8b1cf-1fc8-4c41-804c-fe214db01c13">

## Intuitive from Now on!
- Simply just upload the desired image you wish the model to 'attempt' to read
- Click on 'Upload'
- and BOOM, will probably be the incorrect output but will eventually get it right.

<img width="480" alt="image" src="https://github.com/mando34/HTTO/assets/89607986/0cd9f711-842d-47fc-9fbd-16b1507796d4">
<img width="480" alt="image" src="https://github.com/mando34/HTTO/assets/89607986/86bc4279-ad0b-48a9-a551-f7dd475d3bc8">



