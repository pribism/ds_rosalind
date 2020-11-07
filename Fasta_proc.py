#Import and process fasta file

def process_fasta(fasta_file):
    str_names = []
    strs = []
    batch = []
    in_file = open(fasta_file,'r')
    for line in in_file:
        if line[0] == '>':
            str_names.append(line.strip())
            temp = ''.join(map(str, batch))
            if temp == '':
                continue
            else:
                strs.append(temp)
            batch = []
        else:
            batch.append(line.strip())
        print(str_names)
        print(strs)
    strs.append(''.join(map(str, batch)))

    l = list(zip(str_names,strs))
    d = dict(l)
    #print(d)
    return(d)


def fasta_to_list(fasta_dic):
    inp = fasta_dic
    for key in inp.keys():
        inp[key] = list(inp[key])
    return(inp)

process_fasta('./rosalind_cons (1).txt')

