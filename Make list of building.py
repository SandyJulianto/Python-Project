# Make list of building
# List of building
list_building = [['length','width','area'],[10,40,400],[20,50,1000],[30,20,600]]
building_size = []
# Key value of building
key_building = list_building[0]

# Loops for list size in list_building
for row_building in list_building[1:]:
    # New dictionary set
    dict_row_building = dict()
    # Loops for index of row building
    for i in range(len(row_building)):
        # Assing index (i) of row_building to dict_row_building[i index] variable
        dict_row_building[key_building[i]] = row_building[i]
    # Add dict_row_building to building_size variable
    building_size.append(dict_row_building)

#Print the building_size
print(building_size)