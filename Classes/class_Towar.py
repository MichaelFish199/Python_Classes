from class_Data import Data
from class_Produkt import Produkt


class Towar(Produkt):

    """
    Klassa Do Tworzenia Towarów

        Parameters
        ----------
        *   nazwa   (str):              Nazwa Produktu
        *   producent(str):             Nazwa producenta
        *   data_produkcji(tuple):      Data Produkcji
                - dzien   (int):        Dzien Produkcji
                - miesiac (int):        Miesiac Produkcji
                - rok     (int):        Rok Produkcji
        *   nr_Inwent(int):             Numer Inwentarzowy
        *   data_dostawy(tuple):        Data Dostawy
                - dzien   (int):        Dzień Produkcji
                - miesiac (int):        Miesiąc Produkcji
                - rok     (int):        Rok Produkcji
        *   cena(float):                Cena Za 1 Produkt
        *   ilosc(int):                 Ilość Towaru

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
            Assertion_error:    Jeśli numer inwentarzowy jest mniejszy lub równy zeru
            Assertion_error:    Jeśli cena jest mniejsza od zera
            Assertion_error:    Jeśli ilość jest mniejsza od zera
    """

    __Ilosc_Towarow_Na_Magazynie = 0
    __Wartosc_Towarow_Na_Magazynie = 0

    def __init__(self, nazwa: str, producent: str, data_produkcji,
                 nr_Inwent: int, data_dostawy, cena: float, ilosc: int):

        assert nr_Inwent > 0, "Numer inwentarzowy nie moze byc mniejszy od zera"
        assert cena > 0, "Cena nie moze byc mniejsza od zera"
        assert ilosc > 0, "Ilosc nie moze byc mniejsza od zera"

        super().__init__(nazwa, producent, data_produkcji)
        self._nr_Inwent = nr_Inwent
        self._data_dostawy = Data(*data_dostawy)
        self._cena = cena
        self._ilosc = ilosc
        Towar.__Ilosc_Towarow_Na_Magazynie += ilosc
        Towar.__Wartosc_Towarow_Na_Magazynie += cena * ilosc

    def __str__(self):  #przy str_ach zastanawiałem się nad użciem self.__dict__() aby zmniejszyć ilość pisania ale wyskakiwały napisy: 'obiekt klasy ...' a nie oczekiwana stringowa reprezentacja tych obiektów
        return f"\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndata_produkcji = {self._data_produkcji},\ndata_dostawy = {self._data_dostawy},\nnr_Inwent = {self._nr_Inwent},\nilosc = {self._ilosc},\ncena = {self._cena}"

    def sprzedaj(self, ile):
        if self._ilosc >= ile:
            self._ilosc -= ile
            Towar.__Ilosc_Towarow_Na_Magazynie -= ile
            Towar.__Wartosc_Towarow_Na_Magazynie -= ile * self._cena
            return f"sprzedano {ile}"
        else:
            return "\033[91mBrak towaru\033[0m"

    @property
    def ilosc_towarow_na_magazynie(self):
        return self.__Ilosc_Towarow_Na_Magazynie

    @property
    def wartosc_towarow_na_magazynie(self):
        return round(self.__Wartosc_Towarow_Na_Magazynie, 2)

    @property
    def wartosc_danego_towaru(self):
        return round(self._cena * self._ilosc, 2)


    @property
    def nr_Inwent(self):
        return self._nr_Inwent
    @nr_Inwent.setter
    def nr_Inwent(self, value):
        self._nr_Inwent = value


    @property
    def data_dostawy(self):
        return self._data_dostawy
    @data_dostawy.setter
    def data_dostawy(self, value):
        self._data_dostawy = value


    @property
    def cena(self):
        return self._cena
    @cena.setter
    def cena(self, value):
        self._cena = value


    @property
    def ilosc(self):
        return self._ilosc
    @ilosc.setter
    def ilosc(self, value):
        self._ilosc = value






if __name__ == "__main__":
    a = Towar("Pierniki", "StefanekLUL", (), 2363, (23,1,2022), 23, 5)
    print(a.wartosc_danego_towaru)
    print(a.ilosc_towarow_na_magazynie)
    print(a.posiadane_produkty)
    print(a.wartosc_towarow_na_magazynie)

