# stack=[]
# while True:
#     print("1.push 2.pop 3.exit")
#     n=int(input("enter your choice :"))
#     if n==1:
#         stack.append(input("enter the braces :"))
#         print(stack)
#     elif n==2:
#         stack.pop()
#         print(stack)
#     else:
#         exit(0)
import requests
def message(phone):
        url = "https://www.fast2sms.com/dev/bulk"
        msg = ". \n you have been charged Rs:500/- for parking in no parking zone, please remove your vehicle"
        payload = f"sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={phone}"
        headers = {
                'authorization': "g7I1OrsaLSZRivnDTHQb02XzCA5dolPNmkK3BMu8eJty9YW6jfK9LdhtH1ZuxVR0z4I6mM2iJ8XAjcWY",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
message('9591537379')
