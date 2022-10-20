from functools import reduce
s = input()
hetao = 'HETAO'

def countSub(string, sub_s):
    string = [c for c in string if c in sub_s]
    i = 0
    seqs = []
    for c in string:
        if c == sub_s[0]:
            pos = 1
            seq = [1]
            for c2 in string[i + 1:]:
                if pos > len(sub_s):
                    break
                if pos < len(sub_s) and c2 == sub_s[pos]:
                    try:
                        seq[pos] += 1
                    except IndexError:
                        seq.append(1)
                        pos += 1
                elif pos > 1 and c2 == sub_s[pos - 1]:
                    seq[pos - 1] += 1
            if len(seq) == len(sub_s):
                seqs.append(seq)
        i += 1
    return sum(reduce(lambda x, y: x * y, seq) for seq in seqs)



a=countSub(s, hetao)
print(a)