from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    ndc_x = 0.3
    ndc_y = -0.6

    screen_x = (ndc_x + 1) * 400
    screen_y = (-ndc_y + 1) * 300

    return render_template('index.html', screen_x=screen_x, screen_y=screen_y)

if __name__ == '__main__':
    app.run(debug=True)
