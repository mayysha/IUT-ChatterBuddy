import verbs
import adjectives

pronouns = [
    'i', 'you', 'he', 'she', 'it', 'they',
    'me', 'you', 'him', 'her', 'it',
    'she', 'her', 'he', 'him', 'it', 'they', 'them',
    'my', 'mine', 'your', 'yours', 'his', 'her', 'hers', 'its',
    'who', 'whom', 'whose',
    'myself', 'yourself', 'himself', 'herself', 'itself',
    'this', 'that'
]

auxiliary_verbs = [
    'am', 'is', 'are', 'was', 'were', 'being', 'been', 'be',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
    'may', 'might', 'must', 'can', 'could'
]

prepositions = [
    'with',
    'at',
    'from',
    'into',
    'during',
    'including',
    'until',
    'against',
    'among',
    'throughout',
    'despite',
    'towards',
    'upon',
    'concerning',
    'to',
    'in',
    'for',
    'on',
    'by',
    'about',
    'like',
    'through',
    'over',
    'before',
    'between',
    'after',
    'since',
    'without',
    'under',
    'within',
    'along',
    'following',
    'across',
    'behind',
    'beyond',
    'plus',
    'except',
    'but',
    'up',
    'out',
    'around',
    'down',
    'off',
    'above',
    'near',
    'of'
]

articles = [
    'a',
    'an',
    'the'
]


def extractor(strr):
    strr = strr.lower()
    splitted = strr.split(' ')
    print(splitted)
    for word in pronouns + auxiliary_verbs + prepositions + articles + adjectives.list_adjectives:
        if word in splitted:
            splitted = list(filter(lambda a: a != word, splitted))
            print(splitted)
    for keyword, words in verbs.create_dictionary().items():
        for word in words:
            if word in splitted and word == words[2]:
                splitted.remove(word)
                splitted.append(keyword)

    return ' '.join(splitted)


print(extractor('i am feeling tired'))
