from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/3D')
def threeD():
    return render_template('3D_Model.html')

if __name__ == '__main__':
    app.run()
