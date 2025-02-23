"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    long = len(result)
    for k in range(long):
        if k==0:
            p=1
        else:
            p=p+2    
        result.insert(p  , '@')
    return result  

print(fn_hack_9())