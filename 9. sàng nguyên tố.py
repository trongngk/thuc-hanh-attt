def snt(n):
  check=[True]*(n+1)
  for i in range(2,n+1):
    if check[i]:
      for j in range(i*i,n+1,i):
        check[j]=False
  s=[]
  for i in range(2,n+1):
    if check[i]:
      s.append(i)
  return s
n=int(input('Nhap n = '))
print(snt(n))

