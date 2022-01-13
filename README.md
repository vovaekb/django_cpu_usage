# django_cpu_usage

Simple client - server system for collecting informatin about CPU usage.
Components:
- Python Django server
- Python client script

Features:
- client running as daemon
- client send CPU usage every 10 seconds
- SQLite used for storing CPU information

## Run application
Clone the repo, change to the project root folder. Install dependencies from requirements.txt file:

```bash
pip install -r requirements.txt
```
Run the application:
```bash
python manage.py runserver 8001
```

Run the client script:
```bash
python3 cpu_usage_service.py
```
To see the running service use command
```bash
ps ax | grep cpu_usage_service
```
You can see page with last 100 records on page: 
To see records API data open page:  http://127.0.0.1:8001/api/records.
