N = input()
data = list(map(int, N))
length = len(data)

if sum(data[:(length//2)]) == sum(data[(length//2):]):
  print("LUCKY")
else :
  print("READY")