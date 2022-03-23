from class_Data import Data


class Produkt:

    """
    Klassa Do Tworzenia Produktów

        Parameters
        ----------
        *   nazwa   (str):          Nazwa Produktu
        *   producent(str):         Nazwa producenta
        *   data_produkcji(tuple):  Data Produkcji
                - dzien   (int):    Dzień Produkcji
                - miesiac (int):    Miesiąc Produkcji
                - rok     (int):    Rok Produkcji

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
    """

    __Posiadane_Produkty = "\n\033[4mPosiadane Produkty:\033[0m\n"

    def __init__(self, nazwa: str, producent: str, data_produkcji):
        self._nazwa = nazwa
        self._producent = producent
        self._data_produkcji = Data(*data_produkcji)
        Produkt.__Posiadane_Produkty += ("- "+ nazwa + "\n")

    def __str__(self):
        return f"\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndataProdukcji = {self._data_produkcji}"

    @property
    def posiadane_produkty(self):
        return Produkt.__Posiadane_Produkty
    def reset_posiadane_produkty(self, password):
        if password == "0000":
            Produkt.__Posiadane_Produkty = 0

    def create_email(self):
        a = self._producent.replace(" ", "")
        self.__email = f"{a}@gmail.com"
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value
    @email.deleter
    def email(self):
        self.__email = None


    @property
    def nazwa(self):
        return self._nazwa
    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value


    @property
    def producent(self):
        return self._producent
    @producent.setter
    def producent(self, value):
        self._producent = value


    @property
    def data_produkcji(self):
        return self._data_produkcji
    @data_produkcji.setter
    def data_produkcji(self, value):
        self._data_produkcji = value








if __name__ == "__main__":
    a = Produkt("Telewizor", "Pawel Plusa", (13,1,2020))
    b = Produkt("Mleko", "Chatys", (23,12,2021))
    c = Produkt("PS4", "Kowlaski", (9,11,2007))
    a.create_email()
    print(a.email)
    a.email = "23r32r"
    print(a.email)
    del a.email
    print(a.email)