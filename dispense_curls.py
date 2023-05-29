
import sys
import requests

# web_host = "https://dispensego.com"
web_host = "http://localhost:9090/"
machine_host = "http://localhost:9090"
order_id = 22 # sys.argv[1]
log = ""

url = web_host + "/order-check/{}".format(order_id)
headers = {}

response = requests.get(url, headers=headers, verify=False)
json_result = response.json()
print( json_result )
valid = json_result.get('order', False)
print("valid?{} ".format( valid ))
# if valid:
products = json_result['products']
    
url = machine_host + "/avend?action=start"
#     headers = {}
        
#     response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
#     log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
#     print(response.text)
    
#     for p in products:
#         url = machine_host + "/avend?action=add&code=" + p
#         response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
#         log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
#         print(response.text)
        
#     url = machine_host + "/avend?action=dispense"
#     response = requests.get(url, headers=headers, cookies=requests.cookies.RequestsCookieJar())
#     log += datetime.now().strftime('%H:%M:%S') + " - " + response.text + "\n"
#     print(response.text)
    
# else:
#     message = json_result.get('message', response.text)
#     log += datetime.now().strftime('%H:%M:%S') + " - " + message + "\n"
#     print(message)

# with open(datetime.now().strftime('%m_%d_%y') + '.txt', 'a') as f:
#     f.write(log + "\n")