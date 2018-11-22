from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

from servos.controller import servosRoute
app.register_blueprint(servosRoute)

from luces.controller import lucesRoute
app.register_blueprint(lucesRoute)

from sensores.controller import sensoresRoute
app.register_blueprint(sensoresRoute)

@app.route('/')
def root():
    return app.send_static_file('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
