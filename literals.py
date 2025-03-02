#literals are data items that have a fixed/constant value

#string literals : enclosed characters in single , double or triple quotes
#single line
text1 = 'Hello'
print(text1)

#multi-line string
text2 = "hello\
 world"
#need backlash for next line
print(text2)

text3 = '''hello
my name
is nick fury''' #no need for backlash in triple quote , nd will print the text in next line
print(text3)



#numeric literals
#numeric literals are numeric value
#a : int(signed integer): positive , negative or whole numbers with no decimal point
#>decimal form :
a = -12
b = 21

#> octal form : an integer beginning with 0o(zero followed by letter o) e.g 0o35,0o4

#>hexadecimal form : an integer becoming with 0x(zero followed by letter X) e.g,0x73

#b : floating point literals.Floating point literals or real literals floats represent real numbers and are written with a decimal point dividing the integer and practional parts are numbers having fractional parts.
flt = 0.23
flt2 = 1.23
print(flt)
print(flt2)

#c : boolean : a boolean literals in python is used to represent one of the two boolean values i.e True or False

is_true = True
is_false = False
print(is_true)
print(is_false)

#d : special literals None : which is none .The none literal is used to indicate absence of value

