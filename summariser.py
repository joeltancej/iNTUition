# 1. Count occurrences per word in the text (stop words excluded)
# 2. Calculate weight per used word
# 3. Calculate sentence weight by summarizing weight per word
# 4. Find sentences with the highest weight
# 5. Place these sentences in their original order


from nltk import tokenize, word_tokenize
import nltk
# nltk.download('punkt')

with open("stopwords.txt", "r", encoding="utf-8") as f:
     text = " ".join(f.readlines())
STOP_WORDS = set(text.split())

def summarize(text, no_sentences=3):
    word_weights={}
    for word in word_tokenize(text):
        word = word.lower()
        if len(word) > 1 and word not in STOP_WORDS:
            if word in word_weights.keys():            
                word_weights[word] += 1
            else:
                word_weights[word] = 1

    sentence_weights={}
    for sent in tokenize.sent_tokenize(text):
        sentence_weights[sent] = 0
        for word in word_tokenize(sent) :  
            word = word.lower()
            if word in word_weights.keys():            
                sentence_weights[sent] += word_weights[word]
    highest_weights = sorted(sentence_weights.values())[-no_sentences:]

    summary=""
    for sentence,strength in sentence_weights.items():  
        if strength in highest_weights:
            summary += sentence + " "
    summary = summary.replace('_', ' ').strip()
    return summary

# def main():
#     text = input("Enter text: ")
#     print(summarize(text))

# main()
