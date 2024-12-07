import os
import re

path = r''

files = os.listdir(path)


for filename in files:
    src = os.path.join(path, filename)
    new_name = re.sub(r'^\d+_', '', filename)
    dst = os.path.join(path, new_name)
    os.rename(src, dst)

print("Числовые префиксы успешно удалены из имен файлов.")
