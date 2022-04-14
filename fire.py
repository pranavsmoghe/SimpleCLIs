import fire

def addupto(x):
  return (x(x+1))/2

def square(x):
  return x * x

if __name__ == '__main__':
  fire.Fire({
      'addupto': addupto,
      'square': square,
  })
