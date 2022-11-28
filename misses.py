#################################                   ###################################
# Title : Looking for Fermat's Last Theorem Near Misses
# Filename : misses.py
# Necessary external files : none
# created external files : misses.exe, a windows executable file of the program
# Name: Vikas Chowdary Medarametla
# Email: VikasChowdaryMedar@lewisu.edu
# Course and Sections SU22-CPSC-60500-001 & 002
# Date: 17/07/2022
# Explanation: program that helps an interactive user search for near misses
# of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
# are positive integers, where 2< n <12, where 10 <= x <= k, and where 10 <= y <= k
# compiled on: Python 3.8.10
################################                    ###################################

def nearMisses(n, k):
    """
    Calculate near misses of the formula of Fermat's Last Theorem
    
    Calculate x^n + y^n = z^n, and then look for the minimum miss for which
    z^n < (x^n + y^n) < (z+1)^n satisfies. Find out which one (either z^n or (z+1)^n) is
    closer to (x^n + y^n), and determine the miss as the smallest of these two 
    values: [(x^n + y^n) - z^n] or [(z+1)^n- (x^n + y^n)]. Then get the
    RELATIVE size of the miss divide that miss by (x^n + y^n) and print the values
    
    Parameters
    ----------
    n : int
        power to use in the equation.
    k : int
        limits the range of x and y possibilities to test.

    Returns
    -------
    None.

    """
    f = False # for checking the first iteration or not
    relative_miss = 0
    for x in range(10, k): # Outer loop for first variable x of function x^n + y^n = z^n
        for y in range(10, k): # loop for y
            xysum_pow = pow(x, n) + pow(y, n) # calculate (x^n + y^n) using python's built in pow method
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss_temp = miss / xysum_pow
            if f==False:
                relative_miss = relative_miss_temp # for the first iteration get the relative miss
                print("\nx: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
                f = True
            else:
                if relative_miss_temp < relative_miss: 
                    relative_miss = relative_miss_temp # get the minimum relative miss
                    print("x: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
    print("\n#######Final result:##########\n")
    # print the final 
    print("x: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
    
def main():
    """
    Get the input of n(power) and k(limit) from user then call the calculate function
 
    Returns
    -------
    None.

    """
    n = int(input("Exponent value(n): "))
    while(n<3):
        # check if n is bigger than 2
        n = int(input("Exponent value should be bigger than '2' New Exponent value(n): "))
    k = int(input("Limit of x and y(k) "))
    while(k<11):
        # check if k is bigger than 10
        k = int(input("Limit value should be bigger than '10' New Exponent value(k): "))
    nearMisses(n,k)
    s = input("Prees Enter for exit ")
        
if __name__ == "__main__":
    main()
