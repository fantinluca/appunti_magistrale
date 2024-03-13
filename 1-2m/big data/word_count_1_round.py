def main():

    # SPARK SETUP
    conf = SparkConf(true).setAppName('WordCount')
    sc = SparkContext(conf=conf)

    # INPUT READING
    K = sys.argv[1]
    K = int(K) # ora abbiamo num. partizioni
    data_path = sys.argv(2)
    docs = sc.textFile(data_path).repartition(K).cache() # RDD

    # COMPUTATION OF WORD COUNTS
    wordCounts = word_count_1(docs)


def word_count_per_doc(document):
    pairs_dict = {}
    for word in document.split(' '):
        if word not in pairs_dict.keys():
            pairs_dict[word]=1
        else:
            pairs_dict[word]+=1
    return [(key,pairs_dict[key]) for key in pairs_dict.keys()] # (parola, num. occorrenze parola in docs)

def word_count_1(docs):
    word_count = (docs.flatMap(word_count_per_doc)  # MAP phase: ad ogni doc, applicare funzione data in parametro
                  .groupByKey()                     # SHUFFLE + GROUPING
                  .mapValues(lambda vals:sum(vals)))# REDUCE phase
    return word_count
