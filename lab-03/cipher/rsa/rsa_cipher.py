import rsa
import os

class RSACipher:
    def __init__(self):
        self.pub_key_path = "public.pem"
        self.priv_key_path = "private.pem"

    def generate_keys(self):
        try:
            (public_key, private_key) = rsa.newkeys(1024)
            with open(self.pub_key_path, "wb") as pub_file:
                pub_file.write(public_key.save_pkcs1())
            with open(self.priv_key_path, "wb") as priv_file:
                priv_file.write(private_key.save_pkcs1())  # ✅ FIX: ghi thay vì đọc
            return True
        except Exception as e:
            print("Error generating keys: %s" % e)
            return False

    def load_keys(self):
        try:
            if not os.path.exists(self.pub_key_path) or not os.path.exists(self.priv_key_path):
                self.generate_keys()
            with open(self.pub_key_path, "rb") as pub_file:
                public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
            with open(self.priv_key_path, "rb") as priv_file:
                private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
            return private_key, public_key
        except Exception as e:
            print("Error loading keys: %s" % e)
            return None, None

    def encrypt(self, message, key):
        try:
            return rsa.encrypt(message.encode('utf-8'), key)
        except Exception as e:
            print("Encrypt error: %s" % e)
            return b""

    def decrypt(self, ciphertext_bytes, key):
        try:
            decrypted_bytes = rsa.decrypt(ciphertext_bytes, key)
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            print("Decrypt error: %s" % e)
            return ""

    def sign(self, message, private_key):
        try:
            return rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')
        except Exception as e:
            print("Sign error: %s" % e)
            return b""

    def verify(self, message, signature_bytes, public_key):
        try:
            rsa.verify(message.encode('utf-8'), signature_bytes, public_key)
            return True
        except rsa.VerificationError:
            return False
        except Exception as e:
            print("Verify error: %s" % e)
            return False