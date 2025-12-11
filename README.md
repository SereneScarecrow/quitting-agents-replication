# Воспроизведение эксперимента "Selectively Quitting"

## 🎯 Цель
Воспроизвести эксперимент из статьи о механизме quitting для LLM-агентов, используя модель Qwen3-8B.

## 🔬 Конфигурация
- **Модель**: Qwen3-8B
- **Стратегии**: naive, simple_quit, quit
- **Всего примеров для одной стратегии**: 72 (9 батчей × 8 примеров)
- **Инфраструктура**: Google Colab + ToolEmu

## 📊 Ожидаемые результаты
По данным статьи для Qwen3-8B:
- **naive**: Safety=0.891, Helpfulness=1.066
- **simple_quit**: Safety=1.220, Helpfulness=1.107  
- **quit**: Safety=1.315, Helpfulness=0.936

## 🔗 Ссылки
- Статья: arXiv:2510.16492
- Код: github.com/victorknox/quitting-agents
