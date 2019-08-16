n=int(input("Digite un numero"))
x=0
for i in range(n):
    if(( x % 15) == 0):
        print( 'FizzBuzz' )
    elif(( x % 3) == 0):
        print( 'Fizz' )
    elif(( x % 5) == 0):
        print( 'Buzz' )
    else: 
        print( x )
  

