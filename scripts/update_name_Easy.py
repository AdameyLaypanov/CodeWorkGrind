import os
import re

# Укажите полный путь к директории с файлами
path = r'D:\A_Local_reps\CodeWorkGrind\LeetCode\Medium\Suffix_Sum'

# Получаем список файлов в директории
files = os.listdir(path)

# Переименовываем файлы, удаляя числовые префиксы
for filename in files:
    src = os.path.join(path, filename)
    # Удаляем числовой префикс, если он есть
    new_name = re.sub(r'^\d+_', '', filename)
    dst = os.path.join(path, new_name)
    os.rename(src, dst)

print("Числовые префиксы успешно удалены из имен файлов.")
