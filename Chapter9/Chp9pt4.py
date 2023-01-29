# jwt/claims_time.py
from datetime import datetime, timedelta, timezone
from time import sleep, time 
import jwt
iat = datetime.now(tz=timezone.utc)
nfb = iat + timedelta(seconds=1)
exp = iat + timedelta(seconds=3)
data = {'payload': 'data', 'nbf': nfb, 'exp': exp, 'iat': iat}
def decode(token, secret):
    print(time())
    try:
        print(jwt.decode(token, secret, algorithms=['HS256']))
    except  (
        jwt.ImmatureSignatureError, jwt.ExpiredSignatureError
    ) as err:
        print(err)
        print(type(err))
secret = 'secret-key'
token = jwt.encode(data, secret)
decode(token, secret)
sleep(2)
decode(token, secret)
sleep(2)
decode(token, secret)