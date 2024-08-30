symbol = input()
def getSymbol(card):
  cardsymbols = {
    'A': 'Ace',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10'
  }
  units = {
    'D': 'Diamonds',
    'H': 'Hearts',
    'S': 'Spades',
    'C': 'Clubs'
  }
  if card[:-1] == '10':
    symbol = '10'
    suit = card[-1]
  else:
    symbol = card[0]
    suit = card[1]

  
  symbol_name_full = cardsymbols.get(symbol, 'Unknown')
  unit_name_full = units.get(suit, 'Unknown')
  
  return f"{symbol_name_full} of {unit_name_full}"

print(getSymbol(symbol))




