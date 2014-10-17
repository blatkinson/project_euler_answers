# 20140923
# ProjectEuler.net Solutions
################################################################################
# 001 Find the sum of all the multiples of 3 or 5 below 1000.

# tripleQuintupleSummer adds all the triples and quintuples between two values
# i: (num) lowerBound = number to start with
# i: (num) upperBound = number not to exceed
# o: (str) set of generated multiples
# o: (num) sum of generated multiples
# r: (num) sum of generated multiples
def tripleQuintupleSummer(lowerBound,upperBound):
	n = lowerBound
	s = []
	t = 0
	while n < upperBound:
		if n % 3 == 0 or n % 5 == 0:
			s.append(n)
			t += n
		n += 1
	print "The set of multiples of 3 and 5 between 1 and 1000 is: " + str(s)
	print "The sum of this set is " + str(t)
	return t
################################################################################
# 002 By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

# basicFib() takes two initializing numbers and runs the Fib sequence
# until it reaches the highest Fib number below the upper limit
# i: (num) first = number of the first Fib number
# i: (num) second = number of the second Fib number
# i: (num) upperLimit = max value of highest Fib number
# i: (num) l = if feedback is printed to the console (not for debugging)
#          (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
# o: (str) prints the fib numbers in the current sequence
# r: (num) max value for the upper fib number
def basicFib(first,second,upperLimit,l,d):
    curTot = 0 # Initialize the current total
    if second < first:
        if l > 0: print "The second input is less than the first, adjusting ..."
        first,second = second,first
    if first + second < upperLimit: # Start the Fib sequence
        currTot = first + second
    elif first > upperLimit: # Make sure the first isn't bigger than upperLimit
        if d > 0: print "Debug: There is an error. The first input number is \
        already greater than the upper limit. Aborting"
        return
    elif second > upperLimit and d > 0: # Do the same for the second number
        if d > 0: print "Debug: There is an error. The second input number is \
        already greater than the upper limit. Aborting"
        return
    else:
        if d > 0: print "Debug: There was an unknown error."
        return

    # Fib number generator
    fibSet = [first,second,currTot] # Create array to store fib numbers
    a = first # Switch variables for more coherent code
    b = second
    while currTot + b <= upperLimit: # Run the rest of the fib sequence
        currTot += b
        fibSet.append(currTot)
        a = b
        b = currTot - b

    # Report builder
    evnTot = 0 # Create var for final summation
    print "Fib numbers = " + str(fibSet)
    for n in fibSet: # Add all generated fib numbers together
        if n % 2 == 0:
            evnTot += n
            if l > 0:
                print evnTot # Write out fib numbers
                             # ** Caution, this could backfire
    print "The sum = " + str(evnTot)
    return evnTot

basicFib(1,2,4000000,1,1)
################################################################################
# 003 What is the largest prime factor of the number 600851475143?

from __future__ import division

# isPrime(i) returns true/false if a number is a prime
# i: (num) i = number to be tested
# r: (boo)
def isPrime(n):
    t = n - 1 # Test for factors starting (desc)
    while t > 1:
        if n % t == 0:
            return False
        elif t == 2:
            return True
        t -= 1

# lowestFactor(i) returns the lowest factor of the input number, or, if the
# number has no factors, returns 0
# i: (num) i = input number
# r: (num)   = lowest factor of input number
def lowestFactor(n):
    t = 2 # Lowest possible prime is 2
    if isPrime(n):
        print str(n) + " is prime. Returning 0"
        return 0
    while t < n:
        if n % t == 0: # ... test for factors (asc)
            return t
        else:
            t += 1

# highestFactor(i) completely factors the input number and returns the highest
# factor of the input number, or if the number has no primes, returns 0
# i: (num) i = input number
# o: (str)   = warning if input number has no factors
# r: (num)   = highest factor
def highestFactor(n):
    f = []
    if isPrime(n):
        return str(n) + " is a prime number."
    while lowestFactor(n) > 0:
        f.append(lowestFactor(n))
        n = n / lowestFactor(n)
    f.sort()
    return f[len(f) - 1]

print highestFactor(600851475143)
################################################################################
# 004 Q A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the
# largest palindrome made from the product of two 3-digit numbers.

# func004(i,c,d) takes an number as a length, and finds the largest palindromic
# number the is the result of the product of two numbers of length i
# i: (num) i = length of numbers to be multiplied
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the largest palindromic product of two num of length i
# r: (num) returns the largest palindromic product of two num of length i
def func004(i,c,d):
    # Make sure the input value is valid
    if i < 1:
        if c > 0: # If logging to console is turned on
            print str(i) + " is non-positive. Please try another length."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing non-positive numbers may break this function"

    tempAnswer, tempA, tempB = 0, 0, 0 # Initialize temp value holders
    a = (10**i) - 1 # Initialize first test number with highest value
    while a >= 10**(i-1):
        b = (10**i) - 1 # Reset second test number with each pass
        while b >= 10**(i-1):
            print str(a) + " * " + str(b) + " = " + str(a * b)
            print "Reversed: " + str(a * b)[::-1]
            if str(a * b) == str(a * b)[::-1]:
                if int(a * b) > tempAnswer:
                    tempA = a
                    tempB = b
                    tempAnswer = (a * b)
            b -= 1
        a -= 1
    print str(a) + "*" + str(b) + " is the palindrome " + str(a * b)
    finalAnswer004 = (a * b)
    return finalAnswer004

    print "The final answer is " + str(finalAnswer004) + "."
    return finalAnswer004

func004(3,1,1)
################################################################################
# 005 Q

# func005(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func005(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer005 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer005) + "."
    return finalAnswer005

func005(0,1,1)
################################################################################
# 006 Q

# func006(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func006(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer006 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer006) + "."
    return finalAnswer006

func006(0,1,1)
################################################################################
# 007 Q

# func007(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func007(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer007 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer007) + "."
    return finalAnswer007

func007(0,1,1)
################################################################################
# 008 Q

# func008(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func008(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer008 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer008) + "."
    return finalAnswer008

func008(0,1,1)
################################################################################
# 009 Q

# func009(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func009(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer009 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer009) + "."
    return finalAnswer009

func009(0,1,1)
################################################################################
# 010 Q

# func010(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func010(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer010 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer010) + "."
    return finalAnswer010

func010(0,1,1)
################################################################################
# 011 Q

# func011(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func011(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer011 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer011) + "."
    return finalAnswer011

func011(0,1,1)
################################################################################
# 012 Q

# func012(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func012(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer012 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer012) + "."
    return finalAnswer012

func012(0,1,1)
################################################################################
# 013 Q

# func013(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func013(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer013 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer013) + "."
    return finalAnswer013

func013(0,1,1)
################################################################################
# 014 Q

# func014(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func014(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer014 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer014) + "."
    return finalAnswer014

func014(0,1,1)
################################################################################
# 015 Q

# func015(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func015(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer015 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer015) + "."
    return finalAnswer015

func015(0,1,1)
################################################################################
# 016 Q

# func016(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func016(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer016 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer016) + "."
    return finalAnswer016

func016(0,1,1)
################################################################################
# 017 Q

# func017(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func017(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer017 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer017) + "."
    return finalAnswer017

func017(0,1,1)
################################################################################
# 018 Q

# func018(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func018(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer018 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer018) + "."
    return finalAnswer018

func018(0,1,1)
################################################################################
# 019 Q

# func019(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func019(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer019 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer019) + "."
    return finalAnswer019

func019(0,1,1)
################################################################################
# 020 Q

# func020(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func020(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer020 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer020) + "."
    return finalAnswer020

func020(0,1,1)
################################################################################
# 021 Q

# func021(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func021(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer021 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer021) + "."
    return finalAnswer021

func021(0,1,1)
################################################################################
# 022 Q

# func022(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func022(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer022 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer022) + "."
    return finalAnswer022

func022(0,1,1)
################################################################################
# 023 Q

# func023(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func023(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer023 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer023) + "."
    return finalAnswer023

func023(0,1,1)
################################################################################
# 024 Q

# func024(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func024(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer024 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer024) + "."
    return finalAnswer024

func024(0,1,1)
################################################################################
# 025 Q

# func025(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func025(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer025 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer025) + "."
    return finalAnswer025

func025(0,1,1)
################################################################################
# 026 Q

# func026(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func026(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer026 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer026) + "."
    return finalAnswer026

func026(0,1,1)
################################################################################
# 027 Q

# func027(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func027(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer027 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer027) + "."
    return finalAnswer027

func027(0,1,1)
################################################################################
# 028 Q

# func028(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func028(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer028 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer028) + "."
    return finalAnswer028

func028(0,1,1)
################################################################################
# 029 Q

# func029(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func029(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer029 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer029) + "."
    return finalAnswer029

func029(0,1,1)
################################################################################
# 030 Q

# func030(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func030(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer030 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer030) + "."
    return finalAnswer030

func030(0,1,1)
################################################################################
# 031 Q

# func031(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func031(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer031 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer031) + "."
    return finalAnswer031

func031(0,1,1)
################################################################################
# 032 Q

# func032(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func032(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer032 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer032) + "."
    return finalAnswer032

func032(0,1,1)
################################################################################
# 033 Q

# func033(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func033(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer033 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer033) + "."
    return finalAnswer033

func033(0,1,1)
################################################################################
# 034 Q

# func034(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func034(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer034 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer034) + "."
    return finalAnswer034

func034(0,1,1)
################################################################################
# 035 Q

# func035(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func035(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer035 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer035) + "."
    return finalAnswer035

func035(0,1,1)
################################################################################
# 036 Q

# func036(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func036(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer036 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer036) + "."
    return finalAnswer036

func036(0,1,1)
################################################################################
# 037 Q

# func037(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func037(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer037 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer037) + "."
    return finalAnswer037

func037(0,1,1)
################################################################################
# 038 Q

# func038(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func038(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer038 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer038) + "."
    return finalAnswer038

func038(0,1,1)
################################################################################
# 039 Q

# func039(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func039(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer039 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer039) + "."
    return finalAnswer039

func039(0,1,1)
################################################################################
# 040 Q

# func040(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func040(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer040 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer040) + "."
    return finalAnswer040

func040(0,1,1)
################################################################################
# 041 Q

# func041(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func041(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer041 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer041) + "."
    return finalAnswer041

func041(0,1,1)
################################################################################
# 042 Q

# func042(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func042(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer042 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer042) + "."
    return finalAnswer042

func042(0,1,1)
################################################################################
# 043 Q

# func043(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func043(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer043 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer043) + "."
    return finalAnswer043

func043(0,1,1)
################################################################################
# 044 Q

# func044(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func044(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer044 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer044) + "."
    return finalAnswer044

func044(0,1,1)
################################################################################
# 045 Q

# func045(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func045(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer045 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer045) + "."
    return finalAnswer045

func045(0,1,1)
################################################################################
# 046 Q

# func046(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func046(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer046 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer046) + "."
    return finalAnswer046

func046(0,1,1)
################################################################################
# 047 Q

# func047(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func047(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer047 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer047) + "."
    return finalAnswer047

func047(0,1,1)
################################################################################
# 048 Q

# func048(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func048(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer048 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer048) + "."
    return finalAnswer048

func048(0,1,1)
################################################################################
# 049 Q

# func049(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func049(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer049 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer049) + "."
    return finalAnswer049

func049(0,1,1)
################################################################################
# 050 Q

# func050(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func050(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer050 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer050) + "."
    return finalAnswer050

func050(0,1,1)
################################################################################
# 051 Q

# func051(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func051(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer051 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer051) + "."
    return finalAnswer051

func051(0,1,1)
################################################################################
# 052 Q

# func052(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func052(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer052 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer052) + "."
    return finalAnswer052

func052(0,1,1)
################################################################################
# 053 Q

# func053(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func053(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer053 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer053) + "."
    return finalAnswer053

func053(0,1,1)
################################################################################
# 054 Q

# func054(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func054(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer054 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer054) + "."
    return finalAnswer054

func054(0,1,1)
################################################################################
# 055 Q

# func055(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func055(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer055 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer055) + "."
    return finalAnswer055

func055(0,1,1)
################################################################################
# 056 Q

# func056(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func056(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer056 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer056) + "."
    return finalAnswer056

func056(0,1,1)
################################################################################
# 057 Q

# func057(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func057(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer057 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer057) + "."
    return finalAnswer057

func057(0,1,1)
################################################################################
# 058 Q

# func058(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func058(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer058 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer058) + "."
    return finalAnswer058

func058(0,1,1)
################################################################################
# 059 Q

# func059(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func059(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer059 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer059) + "."
    return finalAnswer059

func059(0,1,1)
################################################################################
# 060 Q

# func060(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func060(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer060 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer060) + "."
    return finalAnswer060

func060(0,1,1)
################################################################################
# 061 Q

# func061(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func061(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer061 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer061) + "."
    return finalAnswer061

func061(0,1,1)
################################################################################
# 062 Q

# func062(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func062(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer062 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer062) + "."
    return finalAnswer062

func062(0,1,1)
################################################################################
# 063 Q

# func063(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func063(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer063 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer063) + "."
    return finalAnswer063

func063(0,1,1)
################################################################################
# 064 Q

# func064(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func064(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer064 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer064) + "."
    return finalAnswer064

func064(0,1,1)
################################################################################
# 065 Q

# func065(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func065(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer065 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer065) + "."
    return finalAnswer065

func065(0,1,1)
################################################################################
# 066 Q

# func066(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func066(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer066 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer066) + "."
    return finalAnswer066

func066(0,1,1)
################################################################################
# 067 Q

# func067(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func067(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer067 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer067) + "."
    return finalAnswer067

func067(0,1,1)
################################################################################
# 068 Q

# func068(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func068(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer068 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer068) + "."
    return finalAnswer068

func068(0,1,1)
################################################################################
# 069 Q

# func069(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func069(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer069 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer069) + "."
    return finalAnswer069

func069(0,1,1)
################################################################################
# 070 Q

# func070(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func070(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer070 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer070) + "."
    return finalAnswer070

func070(0,1,1)
################################################################################
# 071 Q

# func071(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func071(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer071 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer071) + "."
    return finalAnswer071

func071(0,1,1)
################################################################################
# 072 Q

# func072(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func072(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer072 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer072) + "."
    return finalAnswer072

func072(0,1,1)
################################################################################
# 073 Q

# func073(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func073(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer073 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer073) + "."
    return finalAnswer073

func073(0,1,1)
################################################################################
# 074 Q

# func074(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func074(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer074 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer074) + "."
    return finalAnswer074

func074(0,1,1)
################################################################################
# 075 Q

# func075(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func075(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer075 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer075) + "."
    return finalAnswer075

func075(0,1,1)
################################################################################
# 076 Q

# func076(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func076(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer076 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer076) + "."
    return finalAnswer076

func076(0,1,1)
################################################################################
# 077 Q

# func077(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func077(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer077 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer077) + "."
    return finalAnswer077

func077(0,1,1)
################################################################################
# 078 Q

# func078(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func078(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer078 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer078) + "."
    return finalAnswer078

func078(0,1,1)
################################################################################
# 079 Q

# func079(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func079(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer079 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer079) + "."
    return finalAnswer079

func079(0,1,1)
################################################################################
# 080 Q

# func080(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func080(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer080 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer080) + "."
    return finalAnswer080

func080(0,1,1)
################################################################################
# 081 Q

# func081(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func081(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer081 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer081) + "."
    return finalAnswer081

func081(0,1,1)
################################################################################
# 082 Q

# func082(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func082(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer082 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer082) + "."
    return finalAnswer082

func082(0,1,1)
################################################################################
# 083 Q

# func083(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func083(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer083 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer083) + "."
    return finalAnswer083

func083(0,1,1)
################################################################################
# 084 Q

# func084(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func084(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer084 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer084) + "."
    return finalAnswer084

func084(0,1,1)
################################################################################
# 085 Q

# func085(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func085(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer085 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer085) + "."
    return finalAnswer085

func085(0,1,1)
################################################################################
# 086 Q

# func086(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func086(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer086 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer086) + "."
    return finalAnswer086

func086(0,1,1)
################################################################################
# 087 Q

# func087(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func087(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer087 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer087) + "."
    return finalAnswer087

func087(0,1,1)
################################################################################
# 088 Q

# func088(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func088(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer088 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer088) + "."
    return finalAnswer088

func088(0,1,1)
################################################################################
# 089 Q

# func089(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func089(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer089 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer089) + "."
    return finalAnswer089

func089(0,1,1)
################################################################################
# 090 Q

# func090(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func090(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer090 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer090) + "."
    return finalAnswer090

func090(0,1,1)
################################################################################
# 091 Q

# func091(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func091(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer091 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer091) + "."
    return finalAnswer091

func091(0,1,1)
################################################################################
# 092 Q

# func092(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func092(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer092 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer092) + "."
    return finalAnswer092

func092(0,1,1)
################################################################################
# 093 Q

# func093(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func093(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer093 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer093) + "."
    return finalAnswer093

func093(0,1,1)
################################################################################
# 094 Q

# func094(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func094(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer094 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer094) + "."
    return finalAnswer094

func094(0,1,1)
################################################################################
# 095 Q

# func095(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func095(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer095 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer095) + "."
    return finalAnswer095

func095(0,1,1)
################################################################################
# 096 Q

# func096(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func096(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer096 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer096) + "."
    return finalAnswer096

func096(0,1,1)
################################################################################
# 097 Q

# func097(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func097(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer097 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer097) + "."
    return finalAnswer097

func097(0,1,1)
################################################################################
# 098 Q

# func098(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func098(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer098 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer098) + "."
    return finalAnswer098

func098(0,1,1)
################################################################################
# 099 Q

# func099(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func099(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer099 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer099) + "."
    return finalAnswer099

func099(0,1,1)
################################################################################
# 100 Q

# func100(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func100(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer100 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer100) + "."
    return finalAnswer100

func100(0,1,1)
################################################################################
# 101 Q

# func101(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func101(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer101 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer101) + "."
    return finalAnswer101

func101(0,1,1)
################################################################################
# 102 Q

# func102(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func102(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer102 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer102) + "."
    return finalAnswer102

func102(0,1,1)
################################################################################
# 103 Q

# func103(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func103(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer103 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer103) + "."
    return finalAnswer103

func103(0,1,1)
################################################################################
# 104 Q

# func104(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func104(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer104 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer104) + "."
    return finalAnswer104

func104(0,1,1)
################################################################################
# 105 Q

# func105(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func105(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer105 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer105) + "."
    return finalAnswer105

func105(0,1,1)
################################################################################
# 106 Q

# func106(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func106(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer106 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer106) + "."
    return finalAnswer106

func106(0,1,1)
################################################################################
# 107 Q

# func107(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func107(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer107 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer107) + "."
    return finalAnswer107

func107(0,1,1)
################################################################################
# 108 Q

# func108(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func108(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer108 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer108) + "."
    return finalAnswer108

func108(0,1,1)
################################################################################
# 109 Q

# func109(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func109(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer109 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer109) + "."
    return finalAnswer109

func109(0,1,1)
################################################################################
# 110 Q

# func110(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func110(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer110 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer110) + "."
    return finalAnswer110

func110(0,1,1)
################################################################################
# 111 Q

# func111(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func111(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer111 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer111) + "."
    return finalAnswer111

func111(0,1,1)
################################################################################
# 112 Q

# func112(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func112(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer112 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer112) + "."
    return finalAnswer112

func112(0,1,1)
################################################################################
# 113 Q

# func113(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func113(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer113 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer113) + "."
    return finalAnswer113

func113(0,1,1)
################################################################################
# 114 Q

# func114(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func114(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer114 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer114) + "."
    return finalAnswer114

func114(0,1,1)
################################################################################
# 115 Q

# func115(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func115(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer115 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer115) + "."
    return finalAnswer115

func115(0,1,1)
################################################################################
# 116 Q

# func116(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func116(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer116 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer116) + "."
    return finalAnswer116

func116(0,1,1)
################################################################################
# 117 Q

# func117(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func117(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer117 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer117) + "."
    return finalAnswer117

func117(0,1,1)
################################################################################
# 118 Q

# func118(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func118(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer118 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer118) + "."
    return finalAnswer118

func118(0,1,1)
################################################################################
# 119 Q

# func119(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func119(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer119 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer119) + "."
    return finalAnswer119

func119(0,1,1)
################################################################################
# 120 Q

# func120(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func120(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer120 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer120) + "."
    return finalAnswer120

func120(0,1,1)
################################################################################
# 121 Q

# func121(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func121(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer121 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer121) + "."
    return finalAnswer121

func121(0,1,1)
################################################################################
# 122 Q

# func122(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func122(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer122 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer122) + "."
    return finalAnswer122

func122(0,1,1)
################################################################################
# 123 Q

# func123(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func123(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer123 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer123) + "."
    return finalAnswer123

func123(0,1,1)
################################################################################
# 124 Q

# func124(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func124(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer124 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer124) + "."
    return finalAnswer124

func124(0,1,1)
################################################################################
# 125 Q

# func125(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func125(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer125 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer125) + "."
    return finalAnswer125

func125(0,1,1)
################################################################################
# 126 Q

# func126(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func126(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer126 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer126) + "."
    return finalAnswer126

func126(0,1,1)
################################################################################
# 127 Q

# func127(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func127(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer127 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer127) + "."
    return finalAnswer127

func127(0,1,1)
################################################################################
# 128 Q

# func128(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func128(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer128 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer128) + "."
    return finalAnswer128

func128(0,1,1)
################################################################################
# 129 Q

# func129(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func129(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer129 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer129) + "."
    return finalAnswer129

func129(0,1,1)
################################################################################
# 130 Q

# func130(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func130(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer130 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer130) + "."
    return finalAnswer130

func130(0,1,1)
################################################################################
# 131 Q

# func131(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func131(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer131 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer131) + "."
    return finalAnswer131

func131(0,1,1)
################################################################################
# 132 Q

# func132(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func132(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer132 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer132) + "."
    return finalAnswer132

func132(0,1,1)
################################################################################
# 133 Q

# func133(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func133(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer133 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer133) + "."
    return finalAnswer133

func133(0,1,1)
################################################################################
# 134 Q

# func134(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func134(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer134 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer134) + "."
    return finalAnswer134

func134(0,1,1)
################################################################################
# 135 Q

# func135(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func135(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer135 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer135) + "."
    return finalAnswer135

func135(0,1,1)
################################################################################
# 136 Q

# func136(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func136(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer136 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer136) + "."
    return finalAnswer136

func136(0,1,1)
################################################################################
# 137 Q

# func137(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func137(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer137 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer137) + "."
    return finalAnswer137

func137(0,1,1)
################################################################################
# 138 Q

# func138(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func138(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer138 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer138) + "."
    return finalAnswer138

func138(0,1,1)
################################################################################
# 139 Q

# func139(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func139(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer139 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer139) + "."
    return finalAnswer139

func139(0,1,1)
################################################################################
# 140 Q

# func140(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func140(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer140 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer140) + "."
    return finalAnswer140

func140(0,1,1)
################################################################################
# 141 Q

# func141(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func141(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer141 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer141) + "."
    return finalAnswer141

func141(0,1,1)
################################################################################
# 142 Q

# func142(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func142(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer142 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer142) + "."
    return finalAnswer142

func142(0,1,1)
################################################################################
# 143 Q

# func143(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func143(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer143 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer143) + "."
    return finalAnswer143

func143(0,1,1)
################################################################################
# 144 Q

# func144(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func144(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer144 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer144) + "."
    return finalAnswer144

func144(0,1,1)
################################################################################
# 145 Q

# func145(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func145(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer145 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer145) + "."
    return finalAnswer145

func145(0,1,1)
################################################################################
# 146 Q

# func146(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func146(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer146 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer146) + "."
    return finalAnswer146

func146(0,1,1)
################################################################################
# 147 Q

# func147(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func147(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer147 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer147) + "."
    return finalAnswer147

func147(0,1,1)
################################################################################
# 148 Q

# func148(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func148(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer148 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer148) + "."
    return finalAnswer148

func148(0,1,1)
################################################################################
# 149 Q

# func149(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func149(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer149 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer149) + "."
    return finalAnswer149

func149(0,1,1)
################################################################################
# 150 Q

# func150(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func150(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer150 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer150) + "."
    return finalAnswer150

func150(0,1,1)
################################################################################
# 151 Q

# func151(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func151(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer151 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer151) + "."
    return finalAnswer151

func151(0,1,1)
################################################################################
# 152 Q

# func152(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func152(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer152 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer152) + "."
    return finalAnswer152

func152(0,1,1)
################################################################################
# 153 Q

# func153(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func153(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer153 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer153) + "."
    return finalAnswer153

func153(0,1,1)
################################################################################
# 154 Q

# func154(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func154(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer154 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer154) + "."
    return finalAnswer154

func154(0,1,1)
################################################################################
# 155 Q

# func155(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func155(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer155 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer155) + "."
    return finalAnswer155

func155(0,1,1)
################################################################################
# 156 Q

# func156(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func156(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer156 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer156) + "."
    return finalAnswer156

func156(0,1,1)
################################################################################
# 157 Q

# func157(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func157(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer157 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer157) + "."
    return finalAnswer157

func157(0,1,1)
################################################################################
# 158 Q

# func158(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func158(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer158 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer158) + "."
    return finalAnswer158

func158(0,1,1)
################################################################################
# 159 Q

# func159(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func159(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer159 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer159) + "."
    return finalAnswer159

func159(0,1,1)
################################################################################
# 160 Q

# func160(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func160(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer160 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer160) + "."
    return finalAnswer160

func160(0,1,1)
################################################################################
# 161 Q

# func161(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func161(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer161 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer161) + "."
    return finalAnswer161

func161(0,1,1)
################################################################################
# 162 Q

# func162(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func162(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer162 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer162) + "."
    return finalAnswer162

func162(0,1,1)
################################################################################
# 163 Q

# func163(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func163(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer163 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer163) + "."
    return finalAnswer163

func163(0,1,1)
################################################################################
# 164 Q

# func164(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func164(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer164 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer164) + "."
    return finalAnswer164

func164(0,1,1)
################################################################################
# 165 Q

# func165(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func165(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer165 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer165) + "."
    return finalAnswer165

func165(0,1,1)
################################################################################
# 166 Q

# func166(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func166(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer166 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer166) + "."
    return finalAnswer166

func166(0,1,1)
################################################################################
# 167 Q

# func167(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func167(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer167 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer167) + "."
    return finalAnswer167

func167(0,1,1)
################################################################################
# 168 Q

# func168(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func168(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer168 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer168) + "."
    return finalAnswer168

func168(0,1,1)
################################################################################
# 169 Q

# func169(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func169(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer169 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer169) + "."
    return finalAnswer169

func169(0,1,1)
################################################################################
# 170 Q

# func170(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func170(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer170 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer170) + "."
    return finalAnswer170

func170(0,1,1)
################################################################################
# 171 Q

# func171(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func171(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer171 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer171) + "."
    return finalAnswer171

func171(0,1,1)
################################################################################
# 172 Q

# func172(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func172(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer172 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer172) + "."
    return finalAnswer172

func172(0,1,1)
################################################################################
# 173 Q

# func173(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func173(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer173 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer173) + "."
    return finalAnswer173

func173(0,1,1)
################################################################################
# 174 Q

# func174(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func174(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer174 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer174) + "."
    return finalAnswer174

func174(0,1,1)
################################################################################
# 175 Q

# func175(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func175(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer175 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer175) + "."
    return finalAnswer175

func175(0,1,1)
################################################################################
# 176 Q

# func176(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func176(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer176 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer176) + "."
    return finalAnswer176

func176(0,1,1)
################################################################################
# 177 Q

# func177(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func177(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer177 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer177) + "."
    return finalAnswer177

func177(0,1,1)
################################################################################
# 178 Q

# func178(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func178(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer178 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer178) + "."
    return finalAnswer178

func178(0,1,1)
################################################################################
# 179 Q

# func179(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func179(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer179 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer179) + "."
    return finalAnswer179

func179(0,1,1)
################################################################################
# 180 Q

# func180(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func180(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer180 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer180) + "."
    return finalAnswer180

func180(0,1,1)
################################################################################
# 181 Q

# func181(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func181(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer181 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer181) + "."
    return finalAnswer181

func181(0,1,1)
################################################################################
# 182 Q

# func182(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func182(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer182 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer182) + "."
    return finalAnswer182

func182(0,1,1)
################################################################################
# 183 Q

# func183(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func183(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer183 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer183) + "."
    return finalAnswer183

func183(0,1,1)
################################################################################
# 184 Q

# func184(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func184(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer184 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer184) + "."
    return finalAnswer184

func184(0,1,1)
################################################################################
# 185 Q

# func185(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func185(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer185 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer185) + "."
    return finalAnswer185

func185(0,1,1)
################################################################################
# 186 Q

# func186(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func186(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer186 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer186) + "."
    return finalAnswer186

func186(0,1,1)
################################################################################
# 187 Q

# func187(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func187(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer187 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer187) + "."
    return finalAnswer187

func187(0,1,1)
################################################################################
# 188 Q

# func188(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func188(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer188 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer188) + "."
    return finalAnswer188

func188(0,1,1)
################################################################################
# 189 Q

# func189(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func189(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer189 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer189) + "."
    return finalAnswer189

func189(0,1,1)
################################################################################
# 190 Q

# func190(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func190(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer190 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer190) + "."
    return finalAnswer190

func190(0,1,1)
################################################################################
# 191 Q

# func191(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func191(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer191 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer191) + "."
    return finalAnswer191

func191(0,1,1)
################################################################################
# 192 Q

# func192(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func192(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer192 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer192) + "."
    return finalAnswer192

func192(0,1,1)
################################################################################
# 193 Q

# func193(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func193(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer193 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer193) + "."
    return finalAnswer193

func193(0,1,1)
################################################################################
# 194 Q

# func194(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func194(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer194 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer194) + "."
    return finalAnswer194

func194(0,1,1)
################################################################################
# 195 Q

# func195(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func195(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer195 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer195) + "."
    return finalAnswer195

func195(0,1,1)
################################################################################
# 196 Q

# func196(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func196(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer196 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer196) + "."
    return finalAnswer196

func196(0,1,1)
################################################################################
# 197 Q

# func197(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func197(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer197 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer197) + "."
    return finalAnswer197

func197(0,1,1)
################################################################################
# 198 Q

# func198(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func198(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer198 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer198) + "."
    return finalAnswer198

func198(0,1,1)
################################################################################
# 199 Q

# func199(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func199(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer199 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer199) + "."
    return finalAnswer199

func199(0,1,1)
################################################################################
# 200 Q

# func200(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func200(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer200 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer200) + "."
    return finalAnswer200

func200(0,1,1)
################################################################################
# 201 Q

# func201(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func201(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer201 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer201) + "."
    return finalAnswer201

func201(0,1,1)
################################################################################
# 202 Q

# func202(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func202(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer202 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer202) + "."
    return finalAnswer202

func202(0,1,1)
################################################################################
# 203 Q

# func203(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func203(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer203 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer203) + "."
    return finalAnswer203

func203(0,1,1)
################################################################################
# 204 Q

# func204(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func204(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer204 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer204) + "."
    return finalAnswer204

func204(0,1,1)
################################################################################
# 205 Q

# func205(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func205(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer205 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer205) + "."
    return finalAnswer205

func205(0,1,1)
################################################################################
# 206 Q

# func206(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func206(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer206 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer206) + "."
    return finalAnswer206

func206(0,1,1)
################################################################################
# 207 Q

# func207(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func207(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer207 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer207) + "."
    return finalAnswer207

func207(0,1,1)
################################################################################
# 208 Q

# func208(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func208(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer208 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer208) + "."
    return finalAnswer208

func208(0,1,1)
################################################################################
# 209 Q

# func209(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func209(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer209 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer209) + "."
    return finalAnswer209

func209(0,1,1)
################################################################################
# 210 Q

# func210(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func210(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer210 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer210) + "."
    return finalAnswer210

func210(0,1,1)
################################################################################
# 211 Q

# func211(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func211(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer211 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer211) + "."
    return finalAnswer211

func211(0,1,1)
################################################################################
# 212 Q

# func212(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func212(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer212 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer212) + "."
    return finalAnswer212

func212(0,1,1)
################################################################################
# 213 Q

# func213(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func213(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer213 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer213) + "."
    return finalAnswer213

func213(0,1,1)
################################################################################
# 214 Q

# func214(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func214(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer214 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer214) + "."
    return finalAnswer214

func214(0,1,1)
################################################################################
# 215 Q

# func215(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func215(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer215 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer215) + "."
    return finalAnswer215

func215(0,1,1)
################################################################################
# 216 Q

# func216(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func216(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer216 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer216) + "."
    return finalAnswer216

func216(0,1,1)
################################################################################
# 217 Q

# func217(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func217(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer217 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer217) + "."
    return finalAnswer217

func217(0,1,1)
################################################################################
# 218 Q

# func218(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func218(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer218 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer218) + "."
    return finalAnswer218

func218(0,1,1)
################################################################################
# 219 Q

# func219(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func219(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer219 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer219) + "."
    return finalAnswer219

func219(0,1,1)
################################################################################
# 220 Q

# func220(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func220(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer220 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer220) + "."
    return finalAnswer220

func220(0,1,1)
################################################################################
# 221 Q

# func221(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func221(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer221 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer221) + "."
    return finalAnswer221

func221(0,1,1)
################################################################################
# 222 Q

# func222(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func222(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer222 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer222) + "."
    return finalAnswer222

func222(0,1,1)
################################################################################
# 223 Q

# func223(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func223(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer223 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer223) + "."
    return finalAnswer223

func223(0,1,1)
################################################################################
# 224 Q

# func224(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func224(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer224 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer224) + "."
    return finalAnswer224

func224(0,1,1)
################################################################################
# 225 Q

# func225(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func225(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer225 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer225) + "."
    return finalAnswer225

func225(0,1,1)
################################################################################
# 226 Q

# func226(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func226(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer226 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer226) + "."
    return finalAnswer226

func226(0,1,1)
################################################################################
# 227 Q

# func227(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func227(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer227 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer227) + "."
    return finalAnswer227

func227(0,1,1)
################################################################################
# 228 Q

# func228(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func228(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer228 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer228) + "."
    return finalAnswer228

func228(0,1,1)
################################################################################
# 229 Q

# func229(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func229(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer229 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer229) + "."
    return finalAnswer229

func229(0,1,1)
################################################################################
# 230 Q

# func230(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func230(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer230 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer230) + "."
    return finalAnswer230

func230(0,1,1)
################################################################################
# 231 Q

# func231(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func231(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer231 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer231) + "."
    return finalAnswer231

func231(0,1,1)
################################################################################
# 232 Q

# func232(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func232(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer232 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer232) + "."
    return finalAnswer232

func232(0,1,1)
################################################################################
# 233 Q

# func233(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func233(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer233 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer233) + "."
    return finalAnswer233

func233(0,1,1)
################################################################################
# 234 Q

# func234(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func234(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer234 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer234) + "."
    return finalAnswer234

func234(0,1,1)
################################################################################
# 235 Q

# func235(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func235(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer235 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer235) + "."
    return finalAnswer235

func235(0,1,1)
################################################################################
# 236 Q

# func236(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func236(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer236 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer236) + "."
    return finalAnswer236

func236(0,1,1)
################################################################################
# 237 Q

# func237(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func237(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer237 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer237) + "."
    return finalAnswer237

func237(0,1,1)
################################################################################
# 238 Q

# func238(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func238(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer238 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer238) + "."
    return finalAnswer238

func238(0,1,1)
################################################################################
# 239 Q

# func239(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func239(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer239 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer239) + "."
    return finalAnswer239

func239(0,1,1)
################################################################################
# 240 Q

# func240(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func240(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer240 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer240) + "."
    return finalAnswer240

func240(0,1,1)
################################################################################
# 241 Q

# func241(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func241(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer241 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer241) + "."
    return finalAnswer241

func241(0,1,1)
################################################################################
# 242 Q

# func242(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func242(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer242 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer242) + "."
    return finalAnswer242

func242(0,1,1)
################################################################################
# 243 Q

# func243(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func243(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer243 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer243) + "."
    return finalAnswer243

func243(0,1,1)
################################################################################
# 244 Q

# func244(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func244(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer244 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer244) + "."
    return finalAnswer244

func244(0,1,1)
################################################################################
# 245 Q

# func245(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func245(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer245 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer245) + "."
    return finalAnswer245

func245(0,1,1)
################################################################################
# 246 Q

# func246(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func246(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer246 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer246) + "."
    return finalAnswer246

func246(0,1,1)
################################################################################
# 247 Q

# func247(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func247(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer247 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer247) + "."
    return finalAnswer247

func247(0,1,1)
################################################################################
# 248 Q

# func248(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func248(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer248 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer248) + "."
    return finalAnswer248

func248(0,1,1)
################################################################################
# 249 Q

# func249(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func249(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer249 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer249) + "."
    return finalAnswer249

func249(0,1,1)
################################################################################
# 250 Q

# func250(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func250(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer250 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer250) + "."
    return finalAnswer250

func250(0,1,1)
################################################################################
# 251 Q

# func251(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func251(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer251 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer251) + "."
    return finalAnswer251

func251(0,1,1)
################################################################################
# 252 Q

# func252(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func252(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer252 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer252) + "."
    return finalAnswer252

func252(0,1,1)
################################################################################
# 253 Q

# func253(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func253(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer253 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer253) + "."
    return finalAnswer253

func253(0,1,1)
################################################################################
# 254 Q

# func254(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func254(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer254 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer254) + "."
    return finalAnswer254

func254(0,1,1)
################################################################################
# 255 Q

# func255(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func255(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer255 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer255) + "."
    return finalAnswer255

func255(0,1,1)
################################################################################
# 256 Q

# func256(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func256(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer256 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer256) + "."
    return finalAnswer256

func256(0,1,1)
################################################################################
# 257 Q

# func257(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func257(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer257 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer257) + "."
    return finalAnswer257

func257(0,1,1)
################################################################################
# 258 Q

# func258(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func258(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer258 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer258) + "."
    return finalAnswer258

func258(0,1,1)
################################################################################
# 259 Q

# func259(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func259(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer259 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer259) + "."
    return finalAnswer259

func259(0,1,1)
################################################################################
# 260 Q

# func260(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func260(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer260 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer260) + "."
    return finalAnswer260

func260(0,1,1)
################################################################################
# 261 Q

# func261(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func261(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer261 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer261) + "."
    return finalAnswer261

func261(0,1,1)
################################################################################
# 262 Q

# func262(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func262(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer262 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer262) + "."
    return finalAnswer262

func262(0,1,1)
################################################################################
# 263 Q

# func263(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func263(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer263 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer263) + "."
    return finalAnswer263

func263(0,1,1)
################################################################################
# 264 Q

# func264(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func264(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer264 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer264) + "."
    return finalAnswer264

func264(0,1,1)
################################################################################
# 265 Q

# func265(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func265(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer265 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer265) + "."
    return finalAnswer265

func265(0,1,1)
################################################################################
# 266 Q

# func266(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func266(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer266 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer266) + "."
    return finalAnswer266

func266(0,1,1)
################################################################################
# 267 Q

# func267(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func267(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer267 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer267) + "."
    return finalAnswer267

func267(0,1,1)
################################################################################
# 268 Q

# func268(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func268(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer268 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer268) + "."
    return finalAnswer268

func268(0,1,1)
################################################################################
# 269 Q

# func269(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func269(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer269 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer269) + "."
    return finalAnswer269

func269(0,1,1)
################################################################################
# 270 Q

# func270(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func270(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer270 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer270) + "."
    return finalAnswer270

func270(0,1,1)
################################################################################
# 271 Q

# func271(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func271(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer271 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer271) + "."
    return finalAnswer271

func271(0,1,1)
################################################################################
# 272 Q

# func272(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func272(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer272 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer272) + "."
    return finalAnswer272

func272(0,1,1)
################################################################################
# 273 Q

# func273(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func273(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer273 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer273) + "."
    return finalAnswer273

func273(0,1,1)
################################################################################
# 274 Q

# func274(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func274(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer274 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer274) + "."
    return finalAnswer274

func274(0,1,1)
################################################################################
# 275 Q

# func275(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func275(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer275 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer275) + "."
    return finalAnswer275

func275(0,1,1)
################################################################################
# 276 Q

# func276(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func276(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer276 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer276) + "."
    return finalAnswer276

func276(0,1,1)
################################################################################
# 277 Q

# func277(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func277(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer277 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer277) + "."
    return finalAnswer277

func277(0,1,1)
################################################################################
# 278 Q

# func278(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func278(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer278 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer278) + "."
    return finalAnswer278

func278(0,1,1)
################################################################################
# 279 Q

# func279(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func279(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer279 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer279) + "."
    return finalAnswer279

func279(0,1,1)
################################################################################
# 280 Q

# func280(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func280(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer280 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer280) + "."
    return finalAnswer280

func280(0,1,1)
################################################################################
# 281 Q

# func281(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func281(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer281 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer281) + "."
    return finalAnswer281

func281(0,1,1)
################################################################################
# 282 Q

# func282(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func282(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer282 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer282) + "."
    return finalAnswer282

func282(0,1,1)
################################################################################
# 283 Q

# func283(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func283(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer283 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer283) + "."
    return finalAnswer283

func283(0,1,1)
################################################################################
# 284 Q

# func284(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func284(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer284 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer284) + "."
    return finalAnswer284

func284(0,1,1)
################################################################################
# 285 Q

# func285(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func285(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer285 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer285) + "."
    return finalAnswer285

func285(0,1,1)
################################################################################
# 286 Q

# func286(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func286(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer286 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer286) + "."
    return finalAnswer286

func286(0,1,1)
################################################################################
# 287 Q

# func287(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func287(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer287 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer287) + "."
    return finalAnswer287

func287(0,1,1)
################################################################################
# 288 Q

# func288(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func288(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer288 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer288) + "."
    return finalAnswer288

func288(0,1,1)
################################################################################
# 289 Q

# func289(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func289(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer289 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer289) + "."
    return finalAnswer289

func289(0,1,1)
################################################################################
# 290 Q

# func290(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func290(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer290 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer290) + "."
    return finalAnswer290

func290(0,1,1)
################################################################################
# 291 Q

# func291(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func291(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer291 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer291) + "."
    return finalAnswer291

func291(0,1,1)
################################################################################
# 292 Q

# func292(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func292(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer292 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer292) + "."
    return finalAnswer292

func292(0,1,1)
################################################################################
# 293 Q

# func293(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func293(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer293 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer293) + "."
    return finalAnswer293

func293(0,1,1)
################################################################################
# 294 Q

# func294(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func294(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer294 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer294) + "."
    return finalAnswer294

func294(0,1,1)
################################################################################
# 295 Q

# func295(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func295(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer295 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer295) + "."
    return finalAnswer295

func295(0,1,1)
################################################################################
# 296 Q

# func296(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func296(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer296 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer296) + "."
    return finalAnswer296

func296(0,1,1)
################################################################################
# 297 Q

# func297(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func297(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer297 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer297) + "."
    return finalAnswer297

func297(0,1,1)
################################################################################
# 298 Q

# func298(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func298(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer298 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer298) + "."
    return finalAnswer298

func298(0,1,1)
################################################################################
# 299 Q

# func299(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func299(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer299 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer299) + "."
    return finalAnswer299

func299(0,1,1)
################################################################################
# 300 Q

# func300(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func300(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer300 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer300) + "."
    return finalAnswer300

func300(0,1,1)
################################################################################
# 301 Q

# func301(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func301(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer301 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer301) + "."
    return finalAnswer301

func301(0,1,1)
################################################################################
# 302 Q

# func302(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func302(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer302 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer302) + "."
    return finalAnswer302

func302(0,1,1)
################################################################################
# 303 Q

# func303(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func303(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer303 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer303) + "."
    return finalAnswer303

func303(0,1,1)
################################################################################
# 304 Q

# func304(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func304(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer304 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer304) + "."
    return finalAnswer304

func304(0,1,1)
################################################################################
# 305 Q

# func305(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func305(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer305 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer305) + "."
    return finalAnswer305

func305(0,1,1)
################################################################################
# 306 Q

# func306(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func306(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer306 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer306) + "."
    return finalAnswer306

func306(0,1,1)
################################################################################
# 307 Q

# func307(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func307(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer307 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer307) + "."
    return finalAnswer307

func307(0,1,1)
################################################################################
# 308 Q

# func308(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func308(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer308 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer308) + "."
    return finalAnswer308

func308(0,1,1)
################################################################################
# 309 Q

# func309(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func309(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer309 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer309) + "."
    return finalAnswer309

func309(0,1,1)
################################################################################
# 310 Q

# func310(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func310(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer310 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer310) + "."
    return finalAnswer310

func310(0,1,1)
################################################################################
# 311 Q

# func311(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func311(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer311 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer311) + "."
    return finalAnswer311

func311(0,1,1)
################################################################################
# 312 Q

# func312(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func312(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer312 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer312) + "."
    return finalAnswer312

func312(0,1,1)
################################################################################
# 313 Q

# func313(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func313(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer313 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer313) + "."
    return finalAnswer313

func313(0,1,1)
################################################################################
# 314 Q

# func314(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func314(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer314 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer314) + "."
    return finalAnswer314

func314(0,1,1)
################################################################################
# 315 Q

# func315(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func315(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer315 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer315) + "."
    return finalAnswer315

func315(0,1,1)
################################################################################
# 316 Q

# func316(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func316(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer316 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer316) + "."
    return finalAnswer316

func316(0,1,1)
################################################################################
# 317 Q

# func317(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func317(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer317 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer317) + "."
    return finalAnswer317

func317(0,1,1)
################################################################################
# 318 Q

# func318(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func318(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer318 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer318) + "."
    return finalAnswer318

func318(0,1,1)
################################################################################
# 319 Q

# func319(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func319(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer319 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer319) + "."
    return finalAnswer319

func319(0,1,1)
################################################################################
# 320 Q

# func320(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func320(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer320 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer320) + "."
    return finalAnswer320

func320(0,1,1)
################################################################################
# 321 Q

# func321(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func321(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer321 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer321) + "."
    return finalAnswer321

func321(0,1,1)
################################################################################
# 322 Q

# func322(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func322(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer322 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer322) + "."
    return finalAnswer322

func322(0,1,1)
################################################################################
# 323 Q

# func323(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func323(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer323 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer323) + "."
    return finalAnswer323

func323(0,1,1)
################################################################################
# 324 Q

# func324(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func324(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer324 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer324) + "."
    return finalAnswer324

func324(0,1,1)
################################################################################
# 325 Q

# func325(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func325(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer325 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer325) + "."
    return finalAnswer325

func325(0,1,1)
################################################################################
# 326 Q

# func326(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func326(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer326 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer326) + "."
    return finalAnswer326

func326(0,1,1)
################################################################################
# 327 Q

# func327(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func327(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer327 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer327) + "."
    return finalAnswer327

func327(0,1,1)
################################################################################
# 328 Q

# func328(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func328(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer328 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer328) + "."
    return finalAnswer328

func328(0,1,1)
################################################################################
# 329 Q

# func329(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func329(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer329 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer329) + "."
    return finalAnswer329

func329(0,1,1)
################################################################################
# 330 Q

# func330(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func330(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer330 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer330) + "."
    return finalAnswer330

func330(0,1,1)
################################################################################
# 331 Q

# func331(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func331(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer331 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer331) + "."
    return finalAnswer331

func331(0,1,1)
################################################################################
# 332 Q

# func332(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func332(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer332 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer332) + "."
    return finalAnswer332

func332(0,1,1)
################################################################################
# 333 Q

# func333(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func333(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer333 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer333) + "."
    return finalAnswer333

func333(0,1,1)
################################################################################
# 334 Q

# func334(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func334(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer334 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer334) + "."
    return finalAnswer334

func334(0,1,1)
################################################################################
# 335 Q

# func335(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func335(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer335 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer335) + "."
    return finalAnswer335

func335(0,1,1)
################################################################################
# 336 Q

# func336(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func336(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer336 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer336) + "."
    return finalAnswer336

func336(0,1,1)
################################################################################
# 337 Q

# func337(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func337(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer337 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer337) + "."
    return finalAnswer337

func337(0,1,1)
################################################################################
# 338 Q

# func338(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func338(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer338 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer338) + "."
    return finalAnswer338

func338(0,1,1)
################################################################################
# 339 Q

# func339(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func339(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer339 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer339) + "."
    return finalAnswer339

func339(0,1,1)
################################################################################
# 340 Q

# func340(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func340(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer340 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer340) + "."
    return finalAnswer340

func340(0,1,1)
################################################################################
# 341 Q

# func341(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func341(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer341 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer341) + "."
    return finalAnswer341

func341(0,1,1)
################################################################################
# 342 Q

# func342(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func342(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer342 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer342) + "."
    return finalAnswer342

func342(0,1,1)
################################################################################
# 343 Q

# func343(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func343(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer343 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer343) + "."
    return finalAnswer343

func343(0,1,1)
################################################################################
# 344 Q

# func344(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func344(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer344 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer344) + "."
    return finalAnswer344

func344(0,1,1)
################################################################################
# 345 Q

# func345(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func345(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer345 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer345) + "."
    return finalAnswer345

func345(0,1,1)
################################################################################
# 346 Q

# func346(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func346(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer346 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer346) + "."
    return finalAnswer346

func346(0,1,1)
################################################################################
# 347 Q

# func347(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func347(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer347 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer347) + "."
    return finalAnswer347

func347(0,1,1)
################################################################################
# 348 Q

# func348(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func348(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer348 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer348) + "."
    return finalAnswer348

func348(0,1,1)
################################################################################
# 349 Q

# func349(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func349(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer349 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer349) + "."
    return finalAnswer349

func349(0,1,1)
################################################################################
# 350 Q

# func350(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func350(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer350 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer350) + "."
    return finalAnswer350

func350(0,1,1)
################################################################################
# 351 Q

# func351(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func351(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer351 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer351) + "."
    return finalAnswer351

func351(0,1,1)
################################################################################
# 352 Q

# func352(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func352(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer352 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer352) + "."
    return finalAnswer352

func352(0,1,1)
################################################################################
# 353 Q

# func353(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func353(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer353 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer353) + "."
    return finalAnswer353

func353(0,1,1)
################################################################################
# 354 Q

# func354(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func354(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer354 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer354) + "."
    return finalAnswer354

func354(0,1,1)
################################################################################
# 355 Q

# func355(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func355(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer355 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer355) + "."
    return finalAnswer355

func355(0,1,1)
################################################################################
# 356 Q

# func356(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func356(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer356 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer356) + "."
    return finalAnswer356

func356(0,1,1)
################################################################################
# 357 Q

# func357(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func357(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer357 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer357) + "."
    return finalAnswer357

func357(0,1,1)
################################################################################
# 358 Q

# func358(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func358(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer358 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer358) + "."
    return finalAnswer358

func358(0,1,1)
################################################################################
# 359 Q

# func359(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func359(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer359 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer359) + "."
    return finalAnswer359

func359(0,1,1)
################################################################################
# 360 Q

# func360(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func360(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer360 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer360) + "."
    return finalAnswer360

func360(0,1,1)
################################################################################
# 361 Q

# func361(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func361(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer361 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer361) + "."
    return finalAnswer361

func361(0,1,1)
################################################################################
# 362 Q

# func362(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func362(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer362 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer362) + "."
    return finalAnswer362

func362(0,1,1)
################################################################################
# 363 Q

# func363(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func363(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer363 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer363) + "."
    return finalAnswer363

func363(0,1,1)
################################################################################
# 364 Q

# func364(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func364(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer364 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer364) + "."
    return finalAnswer364

func364(0,1,1)
################################################################################
# 365 Q

# func365(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func365(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer365 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer365) + "."
    return finalAnswer365

func365(0,1,1)
################################################################################
# 366 Q

# func366(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func366(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer366 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer366) + "."
    return finalAnswer366

func366(0,1,1)
################################################################################
# 367 Q

# func367(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func367(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer367 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer367) + "."
    return finalAnswer367

func367(0,1,1)
################################################################################
# 368 Q

# func368(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func368(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer368 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer368) + "."
    return finalAnswer368

func368(0,1,1)
################################################################################
# 369 Q

# func369(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func369(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer369 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer369) + "."
    return finalAnswer369

func369(0,1,1)
################################################################################
# 370 Q

# func370(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func370(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer370 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer370) + "."
    return finalAnswer370

func370(0,1,1)
################################################################################
# 371 Q

# func371(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func371(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer371 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer371) + "."
    return finalAnswer371

func371(0,1,1)
################################################################################
# 372 Q

# func372(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func372(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer372 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer372) + "."
    return finalAnswer372

func372(0,1,1)
################################################################################
# 373 Q

# func373(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func373(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer373 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer373) + "."
    return finalAnswer373

func373(0,1,1)
################################################################################
# 374 Q

# func374(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func374(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer374 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer374) + "."
    return finalAnswer374

func374(0,1,1)
################################################################################
# 375 Q

# func375(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func375(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer375 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer375) + "."
    return finalAnswer375

func375(0,1,1)
################################################################################
# 376 Q

# func376(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func376(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer376 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer376) + "."
    return finalAnswer376

func376(0,1,1)
################################################################################
# 377 Q

# func377(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func377(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer377 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer377) + "."
    return finalAnswer377

func377(0,1,1)
################################################################################
# 378 Q

# func378(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func378(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer378 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer378) + "."
    return finalAnswer378

func378(0,1,1)
################################################################################
# 379 Q

# func379(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func379(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer379 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer379) + "."
    return finalAnswer379

func379(0,1,1)
################################################################################
# 380 Q

# func380(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func380(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer380 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer380) + "."
    return finalAnswer380

func380(0,1,1)
################################################################################
# 381 Q

# func381(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func381(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer381 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer381) + "."
    return finalAnswer381

func381(0,1,1)
################################################################################
# 382 Q

# func382(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func382(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer382 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer382) + "."
    return finalAnswer382

func382(0,1,1)
################################################################################
# 383 Q

# func383(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func383(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer383 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer383) + "."
    return finalAnswer383

func383(0,1,1)
################################################################################
# 384 Q

# func384(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func384(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer384 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer384) + "."
    return finalAnswer384

func384(0,1,1)
################################################################################
# 385 Q

# func385(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func385(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer385 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer385) + "."
    return finalAnswer385

func385(0,1,1)
################################################################################
# 386 Q

# func386(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func386(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer386 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer386) + "."
    return finalAnswer386

func386(0,1,1)
################################################################################
# 387 Q

# func387(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func387(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer387 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer387) + "."
    return finalAnswer387

func387(0,1,1)
################################################################################
# 388 Q

# func388(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func388(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer388 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer388) + "."
    return finalAnswer388

func388(0,1,1)
################################################################################
# 389 Q

# func389(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func389(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer389 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer389) + "."
    return finalAnswer389

func389(0,1,1)
################################################################################
# 390 Q

# func390(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func390(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer390 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer390) + "."
    return finalAnswer390

func390(0,1,1)
################################################################################
# 391 Q

# func391(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func391(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer391 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer391) + "."
    return finalAnswer391

func391(0,1,1)
################################################################################
# 392 Q

# func392(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func392(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer392 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer392) + "."
    return finalAnswer392

func392(0,1,1)
################################################################################
# 393 Q

# func393(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func393(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer393 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer393) + "."
    return finalAnswer393

func393(0,1,1)
################################################################################
# 394 Q

# func394(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func394(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer394 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer394) + "."
    return finalAnswer394

func394(0,1,1)
################################################################################
# 395 Q

# func395(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func395(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer395 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer395) + "."
    return finalAnswer395

func395(0,1,1)
################################################################################
# 396 Q

# func396(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func396(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer396 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer396) + "."
    return finalAnswer396

func396(0,1,1)
################################################################################
# 397 Q

# func397(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func397(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer397 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer397) + "."
    return finalAnswer397

func397(0,1,1)
################################################################################
# 398 Q

# func398(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func398(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer398 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer398) + "."
    return finalAnswer398

func398(0,1,1)
################################################################################
# 399 Q

# func399(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func399(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer399 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer399) + "."
    return finalAnswer399

func399(0,1,1)
################################################################################
# 400 Q

# func400(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func400(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer400 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer400) + "."
    return finalAnswer400

func400(0,1,1)
################################################################################
# 401 Q

# func401(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func401(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer401 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer401) + "."
    return finalAnswer401

func401(0,1,1)
################################################################################
# 402 Q

# func402(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func402(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer402 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer402) + "."
    return finalAnswer402

func402(0,1,1)
################################################################################
# 403 Q

# func403(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func403(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer403 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer403) + "."
    return finalAnswer403

func403(0,1,1)
################################################################################
# 404 Q

# func404(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func404(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer404 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer404) + "."
    return finalAnswer404

func404(0,1,1)
################################################################################
# 405 Q

# func405(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func405(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer405 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer405) + "."
    return finalAnswer405

func405(0,1,1)
################################################################################
# 406 Q

# func406(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func406(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer406 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer406) + "."
    return finalAnswer406

func406(0,1,1)
################################################################################
# 407 Q

# func407(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func407(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer407 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer407) + "."
    return finalAnswer407

func407(0,1,1)
################################################################################
# 408 Q

# func408(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func408(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer408 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer408) + "."
    return finalAnswer408

func408(0,1,1)
################################################################################
# 409 Q

# func409(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func409(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer409 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer409) + "."
    return finalAnswer409

func409(0,1,1)
################################################################################
# 410 Q

# func410(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func410(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer410 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer410) + "."
    return finalAnswer410

func410(0,1,1)
################################################################################
# 411 Q

# func411(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func411(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer411 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer411) + "."
    return finalAnswer411

func411(0,1,1)
################################################################################
# 412 Q

# func412(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func412(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer412 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer412) + "."
    return finalAnswer412

func412(0,1,1)
################################################################################
# 413 Q

# func413(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func413(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer413 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer413) + "."
    return finalAnswer413

func413(0,1,1)
################################################################################
# 414 Q

# func414(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func414(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer414 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer414) + "."
    return finalAnswer414

func414(0,1,1)
################################################################################
# 415 Q

# func415(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func415(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer415 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer415) + "."
    return finalAnswer415

func415(0,1,1)
################################################################################
# 416 Q

# func416(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func416(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer416 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer416) + "."
    return finalAnswer416

func416(0,1,1)
################################################################################
# 417 Q

# func417(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func417(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer417 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer417) + "."
    return finalAnswer417

func417(0,1,1)
################################################################################
# 418 Q

# func418(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func418(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer418 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer418) + "."
    return finalAnswer418

func418(0,1,1)
################################################################################
# 419 Q

# func419(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func419(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer419 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer419) + "."
    return finalAnswer419

func419(0,1,1)
################################################################################
# 420 Q

# func420(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func420(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer420 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer420) + "."
    return finalAnswer420

func420(0,1,1)
################################################################################
# 421 Q

# func421(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func421(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer421 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer421) + "."
    return finalAnswer421

func421(0,1,1)
################################################################################
# 422 Q

# func422(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func422(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer422 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer422) + "."
    return finalAnswer422

func422(0,1,1)
################################################################################
# 423 Q

# func423(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func423(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer423 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer423) + "."
    return finalAnswer423

func423(0,1,1)
################################################################################
# 424 Q

# func424(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func424(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer424 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer424) + "."
    return finalAnswer424

func424(0,1,1)
################################################################################
# 425 Q

# func425(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func425(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer425 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer425) + "."
    return finalAnswer425

func425(0,1,1)
################################################################################
# 426 Q

# func426(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func426(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer426 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer426) + "."
    return finalAnswer426

func426(0,1,1)
################################################################################
# 427 Q

# func427(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func427(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer427 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer427) + "."
    return finalAnswer427

func427(0,1,1)
################################################################################
# 428 Q

# func428(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func428(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer428 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer428) + "."
    return finalAnswer428

func428(0,1,1)
################################################################################
# 429 Q

# func429(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func429(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer429 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer429) + "."
    return finalAnswer429

func429(0,1,1)
################################################################################
# 430 Q

# func430(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func430(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer430 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer430) + "."
    return finalAnswer430

func430(0,1,1)
################################################################################
# 431 Q

# func431(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func431(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer431 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer431) + "."
    return finalAnswer431

func431(0,1,1)
################################################################################
# 432 Q

# func432(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func432(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer432 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer432) + "."
    return finalAnswer432

func432(0,1,1)
################################################################################
# 433 Q

# func433(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func433(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer433 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer433) + "."
    return finalAnswer433

func433(0,1,1)
################################################################################
# 434 Q

# func434(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func434(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer434 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer434) + "."
    return finalAnswer434

func434(0,1,1)
################################################################################
# 435 Q

# func435(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func435(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer435 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer435) + "."
    return finalAnswer435

func435(0,1,1)
################################################################################
# 436 Q

# func436(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func436(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer436 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer436) + "."
    return finalAnswer436

func436(0,1,1)
################################################################################
# 437 Q

# func437(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func437(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer437 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer437) + "."
    return finalAnswer437

func437(0,1,1)
################################################################################
# 438 Q

# func438(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func438(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer438 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer438) + "."
    return finalAnswer438

func438(0,1,1)
################################################################################
# 439 Q

# func439(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func439(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer439 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer439) + "."
    return finalAnswer439

func439(0,1,1)
################################################################################
# 440 Q

# func440(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func440(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer440 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer440) + "."
    return finalAnswer440

func440(0,1,1)
################################################################################
# 441 Q

# func441(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func441(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer441 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer441) + "."
    return finalAnswer441

func441(0,1,1)
################################################################################
# 442 Q

# func442(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func442(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer442 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer442) + "."
    return finalAnswer442

func442(0,1,1)
################################################################################
# 443 Q

# func443(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func443(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer443 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer443) + "."
    return finalAnswer443

func443(0,1,1)
################################################################################
# 444 Q

# func444(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func444(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer444 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer444) + "."
    return finalAnswer444

func444(0,1,1)
################################################################################
# 445 Q

# func445(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func445(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer445 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer445) + "."
    return finalAnswer445

func445(0,1,1)
################################################################################
# 446 Q

# func446(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func446(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer446 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer446) + "."
    return finalAnswer446

func446(0,1,1)
################################################################################
# 447 Q

# func447(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func447(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer447 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer447) + "."
    return finalAnswer447

func447(0,1,1)
################################################################################
# 448 Q

# func448(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func448(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer448 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer448) + "."
    return finalAnswer448

func448(0,1,1)
################################################################################
# 449 Q

# func449(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func449(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer449 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer449) + "."
    return finalAnswer449

func449(0,1,1)
################################################################################
# 450 Q

# func450(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func450(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer450 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer450) + "."
    return finalAnswer450

func450(0,1,1)
################################################################################
# 451 Q

# func451(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func451(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer451 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer451) + "."
    return finalAnswer451

func451(0,1,1)
################################################################################
# 452 Q

# func452(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func452(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer452 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer452) + "."
    return finalAnswer452

func452(0,1,1)
################################################################################
# 453 Q

# func453(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func453(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer453 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer453) + "."
    return finalAnswer453

func453(0,1,1)
################################################################################
# 454 Q

# func454(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func454(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer454 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer454) + "."
    return finalAnswer454

func454(0,1,1)
################################################################################
# 455 Q

# func455(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func455(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer455 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer455) + "."
    return finalAnswer455

func455(0,1,1)
################################################################################
# 456 Q

# func456(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func456(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer456 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer456) + "."
    return finalAnswer456

func456(0,1,1)
################################################################################
# 457 Q

# func457(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func457(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer457 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer457) + "."
    return finalAnswer457

func457(0,1,1)
################################################################################
# 458 Q

# func458(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func458(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer458 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer458) + "."
    return finalAnswer458

func458(0,1,1)
################################################################################
# 459 Q

# func459(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func459(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer459 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer459) + "."
    return finalAnswer459

func459(0,1,1)
################################################################################
# 460 Q

# func460(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func460(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer460 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer460) + "."
    return finalAnswer460

func460(0,1,1)
################################################################################
# 461 Q

# func461(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func461(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer461 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer461) + "."
    return finalAnswer461

func461(0,1,1)
################################################################################
# 462 Q

# func462(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func462(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer462 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer462) + "."
    return finalAnswer462

func462(0,1,1)
################################################################################
# 463 Q

# func463(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func463(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer463 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer463) + "."
    return finalAnswer463

func463(0,1,1)
################################################################################
# 464 Q

# func464(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func464(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer464 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer464) + "."
    return finalAnswer464

func464(0,1,1)
################################################################################
# 465 Q

# func465(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func465(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer465 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer465) + "."
    return finalAnswer465

func465(0,1,1)
################################################################################
# 466 Q

# func466(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func466(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer466 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer466) + "."
    return finalAnswer466

func466(0,1,1)
################################################################################
# 467 Q

# func467(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func467(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer467 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer467) + "."
    return finalAnswer467

func467(0,1,1)
################################################################################
# 468 Q

# func468(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func468(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer468 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer468) + "."
    return finalAnswer468

func468(0,1,1)
################################################################################
# 469 Q

# func469(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func469(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer469 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer469) + "."
    return finalAnswer469

func469(0,1,1)
################################################################################
# 470 Q

# func470(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func470(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer470 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer470) + "."
    return finalAnswer470

func470(0,1,1)
################################################################################
# 471 Q

# func471(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func471(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer471 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer471) + "."
    return finalAnswer471

func471(0,1,1)
################################################################################
# 472 Q

# func472(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func472(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer472 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer472) + "."
    return finalAnswer472

func472(0,1,1)
################################################################################
# 473 Q

# func473(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func473(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer473 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer473) + "."
    return finalAnswer473

func473(0,1,1)
################################################################################
# 474 Q

# func474(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func474(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer474 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer474) + "."
    return finalAnswer474

func474(0,1,1)
################################################################################
# 475 Q

# func475(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func475(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer475 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer475) + "."
    return finalAnswer475

func475(0,1,1)
################################################################################
# 476 Q

# func476(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func476(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer476 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer476) + "."
    return finalAnswer476

func476(0,1,1)
################################################################################
# 477 Q

# func477(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func477(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer477 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer477) + "."
    return finalAnswer477

func477(0,1,1)
################################################################################
# 478 Q

# func478(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func478(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer478 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer478) + "."
    return finalAnswer478

func478(0,1,1)
################################################################################
# 479 Q

# func479(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func479(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer479 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer479) + "."
    return finalAnswer479

func479(0,1,1)
################################################################################
# 480 Q

# func480(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func480(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer480 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer480) + "."
    return finalAnswer480

func480(0,1,1)
################################################################################
# 481 Q

# func481(i,c,d)
# i: (num) i =
# i: (num) c = if feedback is printed to the console (not for debugging)
#         (0 = none, 1 = basic feedback)
# i: (num) d = if debugging information is printed to the console
#         (0 = debug off, 1 = debug on)
# o: (str) prints the final answer
# r: (num) returns the final answer
def func481(i,c,d):
    # Make sure the input value is valid
    if i < 0:
        if c > 0: # If logging to console is turned on
            print str(i) + " is negative."
        if d > 0: # If printing debugging information is turned on
            print "DEBUG: Inputing negative numbers may break this function."

    finalAnswer481 = 0 # Initialize the final answer


    print "The final answer is " + str(finalAnswer481) + "."
    return finalAnswer481

func481(0,1,1)
