import fire
import argparse

parser=argparse.ArgumentParser(description="calculations")
parser.add_argument("-a","--number1",type=int,help="first number")
parser.add_argument("-b","--number2",type=int,help="second number")
args=parser.parse_args()

def add(a,b):
    answer= a+b
    return answer

if __name__ == '__main__':
    print (add(args.number1,args.number2))
  

def modulus(a,b):
    answer=a%b
    return answer 

if __name__ == '__main__':
    print (modulus(args.number1,args.number2))

def division(j,g):
    answer=j/g
    return answer

if __name__ == '__main__':
    print (division(args.number1,args.number2))

def wholenumber(h,r):
    answer=h//r
    return answer

if __name__ == '__main__':
    print (wholenumber(args.number1,args.number2))

def multiply(p,w):
    answer= p*w 
    return answer
if __name__ == '__main__':
    print (multiply(args.number1,args.number2))

def percentage(a,b):
    answer=a/b*100
    return answer

if __name__ == '__main__':
    print (percentage(args.number1,args.number2))    

def subtract (a,b):
    answer= a-b
    return answer 

if __name__ == '__main__':
    print (subtract(args.number1,args.number2))    

def exponent(a,b):
    answer= a**b
    return answer

if __name__ == '__main__':
    print (exponent(args.number1,args.number2))
# if __name__ == '__main__':
#   fire.Fire()     





