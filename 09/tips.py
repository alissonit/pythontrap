import requests

sep, num = ("##", 30)

######################################## tips 01 ########################################
print(num * sep + " TIPS 01 " + num * sep)

r = requests.get("https://httpbin.org/")

print(f"headers: \n{r.headers}") #get headers

print(f"status code: {r.status_code}") #get status code

######################################## tips 02 ########################################
print(num * sep + " TIPS 02 " + num * sep)

payload = {"page": 1, "count": 10}

r = requests.get("https://httpbin.org/get", params=payload) #using params

print(r.url)

######################################## tips 03 ########################################
print(num * sep + " TIPS 03 " + num * sep)

payload = {"username": "pythontrap", "password": "pythontrap2021"}

r = requests.post("https://httpbin.org/post", data=payload) #send data

data_json = r.json() #JSON decoder

print(data_json["form"])

######################################## tips 04 ########################################
print(num * sep + " TIPS 04 " + num * sep)

r = requests.get("https://httpbin.org/basic-auth/pythontrap/pythontrap2021", auth=("pythontrap",
 "pythontrap2021")
)
print(r.text)

#testing error
r = requests.get("https://httpbin.org/basic-auth/pythontrap/pythontrap2021", auth=("pythontrap","pythontrap2022"))

print(r)

######################################## tips 05 ########################################
print(num * sep + " TIPS 05 " + num * sep)
try:
    r = requests.get("https://httpbin.org/delay/4", timeout=3)
    print(r.content)
except requests.exceptions.Timeout as errorTimeout:
    print(errorTimeout)