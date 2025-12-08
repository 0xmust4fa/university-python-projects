pro_P = {'Kabul':  6000000,
         'Ghazni': 2000000,
         'Herat':  4500000,
         'Mazer':  4800000,
         'Konar':  1500000}
del pro_P['Ghazni']
pro_P['Nimrowz'] = 320000
pro_P.pop('Konar')
print(pro_P)
print(pro_P.items())
print(pro_P.keys())
print(pro_P.values())