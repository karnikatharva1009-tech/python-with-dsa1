#type 1
def is_leap(year):
    leap = False
    if year % 400==0:
        return True
    if year % 100==0:
        return False    
    if year %4==0:
        return True    
    return leap
year = int(input())
print(is_leap(year))

#type 2
def is_leap(year):
    return( year%4==0 and year%100!=0 or year%400==0)
year = int(input())
print(is_leap(year))