#Test Whatsapp.Api

# Python 3
import http.client

yourId = "9Q4iNIzdMEuHpXhlKosmq2NocmlzX2RvdF9tcm45Ml9hdF9nbWFpbF9kb3RfY29t"
yourMobile = "+57"
yourMessage = "What a great day."

c = http.client.HTTPSConnection("NiceApi.net")
c.request("POST", "/API", yourMessage, {"X-APIId": yourId, "X-APIMobile": yourMobile})
response = c.getresponse()
data = response.read()
print(data)
