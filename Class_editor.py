import os

# Specify the directory containing your YOLO annotation files
directory = "path/to/your/annotation_directory"

# Function to modify the first value from 0 to 1 in a single file
def modify_annotation_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            parts[0] = '1'
        modified_line = ' '.join(parts)
        modified_lines.append(modified_line)

    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines))

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        modify_annotation_file(file_path)

print("First value in all YOLO annotation files within the directory has been changed from 0 to 1.")