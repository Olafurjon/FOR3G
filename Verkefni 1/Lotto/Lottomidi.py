#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class LottoMachine:

    def VeljaTolur(self):
        lottonumbers = []
        i = 0
        while i != 5:
            r = random.randint(1,38)
            while r not in lottonumbers:
                lottonumbers.append(r)
                i += 1
        lottonumbers.sort()
        return lottonumbers

class LottoTicket:

    def AutoVal(self):
        lottonumbers = []
        i = 0
        while i != 5:
            r = random.randint(1,38)
            while r not in lottonumbers:
                lottonumbers.append(r)
                i += 1
        lottonumbers.sort()
        return lottonumbers
    def VeljaSjalfur(self):
        lottonumbers = []
        i = 0
        while i != 5:
            tala = raw_input("Sláðu inn tölu milli 1 og 38")
            if tala not in lottonumbers:
                lottonumbers.append(tala)
                i += 1
        lottonumbers.sort()
        return lottonumbers

class LottoChecker():
    def AthugaVinning(self,midi, tolva):
        i = 0
        rettar = 0
        while i != 5:
            if midi[i] in tolva:
                rettar += 1
            i += 1
        return rettar

LottoTicket = LottoTicket()
LottoMachine = LottoMachine()
Sjoppa = LottoChecker()

LottoSpilari = LottoTicket.AutoVal()
LottoTolva = LottoMachine.VeljaTolur()

print "Lottótölur spilarans:"
print LottoSpilari
print "Lottótölur kvöldsins: "
print LottoTolva
rett =  Sjoppa.AthugaVinning(LottoSpilari,LottoTolva)
print "Þú ert með "+ str(rett)+" tölur réttar"
