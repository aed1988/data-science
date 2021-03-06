# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_costs_to_float(strng):
    num = 0
    if strng[-1] == 'B':
        num = float(strng[:-1]) * 1000000000
    elif strng[-1] == "M":
        num = float(strng[:-1]) * 1000000
    else:
        return 'Damages not recorded'
    return num

updated_damages = [convert_costs_to_float(x) for x in damages]
# print(damage_costs)



# write your construct hurricane dictionary function here:
hurricane_dictionary = {}
for index in range(34):
    hurricane_dictionary[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index]}
# print(hurricane_dictionary)


# write your construct hurricane by year dictionary function here:
hurricanes_by_year = {}
for k, v in hurricane_dictionary.items():
    year = hurricane_dictionary[k]["Year"]
    if year not in hurricane_dictionary:
        hurricanes_by_year[year] = []
    hurricanes_by_year[year].append(v)
# print(hurricanes_by_year)




# write your count affected areas function here:
count_areas_affected = {}
for a in areas_affected: 
    for b in a:
        if b in count_areas_affected:
            count_areas_affected[b] += 1
        else: count_areas_affected[b] = 1
# print(count_areas_affected)





# write your find most affected area function here:
def find_most_affected_area(lst):
    area_affected_most = ""
    number_of_times_hit = 0
    for k, v in lst.items():
        if v > number_of_times_hit:
            area_affected_most = k
            number_of_times_hit = v
    return "{} was hit the most often, {} times".format(area_affected_most, number_of_times_hit)
# print(find_most_affected_area(count_areas_affected))





# write your greatest number of deaths function here:
greatest_num_of_deaths = sorted(hurricane_dictionary.items(), key=lambda x: x[1]["Deaths"])[-1]

# print(greatest_num_of_deaths)
# print("{} had the most number of deaths, {}.".format(greatest_num_of_deaths[1]["Name"], greatest_num_of_deaths[1]["Deaths"]))





# write your catgeorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
areas_by_mortality_scale = {x+1:[] for x in mortality_scale}
for v in hurricane_dictionary.values():
    if v["Deaths"] < mortality_scale[1]: 
        areas_by_mortality_scale[1].append(v["Name"])
    elif v["Deaths"] < mortality_scale[2]: 
        areas_by_mortality_scale[2].append(v["Name"]) 
    elif v["Deaths"] < mortality_scale[3]: 
        areas_by_mortality_scale[3].append(v["Name"])
    elif v["Deaths"] < mortality_scale[4]: 
        areas_by_mortality_scale[4].append(v["Name"])
    else: 
        areas_by_mortality_scale[5].append(v["Name"])
# print(areas_by_mortality_scale)




# write your greatest damage function here:
def greatest_damage(lst):
    hurricane = ""
    damage_amount = 0
    for k, v in lst.items():
        if isinstance(v["Damage"], float) and v["Damage"] > damage_amount:
            damage_amount = v["Damage"] 
            hurricane = v["Name"]
    print(hurricane, damage_amount)
# greatest_damage(hurricane_dictionary)




# write your catgeorize by damage function here:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
hurricanes_ranked_by_damage = {x+1:[] for x in damage_scale}
print(hurricanes_ranked_by_damage)

for v in hurricane_dictionary.values():
    if not isinstance (v["Damage"], float): continue
    if v["Damage"] < damage_scale[1]: 
        hurricanes_ranked_by_damage[1].append(v["Name"])
    elif v["Damage"] < damage_scale[2]: 
        hurricanes_ranked_by_damage[2].append(v["Name"]) 
    elif v["Damage"] < damage_scale[3]: 
        hurricanes_ranked_by_damage[3].append(v["Name"])
    elif v["Damage"] < damage_scale[4]: 
        hurricanes_ranked_by_damage[4].append(v["Name"])
    else: 
        hurricanes_ranked_by_damage[5].append(v["Name"])
        
        
print(hurricanes_ranked_by_damage)









