import random
def play_crag(money):
    keep_going = True
    count=0
    count_crag=0
   
    while (keep_going):
        # roll the three dice
        min = 1
        max = 6
        first_roll=random.randint(min, max)
        second_roll=random.randint(min, max)
        third_roll=random.randint(min, max)
      
        count=count+1
        if (first_roll==second_roll or second_roll==third_roll or third_roll==first_roll):
            money = money + 10
            count_crag=count_crag+1
            
        elif ( first_roll+second_roll+third_roll==13 ):
            money = money + 3
        elif ( first_roll == second_roll == third_roll  ):
            money = money + 2
        elif ( first_roll+2==second_roll+1==third_roll ):
            money = money + 1
        else:
            money = money - 1
        if (money <= 0):
            keep_going = False 
    print("Total Number of Dice Rolls:",count) 
    print("Total Number of Crag Rolls:",count_crag)  
            
play_crag(10)            
