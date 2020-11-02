#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import *
import math
from PIL import ImageTk, Image

def conversion_window():
    
    from tkinter import ttk
    root = Tk()
    root.title("Conversion Window")
    root.geometry("600x600")
    root.configure(bg='#008891')



    mylabel = Label(root,text="Start Conversion Here!",font="times 20 bold",bg='#00587a',fg="white")
    mylabel.place(x=160,y=10)

    mylabel = Label(root,text="From",font="times 18 bold",bg='#0f3057',fg="white",width="10")
    mylabel.place(x=120,y=123)

    mylabel = Label(root,text="To",font="times 18 bold",bg='#0f3057',fg="white",width="10")
    mylabel.place(x=120,y=182)



    def result_function():
            from_box = mycombo.get()
            to_box = mycombo2.get()
            if from_box=="Binary" and to_box=="Decimal":
                 BinaryToDecimal()
                    
                    
            elif from_box=="Binary" and to_box=="Octal":
                 BinaryToOctal()
                    
                    
            elif from_box=="Binary" and to_box=="Hexadecimal":
                 BinaryToHex()    
                    
                    
            elif from_box=="Decimal" and to_box=="Binary":
                 DecimalToBinary() 
                    
            elif from_box=="Decimal" and to_box=="Octal":
                 DecimalToOctal() 
                    
            elif from_box=="Decimal" and to_box=="Hexadecimal":
                 DecimalToHex()
                    
                    
            elif from_box=="Octal" and to_box=="Decimal":
                 OctalToDecimal()
                    
                    
                    
            elif from_box=="Octal" and to_box=="Binary":
                 OctalToBinary()
                    
                    
            elif from_box=="Octal" and to_box=="Hexadecimal":
                 OctalToHex()  
                    
                    
            elif from_box=="Hexadecimal" and to_box=="Decimal":
                 HexToDecimal()  
                    
                    
            elif from_box=="Hexadecimal" and to_box=="Binary":
                 HexToBinary()
                    
                    
            elif from_box=="Hexadecimal" and to_box=="Octal":
                 HexToOctal()        
    
    def BinaryToDecimal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        binary = myentry2.get()
        decimal = 0 
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        print(decimal)
        myentry.insert(0, decimal)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#009432",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=binarytodecimal)
                 
        explanation_button.place(x=150,y=440,height=30)
      
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
        
    
    
    
    
    
    
    
    
    
    def BinaryToOctal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        binary = myentry2.get()
       
        octal = 0
        decimal = 0
        i = 0
        binary=int(binary,2)
        while(binary != 0):
            
            decimal += (binary%10) * math.pow(2,i);
            i = i + 1
            binary = int(binary/10)

        i = 1

        while (decimal != 0):
            octal += (decimal % 8) * i;
            decimal = int(decimal/8)
            i *= 10;
        print(octal);
        print(decimal);
      
        myentry.insert(0,octal)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=binarytooctal)
                 
        explanation_button.place(x=150,y=440,height=30)
        
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
        
        
    def BinaryToHex():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        invalue = myentry2.get()
        wmap = {"0000": "0",
                    "0001": "1",
                    "0010": "2",
                    "0011": "3",
                    "0100": "4",
                    "0101": "5",
                    "0110": "6",
                    "0111": "7",
                    "1000": "8",
                    "1001": "9",
                    "1010": "A",
                    "1011": "B",
                    "1100": "C",
                    "1101": "D",
                    "1110": "E",
                    "1111": "F"
                                }
        i = 0
        output = ""

        while (len(invalue) % 4 != 0):
            invalue = "0" + invalue

        while (i < len(invalue)):
            output = output + wmap[invalue[i:i + 4]]
            i = i + 4

            output = output.lstrip("0")
            output = "0" if len(output) == 0 else output

            print(output)
        #res=BinaryToHex(invalue)        
        myentry.insert(0,output)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=binarytohex)
                 
        explanation_button.place(x=150,y=440,height=30)
        
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
    #num = myentry2.get()   
    def DecimalToBinary():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        decimal = myentry2.get()
        decimal = int(decimal)
        output = bin(decimal).replace("0b", "")   
      
        
        myentry.insert(0,output)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=decimaltobinary)
                 
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)

        
    def DecimalToOctal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        decimal = myentry2.get()
        decimal = int(decimal)
        output = oct(decimal).replace("0o", "")   
      
        
        myentry.insert(0,output)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=decimaltooctal)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
    def DecimalToHex():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        decimal = myentry2.get()
        decimal = int(decimal)
        output = hex(decimal).replace("0x", "")   
      
        
        myentry.insert(0,output)
    
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=decimaltohex)
                 
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
        
    def OctalToDecimal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        num = myentry2.get()
        num = int(num)
        decimal_value = 0 
        base = 1
        while (num): 
            last_digit = num % 10
            num = int(num / 10)
            decimal_value += last_digit * base
            base = base * 8  
            output=decimal_value
            print(output)   
        myentry.insert(0,output)
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=octaltodecimal)
                 
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
    def OctalToBinary():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        octal = myentry2.get()
        octal = int(octal)
        decimal = 0
        i = 0
        binary = 0
        
        while(octal != 0):
            decimal += (octal%10) * math.pow(8,i)
            i = i + 1
            octal = int (octal / 10)
            
            i = 1

        while (decimal != 0):
            binary = binary + (decimal % 2) * i;
            decimal = int(decimal / 2);
            i *= 10; 
        output=(int(binary))
        myentry.insert(0,output)
        
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=octaltobinary)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
        
    def OctalToHex():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        octnum = myentry2.get()
        #octnum = int(octnum)
        decnum = int(octnum, 8)
        output = hex(decnum).replace("0x", "")
        myentry.insert(0,output)
        
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=octaltohex)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
    def HexToDecimal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        test_string= myentry2.get()
        res = int(test_string, 16)
        res = str(res)
        myentry.insert(0,res)
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=hextodecimal)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
    def  HexToBinary():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        ini_string= myentry2.get()
        res = bin(int(ini_string, 16))
        res = str(res).replace("0b", "")
        myentry.insert(0,res)
        
        
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=hextobinary)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        
        
    def HexToOctal():
        mylabel = Label(root,text="Result",font="times 18 bold",bg='#009432',fg="black",width="10")
        mylabel.place(x=70,y=370,height='35')
        myentry = Entry(root,font="times 18 bold",highlightthickness=3)
        myentry.config(highlightbackground = "#fbc531", highlightcolor= "green")
        myentry.place(x=280,y=370,width=290,height=30)
        hexdec = myentry2.get()
        dec = int(hexdec, 16)
        res = oct(dec).replace("0o", "") 
        myentry.insert(0,res)
        
        
        explanation_button = Button(root,text = "Get Explanation",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=hextooctal)
        
        explanation_button.place(x=150,y=440,height=30)
        def reset_function():
            mycombo.current(0)
            mycombo2.current(0)
            myentry.delete(0,END)
            myentry2.delete(0,END)
        reset_button = Button(root,text = "Reset",bg="#ff4d4d",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=reset_function)
                  
        reset_button.place(x=150,y=500,height=30)
        

        
        
    def decimaltobinary():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root11 = Tk()
        root11.title("Conversion Window")
        root11.geometry("800x600")
        root11.configure(bg='#323232')
        
        mylabel = Label(root11,text="HOW TO CONVERT FROM DECIMAL TO BINARY ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root11,text="Follow these steps to convert from decimal to binary ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img = Image.open("decimaltobinary.png")
        img = img.resize((700,400))
    
        my_image = ImageTk.PhotoImage(img, master=root11)
        my_label = Label(root11,image=my_image,bg="#008891")
        my_label.place(x=50,y=120)
        
        root11.mainloop()
        
        
        
        
    def decimaltooctal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root12 = Tk()
        root12.title("Conversion Window")
        root12.geometry("800x600")
        root12.configure(bg='#323232')
        
        mylabel = Label(root12,text="HOW TO CONVERT FROM DECIMAL TO OCTAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root12,text="Follow these steps to convert from decimal to octal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img22 = Image.open("decimaltooctal.png")
        img22 = img22.resize((700,400))
    
        my_image22 = ImageTk.PhotoImage(img22, master=root12)
        my_label22 = Label(root12,image=my_image22,bg="#008891")
        my_label22.place(x=50,y=120) 
        root12.mainloop()
        
        
        
        
    def decimaltohex():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root13 = Tk()
        root13.title("Conversion Window")
        root13.geometry("800x600")
        root13.configure(bg='#323232')
        
        mylabel = Label(root13,text="HOW TO CONVERT FROM DECIMAL TO HEXADECIMAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root13,text="Follow these steps to convert from decimal to hexadecimal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img33 = Image.open("decimaltohex.png")
        img33 = img33.resize((700,400))
    
        my_image33 = ImageTk.PhotoImage(img33, master=root13)
        my_label33 = Label(root13,image=my_image33,bg="#008891")
        my_label33.place(x=50,y=120) 
        root13.mainloop()   
        
        
    def binarytodecimal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root14 = Tk()
        root14.title("Conversion Window")
        root14.geometry("800x600")
        root14.configure(bg='#323232')
        
        mylabel = Label(root14,text="HOW TO CONVERT FROM BINARY TO DECIMAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root14,text="Follow these steps to convert from binary to decimal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img44 = Image.open("binarytodecimal.png")
        img44 = img44.resize((700,400))
    
        my_image44 = ImageTk.PhotoImage(img44, master=root14)
        my_label44 = Label(root14,image=my_image44,bg="#008891")
        my_label44.place(x=50,y=120) 
        root14.mainloop()   
        
        
        
    def binarytooctal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root15 = Tk()
        root15.title("Conversion Window")
        root15.geometry("800x600")
        root15.configure(bg='#323232')
        
        mylabel = Label(root15,text="HOW TO CONVERT FROM BINARY TO OCTAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root15,text="Follow these steps to convert from binary to octal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img55 = Image.open("binarytooctal.png")
        img55 = img55.resize((700,400))
    
        my_image55 = ImageTk.PhotoImage(img55, master=root15)
        my_label55 = Label(root15,image=my_image55,bg="#008891")
        my_label55.place(x=50,y=120) 
        root15.mainloop()               
        
        
    def binarytohex():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root16 = Tk()
        root16.title("Conversion Window")
        root16.geometry("800x600")
        root16.configure(bg='#323232')
        
        mylabel = Label(root16,text="HOW TO CONVERT FROM BINARY TO OCTAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root16,text="Follow these steps to convert from binary to octal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img66 = Image.open("binarytohex.png")
        img66 = img66.resize((400,480))
    
        my_image66 = ImageTk.PhotoImage(img66, master=root16)
        my_label66 = Label(root16,image=my_image66,bg="#008891")
        my_label66.place(x=200,y=120) 
        root16.mainloop()     
        
        
    def octaltobinary():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root17 = Tk()
        root17.title("Conversion Window")
        root17.geometry("800x600")
        root17.configure(bg='#323232')
        
        mylabel = Label(root17,text="HOW TO CONVERT FROM OCTAL TO BINARY ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root17,text="Follow these steps to convert from octal to binary ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img77 = Image.open("octaltobinary.png")
        img77 = img77.resize((700,400))
    
        my_image77 = ImageTk.PhotoImage(img77, master=root17)
        my_label77 = Label(root17,image=my_image77,bg="#008891")
        my_label77.place(x=50,y=120) 
        root17.mainloop()
        
        
        
    def octaltodecimal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root18 = Tk()
        root18.title("Conversion Window")
        root18.geometry("800x600")
        root18.configure(bg='#323232')
        
        mylabel = Label(root18,text="HOW TO CONVERT FROM OCTAL TO BINARY ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root18,text="Follow these steps to convert from octal to binary ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img88 = Image.open("octaltodecimal.png")
        img88 = img88.resize((700,400))
    
        my_image88 = ImageTk.PhotoImage(img88, master=root18)
        my_label88 = Label(root18,image=my_image88,bg="#008891")
        my_label88.place(x=50,y=120) 
        root18.mainloop() 
        
        
        
    def octaltohex():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root19 = Tk()
        root19.title("Conversion Window")
        root19.geometry("800x600")
        root19.configure(bg='#323232')
        
        mylabel = Label(root19,text="HOW TO CONVERT FROM OCTAL TO BINARY ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root19,text="Follow these steps to convert from octal to binary ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img99 = Image.open("octaltohex.png")
        img99 = img99.resize((700,400))
    
        my_image99 = ImageTk.PhotoImage(img99, master=root19)
        my_label99 = Label(root19,image=my_image99,bg="#008891")
        my_label99.place(x=50,y=120) 
        root19.mainloop()  
        
        

    def hextooctal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root20 = Tk()
        root20.title("Conversion Window")
        root20.geometry("800x600")
        root20.configure(bg='#323232')
        
        mylabel = Label(root20,text="HOW TO CONVERT FROM HEXADEXIMAL TO OCTAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root20,text="Follow these steps to convert from hexadecimal to octal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img100 = Image.open("hextooctal.png")
        img100 = img100.resize((700,400))
    
        my_image100 = ImageTk.PhotoImage(img100, master=root20)
        my_label100 = Label(root20,image=my_image100,bg="#008891")
        my_label100.place(x=50,y=120) 
        root20.mainloop() 
        
        
        
    def hextodecimal():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root21 = Tk()
        root21.title("Conversion Window")
        root21.geometry("800x600")
        root21.configure(bg='#323232')
        
        mylabel = Label(root21,text="HOW TO CONVERT FROM HEXADEXIMAL TO DECIMAL ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root21,text="Follow these steps to convert from hexadecimal to decimal ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img101 = Image.open("hextodecimal.png")
        img101 = img101.resize((700,400))
    
        my_image101 = ImageTk.PhotoImage(img101, master=root21)
        my_label101 = Label(root21,image=my_image101,bg="#008891")
        my_label101.place(x=50,y=120) 
        root21.mainloop()    
        
        
        
    def hextobinary():
        from tkinter import ttk
        from PIL import ImageTk, Image
        root22 = Tk()
        root22.title("Conversion Window")
        root22.geometry("800x600")
        root22.configure(bg='#323232')
        
        mylabel = Label(root22,text="HOW TO CONVERT FROM HEXADEXIMAL TO BINARY ",font="times 18 bold",bg='#009432',fg="black")
        mylabel.place(x=100,y=20,height='35')
        
        
        mylabel = Label(root22,text="Follow these steps to convert from hexadecimal to binary ",font="times 18 bold",bg='#fcbf1e',fg="black")
        mylabel.place(x=5,y=65,height='35')
        
        
        img102 = Image.open("hextodecimal.png")
        img102 = img102.resize((700,400))
    
        my_image102 = ImageTk.PhotoImage(img102, master=root22)
        my_label102 = Label(root22,image=my_image102,bg="#008891")
        my_label102.place(x=50,y=120) 
        root22.mainloop()                 
           
        
        
        
        
    
        
        
        
        
        
        
      
    
   
  
           
        
        
        
        
        


        
        
   
    
    
    
       
        
    
    
    
    
    
    
    
    def comboclick(event):
        mymsg = Label(root,text="Enter " + mycombo.get() + ' number',font="time 13 bold",bg="#e7e7de")
        mymsg.place(x=20,y=250,width=250,height=30)
    
    #myentry2 = Entry(root,font="times 18 bold")
    #myentry2.place(x=300,y=250,width=270,height=30)
    #myentry.grid(ipady=5)
    
    options = [
    "choose option",
    "Binary",
    "Decimal",
     "Octal",
    "Hexadecimal",
    ]

    clicked = StringVar()



    mycombo = ttk.Combobox(root,value=options)
    mycombo.current(0)
    mycombo.bind('<<ComboboxSelected>>',comboclick)

    mycombo.place(x=280,y=120,width=190,height=35)



    mycombo2 = ttk.Combobox(root,value=options)
    mycombo2.current(0)

    mycombo2.place(x=280,y=180,width=190,height=35)


    result_button = Button(root,text = "Get Result",bg="#009432",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command=result_function)
                 
    result_button.place(x=150,y=310,height=30)



    myentry2 = Entry(root,font="times 18 bold",highlightthickness=3)
    myentry2.config(highlightbackground = "#c23616", highlightcolor= "green")
    myentry2.place(x=300,y=250,width=270,height=30)
    
    
    def about_function():
        import tkinter
        window = tkinter.Tk()                                                  #creates label
        window.title("GUI")
        window.geometry("200x200")
        root.mainloop()
    
    
    
    
    


    

         
        
        
        
        
        
        
        
       
         
        
                 
        
                 
       
            

    
   







# In[23]:


from tkinter import*
from PIL import ImageTk, Image
def dashboard():
    
    
    root =Tk()

    root.title('Dashboard')

    c= Canvas(root, bg='#008891', height=500,width=400)

    fnt=('times',30)

    id=c.create_text(200,60, text="Dashboard", font=fnt, fill='#ffffff')

    c.grid()


    Instruction = Button(root,text="Instructions",padx=50,pady=15,background="#666666",width=12,command=instruction_window)

    Instruction.place(x=75,y=220)

    Instruction.config(font=('Segoe',))

    Conversion = Button(root,text="Start Conversion",padx=50,pady=15,background="#666666",width=12,command=conversion_window)

    Conversion.place(x=76,y=120)

    Conversion.config(font=('Segoe',))


    About = Button(root,text="About",padx=50,pady=15,background="#666666",width=12, command=about_window2)

    About.place(x=75,y=320)

    About.config(font=('Segoe',))

    root.mainloop()


# In[24]:


from tkinter import *
import math
from PIL import ImageTk, Image 
def homepage():
    from tkinter import ttk
    root2 = Tk()
    root2.title("Home Page")
    root2.geometry("600x600")
    root2.configure(bg='#008891')
    
    img = Image.open("lpulogo.png")
    img = img.resize((320,151))
    
    my_image = ImageTk.PhotoImage(img)
    my_label = Label(image=my_image,bg="#008891")
    my_label.place(x=300,y=50)
    
    my_label.pack()
    
    
    mylabel = Label(root2,text="WELCOME TO",font="times 20 bold",bg='#008891',fg="black",width="30")
    mylabel.place(x=68,y=160,height='35')
    
    mylabel = Label(root2,text="CONVERT ME ! CALCULATOR",font="times 20 bold",bg='#009432',fg="black")
    mylabel.place(x=104,y=210,height='35')
    
    mylabel = Label(root2,text="CREATED BY",font="times 16 bold",bg='#487eb0',fg="#faf3dd")
    mylabel.place(x=230,y=270,height='35')
    
    mylabel = Label(root2,text="Avinash Verma",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=10,y=310,height='35')
    
    mylabel = Label(root2,text="11901833",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=26,y=338,height='35')
    
    mylabel = Label(root2,text="Roll No - 10",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=18,y=366,height='35')
    
    
    mylabel = Label(root2,text="Gautam verma",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=230,y=310,height='35')
    
    mylabel = Label(root2,text="11901869",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=244,y=338,height='35')
    
    mylabel = Label(root2,text="Roll No - 03",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=240,y=366,height='35')
    
    mylabel = Label(root2,text="Mrityunjay Deepak",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=412,y=310,height='35')
    
    
    mylabel = Label(root2,text="11901849",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=450,y=338,height='35')
    
    mylabel = Label(root2,text="Roll No - 07",font="times 16 bold",bg='#008891',fg="#290001")
    mylabel.place(x=442,y=366,height='35')
    
    
    mylabel = Label(root2,text="SUBMITTED TO",font="times 16 bold",bg='#1e5f74',fg="#faf3dd")
    mylabel.place(x=220,y=410,height='35')
     
    mylabel = Label(root2,text="Mr. Ishan Kumar - Dept. Of Computer Science and Engg.",font="times 16 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=44,y=460,height='35')
    
    
    proceed_button = Button(root2,text = "PROCEED",bg="#008000",fg="white",width=24,font='times 15 bold',cursor="circle",
                  borderwidth = '4',pady=50,command = dashboard)
                 
    proceed_button.place(x=150,y=520,height=40)
    
    
    
        
         
   
    
    
   
    root2.mainloop()
    


# In[ ]:





# In[25]:


from tkinter import *
import math
from PIL import ImageTk, Image

def instruction_window():
    from PIL import ImageTk, Image
    from tkinter import ttk
    root = Tk()
    root.title("Instruction Window")
    root.geometry("800x600")
    root.configure(bg='#008891')
    
    
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill=BOTH, expand=1)
    
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    
    
    my_canvas.configure(yscrollcommand=  my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
   # mylabel = Label(second_frame,text="Welcome, Get Full Guidance on How To Use Our App ",font="times 16 bold",bg='#008891',fg="#290001")
    #mylabel.grid(row=0,column=2)
    img = Image.open("homepage.png")
    img = img.resize((400,400))
    
    my_image = ImageTk.PhotoImage(img, master=root)
    my_label = Label(second_frame,image=my_image,bg="#008891")
    my_label.grid(row=2,column=0)
    
    
    img1 = Image.open("dashboard.png")
    img1 = img1.resize((400,400))
    
    my_image1 = ImageTk.PhotoImage(img1, master=root)
    my_label1 = Label(second_frame,image=my_image1,bg="#008891")
    my_label1.grid(row=4,column=0)
    
  

    img2 = Image.open("conversion.png")
    img2 = img2.resize((700,400))
    
    my_image2 = ImageTk.PhotoImage(img2, master=root)
    my_label2 = Label(second_frame,image=my_image2,bg="#008891")
    my_label2.grid(row=6,column=0)
    
    
    
    
    
    
    
    
    mylabel8 = Label(second_frame,text="Welcome, You Can Get Full Details On How To Use Our App",font="times 19 bold",bg='#1e5f74',fg="#faf3dd")
    mylabel8.grid(row=0,column=0)
    
    mylabel3 = Label(second_frame,text="STEP1: ",font="times 22 bold",bg='#f0a500',fg="#000000",width=50)
    mylabel3.grid(row=1,column=0)
    
    mylabel4 = Label(second_frame,text="STEP2: ",font="times 22 bold",bg='#f0a500',fg="#000000",width=50)
    mylabel4.grid(row=3,column=0)
    
    mylabel5 = Label(second_frame,text="STEP3: ",font="times 22 bold",bg='#f0a500',fg="#000000",width=50)
    mylabel5.grid(row=5,column=0)
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    root.mainloop()


# In[ ]:





# In[28]:


from tkinter import *
import math
from PIL import ImageTk, Image

def about_window2():
    from tkinter import ttk
    from PIL import ImageTk, Image
    root0 = Tk()
    root0.title("about")
    root0.geometry("600x650")
    root0.configure(bg='#008891')
    
   
    
    
    
    
    mylabel = Label(root0,text="WELCOME TO",font="times 20 bold",bg='#008891',fg="black",width="30")
    mylabel.place(x=68,y=160,height='35')
    
    mylabel = Label(root0,text="CONVERT ME ! CALCULATOR",font="times 20 bold",bg='#009432',fg="black")
    mylabel.place(x=104,y=210,height='35')
    
    
    mylabel = Label(root0,text="SUBMITTED TO",font="times 16 bold",bg='#1e5f74',fg="#faf3dd")
    mylabel.place(x=220,y=520,height='35')
     
    mylabel = Label(root0,text="Mr. Ishan Kumar - Dept. Of Computer Science and Engg.",font="times 16 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=44,y=560,height='35')
    
    mylabel = Label(root0,text="Convert me calculator is number conversion calculator which provides",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=250,height='35')
    
    mylabel = Label(root0,text="easy and convenient method to convert one number system in to other  ",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=290,height='35')
    
    mylabel = Label(root0,text="It also provides step wise explanation how work is done in converting   ",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=330,height='35')
    
    mylabel = Label(root0,text="It covers all types of conversion and provides dynamic interface to user",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=330,height='35')
    
    mylabel = Label(root0,text="This calculator has been implemented by python3 programing language",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=370,height='35')
    
    mylabel = Label(root0,text="This calculator describes the best use of python3 and covers all topics  ",font="times 14 bold",bg='#52575d',fg="#faf3dd")
    mylabel.place(x=10,y=410,height='35')
    
    mylabel = Label(root0,text="THANK YOU!, VISIT AGAIN ",font="times 14 bold",bg='#27496d',fg="#ffffff")
    mylabel.place(x=160,y=470,height='35')
    
    
    
    
    
    
    
        
         
   
    
    
   
    root0.mainloop()
    

    
    
    


# In[30]:


homepage()


# In[ ]:




