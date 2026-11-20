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
# [블록 4] CSV 읽기 → 번호별 당첨 횟수 딕셔너리
COLS = ['당첨번호1', '당첨번호2', '당첨번호3',
        '당첨번호4', '당첨번호5', '당첨번호6']

def load_counts(fname):
    df = pd.read_csv(fname, encoding='utf-8-sig')
    count = {}
    for n in range(1, 46):
        count[n] = 0
    for col in COLS:
        for n in df[col]:
            count[n] += 1
    return count

# [블록 5] 자주 나온 번호 top개 (횟수 내림차순)
def top_numbers(count, top=20):
    items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    nums = []
    for n, c in items[:top]:
        nums.append(n)
    return nums

# [블록 6] 자주 나온 번호 20개 중에서 한 게임
def make_hot_game(count):
    return sorted(random.sample(top_numbers(count), 6))
