
class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


world_cups = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 
                 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 
                 2018, 2022]


def world_cup_happened(date):
    year = int(date.split("-")[0])
   
    if year not in world_cups:
        raise InvalidYearCupError('there was no world cup this year')


def is_title_negative(titles):
  
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

def verify_titles(titles,date):
      year = int(date.split('-')[0])
      cups_disputed = [y for y in world_cups if y > year]

      if titles > len(cups_disputed):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
