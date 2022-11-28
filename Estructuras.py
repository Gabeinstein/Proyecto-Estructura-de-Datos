#Visualizacion calendario

import numpy as np
import calendar

class Node():
    def __init__(self, node_act):
        self.actividad = node_act
c = calendar.TextCalendar(calendar.SUNDAY)
strn = c.formatmonth(2022,1)


calendario = np.zeros((5,7))

for i in range(30):
    calendario.itemset(i,i+1)

print(calendario)