from lotto_utils import *

while True:
    try:
        count = int(input('몇 게임 할까요? (1~10) : '))
        if 1 <= count <= 10:
            break
        print('1~10 사이로 입력하세요.')
    except ValueError:
        print('숫자만 입력하세요.')

games = make_games(count)
print('=== 이번 주 로또 번호 ===')
for i in range(count):
    print(f'{i + 1}게임 :', to_text(games[i]))