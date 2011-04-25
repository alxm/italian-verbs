#!/usr/bin/python

"""
    Copyright 2011 Alex Margarit

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random, sys

class Verbo:
    def __init__(self, nome, presente, passato_prossimo):
        self.nome = nome
        self.tempi = [
            ("presente", self.Presente, presente),
            ("passato prossimo", self.PassatoProssimo, passato_prossimo)
        ]

    def Presente(self, frase):
        return frase.split(", ")

    def PassatoProssimo(self, frase):
        soluzione = None
        frase = frase.split(", ")

        if frase[0] == "avere":
            participio = frase[1]

            soluzione = [
                "ho " + participio,
                "hai " + participio,
                "ha " + participio,
                "abbiamo " + participio,
                "avete " + participio,
                "hanno " + participio,
            ]
        else:
            participio = frase[1][:-1]

            soluzione = [
                "sono " + participio + "o",
                "sei " + participio + "o",
                "e " + participio + "o",
                "siamo " + participio + "i",
                "siete " + participio + "i",
                "sono " + participio + "i",
            ]

        return soluzione

class Ita:
    def __init__(self):
        self.verbi = [
            Verbo("avere",
            "ho, hai, ha, abbiamo, avete, hanno",
            "avere, avuto"),

            Verbo("essere",
            "sono, sei, e, siamo, siete, sono",
            "essere, stato"),

            Verbo("cantare",
            "canto, canti, canta, cantiamo, cantate, cantano",
            "avere, cantato"),

            Verbo("scrivere",
            "scrivo, scrivi, scrive, scriviamo, scrivete, scrivono",
            "avere, scritto"),

            Verbo("dormire",
            "dormo, dormi, dorme, dormiamo, dormite, dormono",
            "avere, dormito"),

            Verbo("andare",
            "vado, vai, va, andiamo, andate, vanno",
            "essere, andato"),

            Verbo("fare",
            "faccio, fai, fa, facciamo, fate, fanno",
            "avere, fato"),

            Verbo("dare",
            "do, dai, da, diamo, date, danno",
            "avere, dato"),

            Verbo("stare",
            "sto, stai, sta, stiamo, state, stanno",
            "essere, stato"),

            Verbo("finire",
            "finisco, finisci, finisce, finiamo, finite, finiscono",
            "avere, finito"),

            Verbo("bere",
            "bevo, bevi, beve, beviamo, bevete, bevono",
            "avere, bevuto"),

            Verbo("dovere",
            "devo, devi, deve, dobbiamo, dovete, devono",
            "avere, dovuto"),

            Verbo("potere",
            "posso, puoi, puo, possiamo, potete, possono",
            "avere, potuto"),

            Verbo("volere",
            "voglio, vuoi, vuole, vogliamo, volete, vogliono",
            "voluto"),

            Verbo("dire",
            "dico, dici, dice, diciamo, dite, diciono",
            "avere, detto"),

            Verbo("uscire",
            "esco, esci, esce, usciamo, uscite, escono",
            "essere, uscito"),

            Verbo("venire",
            "vengo, vieni, viene, veniamo, venite, vengono",
            "essere, venuto"),

            Verbo("sapere",
            "so, sai, sa, sappiamo, sapete, sanno",
            "avere, saputo"),

            Verbo("conoscere",
            "conosco, conosci, conosce, conosciamo, conoscete, conoscono",
            "avere, conosciuto"),

            Verbo("leggere",
            "leggo, leggi, legge, leggiamo, leggete, leggono",
            "avere, letto"),

            Verbo("rispondere",
            "rispondo, rispondi, risponde, rispondiamo, rispondete, rispondono",
            "avere, risposto"),

            Verbo("spendere",
            "spendo, spendi, spende, spendiamo, spendete, spendono",
            "avere, speso"),

            Verbo("aprire",
            "apro, apri, apre, apriamo, aprite, aprono",
            "avere, aperto"),

            Verbo("offrire",
            "offro, offri, offre, offriamo, offrite, offrono",
            "avere, offerto"),
        ]

    def run(self):
        print "{0} verbi\n".format(len(self.verbi))

        verbo = None
        ultimo = None

        while True:
            while verbo == ultimo:
                verbo = random.choice(self.verbi)

            ultimo = verbo
            tempo = random.choice(verbo.tempi)

            print verbo.nome + " in " + tempo[0]

            soluzioni = tempo[1](tempo[2])
            pronomi = ["io", "tu", "lui", "noi", "voi", "loro"]

            for i in range(0, len(pronomi)):
                errori = 0

                while True:
                    risposta = raw_input("  [?] " + pronomi[i] + " ")

                    if risposta == "q":
                        sys.exit(0)

                    if risposta == soluzioni[i]:
                        print "      Bravo!"
                        break
                    else:
                        errori += 1
                        consiglio = ""

                        if errori == 1:
                            consiglio = soluzioni[i][0 : len(soluzioni[i]) / 4] + "..."
                        elif errori == 2:
                            consiglio = soluzioni[i][0 : len(soluzioni[i]) / 2] + "..."
                        else:
                            consiglio = soluzioni[i]

                        print "      Errore: " + consiglio

            print ""

if __name__ == "__main__":
    Ita().run()
