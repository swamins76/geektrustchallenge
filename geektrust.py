#################################################################################################################################
#Author Name: Swaminathan Shankar Subbu
#Date       :  June 25 2021
#Version    :   1.0
#Comments   :   First version created by Author
#################################################################################################################################

#Start by Importing the required Modules
import sys
from icecream import ic

import geektrustConfiguration as config

#using the icecream for debug purpose. you can enable the same through ic.enable()
ic.disable()

#Set any Global Variables for usage
weather =''
traffic_speed_orbit1 = 0
traffic_speed_orbit2 = 0

# The function timeToTravel will take the paramerts - vehicle, orbitname, trafficspeed,weather to calculate the travel time.
def timeToTravel(vehicle,orbitname,trafficSpeed,weather):
    #check if the traffic speed is over the vehicle speed
    orbitspeed = 0
    vehiclespeeddata = config.vehicle_options_dict[vehicle]
    #ic(vehiclespeeddata)
    if (vehiclespeeddata[0]<trafficSpeed):
        orbitspeed = vehiclespeeddata[0]
    else:
        orbitspeed = trafficSpeed
    #ic(orbitspeed)
    # time to travel in the given orbit:
    orbitDistance = config.orbit_options_dict[orbitname]
    orbitNormalTime = orbitDistance[0]/orbitspeed #This is the time needed by the vehicle to travel in the given orbit without considering the crators.

    #deduct the time needed to negotiate the craters by first getting the no. of crators and then multiply the same with time needed by the vehicle to negotiate that crator.
    vehicleCraterTime = vehiclespeeddata[1]
    cratorsInOrbit = orbitDistance[1] + (orbitDistance[1]*(config.weather_speed_reduction_dict[weather])/100)
    ic(cratorsInOrbit)
    #calculate the time needed to negotiate the crators
    cratorCrossingTime = vehicleCraterTime*cratorsInOrbit
    ic(cratorCrossingTime)
    # add the crator crossing time to the normal time for overall time needed for the travel.
    return (orbitNormalTime + (cratorCrossingTime/60))
    ic(timeToTravel)

#read the inputs from the input file. The following needs to be provided in the input file - WEATHER ORBIT_1_TRAFFIC_SPEED ORBIT_2_TRAFFIC_SPEED. Note that the separator is "SPACE"
if (len(sys.argv) ==1):   
    inputData = open(config.INPUT_FILE_PATH,'r')
else:
      inputData = open(sys.argv[1],'r')  
for line in inputData:
    weather = line.split(" ")[0].lower() # converting to lower case to avoid case sensitive keys
    traffic_speed_orbit1 = eval(line.split(" ")[1])
    traffic_speed_orbit2 = eval(line.split(" ")[2])
inputData.close()

# get the list of vehicles that can be used for the given weather condition
car_weather = config.weather_vehicle_dict[weather]
orbits = config.orbit_list # get the list of orbit paths
travelTimeSet = []
prefRoute = False # this is a flag set to check if the loop is the first one or not.
# the below 2 for loops will loop through the different vehicle options with different orbitpath for the defined speed. After every loop, we compare the time to travel from the previous
#one to either retain the new old or overwrite with the new data.
for vehicle in car_weather:
    for orbitpath in orbits:
        if (orbitpath == 'Orbit1'):
            traffic_speed = traffic_speed_orbit1
        else:
            traffic_speed = traffic_speed_orbit2
        travelTime= timeToTravel(vehicle,orbitpath,traffic_speed,weather)
        if (prefRoute == False):
            travelTimeSet.append([vehicle,orbitpath,travelTime])
            prefRoute = True
        else:
            if (travelTimeSet[0][2] >= travelTime):
                travelTimeSet.clear()
                travelTimeSet.append([vehicle,orbitpath,travelTime])
print(travelTimeSet[0][0].upper()+" "+travelTimeSet[0][1].upper( ))

