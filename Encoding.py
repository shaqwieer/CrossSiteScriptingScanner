import base64
from html import escape
from html import unescape
from urllib.parse import quote
from urllib.parse import unquote
import binascii

def base64_encode(message):
    return base64.b64encode(message.encode('ascii')).decode('ascii')

def base64_decode(message):
    return base64.b64decode(message.encode('ascii')).decode('ascii')

def html_encode(message):
    return escape(message)

def html_decode(message):
    return unescape(message)


def url_encode(message):
    return quote(message)
    
def url_decode(message):
    return unquote(message)

def ascii_hex_encode(message):
    return binascii.hexlify(bytes(message,'utf-8')).decode('utf-8')

def ascii_hex_decode(message):
    return binascii.unhexlify(message.encode('utf-8')).decode('utf8')

def encode(message, choice):
    if choice=="base64":
        d=base64.b64encode(message.encode('ascii')).decode('ascii')
    elif choice=="html":
        d=escape(message)

    elif choice=="url":
        d=quote(message)
    elif choice=="ascii_hex":
        d=binascii.hexlify(bytes(message,'utf-8')).decode('utf-8')
    return d

def decode(message, choice):
    if choice=="base64":
        d=base64.b64decode(message.encode('ascii')).decode('ascii')
    elif choice=="html":
        d=unescape(message)

    elif choice=="url":
        d=unquote(message)
    elif choice=="ascii_hex":
        d=binascii.unhexlify(message.encode('utf-8')).decode('utf8')
    return d




    