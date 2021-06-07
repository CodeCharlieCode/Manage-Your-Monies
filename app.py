from flask import Flask, render_template

from controllers.merchants_controller import merchants_blueprint

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)