# thuật toán fermat ktra số nguyên tố
from random import randrange
def convertbin(x):
  bin = ""
  while x!=0:
    bin += str(x%2)
    x = x//2
  return bin
def mod(a,n):
  A=a
  b=1
  k = convertbin(n-1)
  if k[0] == '1':
    b=a
  for i in range(1,len(k)):
    A = (A*A) % n
    if k[i] == '1':
      b = (b*A) % n
  return b
def fermat(n):
  a = randrange(2,n-1)
  if mod(a,n)==1:
    return True
  else:
    False

n = int(input("n = "))
if fermat(n):
  print(n,"la so nguyen to")
else:
  print(n,"la hop so")
