import os
import re

# Укажите полный путь к директории с файлами
path = r'D:\A_Local_reps\CodeWorkGrind\LeetCode\Easy'

# Получаем список файлов в директории
files = os.listdir(path)

# Функция для получения числового префикса из имени файла
def get_numeric_prefix(filename):
    match = re.match(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

# Сортируем файлы по числовому префиксу
sorted_files = sorted(files, key=get_numeric_prefix)

# Переименовываем файлы в отсортированном порядке с добавлением префикса
for i, filename in enumerate(sorted_files, start=1):
    src = os.path.join(path, filename)
    # Удаляем старый префикс, если он есть
    new_name = re.sub(r'^\d+_', '', filename)
    dst = os.path.join(path, f'{i:03d}_{new_name}')
    os.rename(src, dst)

# Повторно получить список файлов после удаления префиксов
files = os.listdir(path)

# Повторно сортируем файлы по числовому префиксу
sorted_files = sorted(files, key=get_numeric_prefix)

# Переименовываем файлы в отсортированном порядке с добавлением префикса
for i, filename in enumerate(sorted_files, start=1):
    src = os.path.join(path, filename)
    # Удаляем старый префикс, если он есть
    new_name = re.sub(r'^\d+_', '', filename)
    dst = os.path.join(path, f'{i:03d}_{new_name}')
    os.rename(src, dst)

print("Файлы успешно отсортированы и переименованы.")
