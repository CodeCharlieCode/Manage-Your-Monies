from flask import Flask, render_template

from controllers.merchants_controller import merchants_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.category_controller import category_blueprint
from controllers.profile_controller import profile_blueprint

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(profile_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)