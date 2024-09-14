from script1 import gemini_content as gemini_content3, similarity as similarity3, chunk as chunk3, query as query3
from script2 import gemini_content1 as gemini_content2, similarity1 as similarity2, chunk1 as chunk2, query1 as query2
from script3 import gemini_content2 as gemini_content4, similarity2 as similarity4, chunk2 as chunk4, query2 as query4
from script4 import gemini_content3 as gemini_content5, similarity3 as similarity5, chunk3 as chunk5, query3 as query5
from script5 import gemini_content4 as gemini_content6, similarity4 as similarity6, chunk4 as chunk6, query4 as query6
from script6 import gemini_content5 as gemini_content7, similarity5 as similarity7, chunk5 as chunk7, query5 as query7

import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys
import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()
api_key = os.getenv('key')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

response1 = gemini_content3(query3, chunk3)
response2 = gemini_content2(query2, chunk2)
response3 = gemini_content4(query4, chunk4)
response4 = gemini_content5(query5, chunk5)
response5 = gemini_content6(query6, chunk6)
response6 = gemini_content7(query7, chunk7)

final_prompt = f"Combine the responses from {response1},{response2}, {response3},{response4},{response5} and {response6}and modify it a bit, do not return it just like how it is in the pdf"

gemini_final_response = model.generate_content(final_prompt)

print()
print()
print("Gemini Final Response:")
print(gemini_final_response.text)

