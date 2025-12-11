import json
import os

def merge_jsons_in_folder(folder_path, output_file="combined.jsonl"):
    """
    Простая функция: передай путь к папке → получишь объединенный файл.
    
    Пример:
    merge_jsons_in_folder("C:/Users/user/quitting-agents/models/Qwen3-8B/naive")
    """
    
    # Проверяем папку
    if not os.path.exists(folder_path):
        print(f"❌ Папка не найдена: {folder_path}")
        return
    
    print(f"📁 Ищу .jsonl файлы в: {folder_path}")
    
    # Собираем все .jsonl файлы рекурсивно
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.jsonl'):
                full_path = os.path.join(root, file)
                all_files.append(full_path)
    
    if not all_files:
        print("❌ В папке нет .jsonl файлов")
        return
    
    print(f"   Найдено файлов: {len(all_files)}")
    
    # Объединяем
    merged_data = []
    for file_path in sorted(all_files):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        merged_data.append(json.loads(line))
            print(f"   ✓ {os.path.basename(file_path)}")
        except Exception as e:
            print(f"   ✗ Ошибка в {os.path.basename(file_path)}: {e}")
    
    # Сохраняем
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in merged_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"\n✅ Готово: {output_file}")
    print(f"   Записей: {len(merged_data)}")
    
    return output_file

# merge_jsons_in_folder("models/Qwen3-8B/naive/emulation/all_runs", "Qwen3-8B_naive_emu.jsonl")
merge_jsons_in_folder("models/Qwen3-8B/naive/evaluation/all_runs", "Qwen3-8B_naive_eval.jsonl")