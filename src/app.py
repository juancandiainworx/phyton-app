from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route("/")
def root():
    return "OK", 200

@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little human, Vdddhhhhdd  rrr  yhghhhhfew <3',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route('/api/v1/details')

def details():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'ESTE ES UN NUEVO MENSAJE DE DETALLES   PARA EL USUARIO y nuevos cambios',
    })

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)

