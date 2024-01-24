from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['GET'])
def translate():
    # Get the string from the request
    string = request.form.get('string')

    # Translate the string
    result = translator.translate('I  LOVE YOU', dest='de')
    translated_string = result.text

    # Return the translated string
    return jsonify({'translated_string': translated_string})

if __name__ == '__main__':
    app.run(debug=True)
