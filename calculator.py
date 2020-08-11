class Calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def div(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def sub(self):
        try:
            return  self.a / self.b
        except ZeroDivisionError:
            return("Nie dzielimy przez 0! ")



while True:
    print('''
    Wybierz co chcesz zrobic:
    1: dodawanie:
    2: odejmowanie:
    3: mnozenie:
    4. dzielenie:
    5: wyjscie: ''')
    while True:
        try:
            x = int(input("Wybierz operację: "))
            if x >=6:
                raise ValueError
            else:
                break;
        except ValueError:
            print ("Wybierz prawidłową operacje! ")
    if x == 5:
        print("Wychodzisz z programu! ")
        break;
    while True:
        try:
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            break;
        except ValueError:
            print("Podaj liczbę! ")
    if x == 1:
        print("Wynik: ", Calc(a,b).add())
    if x == 2:
        print("Wynik: ", Calc(a,b).div())
    if x == 3:
        print("Wynik: ", Calc(a,b).mul())
    if x == 4:
        print("Wynik: ", Calc(a,b).sub())
