import math
def floor_ceil(num , round_it):

    if round_it=="up":
        return math.ceil(num)
    
    elif round_it=="down":
        return math.floor(num)
    
    elif round_it=="nearest":
        return round(num)
    else:
        return ValueError("Error")

num=2.6
strategy = "down"
result=floor_ceil(num,strategy)
print(result)



