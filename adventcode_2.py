import sys
from collections import defaultdict
import re

def adventofcode4(path):
    f = open(path).read().strip()
    cardnumbers,mynumbers = '',''
    total, totalwins, index = 0,0,0
    Cardswon = defaultdict(int) # array of int for how many cards won of that specific card
    for card in f.split('\n'):
        index +=1
        card = card.split(':') # get rid of the card text
        card = card[1].split('|') # split at the 
        cardnumbers,mynumbers = card[0],card[1] # define the cardnumber and mynumber by the index due to the split before
        counter,wins = 0,0
        for mynumber in mynumbers.split(): # split on all whitespaces
            for cardnumber in cardnumbers.split(): # split on all the whitespaces
                if mynumber == cardnumber: # check if equal
                    wins += 1   # add win if equal
                    if counter == 0: counter = 1
                    else: counter *= 2 # multiply the counter by 2
        tempindex=index
        while wins > 0:
            tempindex = tempindex+1 # never count the card itself 
            Cardswon[tempindex] += 1+ Cardswon[index] # 1 + the total saved on the current card location defined by the index
            wins -=1
        total += counter
    for x, woncard in Cardswon.items():
        totalwins += woncard # add up all the values of the array
    totalwins = totalwins+index # and add the total cards defined by the index to get the total number of cards at the end
    print(total)
    print(totalwins)


def adventofcode3(path):
    f = open(path).read().strip()
    lines = f.split('\n')
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])

    p1 = 0
    nums = defaultdict(list)
    for r in range(len(G)):
        gears = set() # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for c in range(len(G[r])+1):
            if c<C and G[r][c].isdigit():
                n = n*10+int(G[r][c])
                for rr in [-1,0,1]:
                    for cc in [-1,0,1]:
                        if 0<=r+rr<R and 0<=c+cc<C:
                            ch = G[r+rr][c+cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch=='*':
                                gears.add((r+rr, c+cc))
            elif n>0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()

    print(p1)
    p2 = 0
    for k,v in nums.items():
        if len(v)==2:
            p2 += v[0]*v[1]
    print(p2)

def adventofcode2(path):
    answer = 0
    index = 0
    p1 = 0
    p2 = 0
    #red,green,blue = 12,13,14
    f = open(path).read().strip()
    for line in f.split('\n'):
        index += 1
        valid = True
        line = line.split(':')[1]
        Value = defaultdict(int)
        for game in line.split(';'):
            for balls in game.split(','):
                n,color = balls.split()
                Value[color] = max(Value[color], int(n))
                if int(n) > {'red':12,'green':13,'blue':14}.get(color,0):
                    valid = False
        totalvalues = 1
        for v in Value.values():
            totalvalues *= v
        p2 += totalvalues
        if valid:
            p1 += index
    print(p1)
    print(p2)

def adventofcode1(path):
    D = open(path).read().strip()
    p1 = 0
    p2 = 0
    for line in D.split('\n'):
        p1_digits = []
        p2_digits = []
        for i,c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
            for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_digits.append(str(d+1))
        p1 += int(p1_digits[0]+p1_digits[-1])
        p2 += int(p2_digits[0]+p2_digits[-1])
    print(p1)
    print(p2)

def sum_first_last_digits(file_path):
    f = open(file_path).read().split()
    for line in f.split('\n'):
        digits=[]
        for i,c in enumerate(line):
            if c.isdigit():
                digits.appen(c)
        for d,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if line[i:].startswith(val):   
                digits.append(str(d+1))
        score = int(digits[0]+digits[-1])
        ans += score

adventofcode4('c:/temp/opdracht.txt')
#adventofcode4('c:/temp/example.txt')
#total_sum = sum_first_last_digits('c:/temp/opdracht.txt')