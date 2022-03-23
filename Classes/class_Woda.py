from class_Artykul_Spozywczy import Artykul_Spozywczy


class Woda(Artykul_Spozywczy):

    """
    Klassa Do Tworzenia Wody

        Parameters
        ----------
        *   nazwa           (str):          Nazwa Produktu
        *   producent       (str):          Nazwa producenta
        *   data_produkcji  (tuple):        Data Produkcji
                - dzien     (int):          Dzień Produkcji
                - miesiac   (int):          Miesiąc Produkcji
                - rok       (int):          Rok Produkcji
        *   nr_Inwent       (int):          Numer Inwentarzowy
        *   data_dostawy    (tuple):        Data Dostawy
                - dzien     (int):          Dzień Produkcji
                - miesiac   (int):          Miesiąc Produkcji
                - rok       (int):          Rok Produkcji
        *   cena            (float):        Cena Produktu
        *   ilosc           (int):          Ilość Produktu
        *   termin_przydatnosci(tuple):     Termin Przydatności do Spożycia
                - dzien     (int):          Dzień Terminu Przydatności do Spożycia
                - miesiac   (int):          Miesiąc Terminu Przydatności do Spożycia
                - rok       (int):          Rok Terminu Przydatności do Spożycia
        *   opakowanie      (str):          Materiał z Jakiego Jest Zrobione Opakowanie
        *   rodzaj          (str):          Rodzaj Wody (źródlana, mineralna)
        *   gazowana        (bool):         Woda Gazowana
        *   pojemnosc_ml    (float):        Ilość Wody w Opakowaniu w Mililitrach

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
            Assertion_error:    Jeśli numer inwentarzowy jest mniejszy lub równy zeru
            Assertion_error:    Jeśli cena jest mniejsza od zera
            Assertion_error:    Jeśli ilość jest mniejsza od zera
        """

    def __init__(self,nazwa: str, producent: str, data_produkcji, nr_Inwent: int, data_dostawy, cena: float, ilosc: int, termin_przydatnosci, opakowanie: str = "plastikowe",
                 rodzaj: str = None, gazowana = True, pojemnosc_ml: float = 250):

        super().__init__(nazwa, producent, data_produkcji, nr_Inwent, data_dostawy, cena, ilosc, termin_przydatnosci, opakowanie)
        self._rodzaj = rodzaj
        self._gazowana = gazowana
        self._pojemnosc_ml = pojemnosc_ml

    def __str__(self):
        return f"\n\033[4minformacje:\033[0m\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndata_produkcji = {self._data_produkcji},\ndata_dostawy = {self._data_dostawy},\ntermin_przydatnosci = {self._termin_przydatnosci},\nnr_Inwent = {self._nr_Inwent},\nopakowanie = {self._opakowanie},\nilosc = {self._ilosc},\ncena = {self._cena}"

    def __lt__(self, other):
        return self.pojemnosc_ml < other.pojemnosc_ml

    def __le__(self, other):
        return self.pojemnosc_ml <= other.pojemnosc_ml

    def __eq__(self, other):
        return self.pojemnosc_ml == other.pojemnosc_ml

    def __ne__(self, other):
        return self.pojemnosc_ml != other.pojemnosc_ml

    def __gt__(self, other):
        return self.pojemnosc_ml > other.pojemnosc_ml

    def __ge__(self, other):
        return self.pojemnosc_ml >= other.pojemnosc_ml


    @property
    def woda_info(self):
        return f"\nWoda {self._rodzaj} {'gazowana' if self._gazowana else 'niegazowana'} {self._pojemnosc_ml} mililitrow"


    @property
    def rodzaj(self):
        return self._rodzaj
    @rodzaj.setter
    def rodzaj(self, value):
        self._rodzaj = value


    @property
    def gazowana(self):
        return self._gazowana
    @gazowana.setter
    def gazowana(self, value):
        self._gazowana = value


    @property
    def pojemnosc_ml(self):
        return self._pojemnosc_ml
    @pojemnosc_ml.setter
    def pojemnosc_ml(self, value):
        self._pojemnosc_ml = value





if __name__ == "__main__":
    a = Woda("Masło", "Stefanek", (21,11,2021), 2363, (21,11,2022), 3.99, 40, (1,11,2023), "plastikowe", "zrodlana", False, 500)
    print(a)
    print(a.woda_info)
