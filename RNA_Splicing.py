#Python code to read given DNA string, extrapolate exons and translate the string into mRNA
#MPribis

#reads the genetic code provided in file "gen_code" and processes it into a dictionary used for translation

gen_code = {}
dna = []

transl_table = open('gen_code', 'r')
lines = transl_table.readlines()

for line in lines:
    if line != '\n':
        for entry in line.strip().split('      '):
            code = entry.split('  ')
            #print(code)
            gen_code.update( {code[0] : code[1].split(' ')[0]} )
        else:
            continue

#print(gen_code)

#reads the input coding DNA strand
#HOW TO READ MULTIPLE LINES?

def process_fasta(fasta_file):
    in_file = open(fasta_file, 'r')
    for line in in_file:
        print(line)
        if line[0] == '>':
            #list
            print(line)
            continue
            #print(in_file.readline())
        else:
            entry = []
            print(line)
            r = line.strip()
            while r[0] != '>':
                entry.append(r)
                r = in_file.readline().strip()
                print('r = ' + r)
                if r == '':
                    break
            dna.append(''.join(entry))
            print(dna)
    in_file.close()
    #print(dna)

process_fasta('rosalind_splc.txt')

#print(dna)
#print(dna[0].find(dna[2]))

#identifies given introns and splices them out

i = 1

while i < len(dna):
    pos = dna[0].find(dna[i])
    dna[0] = dna[0][:pos] + dna[0][pos + len(dna[i]):]

    i += 1

print(dna)
#check if that right is

#performs the translation

def translate(coding_dna):
    protein = ''
    i = 0
    while i < len(coding_dna) - 2:
        act_codon = coding_dna[i:i+3]
        if gen_code.get(act_codon) == '*':
            break
        else:
            protein += gen_code.get(act_codon)
            i += 3
    print(protein)

translate(dna[0])