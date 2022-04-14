import fire

'''
This is a simple Fire based CLI which gives the sum of the first x natural numbers or squares x depending
upon the argument passed. This is a slight modification of one of their own examples, provided in their documentation.
'''

def addupto(x):
  return (x(x+1))/2

def square(x):
  return x * x

if __name__ == '__main__':
  fire.Fire({
      'addupto': addupto,
      'square': square,
  })
