from flask import Flask
from blueprints.general import app as general
from blueprints.admin import app as admin

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(general)




if __name__ == '__main__':
    app.run()
