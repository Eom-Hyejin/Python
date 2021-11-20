def plus(a,b):
  if type(a) is str or type(b) is str:
    return int(a) + int(b)
  else:
    return a + b

def minus(a,b):
  if type(a) is str or type(b) is str:
    return int(a) - int(b)
  else:
    return a - b

def times(a,b):
  if type(a) is str or type(b) is str:
    return int(a) * int(b)
  else:
    return a * b

def division(a,b):
  if type(a) is str or type(b) is str:
    return int(a) / int(b)
  else:
    return a / b

def negation(a):
  if type(a) is str:
    return -int(a)
  else:
    return -a

def power(a,b):
  if type(a) is str or type(b) is str:
    return int(a) ** int(b)
  else:
    return a ** b

def remainder(a,b):
  if type(a) is str or type(b) is str:
    return int(a) % int(b)
  else:
    return a % b

print(plus(3,"7"))
print(minus("9",1))
print(times("10",2))
print(division("9","3"))
print(negation("-3"))
print(power("10",2))
print(remainder("9","3"))


def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cannot drink")
  elif age == 18 or age == 19:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still king of young")
  else:
    print("enjoy your drink")

age_check(18)