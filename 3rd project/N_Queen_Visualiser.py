import pygame as p
import time
n = int(input("Enter N: ")) 
ans = [[0 for i in range(n)] for j in range(n)]   
end = False
x = y = 150
p.init()
win = p.display.set_mode((800,600))
p.display.set_caption('N Queen Problem')
def allowed(ans,row,col,size):
    time.sleep(1)
    for i in range(size):
        if ans[row][i]:
            return 0 
        if ans[i][col]:
            return 0 
        if row-i >= 0:
            if col-i >= 0:
                if ans[row-i][col-i]:
                    return 0 
            if col+i < size:
                if ans[row-i][col+i]:
                    return 0 
    return 1 
def place(row,queens,size):
    if queens == 0:
        return True 
    for col in range(size):
        if allowed(ans,row,col,size):
            ans[row][col]=1
            p.draw.rect(win,(0,0,255),(x+50*col,y+50*row,49,49))
            p.display.update()
            if place(row+1,queens-1,size):
                return True
            time.sleep(1)
            ans[row][col]=0
            p.draw.rect(win,(255,0,0),(x+1+50*col,y+1+50*row,49,49))
            p.display.update()
    return False
one = 1
while not end:
    for event in p.event.get():
        if event.type == p.QUIT:
            end = True
    if one == 1:
        win.fill((255,0,0))
    for i in range(n+1):
        p.draw.line(win,(0,0,0),(x,y+50*i),(x+50*n,y+50*i),3)
        p.draw.line(win,(0,0,0),(x+50*i,y),(x+50*i,y+50*n),3)
    p.display.update()
    if one == 1:
        place(0,n,n)
        one = 2 
p.quit()
