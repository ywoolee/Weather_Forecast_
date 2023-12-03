from tkinter import *
import requests
import bs4
root = Tk()

canvas = Canvas(root, height=600, width=800)
canvas.pack()


L=Label(root)
L.place(relwidth=1, relheight=1)


frame_L = Frame(root, bg='#4a4641', bd=6)
frame_L.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1, anchor='n')

l_1=Label(frame_L,text="날씨",font=('calibre',16,'italic'),bg='white')
l_1.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#4a4641', bd=6)
frame.place(relx=0.5, rely=0.12, relwidth=0.92, relheight=0.1, anchor='n')

frame1 = Frame(root,bg='#4a4641',bd=6)
frame1.place(relx=0.5, rely=0.24, relwidth=0.92, relheight=0.1, anchor='n')

l=Label(frame1,text="날씨를 조회할 날을 선택하세요. >>>>",font=('calibre',16,'italic'),bg='white')
l.place(relwidth=0.69, relheight=1)

s = Spinbox(frame1,values=('오늘',"내일",'2일 후', '3일 후', '4일 후','5일 후'), width = 4, font=('calibre',16,'italic'),justify=CENTER)
s.place(relx=0.7, relheight=1, relwidth=0.3)

e1 = Entry(frame,font=('calibre',16,'italic'),justify=CENTER)
e1.place(relwidth=0.69, relheight=1)
e1.insert(0,"조회할 도시의 이름을 입력하세요.")

frame2 = Frame(root, bg='#4a4641', bd=8)
frame2.place(relx=0.5, rely=0.36, relwidth=0.92, relheight=0.5, anchor='n')

l2=Label(frame2,text="",font=('calibre',15,'bold'),bg='white',anchor='c')
l2.place(relwidth=0.5, relheight=1)

lw=Label(frame2,text="",bg='white',anchor='c')
lw.place(relx=0.5,relwidth=0.5, relheight=1)





def weather():
    global l2
    global cityname
    global days
    global lw
    cityname=e1.get()
    if cityname=='':
        print("Enter city name")
    else:
        if(s.get()=='오늘'):
            days="오늘"
        elif(s.get()=='내일'):
            days="내일"
        elif(s.get()=='2일 후'):
            days="2일 후"
        elif(s.get()=='3일 후'):
            days="3일 후"
        elif(s.get()=='3일 후'):
            days="3일 후"
        elif(s.get()=='3일 후'):
            days="3일 후"            
        else:
            days=s.get()

        url='https://www.google.com/search?q=%s+weather+%s'%(cityname,days)

        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
        css='#wob_tm'
        
        request=requests.get(url,headers=headers)
        request.raise_for_status()
        soup=bs4.BeautifulSoup(request.text,"html.parser")

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
        elif(w=='비'or w=='뇌우(약함, 비 동반)' or w=='비바람'):
            img2=PhotoImage(file="9.png")
        elif(w=='비와 눈'):
            img2=PhotoImage(file="5.png")
        elif(w=='눈'):
            img2=PhotoImage(file="6.png")
        elif(w=='바람'):
            img2=PhotoImage(file="7.png")
        elif(w=='뇌우(비 동반)'):
            img2=PhotoImage(file="8.png")
        elif(w=='광역성 뇌우'or w=='국지성 뇌우'):
            img2=PhotoImage(file="10.png")
        else:
            img2=PhotoImage(file="whitebox.png")
        
        
        lw=Label(frame2,image = img2,bg='white',anchor='c')
        lw.image = img2
        lw.place(relx=0.5,relwidth=0.5, relheight=1)


button = Button(frame, text="조회", font=('calibre',16,'italic'), command=weather)
button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()
