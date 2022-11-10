
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# group by endpoint rather than path
metrics = PrometheusMetrics(app, group_by='endpoint', path='/metrics')

# static information as metric
metrics.info('app_info', 'Demo webapp for Prevail', version='1.0.0')

@app.route('/')
@metrics.counter(
    'home_visits', 'Number of invocations of root path')
def hello():
    return '''
    <h2>Simple WebApp Demo for Prevail</h2>
    <p>For Prometheus metrics use /metrics</p>
    <a href="metrics">/metrics</a>
    '''
  

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = False)
