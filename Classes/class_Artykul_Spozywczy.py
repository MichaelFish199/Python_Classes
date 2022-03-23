from class_Data import Data
from class_Towar import Towar


class Artykul_Spozywczy(Towar):

    """
    Klassa Do Tworzenia Artykułów Sprożywczych

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

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
            Assertion_error:    Jeśli numer inwentarzowy jest mniejszy lub równy zeru
            Assertion_error:    Jeśli cena jest mniejsza od zera
            Assertion_error:    Jeśli ilość jest mniejsza od zera
        """

    def __init__(self, nazwa: str, producent: str, data_produkcji, nr_Inwent: int, data_dostawy, cena: float, ilosc: int,
                 termin_przydatnosci, opakowanie: str):

        super().__init__(nazwa, producent, data_produkcji, nr_Inwent, data_dostawy, cena, ilosc)
        self._termin_przydatnosci = Data(*termin_przydatnosci)
        self._opakowanie = opakowanie

    def __str__(self):
        return f"\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndata_produkcji = {self._data_produkcji},\ndata_dostawy = {self._data_dostawy},\ntermin_przydatnosci = {self._termin_przydatnosci},\nnr_Inwent = {self._nr_Inwent},\nopakowanie = {self._opakowanie},\nilosc = {self._ilosc},\ncena = {self._cena}"

    def dni_do_przeterminowania(self, d, m, r):
        Dni = Data(d, m, r) - self._termin_przydatnosci
        return Dni if Dni > 0 else "\033[91mPRZETERMINOWANE!!!\033[0m"


    @property
    def termin_przydatnosci(self):
        return self._termin_przydatnosci
    @termin_przydatnosci.setter
    def termin_przydatnosci(self, value):
        self._termin_przydatnosci = value


    @property
    def opakowanie(self):
        return self._opakowanie
    @opakowanie.setter
    def opakowanie(self, value):
        self._opakowanie = value




if __name__ == "__main__":
    a = Artykul_Spozywczy("Piernik", "Stefanek", (2,11,2023), 2363, (23,1,2022), 23.99, 5, (21,11,2023), "plastikowe")

    print(a)
    print(a.dni_do_przeterminowania)
    print(a.nazwa)

