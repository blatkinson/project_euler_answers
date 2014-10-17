# solutionTemplate(cur,end) generates a numbered set of answer blocks
# i: (num) cur = current problem number
# i: (num) end = ending problem number
# o: (str) template
def solutionTemplate(cur,end):
	# Make sure the input numbers are valid
    if cur > end:
		print "Error: The starting number needs to be less than the ending \
        number"
		return

    a = """################################################################\
    ################# """
    b = """ Q

# func"""
    c = """(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func"""
    d = """(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer"""
    e = """ = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer"""
    f = """) + "."
    return finalAnswer"""
    g = """

func"""
    h = "(0,1,1)"
    while cur <= end: # Make sure all question numbers are 3 digits long
        zero = ""
        if cur < 10:
            zero = "00"
        elif cur < 100:
            zero = "0"
        else:
            zero = ""
        # Create the tamplate
        print a + zero + str(cur) + b + zero + str(cur) + c + zero + str(cur) +\
              d + zero + str(cur) + e + zero + str(cur) + f + zero + str(cur) +\
              g + zero + str(cur) + h
        cur += 1
solutionTemplate(4,481)
################################################################################
