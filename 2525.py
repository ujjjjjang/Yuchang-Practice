A, B = map(int,input().split())
x = int(input())

A += x//60
B += x % 60

if B>=60:
    A+=1
    B-=60
if A >= 24:
    A-=24

print('%d %d' % (A,B))