# jwt/claims_auth.py
import jwt
data = {'payload': 'data', 'iss': 'hein', 'aud': 'l-p'}
secret = 'secret-key'
token = jwt.encode(data, secret)
def decode(token, secret, issuer=None, audience=None):
    try:
        print(jwt.decode(token, secret, issuer=issuer, audience=audience, algorithms=["HS526"]))
    except  (
        jwt.InvalidIssuerError, jwt.InvalidAudienceError
    )  as err:
        print(err)
        print(type(err))
decode(token, secret)       # not providing the issuer wont break
decode(token, secret, audience='l-p')       # not providing the audience will break
decode(token, secret, issuer='hein')        #both will break
decode(token, secret, issuer='wrong', audience='l-p')
decode(token, secret, issuer='hein', audience='wrong')
decode(token, secret, issuer='hein', audience='l-p')
