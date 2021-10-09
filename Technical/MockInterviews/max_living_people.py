# JSON INput
"""
arr = [
  {"name": "Joe", "birth": 1900, "death": 1930},
  {"name": "John", "birth": 1920, "death": 1925},
  {"name": "Bill", "birth": 1900, "death": 1930},
]

What was the year where the most number of people were alive.

"""

class YearEvts:
  def __init__(self):
    self.births = 0
    self.deaths = 0

def mostAlive(arr):
  numAlive = 0
  bestFound = 0
  bestYear = 0
  years = {}
  for person in arr:
    if person['birth'] in years:
      years[person['birth']].births += 1
    else:
      evt = YearEvts()
      evt.births = 1
      years[person['birth']] = evt
    if person['death'] is not None and person['death'] in years:
      years[person['death']].deaths += 1
    elif person['death'] is not None:
      evt = YearEvts()
      evt.deaths = 1
      years[person['death']] = evt
  
  yearKeys = sorted(list(years.keys()), key=lambda y: y)
  for year in yearKeys:
    evt = years[year]
    tally = 0
    tally = evt.births - evt.deaths # Depends on edgecase.
    if evt.births > 0:
      possibleBest = evt.births + numAlive
      if possibleBest > bestFound:
        bestFound = possibleBest
        bestYear = year
    numAlive += tally
  return bestYear

print(mostAlive([
  {"name": "Joe", "birth": 1900, "death": 1930},
  {"name": "Josh", "birth": 1920, "death": 1920},
  {"name": "Bill", "birth": 1950, "death": 1960},
  {"name": "Bill2", "birth": 1950, "death": 1960},
  {"name": "Bill3", "birth": 1950, "death": 1960},
]))
    
  