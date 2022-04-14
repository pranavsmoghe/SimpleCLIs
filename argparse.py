import argparse

'''
A simple argparse based CLI which takes in two integers as 
parameters and returns their sum when passed with the 
appropriate command or simply returns the greatest value
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+")
    parser.add_argument("--sum", dest='accumulate', action='store_const', const=sum, default=max)    
    args = parser.parse_args()
    print(sum(args.integers))
