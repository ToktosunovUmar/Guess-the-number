from decouple import Config, RepositoryIni
from logic import play_game

config = Config(RepositoryIni('settings.ini'))

range_start = config('range_start', cast=int)
range_end = config('range_end', cast=int)
attempts = config('attempts', cast=int)
capital = config('capital', cast=int)

play_game(range_start, range_end, capital, attempts)
