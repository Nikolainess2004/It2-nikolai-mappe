class Bruker:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    """
    def __init__(self, epost, fornavn, etternavn):
        self.epost=epost
        self.fornavn=fornavn
        self.etternavn=etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker):
    """Superklasse for Lærere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: En int med brukers lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto=lønnskonto

class Faglærer(Lærer):
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse=[]
        self.klasser=[]

class Kontaktlærer(Lærer):
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse=klasse
        self.trinn=trinn

class Elev(Bruker):
    """Superklasse for Elever i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        trinn: En string med brukers trinn
        klasse: En string med brukers klasse
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self.trinn=trinn
        self.klasse=klasse
        self.fag=[]

        

# Denne brukes for testing, betyr at koden inne i if-setningen
# kun kjøres hvis vi "trykker play" på denne filen eller kjører denne fila i terminalen
if __name__=="__main__":
    ravi=Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()
    ravi.logg_ut()

    camilla=Elev("cammilac@kkg.no", "Camilla", "Coward", 2, "STG")
    camilla.logg_inn()
    camilla.logg_ut()