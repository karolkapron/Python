class Fraction:

    fraction_type = "ordinal"

    def __init__(self, licznik = None, mianownik = None):
        self.licznik = licznik or 1
        self.mianownik = mianownik or 1

    def listing(self):
        print(f"{self.licznik}/{self.mianownik}")

    def __mul__(self, other):
        x = self.licznik/self.mianownik * other
        return x




if __name__ == "__main__":
    frakcja = Fraction()
    frakcja1 = Fraction(2, 3)
    frakcja.listing()
    frakcja1.listing()
    print(frakcja.fraction_type, frakcja1.fraction_type)
    Fraction.fraction_type = 'test'
    print(frakcja.fraction_type, frakcja1.fraction_type)
    print(frakcja1 * 2.5)