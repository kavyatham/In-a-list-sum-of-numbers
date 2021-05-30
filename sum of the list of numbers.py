Dict1 = {"name1":"50","name2":"60","name3":"70"}

itemMaxValue = max(Dict1.items(), key=lambda x : x[1])
print('Max value in Dict: ', itemMaxValue[1])
print('Key With Max value in Dict: ', itemMaxValue[0])