import re

def freq(letter, text):
    count = 0
    for i in range(len(text)):
        if text[i] == letter:
            count += 1
    return count / len(text)

def pairs(letter, text):
    count = 0
    for i in range(len(text)-1):
        if text[i] == text[i+1] == letter:
            count += 1
    return count

def mystruct(text):
    count = 0
    start = 0
    
    while len(text) - start > 4:
        for i in range(start, len(text)):
            if text[i] == 'G' and (text[i + 1] == 'A' or text[i + 1] == 'T'):
                for j in range(i + 2, len(text) -1):
                    if text[j] == text[j + 1] == 'G':
                        count += 1
                        start = j + 2
                        break
                break
            else:
                start += 1
    
    return count

if __name__ == '__main__':

    text = 'AGTCAATGGAATAGGCCAAGCGAATATTTGGGCTACCA'

    print(freq('C', text))
    print(freq('G', text))
    print(pairs('A', text))
    print(mystruct(text))

    print()
    print(text.count('C') / len(text))
    print(text.count('G') / len(text))
    print(text.count('A' * 2))
    print(len(re.findall('G[AT]+?GG', text)))