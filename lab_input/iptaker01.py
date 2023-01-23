#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")

  #  print ("Please enter an IPv4 IP address:")
    #ip_address = input()
    ip_address = user_input
    print("ip_address = ", ip_address)

    # display the input back to the user.
#    print("You told me the IPv4 address is: " + user_input)
    print("You told me the IPv4 address is: " , ip_address)

# asking user for 'vendor name'
    vendor = input("Please input the vendor name: ")
    print(vendor)
# this calls main
main()

