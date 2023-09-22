import json
from markdown_it import MarkdownIt

# Read the content of the markdown file
with open('docs.md', 'r') as file:
    markdown_text = file.read()

# Initialize the Markdown parser
md = MarkdownIt()

# Parse the markdown text
parsed = md.parse(markdown_text)

# Initialize the JSON structure
result = {}

# Initialize a stack to keep track of headings and their levels
stack = []

# Iterate through the parsed Markdown tokens
for token in parsed:
    if token.type == 'heading_open':
        # Get the heading level
        heading_level = int(token.tag[1])
        
        # Get the heading text from the next token (heading_close)
        heading_text = parsed[parsed.index(token) + 1].content
        
        # Pop stack until the appropriate level is reached
        while len(stack) >= heading_level:
            stack.pop()
        
        # Create a nested structure for the heading
        nested_structure = result
        for i in stack:
            nested_structure = nested_structure[i]
        
        # Add the heading to the nested structure
        if heading_text not in nested_structure:
            nested_structure[heading_text] = {}
        
        # Append the heading to the stack
        stack.append(heading_text)

# Convert the result to a JSON string
json_data = json.dumps(result, indent=2)

# Print the JSON data
print(json_data)



