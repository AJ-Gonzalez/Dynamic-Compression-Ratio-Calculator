#Dynamic Compression Ration calculator
import math as m
borein=input("Cylinder Bore in mm? ")
strokein=input("Stroke in mm? ")
ccvolin=input("Combustion chamber volumein CCs? ")
bore=float(borein)
stroke=float(strokein)
ccvol=float(ccvolin)
#Converting mm to cm, volume(draw) in CCs
bore=bore/10
stroke=stroke/10
draw=(m.pi*((bore/2)**2))*stroke
print(bore, stroke, ccvol, draw,"\n")
timingin=input("Valve closing in degrees after BTDC? ")
timing=int(timingin)
short_stroke=0
stroke2=float(stroke)
#Calculates short stroke
if timing<=90:
    timing2=m.radians(timing)
    print("\n",timing2,"  Valve closing in radians")
    print(m.sin(timing2))
    short_stroke=stroke-((m.sin(timing2))*(stroke/2))
    print(short_stroke*10,"  Effective stroke length in mm")
elif timing>90:
    timing3=m.radians(timing)
    print("\n",timing3, "  Valve closing in radians")
    print(m.sin(timing3))
    short_stroke=stroke-(stroke/2)-((m.sin(timing3))*(stroke/2))
    print(short_stroke*10,"  Effective stroke length in mm")
print("\n Almost done! \n")
#Calculates CR & DCR
regcr=ccvol/draw
sdraw=short_stroke*(m.pi*((bore/2)**2))
dyncr=ccvol/sdraw
print(sdraw," Shortened draw \n")
print(1/regcr,":1"," Regular Compression Ratio \n")
print(1/dyncr,":1"," Dynamic Compression Ratio \n")
input("Exit?")

    


