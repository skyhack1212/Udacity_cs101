# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month):
    '''
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 \
        or month_number == 8 or month_number == 10 or month_number == 12 :
        return days_in_month[0]
    elif month_number == 2:
        return days_in_month[1]
    return days_in_month[3]
    '''
    if month <= 12 and month >= 1:
    	return days_in_month[month - 1]
    return "month must be <=12 and >=1!"
print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

print how_many_days(-1)
print how_many_days(19)


