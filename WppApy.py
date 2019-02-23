#Test Whatsapp.Api

# Python 3
import http.client

yourId = "Nope"
yourMobile = "+57"
yourMessage = "What a great day."

c = http.client.HTTPSConnection("NiceApi.net")
c.request("POST", "/API", yourMessage, {"X-APIId": yourId, "X-APIMobile": yourMobile})
response = c.getresponse()
data = response.read()
print(data)
