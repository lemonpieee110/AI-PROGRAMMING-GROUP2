import tkinter as tk
import tkinter.messagebox as msgbox
import math as cm
from tkinter.messagebox as msgbox

def functions(e):
  #get the text of the button which was clicked
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
  elif(text=="1/x"):
    varEntry1.set(str(1/float(varEntry1.get())))
  else:
    varEntry1.set(varEntry1.get()+text)
  pass

#powFunction can directly use '**',coded this function for differentiating from '*'
def powFunc(line):
  temp = line.split("pow");#split by pow to recognize which number to pow 
  return str(float(temp[0])**float(temp[1]))#after spliting 'temp',it has become a list so its temp[0] pows temp[1](the number before 'pow' and the number after 'pow')

#suqareRoot function using imported 'math Library' for using "√" calculation
def squareRoot(line):
  temp = line.split("√");
  return str(cm.sqrt(float(temp[1])))#find the number after '√' and use sqrt() from math library then return it in string

def btnEquals_Click():
  try:
    if("pow" in varEntry1.get()):#if pow was used in the calculator,process like below
      pow1=varEntry1.get();
      varEntry1.set(powFunc(pow1))
    elif("√" in varEntry1.get()):#if √ was used in the calculator,process like below
      sqr1=varEntry1.get()
      varEntry1.set(squareRoot(sqr1))
    else:
      result=eval(varEntry1.get())
      varEntry1.set(varEntry1.get()+"="+str(result))
  except:
    msgbox.showerror("error","please enter the right formula")
  pass



#load frame
form1=tk.Tk()
form1.title("calculator")
#setting size
form1.geometry("292x343")

#show info function
def msg():
  msgbox.showinfo("INFO","AI Programming group2 project")
#initialize menu of form1(the frame)
menubar=mu(form1)
#set a menubar named INFO and if clicked use msg()
menubar.add_command(label="INFO",command=msg)
#bind menubar to the frame
form1['menu']=menubar




#part1
#get input(entry)
varEntry1=tk.StringVar()
#setting style of input textbox
entry1=tk.Entry(form1,fg="white",bg="black",textvariable=varEntry1)
#setting positon of textbox
entry1.grid(row=0,column=0,sticky=tk.EW,ipady=5)

#part2
#create frame
f1=tk.Frame(form1)
#the position that buttons starts from
f1.grid(row=1,column=0)


#row and col
ro=0
col=0


#create buttons
fh=[7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","%","(",")","pow","√","clear","backspace","^","1/x"]
#using for loop to get all the buttons in the list
for i in fh:
  if(col!=0 and col%4==0):#if its already the fourth cell↓ 
    ro+=1 #go to the next row(br)↓
    col=0 #make the column start from 1 everytime br
  btn1=tk.Button(f1,text=i,width=9,height=2)#buttons' size
  btn1.bind("<Button-1>",functions)
  btn1.grid(row=ro,column=col)
  col+=1


#= button
#the equals button has to be separated cause its doing more than giving inputting infos
btnEquals=tk.Button(f1,text="=",width=6,command=btnEquals_Click)
btnEquals.grid(row=ro+1,column=0,columnspan=4,sticky=tk.EW)


form1.mainloop()
