day_index = 0
month_index = 0
year = 1900
sunday_starter = 0

while year < 2001:
    month_index = 0
    while month_index < 12:
        if day_index % 7 == 6:
            if year != 1900:
                sunday_starter += 1
        
        if  month_index == 8 or month_index == 3 or month_index == 5 or month_index == 10:
            day_index += 30
        elif month_index == 1:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        day_index += 29
                    else :
                        day_index += 28
                else :
                    day_index += 29
            else :
                day_index += 28
        else :
            day_index += 31
        
        month_index += 1
    year += 1
print(sunday_starter)
