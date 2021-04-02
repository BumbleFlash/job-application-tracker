import re


class ProcessorUtils:
    @staticmethod
    def pre_process(body):
        body = re.sub("&lt;/?.*?&gt;", " &lt;&gt ", body)  # removes tags
        body = body.replace('\r', '').replace('\n', '').replace('\t', '')  # removes breaks and returns
        body = body.replace("<", "")
        return re.sub(r'http\S+', '', body)  # remove urls

    @staticmethod
    def get_stop_words(path):
        with open(path, 'r', encoding="utf-8") as f:
            stopwords = f.readlines()
            stop_set = set(s.strip() for s in stopwords)
            return frozenset(stop_set)

    @staticmethod
    def sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    @staticmethod
    def extract_top_n_from_vector(feature_names, sorted_items, topn= 10):
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        for idx, score in sorted_items:
            score_vals.append(round(score,3))
            feature_vals.append(feature_names[idx])

        results = {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]] = score_vals[idx]
        return results
