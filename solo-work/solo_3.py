class Mieszkanie:
    def __init__(self, adres, liczbaPokoi, wlasciciel, metraz, rokBudowy, pietro):
        self.adres_mieszkania = adres
        self.liczbaPokoi = liczbaPokoi
        self.wlasciciel = wlasciciel
        self.metraz = metraz
        self.rokBudowy = rokBudowy
        self.pietro = pietro
        self.mieszkancy = []

    def __str__(self):
        return self.adres_mieszkania + ' , liczba pokoi to: ' + str(self.liczbaPokoi) + ", a metraż wynosi: " \
            + str(self.metraz)

    def zamelduj(self, lokator):
        self.mieszkancy.append(lokator)

    def wymelduj(self, lokator):
        self.mieszkancy.remove(lokator)

    def zliczLokatorow(self):
        self.mieszkancy.len()

mieszkanie1 = Mieszkanie("ul. Łozowa 1/4, 61-146 Poznań", 3, "Jan Nowak", 61, 1956, 2)
mieszkanie1.zamelduj("Anna Kowalska")
mieszkanie1.zamelduj("Marek Szych")
print(mieszkanie1)
print(mieszkanie1.mieszkancy)
mieszkanie1.wymelduj("Marek Szych")
print(mieszkanie1.mieszkancy)