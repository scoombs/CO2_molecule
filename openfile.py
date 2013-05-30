#!/usr/bin/env python

import os, sys

def example_function(a,b,c=17.5,d=True):
    """
    This is an example function
    a: A number that must be handed to the function
    b: A number that must be handed to the function
    c: A value that can be handed to the function but if not
       has a default value of 17.5
    d: A value that can be handed to the function but if not
       has a default value of True
    NOTE: Variables with default values must be given after 
          variables that do not
    """
    # Now just code in the function
   # sum = a+b+c
   # if d:
    #    print 'd = True'
   # else:
    #    print 'd != True'

   # return sum


def main():
    """
    This is the main function.
    """
    # A clean way to ask for user input
   # try:
        # Attempt to retrieve required input from user
    #    prog = sys.argv[0]
     #   a = float(sys.argv[1])
      #  b = float(sys.argv[2])
  #  except IndexError:
        # Tell the user what they need to give
   #     print '\nusage: '+prog+' a b    (where a & b are numbers)\n'
        # Exit the program cleanly
    #    sys.exit(0)

    # Execute the function defined above
#    sum = example_function(a,b)

#    print 'sum =',sum

#Program used to find the bond lengths in a CO2 atom.
    natom = 3 
    inputFile = open('distance.txt','r')
    x_array = []
    y_array = []
    z_array = []
    for i in inputFile.readlines():
         x_array.append(float(i.split()[0]))
         y_array.append(float(i.split()[1]))
         z_array.append(float(i.split()[2]))
   # print z_array

    inputFile.close()
    
    CO1_x = []
    CO2_x = []
    CO1_y = []
    CO2_y = []
    CO1_z = []
    CO2_z = []
    for n in range(len(x_array)/natom):
        #distance between C and each O, called O1 and O2 for convenience
        CO1_x.append(x_array[3*n + 1] - x_array[3*n])
        CO2_x.append(x_array[3*n + 2] - x_array[3*n])

        CO1_y.append(y_array[3*n + 1] - y_array[3*n])
        CO2_y.append(y_array[3*n + 2] - y_array[3*n])
        
        CO1_z.append(z_array[3*n + 1] - z_array[3*n])
        CO2_z.append(z_array[3*n + 2] - z_array[3*n])
       # print CO1_x
    
    outfile = open('coordinates.txt','w')
    for n in range(len(x_array)/natom):
        distance1 = (CO1_x[n]**2 + CO1_y[n]**2 + CO1_z[n]**2)**(1./2.) #Finding the distance b/w C and O1
        distance2 = (CO2_x[n]**2 + CO2_y[n]**2 + CO2_z[n]**2)**(1./2.) #Finding the distance b/w C and O2
       # print distance2 
        outfile.write(str(distance1) + ' ' + str(distance2) +'\n')    

    outfile.close()

# This executes main() only if executed from shell
if __name__ == '__main__':
    main()
