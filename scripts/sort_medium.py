import os
import re
path = r''
files = os.listdir(path)

def get_numeric_prefix(filename):
    match = re.match(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

sorted_files = sorted(files, key=get_numeric_prefix)


for i, filename in enumerate(sorted_files, start=1):
    src = os.path.join(path, filename)

    new_name = re.sub(r'^\d+_', '', filename)
    dst = os.path.join(path, f'{i:03d}_{new_name}')
    os.rename(src, dst)

print("sorted")
