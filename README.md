# stock_screener
Screens every stock on the NYSE to find any that are considered undervalued.

Disclaimer:
  I retain all rights to this source code and no one may reproduce, distribute, or create derivative works from my work.
  
  This is solely for educational and informative purposes. DO NOT MAKE ANY TRADES solely based off this program.


All that is required to run this program is to have Requests installed and that all the files in this folder are included in the same directory when running it. It then
reads a file that has the tickers for every stock in the New York Stock Exchange on it. (I have included this text file, but since IPO's happen frequently you should 
use an updated version for the most accurate results) It then uses requests to get the publically available information we will need for a calculations. As of the early 
11/2020 there are 4 ratios used. 3 are calculated and explained below, the fourth one is just Debt/Equity. It then screens the stocks based on these ratios and creates
multiple text files depending on which of the various screens it passed.

under_valued_all.txt - means that it passed all three screens as well as the D/E screen             
under_valued_best.txt  - means that it passed the first two screens which are based on future expected values as well as the D/E screen.  
under_valued_both.txt - means that it passed the first two screens but not necessarily the D/E screen.      
under_valued_low_debt.txt  - means it passed the first screen as well as the D/E screen.         
under_valued.txt  - means it passed just the first screen but not necessarily the D/E screen.       
under_valued_eps.txt - means it passed the second screen but not neccesarily the D/E screen.      
under_valued_eps_debt - means that it passed the second screen and the D/E screen.

As of 11/19/2020 which is around 2 months after the first version of this code was created. The stocks that passed the first three screens and D/E get hooked up to a 
paper trading account and then $4,000 worth of shares are "bought". Currently the paper trading portfolio is up 20%. For reference, the DOW is up  8% and the S&P 500 is up 7.48%. However, since i run the program twice a week and then buy more shares based off of those results, the newer stocks that have been bought, lower that percentage. As time goes on and new purchases make up less of the overall portfolio it should give a better estimate of its performance. I will be updating this section somewhat frequently.

As of this early 10/2020, I have added a third screen based on past performance, Any new stocks that are purchased must pass this additional screen but previous stocks that do not pass it are not sold. The screen for past performance is primarily for my long term goal of then taking these
stocks that passed through all the screens and then finding undervalued long call options with at least 6+ months of time. In addition, I plan on adding another
screen for past performance using different metrics, likely a shorter time period since I want to use this for options.

For the first 3 ratios. Any value above 1 is considered undervalued. The higher the value the more undervalued the screen believes it is. 
The first two ratios use analyst expectations of the future for its calculations. The third ratio uses past performance for its calculations. 
That way the screen is not solely relying on analyst expectations for the stock. The final ratio is just debt/equity. This just screens out stocks that
seem undervalued but have massive amounts of debt. 

The first ratio. Called "Ratio" or "Ratio1" , Uses the PEG 5 year value, return on equity and forward P/E. 

The second ratio. Called "Ratio2". Uses analyst expectations for eps growth over the next year, return on equity and forward P/E. 

The third ratio called Ratio3. Uses past year EPS and current year EPS to calculate growth past growth, Return on Equity and Trailing PE. 

The Last ratio. Called D/E is just the debt to equity %. so a value of 50 = 50%. It is screened so that any value under 100 is considered good. 

Once a stock no longer passes any of these ratios (D/E excluded) I initiated a sell in the paper trading. So far I have sold 5 stocks

EV - Sold 103 Shares Of EV at $61.75 (6,340.26 -4,015.36 = +2,324.90 ) +59.14%

CNC - Sold 69 shares at $62.60 (4,319.40 - 3999.24 = 320.16) + 8.01%

LHX - Sold 22 shares at $193.80 (4,263.60 - 3.915.78 = 347.82) + 8.88%

PFE - Sold 110 shares at $36.76 (4,043.60 - 4,007.30 = 36.3) + 0.91%

SQM - Sold 125 shares at $45.03 (5,628.75 - 4,007.50 = 1,621.25) + 40.46%

Total Profit From Sold Stocks = $4,650.43



To see the current portfolio list which includes purchase price, current price, percentages, shares, and the total values at the bottom. Go to the portfolio_update_totals.txt file

To see the list of ratios both original and current go to ratios_update.txt
