import pandas as pd
import my_string_preprocessing as msp

# Load the dataset
df = pd.read_csv('tripadvisor_hotel_reviews.csv')
df.info()
#df.head()
print("Original data frame: ", df.head(5))

# Apply the preprocessing function to the 'Review' column
df['preprocessed_text'] = df['Review'].apply(msp.preproc_text_string, lemmatize = False)

# Display the 1st 5 rows of the preprocessed data
#df.head(5)
print("Preprocessed data frame: ", df.head(5))
