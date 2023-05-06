
import sys
import requests

web_host = "https://dispensego.com"
machine_host = "http://localhost"
order_id = sys.argv[1]
log = ""

url = web_host + "/wp-json/dispensgo/v1/order-check/" + order_id
headers = {}

response = requests.get(url, headers=headers, verify=False)
json_result = response.json()

valid = json_result.get('result', False)
if valid:
    products = json_result['products']
    
    url = machine_host + "/avend?action=start"
    headers = {}
        
    response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
    log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
    print(response.text)
    
    for p in products:
        url = machine_host + "/avend?action=add&code=" + p
        response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
        log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
        print(response.text)
        
    url = machine_host + "/avend?action=dispense"
    response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
    log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
    print(response.text)
    
else:
    message = json_result.get('message', response.text)
    log += datetime.now().strftime('%H:%M:%S') + " - " + message + "\n"
    print(message)

with open(datetime.now().strftime('%m_%d_%y') + '.txt', 'a') as f:
    f.write(log + "\n")