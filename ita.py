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

import random

class Verbo:
    def __init__(self, nome, ausiliare, presente, participio, imperfetto, futuro):
        self.nome = nome
        self.ausiliare = ausiliare
        self.presente = presente
        self.participio = participio
        self.imperfetto = imperfetto
        self.futuro = futuro

        self.tempi = [
            ("presente", self.Presente, presente == "[regolare]"),
            ("passato prossimo", self.PassatoProssimo, participio == "[regolare]"),
            ("imperfetto", self.Imperfetto, imperfetto == "[regolare]"),
            ("trapassato prossimo", self.TrapassatoProssimo, participio == "[regolare]"),
            ("futuro", self.Futuro, futuro == "[regolare]"),
            ("condizionale presente", self.CondizionalePresente, futuro == "[regolare]"),
            ("condizionale passato", self.CondizionalePassato, participio == "[regolare]")
        ]

    def il_participio(self):
        if self.participio == "[regolare]":
            prefisso = self.nome[: -3]
            suffisso = self.nome[-3 :]

            if suffisso == "are":
                return prefisso + "ato"
            elif suffisso == "ere":
                return prefisso + "uto"
            elif suffisso == "ire":
                return prefisso + "ito"
        else:
            return self.participio

    def Presente(self):
        soluzione = None

        if self.presente == "[regolare]":
            prefisso = self.nome[: -3]
            suffisso = self.nome[-3 :]

            if suffisso == "are":
                soluzione = [
                    prefisso + "o",
                    prefisso + "i",
                    prefisso + "a",
                    prefisso + "iamo",
                    prefisso + "ate",
                    prefisso + "ano",
                ]
            elif suffisso == "ere":
                soluzione = [
                    prefisso + "o",
                    prefisso + "i",
                    prefisso + "e",
                    prefisso + "iamo",
                    prefisso + "ete",
                    prefisso + "ono",
                ]
            elif suffisso == "ire":
                soluzione = [
                    prefisso + "o",
                    prefisso + "i",
                    prefisso + "e",
                    prefisso + "iamo",
                    prefisso + "ite",
                    prefisso + "ono",
                ]
        else:
            soluzione = self.presente.split(", ")

        return soluzione

    def PassatoProssimo(self):
        soluzione = None
        participio = self.il_participio()

        if self.ausiliare == "avere":
            soluzione = [
                "ho " + participio,
                "hai " + participio,
                "ha " + participio,
                "abbiamo " + participio,
                "avete " + participio,
                "hanno " + participio,
            ]
        elif self.ausiliare == "essere":
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

    def Imperfetto(self):
        soluzione = None

        if self.imperfetto == "[regolare]":
            prefisso = self.nome[: -2]

            soluzione = [
                prefisso + "vo",
                prefisso + "vi",
                prefisso + "va",
                prefisso + "vamo",
                prefisso + "vate",
                prefisso + "vano",
            ]
        else:
            soluzione = self.imperfetto.split(", ")

        return soluzione

    def TrapassatoProssimo(self):
        soluzione = None
        participio = self.il_participio()

        if self.ausiliare == "avere":
            soluzione = [
                "avevo " + participio,
                "avevi " + participio,
                "aveva " + participio,
                "avevamo " + participio,
                "avevate " + participio,
                "avevano " + participio,
            ]
        elif self.ausiliare == "essere":
            participio = participio[: -1]

            soluzione = [
                "ero " + participio + "o",
                "eri " + participio + "o",
                "era " + participio + "o",
                "eravamo " + participio + "i",
                "eravate " + participio + "i",
                "erano " + participio + "i",
            ]

        return soluzione

    def Futuro(self):
        prefisso = self.futuro

        if self.futuro == "[regolare]":
            suffisso = self.nome[-3 :]

            if suffisso == "are":
                prefisso = self.nome[: -3] + "er"
            else:
                prefisso = self.nome[: -1]

        soluzione = [
            prefisso + "o",
            prefisso + "ai",
            prefisso + "a",
            prefisso + "emo",
            prefisso + "ete",
            prefisso + "anno",
        ]

        return soluzione

    def CondizionalePresente(self):
        prefisso = self.futuro

        if self.futuro == "[regolare]":
            suffisso = self.nome[-3 :]

            if suffisso == "are":
                prefisso = self.nome[: -3] + "er"
            else:
                prefisso = self.nome[: -1]

        soluzione = [
            prefisso + "ei",
            prefisso + "esti",
            prefisso + "ebbe",
            prefisso + "emmo",
            prefisso + "este",
            prefisso + "ebbero",
        ]

        return soluzione

    def CondizionalePassato(self):
        soluzione = None
        participio = self.il_participio()

        if self.ausiliare == "avere":
            soluzione = [
                "avrei " + participio,
                "avresti " + participio,
                "avrebbe " + participio,
                "avremmo " + participio,
                "avreste " + participio,
                "avrebbero " + participio,
            ]
        elif self.ausiliare == "essere":
            participio = participio[: -1]

            soluzione = [
                "sarei " + participio + "o",
                "saresti " + participio + "o",
                "sarebbe " + participio + "o",
                "saremmo " + participio + "i",
                "sareste " + participio + "i",
                "sarebbero " + participio + "i",
            ]

        return soluzione

class Ita:
    def __init__(self):
        self.verbi = [
            Verbo("avere", "avere",
            "ho, hai, ha, abbiamo, avete, hanno",
            "[regolare]",
            "[regolare]",
            "avr"),

            Verbo("essere", "essere",
            "sono, sei, e, siamo, siete, sono",
            "stato",
            "ero, eri, era, eravamo, eravate, erano",
            "sar"),

            Verbo("aiutare", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("andare", "essere",
            "vado, vai, va, andiamo, andate, vanno",
            "[regolare]",
            "[regolare]",
            "andr"),

            Verbo("cantare", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("dare", "avere",
            "do, dai, da, diamo, date, danno",
            "[regolare]",
            "[regolare]",
            "dar"),

            Verbo("dimenticare", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "dimenticher"),

            Verbo("fare", "avere",
            "faccio, fai, fa, facciamo, fate, fanno",
            "[regolare]",
            "facevo, facevi, faceva, facevamo, facevate, facevano",
            "far"),

            Verbo("mangiare", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "manger"),

            Verbo("stare", "essere",
            "sto, stai, sta, stiamo, state, stanno",
            "[regolare]",
            "[regolare]",
            "star"),

            Verbo("bere", "avere",
            "bevo, bevi, beve, beviamo, bevete, bevono",
            "bevuto",
            "bevevo, bevevi, beveva, bevevamo, bevevate, bevevano",
            "berr"),

            Verbo("cadere", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "cadr"),

            Verbo("chiudere", "avere",
            "[regolare]",
            "chiuso",
            "[regolare]",
            "[regolare]"),

            Verbo("conoscere", "avere",
            "[regolare]",
            "conosciuto",
            "[regolare]",
            "[regolare]"),

            Verbo("dovere", "avere",
            "devo, devi, deve, dobbiamo, dovete, devono",
            "[regolare]",
            "[regolare]",
            "dovr"),

            Verbo("leggere", "avere",
            "[regolare]",
            "letto",
            "[regolare]",
            "[regolare]"),

            Verbo("piacere", "essere",
            "piaccio, piaci, piace, piacciamo, piacete, piacciono",
            "piaciuto",
            "[regolare]",
            "[regolare]"),

            Verbo("potere", "avere",
            "posso, puoi, puo, possiamo, potete, possono",
            "[regolare]",
            "[regolare]",
            "potr"),

            Verbo("prendere", "avere",
            "[regolare]",
            "preso",
            "[regolare]",
            "[regolare]"),

            Verbo("ridere", "avere",
            "[regolare]",
            "riso",
            "[regolare]",
            "[regolare]"),

            Verbo("rimanere", "essere",
            "rimango, rimani, rimane, rimaniamo, rimanete, rimangono",
            "rimasto",
            "[regolare]",
            "[regolare]"),

            Verbo("rispondere", "avere",
            "[regolare]",
            "risposto",
            "[regolare]",
            "[regolare]"),

            Verbo("sapere", "avere",
            "so, sai, sa, sappiamo, sapete, sanno",
            "[regolare]",
            "[regolare]",
            "sapr"),

            Verbo("scrivere", "avere",
            "[regolare]",
            "scritto",
            "[regolare]",
            "[regolare]"),

            Verbo("spendere", "avere",
            "[regolare]",
            "speso",
            "[regolare]",
            "[regolare]"),

            Verbo("vedere", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "vedr"),

            Verbo("vivere", "avere",
            "[regolare]",
            "vissuto",
            "[regolare]",
            "vivr"),

            Verbo("volere", "avere",
            "voglio, vuoi, vuole, vogliamo, volete, vogliono",
            "[regolare]",
            "[regolare]",
            "vorr"),

            Verbo("aprire", "avere",
            "[regolare]",
            "aperto",
            "[regolare]",
            "[regolare]"),

            Verbo("dire", "avere",
            "dico, dici, dice, diciamo, dite, diciono",
            "detto",
            "dicevo, dicevi, diceva, dicevamo, dicevate, dicevano",
            "[regolare]"),

            Verbo("dormire", "avere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("finire", "avere",
            "finisco, finisci, finisce, finiamo, finite, finiscono",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("offrire", "avere",
            "[regolare]",
            "offerto",
            "[regolare]",
            "[regolare]"),

            Verbo("partire", "essere",
            "[regolare]",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("uscire", "essere",
            "esco, esci, esce, usciamo, uscite, escono",
            "[regolare]",
            "[regolare]",
            "[regolare]"),

            Verbo("venire", "essere",
            "vengo, vieni, viene, veniamo, venite, vengono",
            "[regolare]",
            "[regolare]",
            "verr"),
        ]

        self.opzione1 = None # verbi irregolari o tutti verbi
        self.opzione2 = None # che tempo, o tutti tempi

    def intro(self):
        try:
            read = raw_input("\n1. verbi irregolari\n2. tutti verbi\n\n")
            self.opzione1 = int(read) == 1
        except ValueError:
            return

        opzioni = "0. tutti tempi"
        numero = 1

        for t in self.verbi[0].tempi:
            opzioni += "\n{0}. {1}".format(numero, t[0])
            numero += 1

        try:
            read = raw_input("\n" + opzioni + "\n\n")
            self.opzione2 = int(read) - 1
            print ""
        except ValueError:
            return

        self.run()

    def run(self):
        while True:
            random.shuffle(self.verbi)

            for verbo in self.verbi:
                tempi = None

                if self.opzione2 in range(len(verbo.tempi)):
                    tempi = [verbo.tempi[self.opzione2]]
                else:
                    tempi = verbo.tempi

                for tempo in tempi:
                    if self.opzione1 and tempo[2]:
                        continue

                    while True:
                        print verbo.nome + " in " + tempo[0]

                        soluzioni = tempo[1]()
                        pronomi = ["io", "tu", "lui", "noi", "voi", "loro"]

                        errori_totali = 0

                        for i in range(len(pronomi)):
                            errori = 0

                            while True:
                                risposta = raw_input("  [?] " + pronomi[i] + " ")

                                if risposta == "q":
                                    return

                                if risposta.strip() == soluzioni[i]:
                                    print "      Bravo!"
                                    break
                                else:
                                    errori += 1
                                    errori_totali += 1

                                    consiglio = ""

                                    if errori == 1:
                                        consiglio = soluzioni[i][: len(soluzioni[i]) / 4] + "..."
                                    elif errori == 2:
                                        consiglio = soluzioni[i][: len(soluzioni[i]) / 2] + "..."
                                    else:
                                        consiglio = soluzioni[i]

                                    print "      Consiglio: " + consiglio

                        if errori_totali == 0:
                            break

                    print ""

            print "Questo ciclo e completo!\n"

if __name__ == "__main__":
    Ita().intro()
