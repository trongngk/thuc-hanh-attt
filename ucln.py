def gcd(a,b):
  A=a
  B=b
  while B>0:
    R=A%B
    A=B
    B=R
  return A
a,b=map(int,input("Nhap a,b = ").split())
print(gcd(a,b))
