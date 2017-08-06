# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def judge_year(year):
    sumDaysYears = 365
    feb = 28
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
        sumDaysYears = 366
        feb = 29
    daysOfMonths = [ 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sumDaysYears, daysOfMonths
    

def sumDays(year, month, day):
    sumDaysYears, daysOfMonths = judge_year(year)
    if month >= 2:
        i = 0
        sum1 = 0
        while i < month-1 :
            #print i
            sum1 = sum1 + daysOfMonths[i]
            i += 1
        sumDaysFromOnetoMonthDay =  sum1 + day - 1
    else :
        sumDaysFromOnetoMonthDay = day - 1
    print sumDaysFromOnetoMonthDay, sumDaysYears - sumDaysFromOnetoMonthDay
    return sumDaysFromOnetoMonthDay, sumDaysYears - sumDaysFromOnetoMonthDay


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    sum1Year1, sum2Year1 = sumDays(year1, month1, day1)
    sum1Year2, sum2Year2 = sumDays(year2, month2, day2)
    bwteenYears = year2 - year1
    if bwteenYears < 0 :
        print "year2 must > year1"
    elif bwteenYears == 0 :
        return sum1Year2
    else :
        if bwteenYears >= 2 :
            i = 0
            sumTmp = 0
            while i < bwteenYears-1 :
                sumDaysWholeYear, daysOfMonths = judge_year(year1 + i + 1) 
                sumTmp = sumTmp + sumDaysWholeYear
                i += 1
            return sum2Year1 + sum1Year2 + sumTmp
        return sum2Year1 + sum1Year2
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

