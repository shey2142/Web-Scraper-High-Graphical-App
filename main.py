from customtkinter import *
import customtkinter
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv



# Login Page Function

def main():
    global root
    global entry1
    global entry2
    global message
    
    root = customtkinter.CTk()
    message = StringVar()
    root.title("Login")
    root.geometry(f"{359}x{379}")
    root.bind('<Return>', enter)
    
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx= 20, fill='both', expand=True)
    label_1 = CTkLabel(master = frame, text = "Login System",font= ('Arial',17,'bold'))
    label_1.pack(pady=20, padx=10)

    entry1 = customtkinter.CTkEntry(master= frame, placeholder_text = 'Username',width=150, height=30,corner_radius=15)
    entry1.pack(padx=10, pady=12)

    entry2 = customtkinter.CTkEntry(master= frame, placeholder_text = 'Password',width=150, height=30,show='*',corner_radius=15)
    entry2.pack(padx=10, pady=12)

    global button
    button = customtkinter.CTkButton(master = frame, text = 'Login', command = login,width=150, height=33 ,corner_radius=15)
    button.pack(padx = 10, pady = 12)

    Label_2 = customtkinter.CTkLabel(frame, text="",textvariable=message, text_color = '#ff3838',corner_radius=1)
    Label_2.pack(pady = 10, padx = 10)
    checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember Me" )
    checkbox.pack(pady= 0, padx = 10)


# login with password and username 

def login():
    username = StringVar()
    password = StringVar()
    
    username = entry1.get()
    password = entry2.get()

    if username == 'admin' and password == '1234':
        message.set('Login Success')
        root.destroy()
        main_app()
        
        
    elif username == '' or password == '':
        message.set('Field Empty')
    else:
        message.set('incurrect username or password')
        entry1.delete(0, customtkinter.END)
        entry2.delete(0 , customtkinter.END)
    
# define enter button in login page for login
def enter(event):
    login()



# main app page function
def main_app():
    global root_1
    global search_entry
    
    #global first_entry
    #global second_entry

    root_1 = customtkinter.CTk()
    root_1.geometry(f"{575}x{270}")
    root_1.resizable(False,False)
    root_1.title("Data Scraper")

    # coin search entry and button

    search_entry = customtkinter.CTkEntry(master= root_1, width=260, height=30,corner_radius=10 ,placeholder_text='Coin Name')
    search_entry.place(x= 170, y = 20)
   
    search_button = customtkinter.CTkButton(master= root_1,text= "Search",width=130, height=30,corner_radius=10,command=entry_token)
    search_button.place(x = 440, y = 20)

    # file type option menu
    global variable
    variable = StringVar()
    variable.set('Pick Format')
    format_file = customtkinter.CTkOptionMenu(master= root_1, values=['Excel', 'CSV'],variable=variable,)
    format_file.place(x = 15, y = 20)


    
    # start date entry
    global y_1
    start_label = customtkinter.CTkLabel(master= root_1, text= 'Start :',font=('Arial', 12))
    start_label.place(x = 12, y = 96)

    y_1 = customtkinter.CTkEntry(master= root_1, width= 43, height= 25,placeholder_text='YYYY',font=('Arial',12))
    y_1.place(x = 55, y = 100 )
    
    global m_1 , d_1

    m_1 = customtkinter.CTkEntry(master= root_1, width= 30, height= 25,placeholder_text='MM',font=('Arial',12))
    m_1.place(x = 100, y = 100 )



    d_1 = customtkinter.CTkEntry(master= root_1, width= 30, height= 25,placeholder_text='DD',font=('Arial',12))
    d_1.place(x = 132, y = 100 )


    global message_1
    message_1 = StringVar()
    global message_2
    message_2 = StringVar()
    global message_3
    message_3 = StringVar()

    entry_error = customtkinter.CTkLabel(master= root_1, text= "",textvariable=message_1,text_color = '#ff3838',corner_radius=1)
    entry_error.place(x = 240, y = 55)
    # End date entry 
    global y_2
    y_2 = customtkinter.CTkEntry(master= root_1, width= 43, height= 25,placeholder_text='YYYY',font=('Arial',12))
    y_2.place(x = 55, y = 150 )
    
    global m_2 , d_2

    m_2 = customtkinter.CTkEntry(master= root_1, width= 30, height= 25,placeholder_text='MM',font=('Arial',12))
    m_2.place(x = 100, y = 150 )



    d_2 = customtkinter.CTkEntry(master= root_1, width= 30, height= 25,placeholder_text='DD',font=('Arial',12))
    d_2.place(x = 132, y = 150 )

    end_label = customtkinter.CTkLabel(master= root_1, text= 'End :',font=('Arial', 12))
    end_label.place(x = 12, y = 146)


    date_error = customtkinter.CTkLabel(master= root_1, text= "",textvariable=message_2,text_color = '#ff3838',corner_radius=1)
    date_error.place(x = 32, y = 50)

    # checkbox define 
    # close price
    global close_price
    close_price = IntVar()
    close_price_check = customtkinter.CTkCheckBox(master= root_1, text='Close Price',variable=close_price)
    close_price_check.place(x = 230, y = 100)
    # open price
    global open_price
    open_price = IntVar()
    open_price_check = customtkinter.CTkCheckBox(master= root_1, text='Open Price',variable=open_price)
    open_price_check.place(x = 230, y = 150)
    # marketcap
    global marketcap_value
    marketcap_value = IntVar()
    marketcap_check = customtkinter.CTkCheckBox(master= root_1, text='Market cap',variable=marketcap_value)
    marketcap_check.place(x = 370, y = 100)
    # valume
    global valume_cap
    valume_cap = IntVar()
    valume_check = customtkinter.CTkCheckBox(master= root_1, text='Valume',variable=valume_cap)
    valume_check.place(x = 370 , y= 150)

    # successful generate message
    end_label = customtkinter.CTkLabel(master= root_1, text= 'error',font=('Arial', 12),textvariable=message_3,text_color = '#ff3838')
    end_label.place(x = 230, y = 189)



    # generate button 
    generate_button = customtkinter.CTkButton(master= root_1, text= "Generate",width=470,height=30,command=generate)
    generate_button.place(x = 50, y = 220)

    root_1.mainloop()

# define empty entry error
def entry_token():
    global client_search
    client_search = search_entry.get()

    if search_entry.get() == '':
        raise message_1.set('field is empty')
      
    # send request to get data from coin gecko
    # and define response errors
    url = "https://www.coingecko.com/en/coins/{}".format(str(client_search))
    try:
        res = requests.get(url)
        if str(res) == '<Response [200]>':
            message_1.set('coin found')
        else:
            message_1.set('coin not found')
            search_entry.delete(0 , customtkinter.END)
    except:
        None

# define generate function fot genereate button
            
def generate():
    if search_entry.get() == '':
        raise message_1.set('field is empty')
        

   
    # https://www.coingecko.com/en/coins/bitcoin/historical_data?start_date=2023-02-03&end_date=2023-03-06#panel

    first_year = IntVar()
    first_year = y_1.get()
    if len(first_year) > 4:
        y_1.delete(4, END)

    first_month = IntVar()
    first_month = m_1.get()
    if len(first_month) > 2:
        m_1.delete(2, END)
    
    first_day = IntVar()
    first_day = d_1.get()
    if len(first_day) > 2:
        d_1.delete(2, END)

    end_year = IntVar()
    end_year = y_2.get()
    if len(end_year) > 4:
        y_2.delete(2, END)

    end_month = IntVar()
    end_month = m_2.get()
    if len(end_month) > 2:
        m_2.delete(2, END)

    end_day = IntVar()
    end_day = d_2.get()
    if len(end_day) > 2:
        d_2.delete(2, END)

    
    global first_date, second_date
    first_date = StringVar()
    second_date = StringVar()

    first_date = str(first_year) + '-' + str(first_month) + '-'+ str(first_day)
    second_date = str(end_year) + '-' + str(end_month) + '-'+ str(end_day)

    url_date = 'https://www.coingecko.com/en/coins/{}/historical_data?page=7&end_date={}&start_date={}'.format(client_search, first_date, second_date)
    
    try:
        res = requests.get(url_date)
         
        if res.status_code == 200:
            print('res : 200')
            scraper()
            message_2.set("Date is ok")
        else:
            raise message_2.set('date format Error') 
    
    except:
        # clear date entry if it's not currect
        message_2.set('Please Try again!')
        y_1.delete(0 , customtkinter.END)
        m_1.delete(0 , customtkinter.END)
        d_1.delete(0 , customtkinter.END)
        y_2.delete(0 , customtkinter.END)
        m_2.delete(0 , customtkinter.END)
        d_2.delete(0 , customtkinter.END)


def scraper():
    print('1')
    global date_list
    global close
    global open
    global volume_list
    global market

    date_list = []
    close = []
    open = []
    volume_list = []
    market = []

    url_page = f'https://www.coingecko.com/en/coins/{client_search}/historical_data?start_date={first_date}&end_date={second_date}#panel'
    response = requests.get(url_page)
    if response.status_code != 200:
        raise message_2.set('Date Error')
        
        
 
    soup = BeautifulSoup(response.text , 'html.parser')
    pages= soup.find('ul', class_ = 'pagination').text
    pages = int(pages[-2])

    for page in range(1 , pages + 1 ):
        url = f'https://www.coingecko.com/en/coins/{client_search}/historical_data?page={page}&end_date={second_date}&start_date={first_date}'
        response_1 = requests.get(url)
        print("sec : ", response_1.status_code)
        soup_1 = BeautifulSoup(response_1.text, 'html.parser')
        for tr in soup_1.findAll('table'):
            for i in tr.find_all('th',class_ = 'font-semibold text-center'):
                date_list.append(i.text)
            for j in tr.find_all('td',  class_ ="text-center"):
                close.append(j.text) 
                open.append(j.text) 
                volume_list.append(j.text)
                market.append(j.text)
        
    close = close[3:len(close):4]
    open = open[2:len(open):4]
    volume_list = volume_list[1:len(volume_list):4]
    market = market[0:len(market):4]        
    date_list
    file_dic = {'Date': date_list}
    if close_price.get() == 1:
        file_dic.update({'Close Price' : close})
    if open_price.get() == 1:
        file_dic.update({'Open Price' : open})
    if marketcap_value.get() == 1:
        file_dic.update({'MarketCap ': market})
    if valume_cap.get() == 1:
        file_dic.update({'Volume' : volume_list})
    
    if variable.get() == 'Pick Format':
        raise message_2.set('please Select a format')
    
    if variable.get() == 'CSV':
        print(type(file_dic))
        with open('webscraper.csv', 'w') as f:
        # create the csv writer
            writer = csv.writer(f)

            df = pd.DataFrame(file_dic)
            df.to_csv('webscraper.csv', sep=',',index=False)

        # write a row to the csv file
          
          
        message_3.set('Your csv data is ready')

    
    
    if variable.get() == 'Excel':
        df = pd.DataFrame(file_dic)
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('webscraper.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet1',index=False)

# Close the Pandas Excel writer and output the Excel file.
        writer.close()
        message_3.set('Your Excel data is ready')
        




# for use in other programs

if __name__ == "__main__":
    app = main()
    root.mainloop()
    
