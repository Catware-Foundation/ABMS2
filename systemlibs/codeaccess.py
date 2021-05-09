
#
# Catware CodeAccess System Library
#
# It's provides a conviniently way to access to commands
#

def get_runpath_by_trigger(trig):
    global commands
    trig = str(trig)
    result = "error"
    trigs = []
    for i in commands:
        for b in i["triggers"]:
            if b == trig:
                result = b
    return result

def get_parameter_by_trigger(trig, param):
    global commands
    trig = str(trig)
    result = "error"
    for selected in commands:
        if trig in selected["triggers"]:
            result = selected[param]
    return result
