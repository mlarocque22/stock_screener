import requests
import time
import random
import screen_helper
import stock_screener

def ratio_update():
    
    file = open(r"ratios.txt",'r')
    file1 = open(r"ratios_update.txt",'w')
    
    for line in file:
        
        if 'Symbol' in line:
            
            this_line = line
            file1.write(this_line)
            continue
        
        this_line = line
        
        info = this_line.rsplit(',')
        
        ticker = str(info[0])
        
        temp = ''
        i=2
        while i<6:
            tempstr = info[i]
            tempstr.strip()
            if tempstr[0] == '[':
                tempstr = tempstr[1:]
            if tempstr[-1] == ']':
                tempstr = tempstr[:-1]
            temp += info[i] + ','
            i+=1
        temp = temp[:-2]
        temp = temp[2:]
        temp = temp.split(',')
        temp = [float(i) for i in temp]
        temp = [round(i,3) for i in temp]
        temp = str(temp)
        temp+= ','
        stock_dict = {}
        ratio,ratio2,ratio3,de,stock_dict[ticker] = stock_screener.screen(ticker) 
        arr = [ratio,ratio2,ratio3,de]
        arr = [round(i,3) for i in arr]
        arr = str(arr)
        this_line = info[0] + ', ' + info[1] + ', ' + temp + ' ' + arr + '\n'
        file1.write(this_line)
        print(this_line)
        rest()
        
    
    file.close()
    file1.close()
        


def rest():
    
    r = random.randint(5,35)
    
    r2 = random.randint(2,15)
    
    r= r/r2
    
    time.sleep(r)
    
ratio_update()