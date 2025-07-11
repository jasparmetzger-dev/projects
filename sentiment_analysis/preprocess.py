import os
import joblib
import pandas as pd


def save_preprocessed_data(df, filepath):

    print("[INFO] reading data...")
    
    raw_data = df['review_text'].tolist()
    labels = df['sentiment'].tolist()

    preprocessed_data = preprocess(raw_data)
    joblib.dump(preprocessed_data, filepath)
    print("[INFO] downloading done.")
    return

def preprocess(texts: list[str]) -> list[list[str]]:

    import spacy
    from nltk.corpus import stopwords

    model = spacy.load("de_core_news_sm")
    stop_words = set(stopwords.words("german"))
    CONTENT_POS = {"NOUN", "VERB", "ADJ", "ADV", "AUX"}

    print("[INFO] preprocessing...")

    processed_text = []
    cnt = 0
    for text in model.pipe(texts, batch_size=1000, disable= ["parser", "ner"]):
        doc = model(text)

        processed_tokens = []
        # pos_arr = []

        for token in doc:
            if (
                token.pos_ in CONTENT_POS and
                token not in stop_words and
                not token.is_punct and
                not token.is_space and
                not token.like_url and
                not token.like_email and
                not token.is_digit and
                not token.ent_type_ 
            ):
                processed_tokens.append(token.lemma_.lower())
                # pos_arr.append(token.pos_) #wird noch nicht genutzt
        
        processed_text.append(processed_tokens)
        cnt += 1
        if cnt % 1000 == 0: print(f"[INFO] now at row {cnt}")
        if cnt == 4000:
            break
    print("[INFO] preprocessing done.")
    
    return processed_text

def load_data(filepath):
    print
    data = joblib.load(filepath)
    return data

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(os.getcwd(), "sentiment_analysis", "data", "test_data.csv"))
    file_path = "preprocessed_testing_data.joblib"

    save_preprocessed_data(df, file_path)
