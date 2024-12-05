

class Sõlm:
    def __init__(self, väärtus):
        self.väärtus = väärtus  # Sõlme väärtus
        self.vasak = None       # Viide vasakule alampuule
        self.parem = None       # Viide paremale alampuule

class Binaarpuu:
    def __init__(self):
        self.juur = None        # Puu juursõlm

    def lisa(self, väärtus):
        if not self.juur:
            self.juur = Sõlm(väärtus)  # Kui puu on tühi, loo juursõlm
        else:
            self._lisa(self.juur, väärtus)  # Lisa väärtus rekursiivselt

    def _lisa(self, sõlm, väärtus):
        if väärtus < sõlm.väärtus:        # Kui väärtus on väiksem, liigu vasakule
            if sõlm.vasak is None:
                sõlm.vasak = Sõlm(väärtus)  # Lisa vasakule, kui koht on tühi
            else:
                self._lisa(sõlm.vasak, väärtus)  # Jätka vasakult
        else:                             # Kui väärtus on suurem või võrdne, liigu paremale
            if sõlm.parem is None:
                sõlm.parem = Sõlm(väärtus)  # Lisa paremale, kui koht on tühi
            else:
                self._lisa(sõlm.parem, väärtus)  # Jätka paremalt

    def läbikäik(self, sõlm):
        if sõlm:
            self.läbikäik(sõlm.vasak)         # Käi läbi vasak alampuu
            print(sõlm.väärtus, end=" ")      # Prindi sõlme väärtus
            self.läbikäik(sõlm.parem)         # Käi läbi parem alampuu

# Näide kasutusest
puu = Binaarpuu()
for väärtus in [5, 3, 7, 2, 4, 6, 8]:  # Lisatakse väärtused puusse
    puu.lisa(väärtus)

print("Järjestikune läbikäik:", end=" ") 
puu.läbikäik(puu.juur)  # Prinditakse väärtused järjestatud kujul: vasak alampuu → juur → parem alampuu
