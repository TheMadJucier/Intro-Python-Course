# File: ps11pr2.py
# Author: Wadner Simon casseus@bu.edu , 8/12/22
# Description: Building a Holiday Client

from ps11pr1 import Holiday


#Function 1
def get_holidays(year):
       
        
        #For Loop for All Holidays with no set day
        ##Intialize object
        ### Check if the initialized day is the holiday
        #### run a loop to the holiday
        

        lst = []

        #New Years Day
        New_Years = Holiday(1,1,year, "New Years Day")
        if New_Years.day_name == "Sunday":
                New_Years.day = 2
                lst.append(New_Years)
        else: 
                lst.append(New_Years)

        #Martin Luther King
        Martin_Luther_King = Holiday(1,1, year, "Martin Luther King Day")
        if Martin_Luther_King.day_name() == "Monday":
                Martin_Luther_King.day = 15
                lst.append(Martin_Luther_King)
                
        else: 
                for i in range (1,8):
                        if Martin_Luther_King.day_name() == "Monday":
                                Martin_Luther_King.day = i + 14
                                lst.append(Martin_Luther_King) 
                                break
                        else: 
                                Martin_Luther_King.advance_one()

        #President's Day
        President = Holiday(2,1, year, "President's Day")
        if President.day_name() == "Monday":
                President.day = 15
                lst.append(President)
                  
        else: 
                for i in range (1,8):
                        if President.day_name() == "Monday":
                                President.day = i + 14
                                lst.append(President) 
                                break
                        else: 
                                President.advance_one()


        #Memorial Day
        Memorial = Holiday(5,1, year, "Memorial Day")
        if Memorial.day_name() == "Monday":
                Memorial.day = 29
                lst.append(Memorial)
                
        else: 
                i = 0
                while True:
                    i += 1
                    if Memorial.day_name() == "Monday":
                        if 31 - Memorial.day < 7 : #last monday
                            #Memorial.day = i
                            lst.append(Memorial) 
                            break
                        elif 31 - Memorial.day == 7: #Monday on 31st
                            Memorial.day = 31
                            lst.append(Memorial) 
                            break
                        else:
                            Memorial.day = i 
                            continue
                            
            
                    else: 
                            Memorial.advance_one()

        #Juneteenth Day
        Juneteenth = Holiday(6,19,year, "Juneteenth Day")
        if Juneteenth.day_name == "Sunday":
                Juneteenth.day = 20
                lst.append(Juneteenth)
        else: 
                lst.append(Juneteenth)

         
        #Independence Day
        Independence = Holiday(7,4,year, "Independence Day")
        if Independence.day_name == "Sunday":
                Independence.day = 5
                lst.append(Independence)
        else: 
                lst.append(Independence)


        #Labor Day -- Updated
        Labor = Holiday(9,1, year, "Labor Day")
        if Labor.day_name() == "Monday":
                lst.append(Labor)
                     
        else: 
                for i in range (1,8):
                    
                    if Labor.day_name() == "Monday":
                            Labor.day = i
                            lst.append(Labor) 
                            break
                    else: 
                            Labor.advance_one()


        #Indigenous People's Day
        Indigenous = Holiday(10,1, year, "Indigenous People's Day")
        if Indigenous.day_name() == "Monday":
                Indigenous.day += 8 
                lst.append(Indigenous)
                
        else: 
                for i in range (1,8):
                        if Indigenous.day_name() == "Monday":
                                Indigenous.day = i+7 
                                lst.append(Indigenous) 
                                break
                        else: 
                                Indigenous.advance_one()

        #Thanksgiving Day
        Thanksgiving = Holiday(11,1, year, "Thanksgiving Day")
        if Thanksgiving.day_name() == "Thursday":
                Thanksgiving.day = 21
                lst.append(Thanksgiving)
                
        else: 
                for i in range (1,8):
                        if Thanksgiving.day_name() == "Thursday":
                                Thanksgiving.day = i+21 
                                lst.append(Thanksgiving) 
                                break
                        else: 
                                Thanksgiving.advance_one()
        
        #Christams Day
        Christmas = Holiday(12,25,year, "Christmas Day")
        if Christmas.day_name == "Sunday":
                Christmas.day = 26
                lst.append(Christmas)
        else: 
                lst.append(Christmas)

        return lst
        

#get_holidays(2021)

#Function 2
def closest_holiday(date):
    """ closest_holiday(date), which will find the Holiday that is 
        closest to that parameter date, which is a Date object
    """
    holidays = []
    
    holidays = get_holidays(date.year)
    
    
    
    # Days between
    
    lst = [[holidays[x], abs(holidays[x].days_between(date))] for x in range(len(holidays))]
    #List of List of the days between the date object and the holiday
    
    lst_min = min([x[-1] for x in lst]) # choosing the lowest days between
    lst2 = [x for x in lst if x[-1] == lst_min] #chooaing the smallest value
    
    
    #print(lst)
    #print(lst_min)
    return lst2[0][0]
    
    
    
    
    
    

    





                        





        



                        


        

       
        


        
