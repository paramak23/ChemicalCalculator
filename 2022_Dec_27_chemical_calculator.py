#input value

while True:
    try:
        val_1 = input('Weight: ')
        val_1 = float(val_1)
        if val_1 >= 0:
            pass
            #print(f'wt is: {val_1}')
            break;
        else:
            print('Entered value should be greater than zero!!!')
            
    except ValueError:
        print("Provide an integer or decimal value")
        continue;
        
while True:
    try:
        val_2 = input('Molecular Weight: ')
        val_2 = float(val_2)
        if val_2 > 0:
            pass
            #print(f'Entered Mwt is: {val_2}')
            break;
        else:
            print('Entered value should be greater than zero!!!')
            
    except ValueError:
        print("Provide an integer or decimal value")
        continue;
        
while True:
    try:
        val_3 = input('Volume: ')
        val_3 = float(val_3)
        if val_3 >= 0:
            pass
            #print(f'Entered Mwt is: {val_2}')
            break;
        else:
            print('Entered value should be greater than zero!!!')            
            
    except ValueError:
        print("Provide an integer or decimal value")
        continue;
        
while True:
    try:
        val_4 = input('Density: ')
        val_4 = float(val_4)
        if val_4 >= 0:
            pass
            #print(f'Entered volume is: {val_3}')
            break;
        else:
            print('Entered value should be greater than zero!!!')
            
    except ValueError:
        print("Provide an integer or decimal value")
        continue;
        


if val_1 > 0 and val_2 > 0 and val_3 == 0 and val_4 == 0:
    
    class ChemicalCalculator:
        n = 1000
        def __init__(self, weight, mol_weight, volume, density):
            self.weight = weight
            self.mol_weight = mol_weight
            self.volume = volume
            self.density = density
        def mol(self):
            wt = self.weight
            Mwt = self.mol_weight
            return wt / Mwt
        def mmol(self):
            wt = self.weight
            Mwt = self.mol_weight
            return wt / Mwt * self.n

if val_1 == 0 and val_3 > 0 and val_4 > 0:

    class ChemicalCalculator:
        n = 1000
        def __init__(self, weight, mol_weight, volume, density):
            self.weight = weight
            self.mol_weight = mol_weight
            self.volume = volume
            self.density = density
        def mol(self):
            vol = self.volume
            d = self.density
            Mwt = self.mol_weight
            return (vol * d) / Mwt
        def mmol(self):
            vol = self.volume
            d = self.density
            Mwt = self.mol_weight
            return (vol * d) / Mwt * self.n

calculation = ChemicalCalculator(weight = float(val_1), mol_weight= float(val_2), volume = float(val_3), density = float(val_4))

print(f'Weight: {val_1}')
print(f'Mol_weight: {val_2}')
print(f'Volume: {val_3}')
print(f'Density: {val_4}')
print(f'mol value: {calculation.mol()}')
print(f'Mmol value: {calculation.mmol()}')