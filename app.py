from flask import Flask, render_template, request
import base64
from cairosvg import svg2png

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('draw.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.form['svg']
    with open('drawing.svg', 'w') as file:
        file.write(data)
    return 'Saved'

if __name__ == '__main__':
    app.run(debug=True)
