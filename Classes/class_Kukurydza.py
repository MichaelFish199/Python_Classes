from class_Data import Data

class Kukurydza:

    """
    Klassa Do Tworzenia Artykułów Sprożywczych

        Parameters
        ----------
        *   odmiana_kukurydzy(str):         Odmiana Kukurydzy
        *   data_zasiania   (str):          Data Zasiania
                - dzien     (int):          Dzień Zasiania
                - miesiac   (int):          Miesiąc Zasiania
                - rok       (int):          Rok Zasiania
        *   data_zbioru     (tuple):        Data Zbioru
                - dzien     (int):          Dzień Zbioru
                - miesiac   (int):          Miesiąc Zbioru
                - rok       (int):          Rok Zbioru
        *   ekologine       (bool):         Czy Ekologiczne Zboże

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
    """

    def __init__(self, odmiana_kukurydzy, data_zasiania, data_zbioru, ekologine: bool = False):
        self._odmiana_kukurydzy = odmiana_kukurydzy
        self._data_zasiania = Data(*data_zasiania)
        self._data_zbioru = Data(*data_zbioru)
        self._ekologiczne = ekologine

    def __str__(self):
        return f"\nodmiana kukurydzy = {self._odmiana_kukurydzy}\ndata zasiania = {self._data_zasiania}\ndata zbioru = {self._data_zbioru}\nekologiczne = {self._ekologiczne}"

    @staticmethod   #metoda nie mająca nic wspólnego z klasą
    def place_dla_rolnika_stasia(przepracowane_godziny, stawka_za_godzine):
        return (przepracowane_godziny * stawka_za_godzine) * 0.85


    @property
    def odmiana_kukurydzy(self):
        return self._odmiana_kukurydzy
    @odmiana_kukurydzy.setter
    def odmiana_kukurydzy(self, value):
        self._odmiana_kukurydzy = value


    @property
    def data_zasiania(self):
        return self._data_zasiania
    @data_zasiania.setter
    def data_zasiania(self, value):
        self._data_zasiania = value


    @property
    def data_zbioru(self):
        return self._data_zbioru
    @data_zbioru.setter
    def data_zbioru(self, value):
        self._data_zbioru = value


    @property
    def ekologiczne(self):
        return self._ekologiczne
    @ekologiczne.setter
    def ekologiczne(self, value):
        self._ekologiczne = value




if __name__ == "__main__":
    a = Kukurydza("Biała", (), (), True)
    print(a)
    print(repr(a))
