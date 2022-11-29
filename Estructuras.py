#Visualizacion calendario


import calendar

def menu(year = None,month = None):
    print("")
    print("APLICACION CALENDARIO")
    print("")
    
    if (year == None and month == None):
        year = int(input("Escriba el año: "))
        month = int(input("Escriba el mes: "))
        print("")

    calendario = calendar.TextCalendar(calendar.SUNDAY)
    display = calendario.formatmonth(year,month)

    
    return display


print(menu())