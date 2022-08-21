from tkinter import *
from tkinter import ttk
class MyWindow:
    f = ''
    def __init__(self, win):
            
        self.lbl1=Label(win, text='Adjustment')
        self.lbl2=Label(win, text='File Name')
        self.lbl3=Label(win, text='Volume')
        self.lbl3=Label(win, text='Max Capacity')
        self.lbl4=Label(win, text='X Grid Size')
        self.lbl5=Label(win, text='Y Grid Size')
        self.lbl6=Label(win, text='Distance between X void centers')
        self.lbl7=Label(win, text='Distance between Y void centers')
        self.lbl8=Label(win, text='Volume')
        self.lbl9=Label(win, text='Start X')
        self.lbl10=Label(win, text='Start Y')
        self.lbl11=Label(win, text='Start Z')
        self.lbl12=Label(win, text='Output')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()
        self.t9=Entry()
        self.t10=Entry()
        self.t11=Entry()
        self.t12=Entry()
        #self.frame1 = Frame(win, bg="blue", width=500, height=300)
        #self.frame1.place(x = 600, y = 25)
        self.textbox = Text(win, wrap=WORD, bg="blue", borderwidth=2)
        self.textbox.place(x = 375, y = 50, width=300)

        self.btn1 = Button(win, text='Write to file')
        self.btn2=Button(win, text='Visual Grid')
        self.lbl1.place(x=50, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=50, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=50, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=50, y=200)
        self.t4.place(x=200, y=200)
        self.lbl5.place(x=50, y=250)
        self.t5.place(x=200, y=250)
        self.lbl6.place(x=50, y=300)
        self.t6.place(x=200, y=300)
        self.lbl7.place(x=50, y=350)
        self.t7.place(x=200, y=350)
        self.lbl8.place(x=50, y=400)
        self.t8.place(x=200, y=400)
        self.lbl9.place(x=0, y=450, width=50)
        self.t9.place(x=50, y=450, width=20)
        self.lbl10.place(x=100, y=450, width=50)
        self.t10.place(x=150, y=450, width=20)
        self.lbl11.place(x=200, y=450, width=50)
        self.t11.place(x=250, y=450, width=20)
        self.lbl12.place(x=375, y=25)
        #self.t12.place(x=375, y=50, width=300, height=400)
        

        self.b1=Button(win, text='Write to file', command=self.fillVoids)
        self.b2=Button(win, text='Visual Grid', command=self.create)
        #self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=550)
        self.b2.place(x=200, y=550)
        

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    
    def create(self):
        window2 = Toplevel(window)
        window2.geometry("600x400")
        c= Canvas(window2,width=400, height=400)
        c.pack()
        gridX = (self.t4.get())
        gridY = (self.t5.get())
        ycount = 0
        xpos = 25
        ypos = 25
        deltaX = int((self.t6.get()))
        deltaY = int((self.t7.get()))
        while int(ycount) < int(gridY): # while we haven't exhausted all rows
            xcount = 0
            while xcount < int(gridX): #while we haven't exhausted all columns
               c.create_oval(xpos -5, ypos -5,xpos +5, ypos+5)
               
               xpos = xpos + deltaX
               xcount = xcount + 1
            xpos =25
            ypos = ypos + deltaY
            ycount = ycount + 1
         
        

        
    def startroutine(self):
       
        startRoutine = """M83 ;relative extrusion mode\n
M106 S0 ;Turn-off fan\n
M104 S0 ;Turn-off hotend\n
M140 S0 ;Turn-off bed\n
M302 ;allow-cold-extrude\n
M221 S350 ;set-flow%\n"""
        self.f = self.f + startRoutine #Turns off fan, hotend, bed, allow cold extrude, set flow%
        


    def fillSyringe(self, currentcapacitY):
        maxcapacitY = (self.t3.get())
        
        
        homeY = "G28 Y ; home Y\n"
        homeX = "G28 X ; home X\n" 
        homeZ = "G28 Z ; home Z\n"
        self.f = self.f + homeY #home Y axis first moves the bed out of the way exposing underneath machine
        self.f = self.f + "G1 Z60\n"
        self.f = self.f + homeX #homing x axis next moves us to a known position, but directly over a rail
        self.f = self.f + "G1 X40\n"
        self.f = self.f + homeZ #homing z should move us to the absolute bottom of the reservoir
        #retracts fluid into syringe
        retractionamount = int(maxcapacitY) - currentcapacitY
        self.f = self.f + "G1 F2000 E" + str(retractionamount) + "; filled syringe\n"
        

    def fillVoids(self):
        self.startroutine()
        startingPOS = [0,0,0]
        currentPOS = [0,0,0]
        adjustment = (self.t1.get())
        fileName = (self.t2.get())
        gridX = (self.t4.get())
        gridY = (self.t5.get())
        deltaX = (self.t6.get())
        deltaY = (self.t7.get())
        volume = (self.t8.get())
        maxcapacitY = (self.t3.get())
        startingPOS[0] = (self.t9.get())
        startingPOS[1] = (self.t10.get())
        startingPOS[2] = (self.t11.get())
        
        total = 0 #tracks the total number of voids that have been filled
        ycount = 0
        justfilled = 0 
        currentPOS = [startingPOS[0], startingPOS[1], startingPOS[2]]
        currentcapacity = 0 #program must start with syringe emptied. There is not end stop 
        
        while ycount < int(gridY): # while we haven't exhausted all rows
            xcount = 0
            while xcount < int(gridX): #while we haven't exhausted all columns
                if int(currentcapacity) - int(volume) < 0:
                    
                    self.fillSyringe(currentcapacity)
                    currentcapacity = maxcapacitY # the syringe has been filled so set capacity to max
                    justfilled = 1
                    self.f = self.f + "G1 Z" + str(currentPOS[2]) + "\n" #Move z axis up high enough not to hit the mold
                    
                else:
                    #moves to current pos x and y
                    self.f = self.f + "G1 X" + str(currentPOS[0]) + " Y" + str(currentPOS[1]) + "\n"
                    total = total + 1
                    #extrudes fluid into void
                    if justfilled == 1: #adjustment for slack from change in direction of syringe
                        self.f = self.f + "G1 F2000 E-" + str(int(volume)- int(adjustment)) + "; #filled =" + str(total) + "\n"
                        justfilled = 0
                    else:
                        self.f = self.f + "G1 F2000 E-" + volume + "; #filled =" + str(total) + "\n"
                    currentPOS[0] = int(currentPOS[0]) + int(deltaX)
                    xcount = xcount + 1
                    currentcapacity = int(currentcapacity) - int(volume)
            currentPOS[0] = startingPOS[0]
            print(startingPOS[0])
            currentPOS[1] = int(currentPOS[1]) + int(deltaY)
            ycount = ycount + 1
        self.textbox.insert(END, str(self.f))
        g = open(fileName, "w") #open test.gcode in write mode clearing file
        g.write(self.f)
        g.close()

             

window=Tk()
mywin=MyWindow(window)
window.title('JackThaDripper')
window.geometry("900x600+25+25")
window.mainloop()



