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
    def __init__(self, nome, presente):
        self.nome = nome
        self.tempi = [
            ("presente", presente)
        ]

class Ita:
    def __init__(self):
        self.verbi = [
            Verbo("avere",
            "ho, hai, ha, abbiamo, avete, hanno"),

            Verbo("essere",
            "sono, sei, e, siamo, siete, sono"),

            Verbo("cantare",
            "canto, canti, canta, cantiamo, cantate, cantano"),

            Verbo("scrivere",
            "scrivo, scrivi, scrive, scriviamo, scrivete, scrivono"),

            Verbo("dormire",
            "dormo, dormi, dorme, dormiamo, dormite, dormono"),

            Verbo("andare",
            "vado, vai, va, andiamo, andate, vanno"),

            Verbo("fare",
            "faccio, fai, fa, facciamo, fate, fanno"),

            Verbo("dare",
            "do, dai, da, diamo, date, danno"),

            Verbo("stare",
            "sto, stai, sta, stiamo, state, stanno"),

            Verbo("finire",
            "finisco, finisci, finisce, finiamo, finite, finiscono"),

            Verbo("bere",
            "bevo, bevi, beve, beviamo, bevete, bevono"),

            Verbo("dovere",
            "devo, devi, deve, dobbiamo, dovete, devono"),

            Verbo("potere",
            "posso, puoi, puo, possiamo, potete, possono"),

            Verbo("volere",
            "voglio, vuoi, vuole, vogliamo, volete, vogliono"),

            Verbo("dire",
            "dico, dici, dice, diciamo, dite, diciono"),

            Verbo("uscire",
            "esco, esci, esce, usciamo, uscite, escono"),

            Verbo("venire",
            "vengo, vieni, viene, veniamo, venite, vengono"),

            Verbo("sapere",
            "so, sai, sa, sappiamo, sapete, sanno"),

            Verbo("conoscere",
            "conosco, conosci, conosce, conosciamo, conoscete, conoscono"),
        ]

    def run(self):
        verbo = None
        ultimo = None

        while True:
            while verbo == ultimo:
                verbo = random.choice(self.verbi)

            ultimo = verbo
            tempo = random.choice(verbo.tempi)

            print verbo.nome + " in " + tempo[0]

            pronomi = ["io", "tu", "lui", "noi", "voi", "loro"]
            soluzioni = tempo[1].split(", ")

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
