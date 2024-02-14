# (b) Write a script for computing and printing the speeding fine of a motorist.
# Assume the speed limit is 65 mph, the motorist was traveling at 85 mph and 
# the ticket is $5 for each mph over the speed limit. Your script should include
# in-code comments as necessary to allow a reviewer of the program to
# understand the objective and functioning of it. 
# Comments in Python begin with the # character.


import math
class SurfaceAreaCalc:

    def calculate_speedingTicket():
        
        # Prompt the user to enter the radius of the sphere
        driverSpeed = input("Enter the speed of the driver (mph): ")
           
        # Use the default value of 85 if no input is provided, otherwise convert the input to an integer
        driverSpeed = 85 if driverSpeed == '' else int(driverSpeed)

        # Set the speedLimit of the zone
        speedLimit = 65

        # Assume there is no speeding ticket and initialize variable
        speedingTicketCheck = False
        
        # Compare the speed limit to the radar input
        if driverSpeed > speedLimit:
                speedingTicketCheck = True
                
                # ticket cost is $5 for each mph over the speed limit
                ticketCost = round((driverSpeed - speedLimit)*5, 1)
                
                # Print out the ticket cost
                print(f"The cost of the speeding ticket is ${ticketCost} because the driver was driving at {driverSpeed}mph")
                
        else:
            # Print the computed surface area
            print(f"The Driver was not speeding at {driverSpeed} mph.")

    # Now that it is defined, call it to run the method here
    calculate_speedingTicket()