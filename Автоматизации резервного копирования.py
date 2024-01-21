import shutil
import os
from datetime import datetime

def backup_directory(source_dir, target_dir):
    try:
        # Создаем временную метку для добавления к имени целевой директории
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Формируем имя целевой директории с временной меткой
        target_dir_with_timestamp = f"{target_dir}_backup_{timestamp}"
        
        # Копируем все файлы из исходной директории в целевую
        shutil.copytree(source_dir, target_dir_with_timestamp)
        
        print(f"Резервное копирование завершено. Исходная директория: {source_dir}, Целевая директория: {target_dir_with_timestamp}")
    
    except Exception as e:
        print(f"Ошибка при выполнении резервного копирования: {e}")

# Укажите путь к исходной и целевой директориям
source_directory = "/путь/к/исходной/директории"
target_directory = "/путь/к/целевой/директории"

# Вызываем функцию для резервного копирования
backup_directory(source_directory, target_directory)
