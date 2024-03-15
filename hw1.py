#이영기_201911103


def get_radius(prompt):
  r = int(input(prompt))
  return r

print('시작\n')
R=get_radius('넓이를 구하고자 하는 원의 반지름은? ')

def get_circle_area(some):
  A = some*some*3.14
  print('반지름이 ',R,'인 원의 넓이 = 3.14 x',R,' x ',R,' = ',A)
get_circle_area(R)

