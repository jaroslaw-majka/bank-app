class Card:
    provider = 'MasterCard'
    next_card_number = 1

    def __init__(self, pin, saldo):
        self.card_number = self.next_card_number
        self.pin = pin
        self.saldo = saldo
        Card.next_card_number += 1

    def change_pin(self):
        self.pin = int(input('Podaj nowy PIN: '))

    def change_saldo(self):
        self.saldo = int(input('Podaj nowe saldo: '))
