import pandas as pd
from googletrans import Translator
import time

# Translate text using Google Translate API
def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en').text
    return translated_text

# File path to the Excel file
file_path = 'Order Export.xls'  

# Start the timer
start_time = time.time()

# Read the existing file
df = pd.read_excel(file_path, header=None)

# Translate all text, including headers, to English
df_translated = df.apply(lambda x: x.map(translate_text))


# Save the translated DataFrame to a new Excel file
output_file = 'Translated_Order_Sheet.xlsx'
df_translated.to_excel(output_file, index=False, header=False)

# Stop the timer, calculate elapsed time, and print
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Translation and saving completed in {elapsed_time:.2f} seconds.")