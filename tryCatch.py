def safe_div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Cannot divide by 0",e)
        return None
    finally:
        print("Operation Completed")
    
print(safe_div(10,0))
        
