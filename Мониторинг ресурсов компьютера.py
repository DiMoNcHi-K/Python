import psutil
import time

def monitor_resources(interval=1):
    try:
        while True:
            # Получаем информацию о CPU
            cpu_percent = psutil.cpu_percent(interval=interval)
            
            # Получаем информацию о памяти
            memory_info = psutil.virtual_memory()
            
            # Получаем информацию о дисковом пространстве
            disk_info = psutil.disk_usage("/")
            
            # Выводим информацию на экран
            print(f"CPU: {cpu_percent}%")
            print(f"Память: {memory_info.percent}% используется")
            print(f"Диск: {disk_info.percent}% занято")
            print("-" * 30)
            
            # Ждем указанный интервал перед следующим измерением
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("Мониторинг завершен.")

# Вызываем функцию для мониторинга ресурсов
monitor_resources()
