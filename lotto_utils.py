import random
import pandas as pd

# [블록 1] 한 게임 : 1~45 중 서로 다른 6개를 오름차순으로
def make_game():
    return sorted(random.sample(range(1, 46), 6))

# [블록 2] 여러 게임 : make_game()을 count번 모으기
def make_games(count):
    games = []
    for i in range(count):
        games.append(make_game())
    return games

# [블록 3] 화면용 글자 : [3, 15, 22, …] → '3 - 15 - 22 - …'
def to_text(game):
    words = []
    for n in game:
        words.append(str(n))
    return ' - '.join(words)