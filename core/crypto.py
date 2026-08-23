import base64
import hashlib
import os
import hmac

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from core.config import get_settings, Settings

GCM_NONCE_BIT_SIZE = 12

def _get_encryption_key() -> bytes:
    settings = get_settings()
    key = settings.FIELD_ENCRYPTION_KEY.encode('utf-8')
    return hashlib.sha256(key).digest()

def _get_blind_index() -> bytes:
    settings = get_settings()
    return settings.BLIND_INDEX_KEY.encode('utf-8')

def encrypt_field(plaintext:str) -> str:
    if not plaintext:
        return plaintext
    key = _get_encryption_key()
    aes_gcm = AESGCM(key)
    nonce = os.urandom(GCM_NONCE_BIT_SIZE)
    cipher_text = aes_gcm.encrypt(nonce, plaintext.encode('utf-8'),None)
    return base64.b64encode(nonce + cipher_text).decode('utf-8')

def decrypt_field(ciphertext:str) -> str:
    if not ciphertext:
        return ciphertext
    key = _get_encryption_key()
    aes_gcm = AESGCM(key)
    raw_data = base64.b64decode(ciphertext.encode('utf-8'))
    nonce = raw_data[:GCM_NONCE_BIT_SIZE]
    encrypted_data = raw_data[GCM_NONCE_BIT_SIZE:]
    decrypted_bytes = aes_gcm.decrypt(nonce, encrypted_data,None)
    return decrypted_bytes.decode('utf-8')


def hash_email(email:str) -> str:
    if not email:
        return email
    key = _get_blind_index()
    normalized_email = email.strip().lower()
    return hmac.new(key, normalized_email.encode('utf-8'), hashlib.sha256).hexdigest()