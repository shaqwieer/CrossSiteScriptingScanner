import math

def reverse(plain):
    return plain[-1:]

def Ceasar_encyption(plain,shift):
    letter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    cipher=""
    for char in plain:
        if char in letter:
            n=letter.find(char)
            n=(n+shift)%52
            cipher=cipher+letter[n]
        else:
            cipher=cipher+char
    return cipher

def Ceasar_decyption(cipher,shift):
    letter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plain=""
    for char in cipher:
        if char in letter:
            n=letter.find(char)
            n=(n-shift)%52
            plain=plain+letter[n]
        else:
            plain=plain+char
    return plain

def Transposition_encryption(plain,shift):
    trans=['']*shift
    for i in range(shift):
        pointer=i
        while pointer < len(plain):
            trans[i]+=plain[pointer]
            pointer+=shift
    cipher=''.join(trans)
    return cipher

def Transposition_decryption(cipher,shift):
    trans=['']*shift
    ncol=math.ceil(len(cipher)/shift)
    nrow=shift
    nshade=(ncol*nrow)-len(cipher)
    col=row=0
    for char in cipher:
        trans[col]+=char
        col+=1
        if(col==ncol or (col==ncol-1 and row>=nrow-nshade)):
            col=0
            row+=1
    plain=''.join(trans)
    return plain




