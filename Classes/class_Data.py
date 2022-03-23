class DataException(Exception):
    pass


class DzienException(DataException):
    pass


class MiesiacException(DataException):
    pass


class RokException(DataException):
    pass


class Data:

    """
    Klassa Do Tworzenia Dat

        Parameters
        ----------
        *   dzien   (int):  Liczba pomiędzy 1 ... 30
        *   miesiac (int):  Liczba pomiędzy 1 ... 12
        *   rok     (int):  Liczba pomiędzy 1 ... inf

        Raises
        ------
            DzienException:     Jeśli podany dzień jest poza zakresem: 0 < d < 31
            MiesiacException:   Jeśli podany miesiąc jest poza zakresem: 0 < d < 13
            RokException:       Jeśli podany rok jest poza zakresem: 0 < r
    """

    def __init__(self, d: int = 1, m: int = 1, r: int = 2000):

        if not 0 < d < 31:          #moim zdaniem taka składnia (a<b<c) jest zrozumiała
            raise DzienException    #dla większej ilości osób (naukowców/matematyków)
        if not 0 < m < 13:          #*gdyby był assert wystarczy usunąć not i dodać string
            raise MiesiacException
        if not 0 < r:
            raise RokException

        self.dni = (d - 1) + (m - 1) * 30 + (r - 1900) * 360

    def __str__(self):
        rok = (self.dni // 360) + 1900
        miesiac = ((self.dni % 360) // 30) + 1
        dzien = ((self.dni % 360) % 30) + 1
        return f'{dzien:02}-{miesiac:02}-{rok:04}'

    def __sub__(self, other):
        return self.dni - other.dni

    def setDzien(self, d):
        if d < 0 or d > 30:
            raise DzienException
        rok = (self.dni // 360) + 1900
        miesiac = ((self.dni % 360) // 30) + 1
        self.dni = (d - 1) + (miesiac - 1) * 30 + (rok - 1900) * 360

    def setMiesiac(self, m):
        if m < 0 or m > 12:
            raise MiesiacException
        rok = (self.dni // 360) + 1900
        dzien = ((self.dni % 360) % 30) + 1
        self.dni = (dzien - 1) + (m - 1) * 30 + (rok - 1900) * 360

    def setRok(self, r):
        if r < 0:
            raise RokException
        miesiac = ((self.dni % 360) // 30) + 1
        dzien = ((self.dni % 360) % 30) + 1
        self.dni = (dzien - 1) + (miesiac - 1) * 30 + (r - 1900) * 360

    def setData(self, data_napis):
        data_lista = data_napis.split('-')
        self.setDzien(int(data_lista[0]))
        self.setMiesiac(int(data_lista[1]))
        self.setRok(int(data_lista[2]))

    def getDzien(self):
        return ((self.dni % 360) % 30) + 1

    def getMiesiac(self):
        return ((self.dni % 360) // 30) + 1

    def getRok(self):
        return (self.dni // 360) + 1900

    def getData(self):
        rok = (self.dni // 360) + 1900
        miesiac = ((self.dni % 360) // 30) + 1
        dzien = ((self.dni % 360) % 30) + 1
        return dzien, miesiac, rok

    def getDniOd1900(self):
        return self.dni

    def jutro(self):
        self.dni += 1

    def wczoraj(self):
        self.dni -= 1

    def wPrzyszlosc(self, n):
        self.dni += n

    def doPrzeszlosci(self, n):
        self.dni -= n

    def porownajDaty(self,data1):
        return self.dni - data1.getDniOd1900()

    def roznicaDat(self,data1):
        return self.dni - data1.getDniOd1900()



if __name__ == '__main__':

    a = Data(24, 12, 2010)
    print(a)

    b = Data(24, 12, 2011)
    print(a)

    print(Data.roznicaDat(a,b))
    print(Data.__doc__)