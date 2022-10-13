import re
import collections as cll

def keyword_searcher(file):
    with open(file, encoding='utf-8') as text:
        count = re.findall(r"[0-9a-zA-Z-']+", text.read())
        count = [word.upper() for word in count]
        print("\nWords in this text:",len(count))

        keyword = cll.Counter(count)

        print("\nMost repeated keywords (Top 10):")
        for word in keyword.most_common(10):
            print(word[0],word[1])
