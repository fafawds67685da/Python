import matplotlib.pyplot as p
import numpy as n
x=n.linspace(1,11,10)
y=n.sin(x)
p.plot(x,y , color='red',marker='^',markeredgecolor='yellow',markersize='24', markeredgewidth=12,markerfacecolor='black')
p.title("DEV's FIRST GRAPH" , color ='green',fontsize = 48,fontstyle = 'italic')
p.xlabel("X----->", color='green')
p.ylabel("y----->",color='green')
p.show()
