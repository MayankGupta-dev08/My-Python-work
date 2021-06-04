'''MATH MODULE AND MATHEMATICAL FUNCTIONS IN PYTHON'''


'''Set 1 (Numeric Functions)'''
# 1. ceil() :- This function returns the smallest integral value greater than the number. If number is already integer, same number is returned.
# 2. floor() :- This function returns the greatest integral value smaller than the number. If number is already integer, same number is returned.
# 3. fabs() :- This function returns the absolute value of the number.
# 4. factorial() :- This function returns the factorial of the number. An error message is displayed if number is not integral.
# 5. copysign(a, b) :- This function returns the number with the value of ‘a’ but with the sign of ‘b’. The returned value is float type.
# 6. gcd() :- This function is used to compute the greatest common divisor of 2 numbers mentioned in its arguments. This function works in python 3.5 and above.

import math

a = 2.3
b=-10
c=5

print ("The ceil of 2.3 is : ", math.ceil(a))
print ("The floor of 2.3 is : ", math.floor(a))
print ("The absolute value of -10 is : ", math.fabs(b))
print ("The factorial of 5 is : ", math.factorial(c))
print ("The copysigned value of -10 to 5.5 is : ", math.copysign(5.5, -10))
print ("The gcd of 5 and 15 is : ", math.gcd(5,15), "\n\n")


'''Set 2 (Logarithmic and Power Functions)'''
# 1. exp(a) :- This function returns the value of e raised to the power a (e**a) .
# 2. log(a, b) :- This function returns the logarithmic value of a with base b. If base is not mentioned, the computed value is of natural log.
# 3. log2(a) :- This function computes value of log a with base 2. This value is more accurate than the value of the function discussed above.
# 4. log10(a) :- This function computes value of log a with base 10. This value is more accurate than the value of the function discussed above.
# 5. pow(a, b) :- This function is used to compute value of a raised to the power b (a**b).
# 6. sqrt() :- This function returns the square root of the number.

# Python code to demonstrate the working of
# exp() and log()

import math

print ("The e**4 value is : ", math.exp(4)) # returning the exp of 4
print ("The value of log 2 with base 3 is : ", math.log(2,3)) # returning the log of 2,3
print ("The value of log2 of 16 is : ", math.log2(16))
print ("The value of log10 of 1000000 is : ", math.log10(1000000))
print ("The value of 3 to the power 2 is : ", math.pow(3,2)) # returning the value of 3**2
print ("The value of square root of 25 : ", math.sqrt(25),"\n\n") # returning the square root of 25


'''Set 3 (Trigonometric and Angular Functions)'''
# 1. sin() :- This function returns the sine of value passed as argument. The value passed in this function should be in radians.
# 2. cos() :- This function returns the cosine of value passed as argument. The value passed in this function should be in radians.
# 3. tan() :- This function returns the tangent of value passed as argument. The value passed in this function should be in radians.
# 4. hypot(a, b) :- This returns the hypotenuse of the values passed in arguments. Numerically, it returns the value of sqrt(a*a + b*b).
# 5. degrees() :- This function is used to convert argument value from radians to degrees.
# 6. radians() :- This function is used to convert argument value from degrees to radians.


import math
  
a = math.pi/6
b = 3
c = 4
d = 30
e=1

print ("The value of sine of pi/6 is : ", math.sin(a)) # returning the value of sine of pi/6
print ("The value of cosine of pi/6 is : ", math.cos(a)) # returning the value of cosine of pi/6
print ("The value of tangent of pi/6 is : ", math.tan(a)) # returning the value of tangent of pi/6
print ("The value of hypotenuse of 3 and 4 is : ", math.hypot(b,c)) # returning the value of hypotenuse of 3 and 4
print ("The converted value from radians to degrees is : ", math.degrees(a)) # returning the converted value from radians to degrees
print ("The converted value from degrees to radians is : ", math.radians(d),"\n") # returning the converted value from degrees to radians
print ("The value of sine inverse of 1 is : ", math.degrees(math.asin(e))) # returning the value of sine inverse of 1
print ("The value of cos inverse of 1 is : ", math.degrees(math.acosh(e))) # returning the value of cos inverse of 1
print ("The value of tan inverse of 1 is : ", math.degrees(math.atan(e)), "\n\n") # returning the value of tan inverse of 1


'''Set 4 (Special Functions and Constants)'''
# 1. gamma() :- This function is used to return the gamma function of the argument.
# 2. pi :- This is an inbuilt constant that outputs the value of pi(3.141592).
# 3. e :- This is an inbuilt constant that outputs the value of e(2.718281).
# 4. inf :- This is a positive floating point infinity constant. -inf is used to denote the negative floating point infinity. This constant is defined in python 3.5 and above.
# 5. isinf() :- This function is used to check whether the value is an infinity or not.
# 6. nan :- This constant denotes “Not a number” in python. This constant is defined in python 3.5 and above.
# 7. isnan() :- This function returns true if the number is “nan” else returns false.


import math

a = 4
  
print ("The gamma() of 4 is : ", math.gamma(a)) # returning the gamma() of 4
print ("The value of const. pi is : ", math.pi) # returning the value of const. pi
print ("The value of const. e is : ", math.e, "\n")  # returning the value of const. e
# checking if number is nan
if (math.isnan(math.nan)):
       print ("The number is nan")
else : print ("The number is not nan")
  
# checking if number is positive infinity
if (math.isinf(math.inf)):
       print ("The number is positive infinity")
else : print ("The number is not positive infinity")