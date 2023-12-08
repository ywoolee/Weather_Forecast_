from tkinter import *
import requests
from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
import time
root = Tk()
root.resizable(False, False)

root.geometry("900x600+200+250")

root.title("Weather Forecast")

frame_title = Frame(root, bg='slategrey', bd=3)
frame_title.place(relx=0.5, rely=0.02, relwidth=0.5, relheight=0.1, anchor='n')

frame = Frame(root, bg='slategrey', bd=3)
frame.place(relx=0.5, rely=0.14, relwidth=0.92, relheight=0.1, anchor='n')

frame1 = Frame(root,bg='slategrey',bd=3)
frame1.place(relx=0.5, rely=0.26, relwidth=0.92, relheight=0.1, anchor='n')

frame2 = Frame(root, bg='slategrey', bd=3)
frame2.place(relx=0.5, rely=0.38, relwidth=0.92, relheight=0.5, anchor='n')

frame3 = Frame(root, bg='slategrey', bd=3)
frame3.place(relx=0.22, rely=0.89, relwidth=0.36, relheight=0.09, anchor='n')

frame4 = Frame(root, bg='slategrey', bd=3)
frame4.place(relx=0.83, rely=0.89, relwidth=0.26, relheight=0.09, anchor='n')


l_title=Label(frame_title,text="일기예보",font=('나눔 고딕',16,'bold'),bg='white')
l_title.place(relwidth=1, relheight=1)

l1=Label(frame1,text="날씨를 조회할 날을 선택하세요.",font=('나눔 고딕',16,'bold'),bg='white')
l1.place(relwidth=0.695, relheight=1)

s = Spinbox(frame1,values=('오늘',"내일",'2일 후', '3일 후','4일 후'), width = 4, font=('나눔 고딕',16,'bold'),justify=CENTER)
s.place(relx=0.7, relheight=1, relwidth=0.3)

def entry_focus_in(event):
    if entry1.get() == "도시의 이름을 입력하세요.":
        entry1.delete(0,'end')
        entry1.config(fg="black")
def entry_focus_out(event):
    if entry1.get() == " ":
        entry1.insert(0,"도시의 이름을 입력하세요.")
        entry1.config(fg="gray")

entry1 = Entry(frame,font=('나눔 고딕',16,'bold'),justify=CENTER,fg='gray')
entry1.place(relwidth=0.695, relheight=1)
entry1.insert(0,"도시의 이름을 입력하세요.")
entry1.bind("<FocusIn>", entry_focus_in)
entry1.bind("<FocusOut>", entry_focus_out)

    

l2=Label(frame2,text="",font=('나눔 고딕',15,'bold'),bg='white',anchor='n')
l2.place(relwidth=0.5, relheight=1)

l3=Label(frame2,text="",bg='white',anchor='c')
l3.place(relx=0.5,relwidth=0.5, relheight=1)



def weather():
    global l2
    global cityname
    global days
    global l3
    cityname=entry1.get()
    if cityname=='':
        print("")
    else:

        
        if(s.get()=='오늘'):
            days="오늘"
        elif(s.get()=='내일'):
            days="내일"
        elif(s.get()=='2일 후'):
            days="2일+후"
        elif(s.get()=='3일 후'):
            days="3일+후"
        elif(s.get()=='4일 후'):
            days="4일+지난+후"            
        else:
            days=s.get()

        url='https://www.google.com/search?q=%s+%s+날씨'%(cityname,days)
        

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        request=requests.get(url,headers=headers)
        request.raise_for_status()
        soup=BeautifulSoup(request.text,"html.parser")

        temperature=soup.select('#wob_tm')  
        timedate=soup.select('#wob_dts')  
        location=soup.select('#wob_loc') 
        weathercondition=soup.select('#wob_dc')
        rainprobability = soup.select('#wob_pp')

        l=location[0].text
        t=timedate[0].text
        w=weathercondition[0].text
        temp=temperature[0].text
        rainprobability = rainprobability[0].text
        d= re.sub(r'[^0-9]', '', rainprobability)
        rain = int(d)
        
        if (w=='이슬비' or w=='비'or w=='뇌우(약함, 비 동반)' or w=='비바람' or w=='소나기' or w=='뇌우(비 동반)' or w=='광역성 뇌우'or w=='국지성 뇌우'):
            a="Location: %s\n\nDay: %s\n\n날씨: %s\n\n기온: %s 도\n\n강수확률: %s \n\n비가 오니 우산을 챙기세요!!"%(cityname,t,w,temp,rainprobability)
        elif(w=='눈' or w=='소낙눈'):
            a="Location: %s\n\nDay: %s\n\n날씨: %s\n\n기온: %s 도\n\n강수확률: %s \n\n눈이 오니 우산을 챙기세요!!"%(cityname,t,w,temp,rainprobability)
        elif(w=='비와 눈' or w=='비온 후 밤에 눈' or w=='눈온 후 밤에 비'):
            a="Location: %s\n\nDay: %s\n\n날씨: %s\n\n기온: %s 도\n\n강수확률: %s \n\n비와 눈이 오니 우산을 챙기세요!!"%(cityname,t,w,temp,rainprobability)
        else:
            a="Location: %s\n\nDay: %s\n\n날씨: %s\n\n기온: %s 도\n\n강수확률: %s"%(cityname,t,w,temp,rainprobability)
        
        
      
        l2.config(text=a)
        
        print(a)
        if (w=='맑음'):
            img2=PhotoImage(file="1.png")
        elif(w=='대체로 흐림'or w=='구름 조금'or w=='맑으나 때때로 구름'or w=='대체로 맑음'):
            img2=PhotoImage(file="2.png")
        elif(w=='흐림'):
            img2=PhotoImage(file="3.png")
        elif(w=='이슬비'):
            img2=PhotoImage(file="4.png")
        elif(w=='비'or w=='뇌우(약함, 비 동반)' or w=='비바람' or w=='소나기'):
            img2=PhotoImage(file="9.png")
        elif(w=='비와 눈'):
            img2=PhotoImage(file="5.png")
        elif(w=="눈" or w=='소낙눈'):
            img2=PhotoImage(file="6.png")
        elif(w=='바람'):
            img2=PhotoImage(file="7.png")
        elif(w=='뇌우(비 동반)'):
            img2=PhotoImage(file="8.png")
        elif(w=='광역성 뇌우'or w=='국지성 뇌우'):
            img2=PhotoImage(file="10.png")
        else:
            l3=Label(frame2,text="이미지가 없습니다",bg='white',anchor='c')
            l3.place(relx=0.5,relwidth=0.5, relheight=1)
        
        
        l3=Label(frame2,image = img2,bg='white',anchor='c')
        l3.image = img2
        l3.place(relx=0.5,relwidth=0.5, relheight=1)


button = Button(frame, text="검색", font=('나눔 고딕',16,'bold'), command=weather)
button.place(relx=0.7, relheight=1, relwidth=0.3)



def weekly():
    global cityname
    cityname=entry1.get()
    if cityname == "도시의 이름을 입력하세요." or cityname == "":
        top = Toplevel()
        top.title("Wrong Input")
        top.resizable(False, False)
        top.geometry("350x100+500+500")
        frame_error = Frame(top, bg='slategrey', bd=3)
        frame_error.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.5, anchor='n')
        label = Label(frame_error, text="도시이름을 먼저 입력해주세요",font=('나눔 고딕',16,'bold'))
        label.place(relheight=1, relwidth=1)
        frame_error2 = Frame(top, bg='slategrey', bd=3)
        frame_error2.place(relx=0.5, rely=0.56, relwidth=0.5, relheight=0.4, anchor='n')
        button = Button(frame_error2, text="확인",bg='lightsteelblue', font=('나눔 고딕',16,'bold'), command=top.destroy)
        button.place(relheight=1, relwidth=1)

            
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = chrome_options)

        url_weather= 'https://search.naver.com/search.naver?where=nexearch&sm=top_&fbm=0&ie=utf8&query=%s+날씨'%(cityname)
        driver.get(url=url_weather)
        driver.execute_script("window.scrollTo(0, 350)")
        path = 'C:/Users/user/Desktop/weather/weekly.jpg'
        element = driver.find_element(By.CSS_SELECTOR, '.weekly_forecast_area._toggle_panel, .weekly_forecast_area._weekly_forecast')
        element.screenshot(path)
        top = Toplevel()
        top.title("Weekly Weather")
        top.resizable(False, False)
        top.geometry("700x500+400+250")
        frame_week = Frame(top, bg='slategrey', bd=3)
        frame_week.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.85, anchor='n')
        image_week = PhotoImage(file="weekly.jpg")
        label_week=Label(frame_week,image =image_week ,bg='white',anchor='c')
        label_week.image = image_week
        label_week.place(relx=0,relwidth=1, relheight=1)
        frame2 = Frame(top, bg='slategrey', bd=3)
        frame2.place(relx=0.845, rely=0.89, relwidth=0.26, relheight=0.09, anchor='n')
        button = Button(frame2, text="종료", font=('나눔 고딕',16,'bold'), command=top.destroy)
        button.place(relheight=1, relwidth=1)
            
        
        
    
    
    
    
    
button = Button(frame3, text="주간 날씨", font=('나눔 고딕',16,'bold'), command=weekly)
button.place(relheight=1, relwidth=1)



def quit_():
    root.destroy()

button = Button(frame4, text="종료", font=('나눔 고딕',16,'bold'), command=quit_)
button.place(relheight=1, relwidth=1)

root.mainloop()