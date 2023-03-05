import http.server
import socketserver
from prometheus_client import start_http_server, REGISTRY
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily
import time
import random


PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

#TEMP = 35 , HEART = 72


class CustomCollector(object):     ## Class for CustomCollector which helps us to use different metric types
    
    def __init__(self):
        pass
    
    def collect(self):
        server_status = 1     ## place the logic here to get the server status
        cpu_usage = 7
        ramlal = 3  		  ## place the logic here to get the CPU Usage.

        temp , heart , fall, smoke, humidity= random.randint(25,40) , random.randint(65,80) , random.randint(0,2) ,random.randint(300 , 400) , random.randint(0,100)
        
        value1 = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        #value.add_metric(["server_status"], server_status)
        value1.add_metric(['TEMP'],temp)

        value2 = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        value2.add_metric(['HEART'],heart)
        
        value3 = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        value3.add_metric(['SMOKE'],smoke)

        value5 = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        value5.add_metric(['HUMIDITY'],humidity)

        battery = 75

        value4 = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        value4.add_metric(['BATTERY'],battery)


              
        yield value1
        yield value2
        yield value3
        yield value4
        yield value5


def run_http() :

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()





if __name__ == '__main__':
    start_http_server(8000)         ## port where metrics need to be exposed.
    #run_http()

    
        
    REGISTRY.register(CustomCollector())
    #REGISTRY.register(CustomCollector())

    while True:
        time.sleep(30)		       ## To collect the metrics for every 30s.

