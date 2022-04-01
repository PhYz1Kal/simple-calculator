# Author: Edoardo Gozzi
# Created: 30-31/03/2022

from tkinter import *
from tkinter import messagebox as mb
import math
import time
import os

def app():
    root=Tk()
    resolution=str(root.winfo_screenwidth())+'x'+str(root.winfo_screenheight())
    if resolution=='1920x1080':
        root.title('Calculator')
        root.geometry('275x390')
        root.resizable(False,False)
        root.config(bg='white')
        # RESULT BOX
        res=Entry(root,highlightthickness=0,bd=0,font=('Arial 20 bold'),width=17)
        res.place(x=7,y=7)
        
        # BUTTON SETTINGS
        def fbn():
            if not root['bg']=='#404040': 
                root.config(bg='#404040')
                res.config(bg='#404040',fg='white',bd=0)
                bn.config(bg='#787878',fg='white',borderwidth=0,border=0,highlightthickness=0,bd=0,activebackground='#787878')
                bdel.config(bg='#787878',fg='white',borderwidth=0,border=0,highlightthickness=0,bd=0,activebackground='#787878')
                b1.config(bg='#787878',fg='white',activebackground='#787878')
                b2.config(bg='#787878',fg='white',activebackground='#787878')
                b3.config(bg='#787878',fg='white',activebackground='#787878')
                b4.config(bg='#787878',fg='white',activebackground='#787878')
                b5.config(bg='#787878',fg='white',activebackground='#787878')
                b6.config(bg='#787878',fg='white',activebackground='#787878')
                b7.config(bg='#787878',fg='white',activebackground='#787878')
                b8.config(bg='#787878',fg='white',activebackground='#787878')
                b9.config(bg='#787878',fg='white',activebackground='#787878')
                b0.config(bg='#787878',fg='white',activebackground='#787878')
                bcl.config(bg='#787878',fg='white',activebackground='#787878')
                bp.config(bg='#787878',fg='white',activebackground='#787878')
                bl.config(bg='#787878',fg='white',activebackground='#787878')
                bfor.config(bg='#787878',fg='white',activebackground='#787878')
                bpel2.config(bg='#787878',fg='white',activebackground='#787878')
                bd.config(bg='#787878',fg='white',activebackground='#787878')
                bparl.config(bg='#787878',fg='white',activebackground='#787878')
                bparr.config(bg='#787878',fg='white',activebackground='#787878')
                bpelu.config(bg='#787878',fg='white',activebackground='#787878')
                beq.config(bg='#787878',fg='white',activebackground='#787878')
                bsqr.config(bg='#787878',fg='white',borderwidth=0,border=0,highlightthickness=0,bd=0,activebackground='#787878')
            else:
                root.config(bg='white')
                res.config(bg='white',fg='black',bd=0)
                bn.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bdel.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b1.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b2.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b3.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b4.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b5.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b6.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b7.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b8.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b9.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                b0.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bcl.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bp.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bl.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bfor.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bpel2.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bd.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bparl.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bparr.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bpelu.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                beq.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
                bsqr.config(bg='white',fg='black',highlightthickness=0,bd=1,activebackground='white')
        
        bn=Button(root,text='Change Theme',bg='white',fg='black',width=11,height=1,highlightthickness=0,bd=1,activebackground='white',command=fbn)
        bn.place(x=10,y=45)
        
        # BUTTON SQ ROOT
        def fbsqr():
            a=float(res.get())
            b=math.sqrt(a)
            res.delete(0,END)
            res.insert(0,b)
        bsqr=Button(root,text='√',bg='white',fg='black',width=6,height=1,highlightthickness=0,bd=1,activebackground='white',command=fbsqr)
        bsqr.place(x=123,y=45)
        
        # BUTTON C
        def fbdel():
            res.delete(len(res.get())-1,END)
        bdel=Button(root,text='C',bg='white',fg='black',width=5,height=1,highlightthickness=0,bd=1,activebackground='white',command=fbdel)
        bdel.place(x=196,y=45)
        
        # BUTTON 1
        def fb1():
            res.insert(END,1)
        b1=Button(root,text='1',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb1)
        b1.place(x=7,y=80)
        
        # BUTTON 2
        def fb2():
            res.insert(END,2)
        b2=Button(root,text='2',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb2)
        b2.place(x=68,y=80)
        
        # BUTTON 3
        def fb3():
            res.insert(END,3)
        b3=Button(root,text='3',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb3)
        b3.place(x=133,y=80)
        
        # BUTTON 4
        def fb4():
            res.insert(END,4)
        b4=Button(root,text='4',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb4)
        b4.place(x=7,y=141)
        
        # BUTTON 5
        def fb5():
            res.insert(END,5)
        b5=Button(root,text='5',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb5)
        b5.place(x=68,y=141)
            
        # BUTTON 6
        def fb6():
            res.insert(END,6)
        b6=Button(root,text='6',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb6)
        b6.place(x=133,y=141)
            
        # BUTTON 7
        def fb7():
            res.insert(END,7)
        b7=Button(root,text='7',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb7)
        b7.place(x=7,y=200)
            
        # BUTTON 8
        def fb8():
            res.insert(END,8)
        b8=Button(root,text='8',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb8)
        b8.place(x=68,y=200)
            
        # BUTTON 9
        def fb9():
            res.insert(END,9)
        b9=Button(root,text='9',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb9)
        b9.place(x=133,y=200)
        
        # BUTTON CLEAR
        def fbcl():
            res.delete(0,END)
        bcl=Button(root,text='AC ',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbcl)
        bcl.place(x=7,y=262)
        
        # BUTTON 0
        def fb0():
            res.insert(END,0)
        b0=Button(root,text='0',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fb0)
        b0.place(x=68,y=262)
        
        # BUTTON PLUS
        def fbp():
            res.insert(END,'+')
        bp=Button(root,text='+',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbp)
        bp.place(x=198,y=80)
            
        # BUTTON LESS
        def fbl():
            res.insert(END,'-')
        bl=Button(root,text='-',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbl)
        bl.place(x=198,y=141)
        
        # BUTTON MULTIPLY
        def fbfor():
            res.insert(END,'*')
        bfor=Button(root,text='×',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbfor)
        bfor.place(x=198,y=200)
                                
        # BUTTON ELEVATION ?
        def fbel2():
            res.insert(END,'**')
        bpel2=Button(root,text='nⁿ',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbel2)
        bpel2.place(x=133,y=262)
            
        # BUTTON DIVIDE
        def fbd():
            res.insert(END,'/')
        bd=Button(root,text='÷',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbd)
        bd.place(x=198,y=262)
                
        # BUTTON PAR LEFT
        def fbparl():
            res.insert(END,'(')
        bparl=Button(root,text='(',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbparl)
        bparl.place(x=7,y=324)
                    
        # BUTTON PAR RIGHT
        def fbparr():
            res.insert(END,')')
        bparr=Button(root,text=')',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbparr)
        bparr.place(x=68,y=324)
                        
        # BUTTON PERC
        def fbelu():
            a=int(res.get())
            inp=Toplevel(root)
            inpu=Entry(inp)
            inpu.pack()
            def subm():
                b=int(inpu.get())
                while b>100 or b<1 or isinstance(b, str)==True:
                    inpu.delete(0,END)
                    inpu.insert(0,'Value error, must be >1 and <100')
                    time.sleep(3)
                    inpu.delete(0,END)
                    if b<100 or b>1 or isinstance(b, str)==False:
                        break
                finres=eval(str(a*b/100))
                res.delete(0,END)
                res.insert(0,float(finres))
                inp.destroy()
            sub=Button(inp,text='Submit',bg='white',fg='black',width=18,height=1,highlightthickness=0,bd=1,activebackground='white',command=subm)
            sub.pack()
        bpelu=Button(root,text='%',bg='white',fg='black',width=5,height=3,highlightthickness=0,bd=1,activebackground='white',command=fbelu)
        bpelu.place(x=133,y=324)
                
        # BUTTON EQUAL
        def fbeq():
            result=eval(res.get())
            res.delete(0,END)
            res.insert(0,result)
        beq=Button(root,highlightthickness=0,bg='white',fg='black',text='=',bd=1,width=5,height=3,activebackground='white',command=fbeq)
        beq.place(x=198,y=324)
    else:
        root=Tk()
        root.title("")
        root.geometry('1x1')
        mb.showerror("Error","Sorry, your display is not supported")
        exit()
    root.mainloop()
app()