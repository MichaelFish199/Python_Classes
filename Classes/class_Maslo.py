from class_Artykul_Spozywczy import Artykul_Spozywczy


class Maslo(Artykul_Spozywczy):

    """
    Klassa Do Tworzenia Masła

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
        *   waga_1          (float):        Waga 1 Kostki w Gramach
        *   rodzaj          (str):          Rodzaj Masła

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
            Assertion_error:    Jeśli numer inwentarzowy jest mniejszy lub równy zeru
            Assertion_error:    Jeśli cena jest mniejsza od zera
            Assertion_error:    Jeśli ilość jest mniejsza od zera
            Assertion_error:    Jeśli waga 1 kostki masła jest mniejsza od zera
        """

    def __init__(self,nazwa: str, producent: str, data_produkcji, nr_Inwent: int, data_dostawy, cena: float, ilosc: int, termin_przydatnosci, opakowanie: str,
                 waga_1: float = 1, rodzaj: str = None):

        assert  waga_1 > 0, "waga nie moze byc mniejsza lub rowna zeru"

        super().__init__(nazwa, producent, data_produkcji, nr_Inwent, data_dostawy, cena, ilosc, termin_przydatnosci, opakowanie)
        self._waga = waga_1
        self._rodzaj = rodzaj
        self.__kategoria(rodzaj, waga_1)

    def __str__(self):
        return f"\n\033[4minformacje:\033[0m\nnazwa = {self._nazwa},\nproducent = {self._producent},\ndata produkcji = {self._data_produkcji},\ndata dostawy = {self._data_dostawy},\ntermin_przydatnosci = {self._termin_przydatnosci},\nnumer inwentarzowy = {self._nr_Inwent},\nopakowanie = {self._opakowanie},\nrodzaj = {self._rodzaj},\nilosc = {self._ilosc},\ncena = {self._cena}"

    def __kategoria(self, rodzaj, waga):    # nie chce aby ta metoda była osiągalna dla użytkownika ( __ )
        match rodzaj:       #moglem zrobic podklasy Masel ale nie chcialem sie rozbudowywac
            case "ekstra":  #moglem użyć w przypadkach > str.startswith() or str.endswith() < aby wyeliminowac blad czlowieka
                self._wartosc_energetyczna = 7.35 * waga
                self._bialka = round(0.007 * waga, 2)
                self._weglowodany = round(0.007 * waga, 2)
                self._tluszcze = 0.825 * waga
                self._woda = 0.16 * waga

            case "smietankowe":
                self._wartosc_energetyczna = 6.58 * waga
                self._bialka = round(0.011 * waga, 2)
                self._weglowodany = round(0.011 * waga, 2)
                self._tluszcze = 0.735 * waga
                self._woda = 0.24 * waga

            case "orzechowe":
                self._wartosc_energetyczna = 5.97 * waga
                self._bialka = 0.2221 * waga
                self._weglowodany = 0.2231 * waga
                self._tluszcze = 0.5136 * waga
                self._woda = 0.0123 * waga

            case _: # ostatni przypadek dla rodzaju masla ktore nie znajduje sie w bazie, dzieki temu
                self._wartosc_energetyczna = None    #nadal mozna uzywac metody 'wartosc odzywcza'
                self._bialka = None  #i co najwyzej dynamicznie (pozaklasa) zmienic attrybuty obiektu
                self._weglowodany = None
                self._tluszcze = None
                self._woda = None

    @property
    def wartosc_odzywcza(self):
        return f"\n\033[4mwartosc_odzywcza:\n\033[0mwartosc_energetyczna = {self._wartosc_energetyczna},\nbialka = {self._bialka},\nweglowodany = {self._weglowodany},\ntluszcze = {self._tluszcze},\nwoda = {self._woda}"

    @property
    def maslo_info(self):
        return f"\nMasło {self._rodzaj} {self._cena}"

    def ktore_zdrowsze(self, other):
        x = self._wartosc_energetyczna / self._waga
        y = other._wartosc_energetyczna / other._waga
        return self.rodzaj if x < y else other.rodzaj #pomijam ==


    @property
    def rodzaj(self):
        return self._rodzaj
    @rodzaj.setter
    def rodzaj(self, value):
        self._rodzaj = value


    @property
    def waga(self):
        return self._waga
    @waga.setter
    def waga(self, value):
        self._waga = value


    @property
    def wartosc_energetyczna(self):
        return self._wartosc_energetyczna
    @wartosc_energetyczna.setter
    def wartosc_energetyczna(self, value):
        self._wartosc_energetyczna = value


    @property
    def bialka(self):
        return self._bialka
    @bialka.setter
    def bialka(self, value):
        self._bialka = value


    @property
    def weglowodany(self):
        return self._weglowodany
    @weglowodany.setter
    def weglowodany(self, value):
        self._weglowodany = value


    @property
    def tluszcze(self):
        return self._tluszcze
    @tluszcze.setter
    def tluszcze(self, value):
        self._tluszcze = value


    @property
    def woda(self):
        return self._woda
    @woda.setter
    def woda(self, value):
        self._woda = value





if __name__ == "__main__":
    a = Maslo("Masło", "Stefanek", (21,11,2021), 2363, (21,11,2022), 9.99, 5, (1,11,2023), "plastikowe", 100, "orzechowe")
    b = Maslo("Masło", "Stefanek", (21, 11, 2021), 2363, (21, 11, 2022), 9.99, 5, (1, 11, 2023), "plastikowe", 100, "smietankowe")
    print(a)
    print(a.maslo_info)
    print(a.ktore_zdrowsze(b))