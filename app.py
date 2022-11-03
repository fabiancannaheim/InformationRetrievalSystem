"""
@date: 2022-11-02
@author: Fabian C. Annaheim
@description: Retrieval System
"""

import os
import re
import numpy as np

# Indexing of documents and queriess
print("Indexing documents and queries ...\n")

invIndex, nonInvIndex, queries = {}, {}, {}

# Create inverted and non-inverted index
for document in os.listdir("./documents"):

    filename = "./documents/" + document
    file = open(filename, "r")
    content = file.read()
    terms = re.split("\W", content)

    for term in terms:

        if term in invIndex:
            if document in invIndex[term]:
                invIndex[term][document] += 1
            else:
                invIndex[term][document] = 1
        else:
            invIndex[term] = {
                document: 1
            }

        if document in nonInvIndex:
            if term in nonInvIndex[document]:
                nonInvIndex[document][term] += 1
            else:
                nonInvIndex[document][term] = 1
        else:
            nonInvIndex[document] = {
                term: 1
            }

# Create index of queries
for query in os.listdir("./queries"):

    filename = "./queries/" + query
    file = open(filename, "r")
    content = file.read()
    terms = re.split("\W", content)

    for term in terms:
        if query in queries:
            if term in queries[query]:
                queries[query][term] += 1
            else:
                queries[query][term] = 1
        else:
            queries[query] = {
                term: 1
            }

# Calculating IDFs and document normalizers
print("Calculating IDFs and document normalizers ...\n")

dNorm, idf = {}, {}

total_documents = len(nonInvIndex)

for document in nonInvIndex:
    dNorm[document] = 0
    for word in nonInvIndex[document]:
        df = len(invIndex[word])
        idf[word] = np.log((1 + total_documents) / (1 + df))
        a = nonInvIndex[document][word] * idf[word]
        dNorm[document] += a * a
    dNorm[document] = np.sqrt(dNorm[document])

# Process queries
print("Processing queries ...\n")

for query in queries:
    qNorm = 0
    accu = {}
    for word in queries[query]:
        if word not in idf:
            idf[word] = np.log(1 + total_documents)
        b = queries[query][word] * idf[word]
        qNorm += (b * b)
        if word in invIndex:
            for document in invIndex[word]:
                a = invIndex[word][document] * idf[word]
                if document in accu:
                    accu[document] += a * b
                else:
                    accu[document] = a * b
    qNorm = np.sqrt(qNorm)
    for document in accu:
        accu[document] *= 1000
        accu[document] /= dNorm[document] * qNorm
    results = dict(list(dict(sorted(accu.items(), key=lambda x: x[1], reverse=True)).items())[0: 10])
    rank = 1
    for result in results:
        print(str(query) + " Q0 " + str(result) + " " + str(rank) + " " + str(round(results[result], 4)))
        rank += 1

