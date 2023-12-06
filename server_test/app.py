from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the trained model outside the route to avoid reloading it for each request
model = tf.keras.models.load_model("models/handwritten_character_model_enhanced.h5")
# model = tf.keras.models.load_model("handwritten_text_recognition_rnn_letters_model.h5")

def preprocess_image(file):
    from PIL import Image
    from io import BytesIO
    img = Image.open(BytesIO(file.read())).convert("L").resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


def predict_character(image_path):
    input_image = preprocess_image(image_path)
    predictions = model.predict(input_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
     # Mapping from class index to ASCII value
    ascii_mapping = {
        0: ord('0'), 1: ord('1'), 2: ord('2'), 3: ord('3'), 4: ord('4'),
        5: ord('5'), 6: ord('6'), 7: ord('7'), 8: ord('8'), 9: ord('9'),
        10: ord('A'), 11: ord('B'), 12: ord('C'), 13: ord('D'), 14: ord('E'),
        15: ord('F'), 16: ord('G'), 17: ord('H'), 18: ord('I'), 19: ord('J'),
        20: ord('K'), 21: ord('L'), 22: ord('M'), 23: ord('N'), 24: ord('O'),
        25: ord('P'), 26: ord('Q'), 27: ord('R'), 28: ord('S'), 29: ord('T'),
        30: ord('U'), 31: ord('V'), 32: ord('W'), 33: ord('X'), 34: ord('Y'),
        35: ord('Z'), 36: ord('a'), 37: ord('b'), 38: ord('c'), 39: ord('d'),
        40: ord('e'), 41: ord('f'), 42: ord('g'), 43: ord('h'), 44: ord('i'),
        45: ord('j'), 46: ord('k'), 47: ord('l'), 48: ord('m'), 49: ord('n'),
        50: ord('o'), 51: ord('p'), 52: ord('q'), 53: ord('r'), 54: ord('s'),
        55: ord('t'), 56: ord('u'), 57: ord('v'), 58: ord('w'), 59: ord('x'),
        60: ord('y'), 61: ord('z'),
    }
    predicted_ascii = ascii_mapping.get(predicted_class, ord('?'))
    predicted_character = chr(predicted_ascii)
    return predicted_character


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Predict the character
        predicted_character = predict_character(file)

        # Return the prediction as JSON
        return jsonify({'prediction': predicted_character})

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
