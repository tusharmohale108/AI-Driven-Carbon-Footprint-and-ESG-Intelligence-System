

def emission_calculator(activity, factor):
    try:
        result = activity*factor
        return result
    except:
        print("invalid parametrs")
        return -1
    
