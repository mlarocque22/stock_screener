import requests
import time
import random
import screen_helper
import stock_screener


def portfolio_update():
    
    file = open(r"portfolio.txt",'r')
    file1 = open(r"portfolio_update.txt",'w')
    
    for line in file:
        
        #dont need the first line for our purposes
        if 'Symbol' in line:
            
            this_line = line
            file1.write(this_line)
            continue
        
        this_line = line
        
        info = this_line.rsplit(',')
        
        ticker = str(info[0])
        
        if info[1] == 'n':
            
            file1.write(line)            
            continue
        
        
        
        #print(info)
        
        price = screen_helper.get_price(ticker)
        
        #print(price)
        
        temp = ''
        
        i=0
        for entry in info:
            if i<3:
                entry+= ", "
                temp+=entry
            i+=1
                
        temp+=str(price)+', '
        
        percentage = ((price - float(info[2])) / float(info[2])) *100
        
        str_per = str(round(percentage,2))
        
        temp+= str_per+'% '
                
        temp+='\n'
        
        print(temp)
        
        file1.write(temp)
        
        rest()

        
        
 
    
    
    
    
    
    file.close()
    file1.close()
    
def rest():
    
    r = random.randint(5,35)
    
    r2 = random.randint(2,15)
    
    r= r/r2
    
    time.sleep(r)
        
portfolio_update()
