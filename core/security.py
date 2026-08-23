from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(plaintext: str) -> str:
    """
    Get hash for the plain text password provided.
    :param plaintext:
    :return:
    """
    return password_context.hash(plaintext)

def verify_password(plaintext: str, hashed: str) -> bool:
    """
    Check if the entered password is same as a the hashed password stored on the persistence layer
    :param plaintext:
    :param hashed:
    :return:
    """
    return password_context.verify(plaintext, hashed)