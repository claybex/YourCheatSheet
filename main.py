import markdown, os 
import markdown_to_json

files = os.listdir('.')
markdown_files = [file for file in files if file.endswith(('.MD','.MD'))]
#Parsing md files 
for file in markdown_files:    
    with open(file, 'r') as f:
        text = f.read()
        dictified = markdown_to_json(text)
        print(dictified)

      