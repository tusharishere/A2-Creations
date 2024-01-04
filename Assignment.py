import pandas as pd
from googletrans import Translator
import time
import numpy as np
import httpx

# Translate text using Google Translate API
def translate_text(text1):
    translator = Translator(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    )
    # try:
    translated_text = translator.translate(text1,dest='en').text
    # translated_text = translator.translate(text1, src='en', dest='gu').text
    # except Exception:
    # print("Exception occured.")
    # return "error"
    return translated_text


# s1 = "台州市路桥乐缇电子商务商行"
# s1 = "Hello World"

# eng_word = translate_text(s1)
# print(eng_word)
# exit()

# File path to the Excel file
file_path = 'Order Export.xls'

# Start the timer
start_time = time.time()

# Read the existing file
df = pd.read_excel(file_path, header=None, engine="xlrd", na_filter=False)
df1 = df.replace(np.nan, '', regex=True)
# Translate all text, including headers, to English
print("translate started.")
df_translated = df1.apply(lambda x: x.map(translate_text))
print("translate completed.")
# Save the translated DataFrame to a new Excel file
output_file = 'Translated_Order_Sheet.xlsx'
df_translated.to_excel(output_file, index=False, header=False)

# Stop the timer, calculate elapsed time, and print
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Translation and saving completed in {elapsed_time:.2f} seconds.")
