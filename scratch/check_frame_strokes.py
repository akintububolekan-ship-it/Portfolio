with open(r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="736:16864"')
print(text[idx:idx+1500])
