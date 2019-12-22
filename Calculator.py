import tkinter as tk
import tkinter.messagebox as msgbox


def functions(e):
  text=str(e.widget.configure().get("text")[-1])
  if("=" in varEntry1.get()):
    if(text=="clear"):
      varEntry1.set("")
    elif(text=="backspace"):
      varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])
    else:
      varEntry1.set(text)
  if(text=="clear"):
    varEntry1.set("")
  elif(text=="backspace"):
    varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])
  elif(text=="INFO"):
    msgbox.showinfo("INFO","AI Programming group2")
  else:
    varEntry1.set(varEntry1.get()+text)
  pass

def btnEquals_Click():
  try:
    result=eval(varEntry1.get())
    varEntry1.set(varEntry1.get()+"="+str(result))
  except:
    msgbox.showerror("error","please enter the right formula")
  pass



#load frame
form1=tk.Tk()
form1.title("calculator")
form1.geometry("300x305")
form1.iconbitmap("calculator.ico")




#part1
#get input(entry)
varEntry1=tk.StringVar()
entry1=tk.Entry(form1,fg="white",bg="black",textvariable=varEntry1)
entry1.grid(row=0,column=0,sticky=tk.EW,ipady=5)

#part2
#create frame
f1=tk.Frame(form1)
f1.grid(row=1,column=0)


#row and col
ro=0
col=0


#create buttons
fh=[7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","%","clear","backspace","^","INFO"]
for i in fh:
  if(col!=0 and col%4==0):
    ro+=1 #br
    col=0 #make the column start from 1 everytime br
  btn1=tk.Button(f1,text=i,width=9,height=2)
  btn1.bind("<Button-1>",functions)
  btn1.grid(row=ro,column=col)
  col+=1


#= button
btnEquals=tk.Button(f1,text="=",width=6,command=btnEquals_Click)
btnEquals.grid(row=ro+1,column=0,columnspan=4,sticky=tk.EW)


form1.mainloop()
