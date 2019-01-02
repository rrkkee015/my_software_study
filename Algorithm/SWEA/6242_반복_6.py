blood_type = ['A','A','A','O','B','B','O','AB','AB','O']
blood_type_dict={'A':0,'O':0,'B':0,'AB':0}
for i in blood_type:
    if i=='A':
        blood_type_dict['A'] +=1
    if i=='B':
        blood_type_dict['B'] +=1
    if i=='AB':
        blood_type_dict['AB'] +=1
    if i=='O':
        blood_type_dict['O'] +=1
print(blood_type_dict)
