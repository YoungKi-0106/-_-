import pickle
import os

def input_scores():
    print('[점수 입력]')
    i = 1
    a = {}
    with open('data/score.bin', 'wb') as file:
        while True:
            b = int(input(f'#{i}? '))
            if b < 0:
                pickle.dump(a, file)
                break
            else:
                a[i] = b
                i += 1

def get_average():
    total = 0
    i = 1
    with open('data/score.bin', 'rb') as file:
        a = pickle.load(file)
        while True:
            if i in a:
                b = a.get(i)
                total += b
                i += 1
            else:
                break
        average = total / len(a.keys())
        return average

def show_scores():
    print()
    print('[점수 출력]')
    print('개인점수: ', end='')
    with open('data/score.bin', 'rb') as file:
        a = pickle.load(file)
        i = 1
        while True:
            if i in a:
                print(f'{a.get(i)} ', end='')
                i += 1
            else:
                break
    print()
    print(f'평균: {get_average()}')

if os.path.exists('data/score.bin'):
    print('[파일 읽기]')
    show_scores()
else:
    input_scores()
    show_scores()