from class_Artykul_Spozywczy import Artykul_Spozywczy
from class_Kukurydza import Kukurydza

class Platki_Kukurydziane(Artykul_Spozywczy, Kukurydza):

    """
    Klassa Do Tworzenia Platek Kukurydzianych

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
        *   odmiana_kukurydzy(str):         Odmiana Kukurydzy
        *   data_zasiania   (tuple):        Data Zasiania Kukurydzy
                - dzien     (int):          Dzień Zasiania Kukurydzy
                - miesiac   (int):          Miesiąc Zasiania Kukurydzy
                - rok       (int):          Rok Zasiania Kukurydzy
        *   data_zbioru     (tuple):        Data Zbioru Kukurydzy
                - dzien     (int):          Dzień Zbioru Kukurydzy
                - miesiac   (int):          Miesiąc Zbioru Kukurydzy
                - rok       (int):          Rok Zbioru Kukurydzy
        *   ekologine       (bool):         Czy ekologine zborze
        *   pojemnosc_gramy (int):          Ilość Płatków w Opakowaniu

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
            Assertion_error:    Jeśli numer inwentarzowy jest mniejszy lub równy zeru
            Assertion_error:    Jeśli cena jest mniejsza od zera
            Assertion_error:    Jeśli ilość jest mniejsza od zera
        """

    def __init__(self, nazwa: str, producent: str, data_produkcji, nr_Inwent: int, data_dostawy, cena: float, ilosc: int, termin_przydatnosci, opakowanie: str = "plastikowe",
                 odmiana_kukurydzy = "", data_zasiania = (), data_zbioru = (), ekologine: bool = False,
                 pojemnosc_gramy: int = 100):

        Artykul_Spozywczy.__init__(self, nazwa, producent, data_produkcji, nr_Inwent, data_dostawy, cena, ilosc, termin_przydatnosci, opakowanie)
        Kukurydza.__init__(self, odmiana_kukurydzy, data_zasiania, data_zbioru, ekologine)
        self._pojemnosc_gramy = pojemnosc_gramy

    def __str__(self):
        return f"\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndata_produkcji = {self._data_produkcji},\ndata_dostawy = {self._data_dostawy},\ntermin_przydatnosci = {self._termin_przydatnosci},\nnr_Inwent = {self._nr_Inwent},\nopakowanie = {self._opakowanie},\nilosc = {self._ilosc},\ncena = {self._cena}\nodmiana kukurydzy = {self._odmiana_kukurydzy}\ndata zasiania = {self._data_zasiania}\ndata zbioru = {self._data_zbioru}\nekologiczne = {self._ekologiczne}n\pojemnosc = {self._pojemnosc_gramy}"

    @property
    def wartosci_odzywcze(self):
        return f"sod = {7.29 * self.pojemnosc_gramy} [mg]\nweglowodany = {0.841 * self.pojemnosc_gramy} [g]\nbialka = {0.075 * self._pojemnosc_gramy} [g]\nzelazo = {0.289 * self._pojemnosc_gramy} [mg]\nmagnez = {0.39 * self._pojemnosc_gramy} [mg]"


    @property
    def pojemnosc_gramy(self):
        return self._pojemnosc_gramy
    @pojemnosc_gramy.setter
    def pojemnosc_gramy(self, value):
        self._pojemnosc_gramy = value



if __name__ == "__main__":
        a = Platki_Kukurydziane("Płatki", "Nestle", (2, 11, 2023), 2363, (23, 1, 2022), 23.99, 5, (21, 11, 2023),
                              "plastikowe", "2", (), (), True, 100)

        print(a.wartosci_odzywcze())
