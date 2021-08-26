import pprint

text = "REIAUBLZXYQOKHMRNTEZHFLVIABHDMJMSJOGIRETPHBVVFTQHEXTARVIXSNQRIQPEJOLMDDEJORGVFECUTQVHIIKVMUKHVQPARPIVBIVGQIUFHIWZSTMBTHOSLXDNDFLFYIBPMRPOHCUOLJFEMSXIJBITHPSEQUXRZEEATPHDAFGLLQAXIQAKKRVFYTPHSVFGNLEQRVMTPWAXYQSCURETQONWTINMTMUMFFHEBKQVVPWMOXXYQSMDWMESAVGTMJEUJMQGKEWMPGWKZOBLYEXUNMWTEKFHMUQMJZOBKURXMTBKQFFFTWPAJKTEAHMFLFBIUQCVXLWZEEEP"

def indiceCoincidencia(text):
    LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(text)
    sum = 0
    cont = 0
    index = []
    for i in LETRAS:
        for j in text:
            if j==i:
                cont+=1
        index.append(cont)
        cont = 0
    for i in index:
        sum+= i*(i-1)
    IC = 1/(n*(n-1))*sum
    return IC

def dividirMensaje(text, num):
    list = []
    for i in range(num):
        list.append("")
    cont = 0
    for i in text:
        list[cont]+=i
        cont+=1
        if cont == num:
            cont = 0
    return list

def periodo(text,n):
    IC = {}
    for i in range(1,n+1):
        list = dividirMensaje(text,i)
        IC[i] = []
        for j in list:
            a = indiceCoincidencia(j)
            IC[i].append(a)
    return IC

def list2string(list):
    str = ""
    for i in list:
        str+=i
    return str
#devuelve en lista
def shift(text,num):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista = list(text)
    for i in alphabet:
        for j in range(len(text)):
            if text[j]==i:
                let = text[j]
                nu = alphabet.index(let)
                lista[j] = alphabet[(nu+num)%26]
    return list2string(lista)

def frecuencia(listText):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}
    flag = True
    for i in listText:
        length = len(i)
        cont = 0
        for j in alphabet:
            if flag == True:
                dict[j] = []
            for k in i:
                if k == j:
                    cont+=1
            dict[j].append(cont/length)
            cont = 0
        flag = False
    return dict

english = {
    "A": 0.082,
    "B": 0.015,
    "C": 0.028,
    "D": 0.043,
    "E": 0.127,
    "F": 0.022,
    "G": 0.020,
    "H": 0.061,
    "I": 0.070,
    "J": 0.002,
    "K": 0.008,
    "L": 0.040,
    "M": 0.024,
    "N": 0.067,
    "O": 0.075,
    "P": 0.019,
    "Q": 0.001,
    "R": 0.060,
    "S": 0.063,
    "T": 0.091,
    "U": 0.028,
    "V": 0.010,
    "W": 0.023,
    "X": 0.001,
    "Y": 0.020,
    "Z": 0.001
}

def diference(dic1,dicEn,j):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    diff = []
    sum = 0
    for k in range(0,j):
        for i in alphabet:
            d = (dic1[i][k] - dicEn[i])*(dic1[i][k] - dicEn[i])
            sum+=d
        diff.append(sum)
        sum=0
    return diff

def converter(listText, k):
    for i in range(len(listText)):
        listText[i] = shift(listText[i],k)
    return listText

def final(text,j):
    sumas = []
    # rows = dividirMensaje(text,j)
    for i in range(0,26):
        rows = dividirMensaje(text,j)
        temp = converter(rows,i)
        frecs = frecuencia(temp)
        sums = diference(frecs,english,j)
        sumas.append(sums)
    return sumas

final(text,7)

def mins(lista,j):
    minimos = []
    index =[]
    for k in range(j):
        indices = []
        for i in lista:
            indices.append(i[k])
        num = min(indices)
        minimos.append(num)
    for k in range(j):
        indices = []
        for i in lista:
            indices.append(i[k])
        num = indices.index(minimos[k])
        index.append(num)
    return index

def getKey(text,j):
    var = final(text,j)
    mini = mins(var,j)
    print("The key is: ")
    return mini
a = [12,4,17,12,0,8,3]
pprint.pprint(periodo(text,10))
print(getKey(text,7))
