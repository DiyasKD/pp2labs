from time import sleep
import math
t = int(input())
n = int(input())
def invoke_sleeping(num, ms):
    sleep(ms/1000)
    return math.sqrt(num)
print("Square root of", n , "after", t ,"specific miliseconds is", invoke_sleeping(n, t)) 
