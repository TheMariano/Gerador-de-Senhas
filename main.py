import os, sys, time

print("[+] Gerador de Senhas [+]")
print("Escolha o formato de senha: ")
print("   [ 1 ] > Letras Maiusculas + Minusculas")
print("   [ 2 ] > Letras Mai/Min + Números")
print("   [ 3 ] > Letras Mai/Min + códigos")
print("   [ 4 ] > Letras Mai/Min + Números + Códigos")
print("   [ 5 ] > Sair do programas")
print("")
print("By: TheMariano")
A = input("Alternativa: ")

if A == "1" or A == "01":
    base = input("Digite uma palavra base para sua senha: ")
    senha = ""
    for letra in base:
        if letra in "aA": senha = senha + "A"
        elif letra in "bB": senha = senha + "B"
        elif letra in "cC": senha = senha + "c"
        elif letra in "dD": senha = senha + "D"
        elif letra in "eE": senha = senha + "e"
        elif letra in "fF": senha = senha + "F"
        elif letra in "gG": senha = senha + "g"
        elif letra in "hH": senha = senha + "H"
        elif letra in "iI": senha = senha + "i"
        elif letra in "jJ": senha = senha + "J"
        elif letra in "kK": senha = senha + "k"
        elif letra in "lL": senha = senha + "L"
        elif letra in "mM": senha = senha + "m"
        elif letra in "nN": senha = senha + "N"
        elif letra in "oO": senha = senha + "o"
        elif letra in "pP": senha = senha + "P"
        elif letra in "qQ": senha = senha + "q"
        elif letra in "rR": senha = senha + "R"
        elif letra in "sS": senha = senha + "S"
        elif letra in "tT": senha = senha + "T"
        elif letra in "uU": senha = senha + "u"
        elif letra in "vV": senha = senha + "V"
        elif letra in "wW": senha = senha + "w"
        elif letra in "xX": senha = senha + "X"
        elif letra in "yY": senha = senha + "y"
        elif letra in "zZ": senha = senha + "Z"
        elif letra in "çÇ": senha = senha + "Ç"
        else: senha + letra
    print(senha)
if A == "2" or A == "02":
    base = input("Digite uma palavra base para sua senha: ")
    senha = ""
    for letra in base:
        if letra in "Aa": senha = senha + "4"
        elif letra in "Bb": senha = senha + "b"
        elif letra in "Cc": senha = senha + "C"
        elif letra in "Dd": senha = senha + "d"
        elif letra in "Ee": senha = senha + "3"
        elif letra in "Ff": senha = senha + "f"
        elif letra in "Gg": senha = senha + "6"
        elif letra in "Hh": senha = senha + "h"
        elif letra in "Ii": senha = senha + "1"
        elif letra in "Jj": senha = senha + "j"
        elif letra in "Kk": senha = senha + "k"
        elif letra in "Ll": senha = senha + "l"
        elif letra in "Mm": senha = senha + "M"
        elif letra in "Nn": senha = senha + "n"
        elif letra in "Oo": senha = senha + "0"
        elif letra in "Pp": senha = senha + "P"
        elif letra in "Qq": senha = senha + "9"
        elif letra in "Rr": senha = senha + "R"
        elif letra in "Ss": senha = senha + "5"
        elif letra in "Tt": senha = senha + "7"
        elif letra in "Uu": senha = senha + "u"
        elif letra in "Vv": senha = senha + "v"
        elif letra in "Ww": senha = senha + "W"
        elif letra in "Xx": senha = senha + "x"
        elif letra in "Yy": senha = senha + "y"
        elif letra in "Zz": senha = senha + "Z"
        else: senha + letra
    print(senha)
if A == "3" or A == "03":
    base = input("Digite uma palavra base para sua senha: ")
    senha = ""
    for letra in base:
        if letra in "Aa": senha = senha + "@"
        elif letra in "Bb": senha = senha + "b"
        elif letra in "Cc": senha = senha + "c"
        elif letra in "Dd": senha = senha + "&"
        elif letra in "Ee": senha = senha + "#"
        elif letra in "Ff": senha = senha + "f"
        elif letra in "Gg": senha = senha + "g"
        elif letra in "Hh": senha = senha + "h"
        elif letra in "Ii": senha = senha + "!"
        elif letra in "Jj": senha = senha + "j"
        elif letra in "Kk": senha = senha + "k"
        elif letra in "Ll": senha = senha + "L"
        elif letra in "Mm": senha = senha + "M"
        elif letra in "Nn": senha = senha + "n"
        elif letra in "Oo": senha = senha + "o"
        elif letra in "Pp": senha = senha + "p"
        elif letra in "Qq": senha = senha + "q"
        elif letra in "Rr": senha = senha + "R"
        elif letra in "Ss": senha = senha + "$"
        elif letra in "Tt": senha = senha + "+"
        elif letra in "Uu": senha = senha + "u"
        elif letra in "Vv": senha = senha + "V"
        elif letra in "Ww": senha = senha + "w"
        elif letra in "Xx": senha = senha + "X"
        elif letra in "Yy": senha = senha + "y"
        elif letra in "Zz": senha = senha + "Z"
        else: senha + letra
    print(senha)
if A == "4" or A == "04":
    base = input("Digite uma palavra base para sua senha: ")
    senha = ""
    for letra in base:
        if letra in "Aa": senha = senha + "@"
        elif letra in "Bb": senha = senha + "b"
        elif letra in "Cc": senha = senha + "C"
        elif letra in "Dd": senha = senha + "d"
        elif letra in "Ee": senha = senha + "3"
        elif letra in "Ff": senha = senha + "f"
        elif letra in "Gg": senha = senha + "6"
        elif letra in "Hh": senha = senha + "#"
        elif letra in "Ii": senha = senha + "1"
        elif letra in "Jj": senha = senha + "j"
        elif letra in "Kk": senha = senha + "k"
        elif letra in "Ll": senha = senha + "!"
        elif letra in "Mm": senha = senha + "M"
        elif letra in "Nn": senha = senha + "n"
        elif letra in "Oo": senha = senha + "0"
        elif letra in "Pp": senha = senha + "p"
        elif letra in "Qq": senha = senha + "9"
        elif letra in "Rr": senha = senha + "R"
        elif letra in "Ss": senha = senha + "$"
        elif letra in "Tt": senha = senha + "7"
        elif letra in "Uu": senha = senha + "u"
        elif letra in "Vv": senha = senha + "v"
        elif letra in "Ww": senha = senha + "W"
        elif letra in "Xx": senha = senha + "x"
        elif letra in "Yy": senha = senha + "y"
        elif letra in "Zz": senha = senha + "Z"
        else: senha + letra
    print(senha)
elif A == "5" or A == "5":
    sys.exit()
