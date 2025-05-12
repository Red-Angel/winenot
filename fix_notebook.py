import json

# Open the notebook file
with open('Assignment2_supervised_learning_flow.ipynb', 'r', encoding='utf-8') as file:
    notebook = json.load(file)

# Iterate through cells and find the problematic line
fixed = False
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        # Join the source lines to search for the problematic pattern
        source_text = ''.join(cell['source'])
        
        # Check if this is the problematic cell
        if "sns.kdeplot(X_train[X_train.index[y_train == target]][feature]" in source_text:
            # Fix the line by replacing it with the correct syntax
            new_source = []
            for line in cell['source']:
                if "sns.kdeplot(X_train[X_train.index[y_train == target]][feature]" in line:
                    new_line = line.replace(
                        "sns.kdeplot(X_train[X_train.index[y_train == target]][feature]",
                        "sns.kdeplot(X_train.loc[y_train == target, feature]"
                    )
                    new_source.append(new_line)
                    fixed = True
                else:
                    new_source.append(line)
            
            cell['source'] = new_source

# Save the modified notebook
if fixed:
    with open('Assignment2_supervised_learning_flow.ipynb', 'w', encoding='utf-8') as file:
        json.dump(notebook, file, indent=1)
    print("Notebook has been fixed!")
else:
    print("Could not find the problematic code.") 