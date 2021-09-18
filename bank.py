from card import Card


class Bank:
    client_list = []
    card_list = []

    def __init__(self):
        self.main()

    def main(self):
        while True:
            print('Wybierz opcję')
            print(10 * '*')
            print('1. Dodaj kartę')
            print('2. Pokaż listę kart')
            print('3. Odczytaj saldo')
            option = input('Podaj opcję: ')
            if option == '1':
                pin = input('Podaj PIN: ')
                saldo = input('Podaj saldo: ')
                Bank.card_list.append(Card(pin, saldo))
            elif option == '2':
                print(Bank.card_list)
            elif option == '3':
                # 1. Przyjęcie numeru karty
                card_number = int(input('Podaj numer karty: '))
                # 2. Sprawdzenie, czy dany numer karty istnieje
                if card_number in [card.card_number for card in self.card_list]:
                    # Odzyskuje dla mnie obiekt o numerze karty podanej przez użytkownika
                    card_idx = [card.card_number for card in self.card_list].index(card_number)
                    current_card = self.card_list[card_idx]
                    # 3. Przyjęcie numeru PIN
                    pin = input('Podaj numer PIN: ')
                    # 4. Sprawdzenie czy PIN jest zgodny
                    # 5. Pokazanie salda / info, że PIN jest nieprawidłowy
                    if pin == current_card.pin:
                        print(current_card.saldo)
                    else:
                        print('PIN nieprawidłowy')
                else:
                    print('Nie ma karty o takim numerze')


Bank()
