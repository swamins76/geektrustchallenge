# This file has the configuration details for the different elements like 
# orbit, vehicle and weather limitations
#Weather conditions hampering the speed
weather_speed_reduction_dict = {'sunny': -10, 'rainy': 20, 'windy' : 0 }
weather_vehicle_dict = {'sunny':['Car', 'Bike','Tuktuk'],'rainy':['Car','Tuktuk'],'windy': ['Car','Bike']}
orbit_options_dict = {'orbit1':[18,20],'orbit2':[20,10]}
vehicle_options_dict={'Bike':[10,2],'Tuktuk':[12,1],'Car':[20,3]}
orbit_list={'orbit1','orbit2'}

#paths to the input file(s)
INPUT_FILE_PATH = 'input.txt'
