import json
import os
import re
from pathlib import Path

def merge_sorted_dumps(base_folder, output_prefix="combined"):
    """
    Объединяет дампы в правильном порядке (0, 8, 16, ..., 64)
    
    base_folder - папка где лежат dumps_quit_0, dumps_quit_8 и т.д.
    Создает 3 файла: results_trajectories.jsonl, results_safety.jsonl, results_helpfulness.jsonl
    """
    
    # 1. Находим все папки dumps_quit_*
    dump_folders = []
    for item in os.listdir(base_folder):
        item_path = os.path.join(base_folder, item)
        if os.path.isdir(item_path) and item.startswith("dumps_"):
            dump_folders.append(item_path)
    
    # 2. Сортируем по номеру в конце
    def get_index(folder_path):
        match = re.search(r'dumps_(\d+)$', folder_path)
        return int(match.group(1)) if match else 999
    
    dump_folders.sort(key=get_index)
    
    print(f"📁 Найдено {len(dump_folders)} папок в порядке:")
    for folder in dump_folders:
        print(f"  {os.path.basename(folder)}")
    
    # 3. Создаем словарь для каждого типа файлов
    file_types = {
        'trajectories': [],    # Основные файлы
        'safety': [],          # eval_agent_safe
        'helpfulness': []      # eval_agent_help
    }
    
    # 4. Собираем файлы в правильном порядке
    for folder in dump_folders:
        for file in os.listdir(folder):
            if file.endswith('.jsonl'):
                file_path = os.path.join(folder, file)
                
                if '_eval_agent_safe' in file:
                    file_types['safety'].append(file_path)
                elif '_eval_agent_help' in file:
                    file_types['helpfulness'].append(file_path)
                elif '_eval_' not in file:  # Основной файл
                    file_types['trajectories'].append(file_path)
    
    # 5. Объединяем каждый тип
    for file_type, files in file_types.items():
        if not files:
            print(f"⚠️  Нет файлов типа: {file_type}")
            continue
        
        output_file = f"{output_prefix}_{file_type}.jsonl"
        total_records = 0
        
        print(f"\n📊 Объединяем {len(files)} файлов типа '{file_type}' → {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for file_path in files:
                folder_name = os.path.basename(os.path.dirname(file_path))
                file_name = os.path.basename(file_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_f:
                        records = []
                        for line in in_f:
                            if line.strip():
                                records.append(line.strip())
                        
                        # Записываем все записи из файла
                        for record in records:
                            out_f.write(record + '\n')
                        
                        total_records += len(records)
                        print(f"  ✓ {folder_name}/{file_name} ({len(records)} записей)")
                        
                except Exception as e:
                    print(f"  ✗ Ошибка в {file_name}: {e}")
        
        print(f"  Всего записей: {total_records}")


if __name__ == "__main__":
    # Путь к папке с dumps_quit_* папками
    base_path = "C:/Users/user/dumps/dumps_naive"
    merge_sorted_dumps(base_path, "naive_results")