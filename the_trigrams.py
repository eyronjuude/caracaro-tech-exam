if __name__ == '__main__':
    raw_doc = input()
    tokens = raw_doc.split()
    trigrams = [
        f'{tokens[i].lower()} {tokens[i+1].lower()} {tokens[i+2].lower()}' for i in range(len(tokens)-2)]
    frequencies = {}
    for i in trigrams:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    print(max(frequencies, key=frequencies.get))
