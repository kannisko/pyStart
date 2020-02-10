from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from collections import OrderedDict
import copy
import math

tokenizer = TreebankWordTokenizer()

sentences = ["The faster Harry got to the store, the faster Harry, the faster, would get home.",
"Harry is hairy and faster than Jill.",
"Jill is not as hairy as Harry."]

tokens = []
docLength = []
countedTokens = []


def do_sentences(sentences):
    for sentence in sentences:
        tok = tokenizer.tokenize(sentence.lower())
        tokens.append(tok)
        docLength.append(len(tok))
        countedTokens.append(Counter(tok))

def prepareLexicon(tokensList):
    lexicon = set()
    for token in tokensList:
        for tok in token:
            lexicon.add(tok)
    lexicon = sorted(lexicon)
    return lexicon

def cosine( v1,v2):
    sum = 0.0
    a = 0.0
    b = 0.0
    for i, v in enumerate(v1):
        sum += v*v2[i]
        a += v*v
        b += v2[i]*v2[i]
    return sum/math.sqrt(a*b)

def toVect(ordered, alfa):
    vec = [val/alfa for val in ordered.values()]
    return vec




do_sentences(sentences)
lexicon = prepareLexicon(tokens)
lexiconLength = len(lexicon);

zero_vector = OrderedDict((token, 0) for token in lexicon)

vectors = []
for doc in countedTokens:
    vec = copy.copy(zero_vector)
    for key, value in doc.items():
        vec[key] = value
    vectors.append(vec)


print(cosine(toVect(vectors[0],1.0),toVect(vectors[1],1.0)))
print(cosine(toVect(vectors[0],docLength[0]),toVect(vectors[1],docLength[1])))

