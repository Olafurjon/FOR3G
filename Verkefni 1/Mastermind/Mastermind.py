#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random #Importar random klasanum


print "Velkominn í Mastermind, hefur þú það sem þarf til að sigra handahófskenndar tölur?"
print "Leikreglur: Tölvan hefur ákveðið 5 tölur milli 1 og 8 í ákveðnri röð og þú átt að giska hvaða tölur og í hvaða röð!"
print "Ömögulegt? nei þú færð vísbendingar þér til aðstoðar, ef að þú sérð X í tölunum þýðir að þú hittir á rétta tölu bara hún er á vitlausum stað,"
print "ef þú sérð töluna það þýðir að hún er á réttum stað,"
print "en ef þú sérð bara 0 er talan ekki í listanum."
print "ATH: sama tala getur komið fyrir oftar en einusinni."
print "Gangi þér vel!"

def tolvatolur(): #Dúndrar inn random tölum og skilar lista
    i = 0
    tolur = []

    while i < 5:
        randtala = random.randint(1, 8)
        tolur.append(randtala)
        i+=1
    return tolur
def tolurnotanda():
    tolur=[]
    i = 0
    while i < len(tolvatolur()):
        tala = input("Sláðu inn tölu "+ str(i)+"/5 ")
        if int(tala) > 8:
            print("tala verður að vera 8 eða minni ")
        elif int(tala) < 0:
            print("tala verður að vera stærri en 0" )
        else:
            tolur.append(tala)
            i+=1
    return tolur
def beraSaman(tolva,notandi):
    compare = [0, 0, 0, 0,0]  # Initializar compare tilbuin með 5 gildum til að þau verði endurskrifuð ef notandi gerir rétt
    tolva = list(tolva)
    notandi = list(notandi)
    i = 0
    x = 0
    k = 0
    while i < len(tolva):
       if notandi[i] in tolva:
           if notandi[i] == tolva[i]:
               compare[i] = notandi[i]
               x = x + 1
               i = i + 1
           else:
               compare[i] = "X"
               k = k + 1
               i = i + 1
       else:
           i = i + 1
    return str(compare) + " Þú ert með: " + str(x) + " tölur réttar og "+ str(k)+" tölur á röngum stað"
t = tolvatolur()
x = 0
while x < 8:
    n = tolurnotanda()
    compare = beraSaman(t,n)
    x = x+1
    print compare
    print n
    if n == t:
        print "Þú vannst"
        break
    elif x == 8:
        print "Þú hefur tapað réttar tölur voru: "
        print t

