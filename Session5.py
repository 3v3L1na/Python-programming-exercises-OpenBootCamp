def CheckYear (year):             # Define a function with arguments using def keywords.
    if (year %4)==0:              # Return true if the year is multiple of 4
        if (year %100)==0:        # And not a multiple of 100
         if (year%400)==0:        # Or year is multiple of 400
             return True
         else:
             return False
    else: 
        return True
    else:
    return False
year=3200                       # The variable is defined as year=3200
if (CheckYear(year)):           # Value is passed to the function argument
    print ('Leap Year')         # Print 'Leap Year'
else: 
    print ('Not a Leap Year')   # If the condition is not fulfilled print 'Not a Leap Year'