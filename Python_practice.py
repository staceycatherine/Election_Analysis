# counties= {"Arapahoe","Denver","Jefferson"}
# print(counties)
counties=["Arapahoe","Denver","Jefferson"]
print(counties)
if counties[1] == "Denver":
    print(counties[1])

counties_dict={}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters": 432438})
print(voting_data)
# if counties[3]!="Jefferson":
    # print(counties[2])
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
     print("El Paso is in the list of counties")  
else: 
     print("El Paso is not in the list of counties") 
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in list of counties")
else:
    print("Arapahoe or El Paso is not in list of counties")
for county in counties:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)
voting_data=[{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson","registered_voters": 432438}] 
for county_dict in voting_data:
    print(county_dict) 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
        




    
















