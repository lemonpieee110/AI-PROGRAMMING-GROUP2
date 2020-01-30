# AI-Programming-group2-calculator

[TOC]

## Used environment & Programming language
- Python
- Visual Studio Code
- Anaconda/Jupyter notebook

## Achieved functions
- Input/edit formula with buttons
- Plus
- Minus
- Divide
- Times
- Remainder
- Square root
- Power
- Inverse proportional function
- Exclusive or operation
- Multistage Operations
- Menubar info showing

## Markable codes
1. Check what was the last inputted operator and store it into a variable for later using
```
text=str(e.widget.configure().get("text")[-1])
```
2. Check if there is already a sorted formula showed in the textbox and if there is, then go in to IF&ELIF statement to decide clear the input box or backspace it to recreate a formula 
```
if("=" in varEntry1.get()):
    if(text=="clear"):
      varEntry1.set("")
    elif(text=="backspace"):
      varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])
    else:
      varEntry1.set(text)
```
3. Inverse proportional function is for one number only so it's also in the functionality judging statement ( : ) can't seem to be done by using eval(), lol )
```
elif(text=="1/x"):
    varEntry1.set(str(1/float(varEntry1.get())))
```
4. Independent functions power and square root are both using split() to decide which number to be operated(square root used math library)
```
emp = line.split("pow")
return str(float(temp[0])**float(temp[1]))

temp = line.split("√")
return str(cm.sqrt(float(temp[1])))
```

## Unsorted issues
1. Power function can only be done independently and be like "num1 pow num2"
2. Square root function has the same problem as power's, and be like "√ num"
3. Using eval() seems limited lots of later stage update, or just there's not enough IF&ELSE statements

