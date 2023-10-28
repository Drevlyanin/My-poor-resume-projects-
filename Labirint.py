import random

N = 15
D = (-2, 0), (0, 2), (2, 0), (0, -2)
Map = {(i, j):2-(i%2|j%2) for i in range(N) for j in range (N)}
Todo = [(N//2&-2,N//2&-2)] if random.randrange(2) else [(0,0), (N-1,N-1)]
for x,y in Todo:
    Map[x,y]=0
    
while Todo:
    x,y = Todo.pop(random.randrange(len(Todo)))
    Check = [(dx,dy) for dx,dy in D if 0<=x+dx<N and 0<=y+dy<N and Map [x+dx,y+dy]]
    if Check:
         dx,dy = random.choice(Check)
         Todo.append((x,y))
         Todo.append((x+dx,y+dy))
         Map[x+dx,y+dy]=Map[x+dx/2,y+dy/2]=0

for i in range(N):
    print ("".join(".#"[Map[i,j]] for j in range(N)))