from twilio.rest import Client

account_sid = 'ACb0427ef95333ae4596222e44752e1787'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG3b3cf35c3a9a6209228129bb4e61a340',
  to='+16099151091'
)

print(message.sid)