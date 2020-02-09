# For at filtrere kan man gøre som i java, og selv definere get og set metoder. Gør values private også
class Product:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris

    # bruges til at fortælle python at der er en setter metode til den.
    @property
    def navn(self):
        return self.__navn

    @navn.setter
    def navn(self, nytNavn):
        self.__navn = nytNavn

    @property
    def pris(self):
        return self.__pris

    @pris.setter
    def pris(self, Nypris):
        if type(Nypris) == int and Nypris > 0:
            self.__pris = Nypris
        else:
            raise ValueError("Ikke heltal")


Bil = Product("Toyoda", 22)
Bil2 = Product("Lolo", "2321")
