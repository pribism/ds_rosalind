#Calculate the monoisotopic mass of a protein of known sequence using the monoisotopic mass table

#parse the monoisotopic mass table

mass_table = {}

transl_table = open('monoisotopic_mass_table', 'r')
lines = transl_table.readlines()

for line in lines:
    if line != '\n':
        aa = line.strip().split('   ')[0]
        weight = float(line.strip().split('   ')[1])
        mass_table.update( {aa : weight} )

print(mass_table)
transl_table.close()
#read the protein sequence
#calculate the monoisotopic mass of the given proteins

def calc_mass(file):
    mass = 0
    f = open(file, 'r')

    prot = f.readline().strip()

    for i in prot:
        #print(i)
        mass += mass_table.get(i)
    print(mass.__round__(3))

calc_mass('rosalind_prtm.txt')
#119262.139