def normalize_sentences(text):
    sentences = []
    i = text.find(".")
    if i == -1:
        return text
    while i > -1:
        sentences.append(i)
        i = text.find(".", i + 1)
    periods = text.split(".")
    print(f"{sentences}")
    segments = [text[: sentences[0]]]
    for i in range(len(sentences) - 1):
        if not (i < len(sentences)):
            break
        segments.append(text[sentences[i] + 1 : sentences[i + 1]])
    segments.append(text[sentences[-1] + 1 :])
    print(f"{segments}")
    new_text = ".  ".join([s.strip(" ") for s in segments]).strip(" ")
    print(f"{new_text}")
    lines = [l.strip(" ") for l in new_text.splitlines()]
    return "\n".join(lines)


# [19, 45, 63, 75, 98]
