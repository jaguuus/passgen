import string
import secrets

apl = string.ascii_letters + string.digits + string.punctuation
password = ''.join (secrets.choice(apl) for i in range (30))

print(password)