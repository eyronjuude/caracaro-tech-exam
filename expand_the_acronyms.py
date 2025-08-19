import re


def main():
    lines = int(input())
    snippets = []
    acronyms = []
    for _ in range(lines):
        try:
            snippet = input()
        except EOFError:
            break
        snippets.append(snippet)
    doc = '\n'.join(snippets)
    for _ in range(lines):
        try:
            acronym = input()
        except EOFError:
            break
        acronyms.append(acronym)
    for acronym in acronyms:
        regex1 = ''
        regex2 = ''
        posix_print_regex = r"[\x20-\x7E]"
        posix_graph_regex = r"[\x21-\x7E]"
        for ch_idx in range(len(acronym)-1):
            regex1 += acronym[ch_idx] + f"{posix_print_regex}+?"
        regex1 += acronym[-1] + f"{posix_graph_regex}+"
        match1 = re.findall(regex1, doc)
        if len(match1) != 0:
            print(match1[0])
            continue

        regex2 += acronym[0] + f"{posix_print_regex}+?"
        for ch_idx in range(1, len(acronym)-1):
            regex2 += f"(?:{acronym[ch_idx]}|{acronym[ch_idx].lower()})" + \
                f"{posix_print_regex}+?"
        regex2 += f"(?:{acronym[-1]}|{acronym[-1].lower()})" + \
            f"{posix_graph_regex}+"
        match2 = re.findall(regex2, doc)
        if len(match2) != 0:
            print(match2[0])
            continue
        continue


if __name__ == '__main__':
    main()
