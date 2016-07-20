from twilio import Rest

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd24d8e331df193bfb4d80d038a924013"
auth_token  = "81e78d03f16caffa104c6f905024215"
Client = rest.TwilioRestClient (account_sid, auth_token)

mesage = client.sms.messages.create(
    body="My name is Ron Burgandy?",
    to="+1260530----",    #Where you put in your number
    from_="+1260344----") #where you put in twilio's number
print message.sid
