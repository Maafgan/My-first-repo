import sys
print ('argument list', sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
    print ("Hello {}. How are you?".format(name))
else:
    print ("\033[91mERROR: You didn't supply a name as an argument\033[0m")
    
print ("Ali")
import numpy
