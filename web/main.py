from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import Flask
from multiprocessing import cpu_count, Process

monkey.patch_all()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '200 Ok'

def run(fork):
    if not fork:
        WSGIServer(('0.0.0.0', 8080), app).serve_forever()
    else:
        http_server = WSGIServer(('0.0.0.0', 8080), app)
        http_server.start()

        def serve_forever():
            http_server.start_accepting()
            http_server._stop_event.wait()

        for i in range(cpu_count()):
            p = Process(target=serve_forever)
            p.start()

if __name__ == '__main__':
    run(fork=False)
