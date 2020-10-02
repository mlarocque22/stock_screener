import requests
import time
import random
import screen_helper


#read the readme.txt first for explanations on the algorithms and calculations used in this program

#this is the main function
def stock_screener():
    
    
    # "NYSE.txt" is just a file containing a list of every stock in the new york stock exchange
    file = open(r"NYSE.txt",'r')
    
    our_list = []
    
    print('Ticker, Ratio1, Ratio2, Ratio3, Debt/Equity')
    
    for line in file:
        
        #dont need the first line for our purposes
        if 'Symbol' in line:
            
            continue
        
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        #gets a list of stock tickers
        our_list.append(ticker)    
    
    #creates a bunch of lists that we will use to generate the text files
    under_valued_low_debt = []
    
    under_valued = []
    
    under_valued_best = []
    
    under_valued_eps = []
    
    under_valued_eps_low_debt = []
    
    under_valued_both = []
    
    under_valued_all = []
    
    i=0
    
    #dictionary of classes that hold the different values for each stock
    #as of 10/2020 this is largely unnecessary but it might become handy for future updates
    stock_dict = {}
    
    for ticker in our_list:
        
        if '-' in ticker:
            
            i+=1
            
            continue
        
        #gets the different ratios we will need. 
        #full explanations in the readme
        ratio,ratio2,ratio3,de,stock_dict[ticker] = screen(ticker)   
        
        #uses the ratios and appends them to the appropriate list
        if ratio>1 and de<100 and de != -1:
            
            under_valued_low_debt.append((ticker,ratio,de))
            
        if ratio>1:
            
            under_valued.append((ticker,ratio))
            
        if ratio>1 and ratio2>1 and de<100 and de!= -1:
            
            under_valued_best.append((ticker,ratio,ratio2,ratio3,de))
            
        if ratio2>1:
            
            under_valued_eps.append((ticker,ratio2))
            
        if ratio2>1 and de<100 and de!=-1:
            
            under_valued_eps_low_debt.append((ticker,ratio2,de))
            
        if ratio2>1 and ratio>1:
            
            under_valued_both.append((ticker,ratio,ratio2))
            
        if ratio>1 and ratio2>1 and ratio3>1 and de<100 and de !=-1:
            
            under_valued_all.append((ticker,ratio,ratio2,ratio3,de))
            
        print(ticker,ratio,ratio2,ratio3,de)
        
        
        #takes a random amount of seconds between 5 and 35 and divides it by a random amount of seconds between 2/15
        #since I am using requests i added this part in two prevent problems with using requests on Yahoo.finance.com
        r = random.randint(5,35)
        
        r2 = random.randint(2,15)
        
        r= r/r2
        
        time.sleep(r)
        
        i+=1
        
        #more sleep times to prevent problems
        if i%20 == 0 and i%100 !=0:
            
            r = random.randint(30,40)
            
            time.sleep(r)
            
        if i%100 == 0:
            
            r = random.randint(10,20)
            
            r=r*6
            
            time.sleep(r)
    
    #creates a bunch of files from those lists we made earlier writes to them and then closes them
            
    file1 = open(r"under_valued_low_debt.txt",'w')
    
    file2 = open(r"under_valued.txt",'w')
    
    filebest = open(r"under_valued_best.txt",'w')
    
    fileeps = open(r"under_valued_eps.txt",'w')
    
    fileepsdebt = open(r"under_valued_eps_debt.txt",'w')
    
    fileboth = open(r"under_valued_both.txt",'w')
    
    fileall = open(r"under_valued_all.txt",'w')
    
    file1.write('Ticker, Ratio, Debt/Equity')
    
    file2. write('Ticker, Ratio')
    
    filebest.write('Ticker, Ratio, Ratio2, Ratio3, Debt/Equity')
    
    fileeps.write('Ticker, Ratio2')
    
    fileepsdebt.write('Ticker, Ratio2, Debt/Equity')
    
    fileboth.write('Ticker, Ratio, Ratio2')
    
    fileall.write('Ticker, Ratio1, Ratio2, Ratio3, Debt/Equity')
    
    for line in under_valued_low_debt:
        
        file1.write(str(line))
        
    for line in under_valued:
        
        file2.write(str(line))
        
    for line in under_valued_best:
        
        filebest.write(str(line))
        
    for line in under_valued_eps:
        
        fileeps.write(str(line))
        
    for line in under_valued_eps_low_debt:
        
        fileepsdebt.write(str(line))
        
    for line in under_valued_both:
        
        fileboth.write(str(line))
        
    for line in under_valued_all:
        
        fileall.write(str(line))
        
    file1.close()
    
    file.close()
    
    file2.close()
    
    filebest.close()
    
    fileeps.close()
    
    fileepsdebt.close()
    
    fileboth.close()


#this is where it uses the requests to finance.yahoo.com in order to get the various financial details we will need
#I used try and excepts because often times especially with lesser known stocks, some of these values may not exist as
#there are not enough analyst for that particular stock in order to determine them
def screen(ticker):
    
    path = 'https://finance.yahoo.com/quote/' + ticker + '/key-statistics?p=' + ticker
    
    x = requests.get(path)
    
    str_x = x.text
  
    #this is where we get all the publically available data that we will need for our calculations
    try:
        
        peg = screen_helper.PEG(str_x)
        
    except:
        
        peg=-1
        
    try:
        
        roe = screen_helper.ROE(str_x)
        
    except:
        
        roe = -1
        
    try:
        
        trail_pe = screen_helper.Trail_PE(str_x)
        
    except:
        
        trail_pe = -1
        
    try:
        
        forw_pe = screen_helper.Forw_PE(str_x)
        
    except:
        
        forw_pe = -1
        
    try:
        
        de = screen_helper.DE(str_x)
        
    except:
        
        de = -1
        
    #sleep once again since we have to do a new request to get this data
    r = random.randint(5,35)
    
    r2 = random.randint(2,15)
    
    r= r/r2
    
    time.sleep(r)
    
    path2 = 'https://finance.yahoo.com/quote/' + ticker + '/analysis?p=' + ticker 
    
    y = requests.get(path2)
    
    str_y = y.text
    
    try:
        
        eps_growth = screen_helper.EPS_GROWTH(str_y)
        
    except:
        
        eps_growth = -1
        
    try:
        
        
        past_eps_growth = screen_helper.PAST_EPS_GROWTH(str_y)
    
    except:
        
        past_eps_growth = -1
        
    #this is where we create the class for the stock which does the calculations for us and holds the data
        
    this_stock = Stock(peg, roe, trail_pe,forw_pe,de, eps_growth,past_eps_growth,ticker)
    
    ratio = this_stock.RATIO1()
    
    ratio2 = this_stock.RATIO2()
    
    ratio3 = this_stock.RATIO3()
    
    return ratio,ratio2,ratio3,de,this_stock



#The class that does the calculations for us
#all these calculations are explained in the read me file
#the code itself is extremely straight forward so i will not comment on it
class Stock:
    
    def __init__(self, peg, roe, trail_pe,forw_pe,de, eps_growth,past_eps_growth,ticker):
        
        self.peg = peg
        
        self.roe = roe
        
        self.trail_pe = trail_pe
        
        self.forw_pe = forw_pe
        
        self.de = de
        
        self.eps_growth=eps_growth
        
        self.past_eps_growth = past_eps_growth
        
        self.ticker = ticker
    
    def RATIO1(self):
        
        if self.peg!= -1 and self.roe!= -1 and self.forw_pe != -1:
        
            ratio = (1/self.peg+self.roe/self.forw_pe)/2
        
        else:
            
            ratio = -1
        
        return ratio
    
    def RATIO2(self):
        
        if self.eps_growth!= -1 and self.roe != -1 and self.forw_pe != -1:
        
           ratio2 = ((self.eps_growth + self.roe)/(2*self.forw_pe))
          
        else:
            
            ratio2 = -1
        
        return ratio2

    def RATIO3(self):
        
        if self.past_eps_growth!= -1 and self.roe != -1 and self.trail_pe != -1:
        
            ratio3 = ((self.past_eps_growth + self.roe)/(2*self.trail_pe))
    
        else:
        
            ratio3 = -1
        
        return ratio3
    
    def values(self):
        
        ratio1 = self.RATIO1()
        
        ratio2 = self.RATIO2()
        
        ratio3 = self.RATIO3()
        
        return [('peg',self.peg),('roe',self.roe),('trail_pe',self.trail_pe),
                
                ('forw_pe',self.forw_pe),('de',self.de),('eps_growth',self.eps_growth),
                
                ('past_eps_growth',self.past_eps_growth),('ticker',self.ticker),
                
                ('ratio1',ratio1),('ratio2',ratio2),('ratio3',ratio3)]

stock_screener()