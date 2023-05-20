# zadanie 1.1

hello = "Hello"
student = "Ola"
# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
x = "{} {}".format(hello, student)
print(x)

# zadanie 1.2

student = input("Wpisz swoje imie: ")
print("Hello " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]
# policz liczbe studentow w tablicy studenci
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: " + str(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for x in studenci:
 print("Hello " + x)

# zadanie 1.5

liczba = 3
potega = 4
wynik = liczba ** potega
print("Wynik wynosi: " + str(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci = sorted(studenci)
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)