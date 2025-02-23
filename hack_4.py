"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[0:len(result)-1] + result[len(result)-1:len(result)].upper()
    return result

print(fn_hack_4())