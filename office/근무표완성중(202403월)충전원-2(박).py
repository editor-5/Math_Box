
a = {'주간': '이성용', '야간': '이재평', '휴무': '박병훈'}
b = {'주간': '박병훈', '야간': '이성용', '휴무': '이재평'}
c = {'주간': '이재평', '야간': '박병훈', '휴무': '이성용'}
d = {'주간': '     ', '야간': '이재평', '휴무': '이성용,박병훈'}
e = {'주간': '     ', '야간': '이성용', '휴무': '박병훈,이재평'}
f = {'주간': '     ', '야간': '박병훈', '휴무': '이재평,이성용'}
g = {'주간': '이성용', '야간': '박병훈', '휴무': '이재평'}
h = {'주간': '이재평', '야간': '이성용', '휴무': '박병훈'}
i = {'주간': '박병훈', '야간': '이재평', '휴무': '이성용'}

data = [a, b, c, d, e, f, g, h, i]

# a ->x c, b ->x a, c ->x b,    
# a ->x h, b ->x g, c ->x i   
# d ->x b, e ->x a, f ->x c  
# d ->x i, e ->x g, f ->x h
# g ->x i, g ->x b
# h->x g, h->x a
# i ->x h, i ->x c

for _ in range(1):

  print(data[data.index(a)])   
  
for _ in range(2):
  
  print(data[data.index(b)])
  print(data[data.index(b)]) 
  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])
  print(data[data.index(a)])
  
for _ in range(1):

  print(data[data.index(b)])
  print(data[data.index(b)]) 
  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(c)])
  print(data[data.index(a)])  
  print(data[data.index(a)])

for _ in range(1):

  print(data[data.index(b)])
  print(data[data.index(b)]) 
  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])
  print(data[data.index(a)])  

for _ in range(1):

  print(data[data.index(b)])
  print(data[data.index(b)]) 
  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])
  
  
