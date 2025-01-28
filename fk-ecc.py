from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


def generate_keys():
    # Generate ECC key pair
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message):
    # Sign the message
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return signature


def verify_signature(public_key, message, signature):
    # Verify the signature
    try:
        public_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False


# Main function
def main():
    # Generate keys
    private_key, public_key = generate_keys()

    # Serialize keys
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Display keys
    print("Private Key:")
    print(private_key_pem.decode())
    print("Public Key:")
    print(public_key_pem.decode())

    # Message to sign
    message = "Hello, ECC!"

    # Sign message
    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())

    # Verify signature
    verified = verify_signature(public_key, message, signature)
    if verified:
        print("Signature verified!")
    else:
        print("Signature verification failed!")


if __name__ == "__main__":
    main()
