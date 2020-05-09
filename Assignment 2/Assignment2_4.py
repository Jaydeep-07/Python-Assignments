def sum_of_factors(x, y=1):
  if (y >= x):
    return 0
  if (x % y == 0):
    return y + sum_of_factors(x, y + 1)
  return sum_of_factors(x, y + 1)
  
print("Enter The Number")
no=input()
no=int(no)
r=sum_of_factors(no)
print(r)