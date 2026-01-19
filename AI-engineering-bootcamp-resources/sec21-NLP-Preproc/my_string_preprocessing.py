import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

def download_nltk_resource_if_not_exists(resource_name):
    """Downloads an NLTK resource if it is not already installed."""
    try:
        # Try to find the resource. This raises a LookupError if not found.
        nltk.data.find(f"tokenizers/{resource_name}")
        print(f"'{resource_name}' is already installed. Skipping download.")
    except LookupError:
        # If the resource is not found, download it.
        print(f"'{resource_name}' not found. Downloading...")
        try:
            nltk.download(resource_name)
            print(f"Successfully downloaded '{resource_name}'.")
        except FileExistsError:
            # This can happen in some specific parallel processing scenarios,
            # but generally indicates the file was created by another process
            # during the short window between `find` and `download`.
            print(f"'{resource_name}' was just installed by another process.")
        except Exception as e:
            print(f"An error occurred during download: {e}")



# # Download necessary NLTK data
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')

download_nltk_resource_if_not_exists('punkt_tab')
download_nltk_resource_if_not_exists('stopwords')
download_nltk_resource_if_not_exists('wordnet')

def preproc_text_string(text, lemmatize_flag = True):
    """# Preprocesses a single text-string and returns a string of tokens for use with NLP tasks."""
    
    ## Remove HTML tags
    #text = re.sub(r'<.*?>', '', text)
    
    # Convert to lower case
    text = text.lower()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Convert asterisk (*) to the word star in the context of hotel ratings, so that it's not removed by punctuation removal
    tokens = [re.sub(r'[*]', 'star', word) for word in tokens]

    # Remove stop words & strip punctuation
    stop_words = set(stopwords.words('english'))
    stop_words.remove('not')  # Keep 'not' as it's important for sentiment analysis
    tokens = [re.sub(r'[^\w\s]', '', word) for word in tokens if word not in stop_words] 
    # # print(tokens)

    # Remove any empty tokens
    tokens = [word for word in tokens if word != '']
    # # print(tokens)

    if lemmatize_flag:
        # Lemmatize the text
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # else:
    #     print("Skipping lemmatization!")

    # Join the tokens back into a single string
    text = ' '.join(tokens)
    return text
