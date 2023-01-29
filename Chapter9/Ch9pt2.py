# secrs/secr_rand.py
import secrets
print(secrets.choice('Choose one of these words'.split()))
print(secrets.randbelow(10 ** 6))
print(secrets.randbits(32))


# secrs/secr_rand.py
print(secrets.token_bytes(16))
print(secrets.token_hex(32))
print(secrets.token_urlsafe(32))


# secrs/secr_gen.py
import secrets
from string import digits, ascii_letters
def generate_pwd(length=8):
    chars = digits + ascii_letters
    return ''.join(secrets.choice(chars) for c in range (length))
def generate_secure_pwd(length=16, upper=3, digits=3):
    if length < upper + digits + 1:
        raise ValueError('Nice try!')
    while True:
        pwd = generate_pwd(length)
        if (any(c.islower() for c in pwd)
            and sum(c.isupper() for c in pwd) >= upper
            and sum(c.isdigit() for c in pwd) >= digits): 
            return pwd
print(generate_secure_pwd())
print(generate_secure_pwd(length=3, upper=1, digits=1))


# secrs/secr_reset.py
import secrets 
def get_reset_pwd_url(token_length=16):
    token = secrets.token_urlsafe(token_length)
    return f'https://example.com/reset-pwd/{token}'
print(get_reset_pwd_url())
