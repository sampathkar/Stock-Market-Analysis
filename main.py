import investpy as inv
import time
from datetime import date

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")


with open ("share_list.txt", "w") as o:
  o.write(f"Following Stocks meets the selection Criteria as at {d1} : \n\n")

with open ("early_signals.txt","w") as p:
  p.write(f"Following Stocks shows early signs of an uptrend as at {d1} :\n\n ")

# List of shares below. maintain separate lists to avoid disconnections from the server
all_shares_list = ['DIMO', 'MGT', 'MBSL', 'RGEM', 'RICH', 'SINI', 'ACME', 'BALA']

all_shares_list1 = ['GLAS', 'RCL', 'SIL', 'RHTL', 'LHL', 'WATA', 'YORK', 'ALLI', 'BBH', 'CTLD', 'CARS', 'CHLt', 'CTEA','DPL', 'GEST', 'ASPH', 'KGAL', 'KDL', 'LDEV', 'COCO', 'CSD', 'UML', 'CIND', 'CINS','CCS', 'HARI', 'HOPL', 'HUNA', 'KHL', 'LOLC', 'LITE', 'NTB', 'NHL', 'PALM', 'SHOTt', 'ABAN', 'CARG','CINV', 'SOY', 'EMER', 'RNUK', 'RENU', 'SLTL', 'SUN', 'PARQ', 'TRAN', 'CHL', 'DOCK', 'PHAR', 'EDEN','LAMB', 'TILE', 'MARA', 'SINS', 'TAJ', 'TAFL', 'BRWN', 'CFIN', 'CICt', 'COLO', 'DIPD', 'GHLL','ONAL', 'SHOT', 'BUKI', 'UAL', 'CTC', 'REEF', 'STAF', 'EBCR', 'HHL', 'HSIG', 'LVEN']

all_shares_list2 = ['ASIA', 'ASSO', 'BROW', 'DIAO', 'CEYL', 'CDBF', 'COMN','BERU', 'EXPO', 'HAYL', 'HUNT', 'HVAF', 'HYDP', 'IDL', 'JINS', 'LALU', 'LOLF', 'LWL', 'LGGL','MWEL', 'MSL', 'MULT', 'LOLD', 'NEH', 'ODEL', 'PANA', 'PEOP','RAIG', 'RFLL', 'RAFL', 'RHL', 'SANA', 'SIFI', 'SOCL', 'SOFT', 'AMBE', 'TEEJ','UNIO', 'UCHE', 'VALL', 'VALI', 'CITW', 'LANK', 'GOOD', 'AFSL', 'ALUM', 'ABLT', 'HPWR','CITH', 'ASHO', 'BANS', 'SLND', 'MHDL', 'SFL', 'CAPR']

all_shares_list3 =['CIT', 'SHAL', 'ARIC', 'SWAD', 'INDO', 'SIGH', 'PEIN', 'ORIT', 'COCOt', 'SFL_p', 'ANTK','LGGLt', 'RHLt', 'CDBFt', 'MALt', 'MELS', 'JETW', 'LVLE', 'HATT', 'MAHA', 'RENH', 'SMOT', 'SEYBt','SEMBt', 'SPEN', 'ATL', 'CONN', 'BFL', 'CHOT', 'DIAL', 'ECL', 'HEXP', 'LLUB','HASU', 'KCAB', 'CERA', 'LCEY', 'REG', 'SIRA', 'AUTO', 'APLA', 'ACAP', 'CIC', 'KHC', 'TYRE','NEST', 'SAMP', 'CTHR', 'CWM', 'JKL', 'SEYB', 'SEMB', 'ACL', 'ETWO', 'LFIN', 'SHAW', 'VLL','DFCC', 'LIOC', 'CARE', 'SELI', 'TESS', 'CHMX', 'HAYC', 'UNIS', 'ACCE', 'AGST', 'ASAS']

all_shares_list4 =['ABEO', 'BLUE', 'DIST', 'GUAR', 'LPRT', 'CFLB', 'HDFC', 'COMD', 'LHCL', 'BLUEt', 'AHUN', 'COMBt','PABC', 'MAL', 'CLND', 'AHPL', 'BOPL', 'COMB', 'WAPO', 'KVAL', 'NDB', 'TSML', 'UDPL', 'SFTL','BREW','HAPU', 'MULL', 'OSEA', 'PEG', 'PMB', 'RPBH', 'TKYOt', 'AMSL', 'ASIR', 'HNBt', 'SERC', 'SIGV','TPL', 'LION', 'TKYO', 'AGAL', 'CABO', 'GRAN', 'CFVF', 'LMF', 'NAMU', 'REXP', 'TANG', 'VPEL','BOGA', 'KAHA', 'MADU', 'MRH', 'MASK', 'EAST', 'ELPL', 'HNB', 'JKH', 'KFP', 'KOTA', 'CSF']

my_portfolio = []


# End of the list of shares


# below is the function with the stock selection criteria.
def share_criteria(share_list_no):
  for x in share_list_no:
    time.sleep(2)
    try:
        mov_avg_data = inv.moving_averages(name=x, country='Sri Lanka', product_type='stock', interval='daily')
        
        try:
            mov10 = mov_avg_data.iloc[1, 1]
            mov20 = mov_avg_data.iloc[2, 1]
            mov50 = mov_avg_data.iloc[3, 1]
            mov100 = mov_avg_data.iloc[4, 1]
            mov200 = mov_avg_data.iloc[5, 1]
            
            ema10 = mov_avg_data.iloc[1, 3]
            ema20 = mov_avg_data.iloc[2, 3]
            ema50 = mov_avg_data.iloc[3, 3]
          
            last_price = inv.get_stock_recent_data(stock=x, country='Sri Lanka', as_json=False, order="ascending", interval="Daily").Close.iat[-1] #getting only the closing price.last row close column
            
            time.sleep(2)
          
            if  ema10 > ema20 and ema10 <= (ema20*1.3) and ema20 <= (ema50*1.6):
              with open ("early_signals.txt","a") as p:
                      p.write(f"{x} \n ✅ Closing Price is {last_price}\n✅10ema= {ema10}\n✅20ema= {ema20}\n✅50ema= {ema50}\n\n\n ")
                    
            
    
            elif last_price >= mov10 >= mov20 >= mov50 >= mov100 and last_price >= mov200:#condition 1
              tech_ind_data = inv.technical_indicators(name=x, country='Sri Lanka', product_type='stock', interval='daily')
              rsi=tech_ind_data.iloc[0, 1] #getting only the rsi indicator result
              
              time.sleep(2)
              
              
              if rsi >= 65:#condition 2
                stock_info = inv.get_stock_information(stock=x, country='Sri Lanka', as_json=False)
                fiftytwo_week_range = stock_info.iloc[0, 5].rsplit('-', 1) #getting the high and low as a same string from the dataframe and convert them to a list with high value and low value using rsplit.
                fiftytwo_high = fiftytwo_week_range[1] #getting the 2nd value of the list 
                fiftytwo_low = fiftytwo_week_range[0] #getting the 1st value of the list
            
                
                
                if (float(fiftytwo_high)*.75)<= last_price and (float(fiftytwo_low)*1.3)<=last_price:#condition 3
                  
                  price_range = stock_info.iloc[0, 2]
                  pe_ratio = stock_info.iloc[0, 11]
                  mov5 = mov_avg_data.iloc[0, 1]
                  mov10_vs_closing_price =int((last_price-mov10)/last_price*100)
                  mov5_vs_closing_price =int((last_price-mov5)/last_price*100)
                  
                  with open ("share_list.txt", "a") as o:
                    o.write(f"{x} : \n✅ Price Range is {price_range} \n✅ Closing Price is {last_price} \n✅ 20 day mov avg : {mov20} and 50 day mov avg : {mov50}\n✅ 52 Week Range :{fiftytwo_week_range}\n✅ Closing price is {mov10_vs_closing_price} % higher/lower than the 10 day mov avg \n✅ Closing price is {mov5_vs_closing_price} % higher/lower than the 5 day mov avg \n✅ P/E Ratio is {pe_ratio}   \n\n")
                  
                  volume = stock_info.iloc[0, 7]
                  avg_volume = stock_info.iloc[0, 10]
                                   
                  
                  if rsi >= 70 and tech_ind_data.iloc[1, 2] == tech_ind_data.iloc[3, 2] == tech_ind_data.iloc[9, 2] == tech_ind_data.iloc[1, 2] == "buy" and last_price >= ema10 >= ema20 >= ema50 and volume / avg_volume >= 2:
                    with open ("share_list.txt", "a") as o:
                      o.write(f"🔥🔥 Technical Indicators Say 'BUY' {x} 🔥🔥\n\n\n")
                    
        except Exception as e: #getting the error message as e
            with open ("share_list.txt", "a") as o:
              o.write(f"Error in the stock {x}.\nError message : {e}\n\n")

      
          
    except Exception as f: #getting the error message as f
      with open ("share_list.txt", "a") as o:
        o.write(f"Error in the stock {x}.\nError message : {f}\n\n")
# end of the function.

# calling the function for each table with few seconds of sleep after running the code.
# this is to avoid disconnection from the server




def my_portfolio(my_portfolio):
  for x in my_portfolio:
    time.sleep(2)
    try:
      mov_avg_data = inv.moving_averages(name=x, country='Sri Lanka', product_type='stock', interval='daily')
      try:
        mov10 = mov_avg_data.iloc[1, 1]
        mov20 = mov_avg_data.iloc[2, 1]
        mov50 = mov_avg_data.iloc[3, 1]
        
        ema10 = mov_avg_data.iloc[1, 3]
        ema20 = mov_avg_data.iloc[2, 3]
        ema50 = mov_avg_data.iloc[3, 3]

        if #sell signals for the portfolio


    except Exception as g: #getting the error message as g
      print("error")












share_criteria(all_shares_list)

share_criteria(all_shares_list1)
print ("all_shares_list1 is checked")
time.sleep(150)

share_criteria(all_shares_list2)
print ("all_shares_list2 is checked")
time.sleep(200)

share_criteria(all_shares_list3)
print ("all_shares_list3 is checked")
time.sleep(100)

share_criteria(all_shares_list4)
print("Process completed")
o.close()

