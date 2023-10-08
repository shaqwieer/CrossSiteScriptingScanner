import hashlib

def hash(message, choice):
    x=message.encode("ASCII")
    if choice=="md5":
        d=hashlib.md5(x).hexdigest()

    elif choice=="sha1":
        d=hashlib.sha1(x).hexdigest()

    elif choice=="sha224":
        d=hashlib.sha224(x).hexdigest()

    elif choice=="sha256":
        d=hashlib.sha256(x).hexdigest()

    elif choice=="sha384":
        d=hashlib.sha384(x).hexdigest()

    elif choice=="sha512":
        d=hashlib.sha512(x).hexdigest()

    elif choice=="blake2b":
        d=hashlib.blake2b(x).hexdigest()

    elif choice=="blake2s":
        d=hashlib.blake2s(x).hexdigest()

    elif choice=="sha3_224":
        d=hashlib.sha3_224(x).hexdigest()

    elif choice=="sha3_256":
        d=hashlib.sha3_256(x).hexdigest()

    elif choice=="sha3_384":
        d=hashlib.sha3_384(x).hexdigest()

    elif choice=="sha3_512":
        d=hashlib.sha3_512(x).hexdigest()
    return d



