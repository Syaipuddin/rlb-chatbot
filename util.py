def extend_text(text):
    extender = {
        "kk": 'kartu keluarga',
        "ktp": 'kartu tanda penduduk',
        "ktpel": 'kartu tanda penduduk',
        'ektp': 'kartu tanda penduduk elektronik',
        'skk': 'surat keterangan kematian',
    }

    result = ""
    for text in text.split(' '):
        if text.lower() in extender:
            result += extender[text.lower()] + " "
        else:
            result += text + " "
    return result.strip()

def similarity_score(s1, s2):
    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)

def c(input, pairs):
    percentage = {}
    sequence = 0

    for (pattern, responses) in pairs:
        keysentences = pattern.pattern.replace("(", "").replace(")", "").split("|")

        max_similarity = 0
        for keysentece in keysentences:
            keysentence = keysentece.strip()
            similiarity = similarity_score(input, keysentence)
            max_similarity = max(max_similarity, similiarity)

        percentage[f"{sequence}"] = max_similarity if max_similarity else 0
        sequence += 1

    return percentage