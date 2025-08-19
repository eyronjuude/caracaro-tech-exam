def main():
    inputs = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        inputs.append(line)
    raw_doc = '\n'.join(inputs)
    sentences = raw_doc.lower().replace('. ', '.').split('.')[:-1]
    trigrams = []
    frequencies = {}
    for sentence in sentences:
        tokens = sentence.split()
        if len(tokens) < 3:
            continue
        for i in range(len(tokens)-2):
            trigrams.append(' '.join(tokens[i:i+3]))
    for trigram in trigrams:
        if trigram in frequencies:
            frequencies[trigram] += 1
        else:
            frequencies[trigram] = 1
    the_trigram = ''
    max_count = -1
    for trigram in trigrams:
        if frequencies[trigram] > max_count:
            the_trigram = trigram
            max_count = frequencies[trigram]
    print(the_trigram)


if __name__ == '__main__':
    main()
