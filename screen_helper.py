#this is the helper file where a lot of the functions are stored

#every function in here works the same way. 
#it is fed a string with the html text files for an individual stock
#it then searches for the first instance of the key word we are looking for
#then makes a substring out of it. 
#then looks for an html code that is exlusive to that specific number we are looking for 
#and that signifies that number is the next value in the html code
#then we keep going until we reach a '>' and a '<' signifying that the value we want is in there
#then converts to float and returns it.
#the last two functions involving EPS have a few extra steps since we need to caluclate the expected and past eps growth during the course of a year
#and the html is formatted differently which requires a few extra steps


#I have little to no expierence with html, there is probably be a better way to accomplish this
#but this method works and will continue to work until there is a large change in the format of the yahoo finance page


#takes in the string
def PEG(str_x):
    
    #finds first instance of the term
    find = str_x.find('PEG Ratio')
    
    #makes a substring
    subx = str_x[find:find+8000]
    
    #looks for a unique identifyer in the code
    val = subx.find('$hoverBgColor)" data')
    
    #makes a much smaller substring
    sub = subx[val:val+70]
    
    #finds the indexes for the value we are looking for
    begin = sub.find('>')
    
    begin+=1
    
    end = sub.find('<')
    
    #converts and returns
    str_PEG = sub[begin:end]
    
    PEG = float(str_PEG)
    
    return PEG

#the rest of these work the exact same until current_eps_growth()
def ROE(str_x):
    
    find1 = str_x.find('Return on Equity')

    subx = str_x[find1+500:]
    
    find=subx.find('Return on Equity')
    
    subxx = subx[find:find+8000]

    val = subxx.find('%<')
    
    sub = subxx[val-5:val+5]
    
    begin = sub.find('>')
    
    begin+=1
    
    end = sub.find('<')
    
    str_ROE = sub[begin:end]
    
    str_ROE = str_ROE[:-1]
    
    ROE = float(str_ROE)
    
    return ROE

def Trail_PE(str_x):
    
    find = str_x.find('Trailing P/E')

    subx = str_x[find:find+8000]

    val = subx.find('($hoverBgColor)')
    
    sub = subx[val:val+70]
    
    begin = sub.find('>')
    
    begin+=1
    
    end = sub.find('<')
    
    str_PE = sub[begin:end]
    
    PE = float(str_PE)
    
    return PE

def Forw_PE(str_x):
    
    find = str_x.find('Forward P/E')

    subx = str_x[find:find+8000]

    val = subx.find('($hoverBgColor)')
    
    sub = subx[val:val+70]
    
    begin = sub.find('>')
    
    begin+=1
    
    end = sub.find('<')
    
    str_PE = sub[begin:end]
    
    PE = float(str_PE)
    
    return PE

def DE(str_x):
    
    find = str_x.find('Total Debt/Equity')

    subx = str_x[find:find+8000]

    val = subx.find('Fw(500) Ta(end) Pstart(10px) Miw(60px)')
    
    sub= subx[val:val+70]
    
    begin = sub.find('>')
    
    begin+=1
    
    end = sub.find('<')
    
    str_DE = sub[begin:end]
    
    DE = float(str_DE)
    
    return DE


#this is still the exact same principle just uses a different page on yahoo finance and as such is formated very differently
#still takes in a string with the html code
def EPS_GROWTH(str_x):
    
    #searches for the instance of the key work we are looking for
    find = str_x.find('Avg. Estimate')

    #makes a substring
    subx = str_x[find:find+8000]

    #finds the unique identifier
    val = subx.find('dc($seperatorColor)')
    
    sub = subx[:val] 
    
    #this is where it gets different because the value we are looking for is now part of a 2 dimensional table
    #principle is the same we are just iterating through the values we dont need
    val2 = subx.find('</span>')
    
    subs = sub[val2+10:]
    
    val3 = subs.find('</span>')
    
    subss = subs[val3+10:]
    
    val4 = subss.find('</span>')
    
    subxx = subss[val4+10:]
    
    val5 = subxx.find('</span>')
    
    sub1 = subxx[val5-10:]
    
    #grabs the value we do not and converts it

    begin = sub1.find('>')
    
    begin+=1
    
    end = sub1.find('<')
    
    str_Current_EPS = sub1[begin:end]
    

    Current_EPS = float(str_Current_EPS)
    
    #does the same thing but for the future analyst eps value

    suby = subxx[val5++10:]

    val6 = suby.find('</span>')
    
    sub2 = suby[val6-10:]

    begin = sub2.find('>')
    
    begin+=1
    
    end = sub2.find('<')
    
    str_Next_EPS = sub2[begin:end]

    Next_EPS = float(str_Next_EPS)

    #just calculates the expected eps growth based on the two eps values we have
    EPS_Growth = ( (Next_EPS - Current_EPS) / Current_EPS) * 100
    
    return EPS_Growth

#this works the same way as the previous function
def PAST_EPS_GROWTH(str_x):
    
    #x = requests.get(path)
    
    #str_x = x.text
    
    find = str_x.find('Year Ago EPS')

    subx = str_x[find:find+8000]
    
    

    val = subx.find('dc($seperatorColor)')

    sub = subx[:val] 
    
    val2 = subx.find('</span>')
    
    subs = sub[val2+10:]
    
    val3 = subs.find('</span>')
    
    subss = subs[val3+10:]
    
    val4 = subss.find('</span>')
    
    subxx = subss[val4+10:]
    
    val5 = subxx.find('</span>')
    
    sub1 = subxx[val5-10:]

    begin = sub1.find('>')
    
    begin+=1
    
    end = sub1.find('<')
    
    str_Year_Ago_EPS = sub1[begin:end]
    
    Year_Ago_EPS = float(str_Year_Ago_EPS)

    find = str_x.find('Avg. Estimate')

    subx = str_x[find:find+8000]

    val = subx.find('dc($seperatorColor)')
    
    sub = subx[:val] 
    
    val2 = subx.find('</span>')
    
    subs = sub[val2+10:]
    
    val3 = subs.find('</span>')
    
    subss = subs[val3+10:]
    
    val4 = subss.find('</span>')
    
    subxx = subss[val4+10:]
    
    val5 = subxx.find('</span>')
    
    sub1 = subxx[val5-10:]

    begin = sub1.find('>')
    
    begin+=1
    
    end = sub1.find('<')
    
    str_Current_EPS = sub1[begin:end]
    
    

    Current_EPS = float(str_Current_EPS)
    

    EPS_Growth = ( (Current_EPS - Year_Ago_EPS) / Year_Ago_EPS) * 100
    
    
    
    return EPS_Growth

