def is_leap(year):
    leap = False
    if year % 4 == 0:   
        if year % 100 == 0 and year % 400 != 0:
            leap = False
            return leap
            exit()
        leap = True 
    return leap
    
year = int(raw_input())
print is_leap(year)
