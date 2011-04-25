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
    def __init__(self, nome, presente, passato_prossimo, imperfetto):
        self.nome = nome
        self.tempi = [
            ("presente", self.Presente, presente),
            ("passato prossimo", self.PassatoProssimo, passato_prossimo),
            ("imperfetto", self.Imperfetto, imperfetto),
        ]

    def Presente(self, frase):
        soluzione = None

        if frase == "[r]":
            prefix = self.nome[0 : -3]
            suffix = self.nome[-3 :]

            if suffix == "are":
                soluzione = [
                    prefix + "o",
                    prefix + "i",
                    prefix + "a",
                    prefix + "iamo",
                    prefix + "ate",
                    prefix + "ano",
                ]
            elif suffix == "ere":
                soluzione = [
                    prefix + "o",
                    prefix + "i",
                    prefix + "e",
                    prefix + "iamo",
                    prefix + "ete",
                    prefix + "ono",
                ]
            elif suffix == "ire":
                soluzione = [
                    prefix + "o",
                    prefix + "i",
                    prefix + "e",
                    prefix + "iamo",
                    prefix + "ite",
                    prefix + "ono",
                ]
        else:
            soluzione = frase.split(", ")

        return soluzione

    def PassatoProssimo(self, frase):
        soluzione = None
        frase = frase.split(", ")

        prefix = self.nome[0 : -3]
        suffix = self.nome[-3 :]

        participio = frase[1]

        if participio == "[r]":
            if suffix == "are":
                participio = prefix + "ato"
            elif suffix == "ere":
                participio = prefix + "uto"
            elif suffix == "ire":
                participio = prefix + "ito"

        if frase[0] == "avere":
            soluzione = [
                "ho " + participio,
                "hai " + participio,
                "ha " + participio,
                "abbiamo " + participio,
                "avete " + participio,
                "hanno " + participio,
            ]
        elif frase[0] == "essere":
            participio = participio[: -1]

            soluzione = [
                "sono " + participio + "o",
                "sei " + participio + "o",
                "e " + participio + "o",
                "siamo " + participio + "i",
                "siete " + participio + "i",
                "sono " + participio + "i",
            ]

        return soluzione

    def Imperfetto(self, frase):
        soluzione = None

        if frase == "[r]":
            prefix = self.nome[0 : -2]

            soluzione = [
                prefix + "vo",
                prefix + "vi",
                prefix + "va",
                prefix + "vamo",
                prefix + "vate",
                prefix + "vano",
            ]
        else:
            soluzione = frase.split(", ")

        return soluzione

class Ita:
    def __init__(self):
        self.verbi = [
            Verbo("avere",
            "ho, hai, ha, abbiamo, avete, hanno",
            "avere, [r]",
            "[r]"),

            Verbo("essere",
            "sono, sei, e, siamo, siete, sono",
            "essere, stato",
            "ero, eri, era, eravamo, eravate, erano"),

            Verbo("andare",
            "vado, vai, va, andiamo, andate, vanno",
            "essere, [r]",
            "[r]"),

            Verbo("dare",
            "do, dai, da, diamo, date, danno",
            "avere, [r]",
            "[r]"),

            Verbo("cantare",
            "[r]",
            "avere, [r]",
            "[r]"),

            Verbo("fare",
            "faccio, fai, fa, facciamo, fate, fanno",
            "avere, [r]",
            "facevo, facevi, faceva, facevamo, facevate, facevano"),

            Verbo("stare",
            "sto, stai, sta, stiamo, state, stanno",
            "essere, [r]",
            "[r]"),

            Verbo("bere",
            "bevo, bevi, beve, beviamo, bevete, bevono",
            "avere, bevuto",
            "bevevo, bevevi, beveva, bevevamo, bevevate, bevevano"),

            Verbo("chiudere",
            "[r]",
            "avere, chiuso",
            "[r]"),

            Verbo("conoscere",
            "[r]",
            "avere, conosciuto",
            "[r]"),

            Verbo("dovere",
            "devo, devi, deve, dobbiamo, dovete, devono",
            "avere, [r]",
            "[r]"),

            Verbo("leggere",
            "[r]",
            "avere, letto",
            "[r]"),

            Verbo("potere",
            "posso, puoi, puo, possiamo, potete, possono",
            "avere, [r]",
            "[r]"),

            Verbo("prendere",
            "[r]",
            "avere, preso",
            "[r]"),

            Verbo("rispondere",
            "[r]",
            "avere, risposto",
            "[r]"),

            Verbo("sapere",
            "so, sai, sa, sappiamo, sapete, sanno",
            "avere, [r]",
            "[r]"),

            Verbo("scrivere",
            "[r]",
            "avere, scritto",
            "[r]"),

            Verbo("spendere",
            "[r]",
            "avere, speso",
            "[r]"),

            Verbo("vedere",
            "[r]",
            "avere, [r]",
            "[r]"),

            Verbo("volere",
            "voglio, vuoi, vuole, vogliamo, volete, vogliono",
            "avere, [r]",
            "[r]"),

            Verbo("aprire",
            "[r]",
            "avere, aperto",
            "[r]"),

            Verbo("dire",
            "dico, dici, dice, diciamo, dite, diciono",
            "avere, detto",
            "dicevo, dicevi, diceva, dicevamo, dicevate, dicevano"),

            Verbo("dormire",
            "[r]",
            "avere, [r]",
            "[r]"),

            Verbo("finire",
            "finisco, finisci, finisce, finiamo, finite, finiscono",
            "avere, [r]",
            "[r]"),

            Verbo("offrire",
            "[r]",
            "avere, offerto",
            "[r]"),

            Verbo("uscire",
            "esco, esci, esce, usciamo, uscite, escono",
            "essere, [r]",
            "[r]"),

            Verbo("venire",
            "vengo, vieni, viene, veniamo, venite, vengono",
            "essere, [r]",
            "[r]"),
        ]

    def run(self):
        print "{0} verbi * {1} tempi = {2} combinazioni\n".format(
            len(self.verbi), len(self.verbi[0].tempi),
            len(self.verbi) * len(self.verbi[0].tempi))

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

                        print "      Consiglio: " + consiglio

            print ""

if __name__ == "__main__":
    Ita().run()
