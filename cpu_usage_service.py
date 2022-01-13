from daemonize import Daemonize
import psutil
import datetime
import requests
import time

def monitor_cpu_usage():
    ip = '127.0.0.1'
    port = 8001
    while True:
        dt = datetime.datetime.now()
        cpu_usage = psutil.cpu_percent()
        cpu_info_data = {
            'date_time': dt.strftime("%Y-%m-%d %H:%M:%S"),
            'value': cpu_usage
        }
        api_url = f'http://{ip}:{port}/api/records/'
        response = requests.post(api_url, json=cpu_info_data)

        time.sleep(10)

if __name__ == '__main__':
    pid = "/tmp/test.pid"

    print('Start daemon')

    daemon = Daemonize(app="cpu_usage_service", pid=pid, action=monitor_cpu_usage)
    daemon.start()

