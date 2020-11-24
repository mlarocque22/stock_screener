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
        
        if 'n' in info[1]:
            
            file1.write(line)            
            continue
        
        
        
        #print(info)
        
        price = screen_helper.get_price(ticker)
        
        #print(price)
        
        temp = ''
        
        i=0
        for entry in info:
            if i<4:
                entry+= ", "
                temp+=entry
            i+=1
                
        temp+=str(price)+', '
        
        percentage = ((price - float(info[3])) / float(info[3])) *100
        
        str_per = str(round(percentage,2))
        
        temp+= str_per+'%, '
                
        temp+='\n'
        
        print(temp)
        
        file1.write(temp)
        
        rest()

    file.close()
    file1.close()  
    
    file = open(r"portfolio_update.txt",'r')
    file1 = open(r"portfolio_update_totals.txt", 'w')
    total_purch = 0
    total_val = 0
    for line in file:
        
        if 'Symbol' in line:
            
            this_line = line
            file1.write(this_line)
            continue
        
        this_line = line
        
        info = this_line.rsplit(',')
        
        ticker = str(info[0])
        shares = info[2]
        purval = info[3]
        curval = info[4]
        purmount = round(float(purval) * float(shares),2)
        curmount = round(float(curval) * float(shares),2)
        if 'n' in info[1]:
            
            this_temp = round(float(curmount) - float(purmount),2)
            total_val += this_temp
        else:
            total_purch += float(purmount)
            total_val += float(curmount)
        profit = round(curmount - purmount,2)
        str_profit = str(profit)
        if 'n' in info[1]:
            temp = this_line.strip('\n') +' ' + str(purmount) + ', ' + str(curmount) +', ' + str(profit) + '\n'
        else:
            temp = this_line.strip('\n') + str(purmount) + ', ' + str(curmount) +', ' + str(profit) + '\n'
        file1.write(temp)
    
    total_purch = round(total_purch,2)
    total_val = round(total_val,2)
    fin_line = 'Total Purchase Value = ' + str(total_purch) +'\n'
    file1.write(fin_line)
    fin_line = 'Total Current Value = ' + str(total_val) +'\n'
    file1.write(fin_line)
    total_profit = round((total_val - total_purch),2)
    fin_line = 'Total Profit = ' + str(total_profit) + '\n'
    file1.write(fin_line)
    total_perc = round((((total_val - total_purch)/total_purch)*100),2)
    fin_line = 'Percentage Change = ' + str(total_perc)+'%'
    file1.write(fin_line)
    print(total_purch, total_val, total_perc)
        
    
    
    
    
    
    file1.close()
    
def rest():
    
    r = random.randint(5,35)
    
    r2 = random.randint(2,15)
    
    r= r/r2
    
    time.sleep(r)
        
portfolio_update()
