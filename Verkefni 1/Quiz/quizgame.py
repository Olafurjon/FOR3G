#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def questionmaker(q, a, b, c, d):
    if a == "":
        print q
        answer = raw_input()
        if answer.lower() == b.lower():
            print "Mikið rétt!"
            scorekeeper = 1
            return scorekeeper
        else:
            print "Nei því miður rétt svar er " + b
            scorekeeper = -1
            return scorekeeper
    elif a != "":
        print q
        correct = "b"
        listi = [a, b, c, d]
        ans = []
        random.shuffle(listi)
        st = "ABCD"
        for index, x in enumerate(listi):
            print(str(st[index]) + ": " + str(x))
            if b == x:
                correct = st[index]
            ans.append(x)
        answer = raw_input()
        if answer.lower() == correct.lower() or answer.lower() == b.lower():
            print "Mikið rétt!"
            scorekeeper = 1
            return scorekeeper
        else:
            print "Nei því miður rétt svar er " + str(b)
            scorekeeper = -1
            return scorekeeper
    else:
        scorekeeper = 0
        return scorekeeper


def questions():
    spurningar = [
        ("Hvað er 2 + 2?", "", "4", "", ""), ("Hvernig er Já á spænsku?", "Jawohl", "Si", "Pí", "Cí"), ('Hvað kæmi útúr þessu "ten" == 10? í Python 2,7', "True", "False", "Undefine", "Error"),
        ("Hvað var eftirnafn stúlkunnar í Harry Potter Tríóinu?", "", "Granger", "", ""), ("Pabbi Jóns á þrjá syni, Ripp, Rapp og? ", "Rupp", "Jón", "Pop", "Konna"),
        ("Er 79 Prímtala?", "Nei", "Já", "Nei, en 62 er prímtala", "erfið spurning..."), ("Hvað getur orðið árbítur þýtt?", "Geislasverð", "Morgunmatur", "Fréttir", "Erfið uppskera"),
        ("Hvert af eftirfarandi er EKKI orð yfir Snjó?", "Fönn", "Stirni", "Mjöll", "Drífa"), ("Hvað er svarið við ((((10*20)+19/2+10*30)+10*2)*10 /5)", "0", "1058", "1024", "2"),
        ("Botnaðu málsháttinn: Betra er að vera ógiftur en...", "giftur tvem.", "illa giftur.", "illa brókaður.", "gull sem ei glóir.")]
    return spurningar


def callquestion(t, k, g):
    while t in g:
        t = random.randint(0, len(k) - 1)
    return questionmaker(k[t][0], k[t][1], k[t][2], k[t][3], k[t][4])


print "Velkominn í Quizmaster 12.000"
print "Þú færð nokkrar spurningar og þér ber að svara þeim eftir bestu getu, fyrir hverja rétta færðu 1 stig fyrir hverja ranga færðu -1 stig, skemmtilegt?"
print "Hélt ekki... en núna byrjum við"
points = 0
newpoints = 0
rett = 0
rangt = 0
count = 0
done = []
while count != 6:
    print ""
    size = len(questions()) - 1
    r = random.randint(0, size)
    while r in done:
        r = random.randint(0, size)
    newpoints = points
    points = points + int(callquestion(r, questions(), done))
    if newpoints < points:
        rett += 1
    elif newpoints > points:
        rangt += 1
    done.append(r)
    count += 1
    print ""
    print "Þú ert kominn með " + str(points) + " stig"
print "Svaraðir "+ str(rett)+" spurningum rétt og "+ str(rangt) + " spurningum rangt"
total = rett + rangt
prosenta = (float(rett) / float(total)) * 100
prosentaustrengur = str(prosenta)
print "Prósentuhlutfall: " + prosentaustrengur[:-9] + "%"
