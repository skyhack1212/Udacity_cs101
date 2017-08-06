###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    days = 0
    new_day = day + 1
    if new_day > 30 :
        new_month = month + 1
        new_day = 1
        if new_month > 12 :
            new_year = year + 1
            new_month = 1
            return new_year, new_month, new_day
        return year, new_month, new_day
    return year, month, new_day
    
print nextDay(1999, 12, 30)
print nextDay(2013, 12, 30)
    
