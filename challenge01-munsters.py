#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------
#Display the value mapped to names

#print(munsters["names"])

print( "First display names  - .get()")
print (munsters.get("names"))

for x in munsters.get("names"):
    print(x, "is a caharacter on the Munsters")

#Display the value mapped to endDate

#print(munsters["endDate"])

print( "Second display enddate - .get()")
print (munsters.get("endDate"))

#Display the value mapped to startDate

#print(munsters["startDate"])

print( "Third display startdate - .get()")
print (munsters.get("startDate"))


#Add a new key, episodes mapped to the value of 70

print( "Fourth display - ADD new key")
munsters["episodes"] = "70"
print( munsters.get("episodes"))


