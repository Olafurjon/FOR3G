#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def teningakast():
    teningakast = []
    count = 0
    while count < 5:
        teningur = random.randint(1, 6)
        teningakast.append(teningur)
        count += 1
    return teningakast
def kostEftir(a,b):
    c = b-a
    return "Köst eftir:" + str(c)

kast = 0
eftir = 3
tolvakast = teningakast()
notandikast = teningakast()
kast += 1
print("Tolvan hefur kastad")
print("Þitt fyrsta kast endaði svona: ")
print(notandikast)
print(kostEftir(kast,eftir))
b = sum(notandikast)
print("heildarútkoman er: " + str(b))
print("Viltu kasta aftur? Y/N ")
ans = raw_input()
ans.lower()
while ans != 'n':
    if kast == 3:
        print("Köstin þín eru búin")
        break
    else:
        notandikast = teningakast()
        kast += 1
        print(kostEftir(kast, eftir))
        print("Þú fékkst: ")
        print(notandikast)
        b = sum(notandikast)
        print("heildarútkoman er: " + str(b))
        print("Viltu kasta aftur? Y/N")
        ans = raw_input()
a = sum(tolvakast)
print("Tölva fékk:")
print(tolvakast)
print("heildarútkoman er: " + str(a))
if a > b:
    print("Þú tapaðir :(")
elif b > a:
    print("Þú vannst! :)")
elif a == b:
    print("Jafntefli :O")
else:
    print("Villa kom upp... segjum bara að þú vannst?")


