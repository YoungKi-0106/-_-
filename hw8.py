# -*- coding: utf-8 -*-
"""hw8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cOC1TbzchbbvfzBpETwUvYqeQf-T5jIz
"""



#개념확인과제 201911103 이영기
def buy(a):
  print('[구입]')
  item=input('상품명? ')
  if item == '':
    print()
    return False
  else:
    much=int(input('수량은? '))
    a[item]=much
    print(f'장바구니에 {item}가 {much}개가 담겼습니다.')
    print()
def show(a):
  print(f'>>>장바구니 보기: {shopping_bag}\n')

def find(a):
  print(f'[검색]')
  b=input('장바구니에서 확인하고자 하는 상품은? ')
  if b in a:
    print(f'{b}(는) {shopping_bag[b]}개 담겨 있습니다.')
  else:
    print(f'장바구니에 {b}은(는) 없습니다. ')


shopping_bag={}
while True:
  if buy(shopping_bag)==False:
    break
show(shopping_bag)
find(shopping_bag)