import requests
import re
import time
import subprocess
import sys

categories = sys.argv[1::]
sleep_seconds = 30

print('categories:', categories)

task_re = re.compile('<a href="/tasks/(.*?)">(.*?)</a>')

def notify(task):
    print("New task: " + task[1])
    subprocess.run(["notify-send", "New task #" + task[0] + ": " + task[1]])

def fetch_list():
    response = requests.get("https://freelance.habr.com/tasks?categories=" + ','.join(categories))
    return re.findall(task_re, response.text)

last_task_id = int(fetch_list()[0][0])

while True:
    time.sleep(sleep_seconds)
    print("update")
    for item in fetch_list()[::-1]:
        task_id = int(item[0])
        if task_id > last_task_id:
            notify(item)
            last_task_id = task_id 

print(last_task_id)
