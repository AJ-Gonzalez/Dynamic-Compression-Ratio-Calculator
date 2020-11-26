#Dynamic Compression Ratio calculator
from tkinter import *

def calc():
    import math as m
    #Input read
    inbore=borein.get()
    instroke=strokein.get()
    inccvol=ccvolin.get()
    intiming=timingin.get()
    #Float conversions
    bore0=str(inbore)
    bore=float(bore0)
    stroke0=str(instroke)
    stroke=float(stroke0)
    ccvol0=str(inccvol)
    ccvol=float(ccvol0)
    timing0=str(intiming)
    timing=float(timing0)
    #Converting mm to cm, volume(draw) in CCs
    bore=bore/10
    stroke=stroke/10
    draw=(m.pi*((bore/2)**2))*stroke
    short_stroke=0
    stroke2=stroke
    #Calculates short stroke
    if timing<=90:
        timing2=m.radians(timing)
        short_stroke=stroke-((m.sin(timing2))*(stroke/2))
        
    elif 180>timing>90:
        timing2=m.radians(timing)
        halfst=stroke/2
        short_stroke=((m.sin(timing2))*halfst)
        
    else:
        from tkinter import messagebox as tm
        tm.showinfo("Error", "Intake Valve can't close at or after TDC")
        short_stroke=stroke
        
    #Calculates DCR & CR
    sdraw=short_stroke*(m.pi*((bore/2)**2))
    regcr=ccvol/draw
    dyncr=ccvol/sdraw
    dyncrout=1/dyncr
    regcrout=1/regcr
    regcrdis=str(round(regcrout,3))
    dyncrdis=str(round(dyncrout,3))
    sdrawdis=str(round(sdraw,3))
    drawdis=str(round(draw,3))
    short_strokedis=str(round((short_stroke*10),3))
    
    #Output labels
    L5=Label(mwd, text="Static Compression Ratio: ")
    L5.grid(row=5, column=0)
    
    L5=Label(mwd, text=regcrdis+":1")
    L5.grid(row=5, column=1)
    
    L6=Label(mwd, text="Dynamic Compression Ratio: ")
    L6.grid(row=6, column=0)
    
    L6=Label(mwd, text=dyncrdis+":1")
    L6.grid(row=6, column=1)

    L7=Label(mwd, text="Effective Stroke length: ")
    L7.grid(row=7, column=0)
    
    L8=Label(mwd, text=short_strokedis+" mm   ")
    L8.grid(row=7, column=1)

    L9=Label(mwd, text="Maximum Displacement(per cylinder): ")
    L9.grid(row=8, column=0)
    
    L10=Label(mwd, text=drawdis+" cc   ")
    L10.grid(row=8, column=1)
    
    L11=Label(mwd, text="Effective Displacement(per cylinder): ")
    L11.grid(row=9, column=0)
    
    L12=Label(mwd, text=sdrawdis+" cc   ")
    L12.grid(row=9, column=1)
    
#Window parameters
mwd=Tk()
mwd.title("Dynamic Compression Ratio Calculator")

#Cylinder Bore in mm?
L1=Label(mwd, text="Cylinder Bore in mm:                 ")
L1.grid(row=0, column=0)
borein=Entry(mwd, bd=2)
borein.grid(row=0, column=1)
#Stroke in mm?
L2=Label(mwd, text="Stroke in mm:                        ")
L2.grid(row=1, column=0)
strokein=Entry(mwd, bd=2)
strokein.grid(row=1, column=1)
#Combustion chamber volumein CCs?
L3=Label(mwd, text="Combustion chamber volume in CCs:    ")
L3.grid(row=2, column=0)
ccvolin=Entry(mwd, bd=2)
ccvolin.grid(row=2, column=1)
#Valve closing in degrees after BTDC?
L4=Label(mwd, text="Valve closing in degrees after BTDC: ")
L4.grid(row=3, column=0)
timingin=Entry(mwd, bd=2)
timingin.grid(row=3, column=1)
#Go button
gbtn=Button(mwd, text="Calculate", command=calc)
gbtn.grid(row=4, column=0)


#loop
mwd.mainloop()
