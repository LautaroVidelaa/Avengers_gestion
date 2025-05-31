from flask import Flask
from controllers.avengers_controller import avengers_bp

app = Flask(__name__, template_folder='templates')
app.register_blueprint(avengers_bp)

if __name__ == '__main__':
    app.run(debug=True)
