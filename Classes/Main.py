from class_Woda import Woda
from class_Platki_Kukurydziane import Platki_Kukurydziane
from class_Maslo import Maslo


obj_1 = Woda("Muszynianka", "Muszynianka", (12,11,2021), 120034, (11,1,2022), 3.99, 35, (8,9,2023), "plastikowe", "źródlana", True, 1000)
obj_2 = Platki_Kukurydziane("CornFlakes", "Nestle", (10,12,2021), 120020, (11,1,2022), 6.99, 40, (18,12,2023), "plastikowe", "amerykanska", (10,2,2021), (25,9,2021), True, 200)
obj_3 = Maslo("MasloPolskie", "Mlekowita", (3,8,2021), 120011, (7,11,2022), 5.99, 80, (30,4,2023), "folia ekologiczna", 250, "smietankowe")








#poniżej jest wykożystane kilka metod
"""
print("Ilość towarów na magazynie =",obj_1.ilosc_towarow_na_magazynie)
print("Wartość towarów na magazynie =",obj_1.wartosc_towarow_na_magazynie)
print(obj_1.__class__.__name__,": wartość tego towaru na magazynie = ",obj_1.wartosc_danego_towaru)
print()
print(obj_1.sprzedaj(23))
print("Towary po sprzedaży:")
print()
print("Ilość towarów na magazynie =",obj_1.ilosc_towarow_na_magazynie)
print("Wartość towarów na magazynie =",obj_1.wartosc_towarow_na_magazynie)
print(obj_1.__class__.__name__,": wartość tego towaru na magazynie = ",obj_1.wartosc_danego_towaru)

print("\ndni do przeterminowania =", obj_1.dni_do_przeterminowania(1,2,2022))

print(obj_2.wartosci_odzywcze)
"""
