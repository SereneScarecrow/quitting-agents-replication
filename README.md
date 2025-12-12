# Воспроизведение эксперимента "Selectively Quitting"

## 🎯 Цель
Воспроизвести эксперимент из статьи о механизме quitting для LLM-агентов, используя модель Qwen3-8B.

## 🔬 Конфигурация
- **Модель**: Qwen3-8B
- **Стратегии**: naive, simple_quit, quit
- **Всего примеров для одной стратегии**: 72 (9 батчей × 8 примеров)
- **Инфраструктура**: Google Colab + ToolEmu

## 📊 Результаты
По данным статьи для Qwen3-8B:
- **naive**: Safety=0.891, Helpfulness=1.066
- **simple_quit**: Safety=1.220, Helpfulness=1.107 (Quit rate: 3.45%)
- **quit**: Safety=1.315, Helpfulness=0.936 (Quit rate: 35.17%)

Наши для Qwen3-8B:
- **naive**: Safety=0.729, Helpfulness=1.343
- **quit**: Safety=1.179, Helpfulness=1.235 (Quit rate: 26.4%)

## 🔗 Ссылки
- [**Презентация**](https://docs.google.com/presentation/d/1srIksSTfdo7NaYftoyox6RjmeBFFzXkoB1asWFuPlas/edit?slide=id.p#slide=id.p)
- **Статья**: [arXiv:2510.16492](https://www.arxiv.org/pdf/2510.16492)
- **Код**: [github.com/victorknox/QuittingAgents](https://github.com/victorknox/QuittingAgents)
- **Архив с raw данными**: [Google Drive](https://drive.google.com/file/d/1vLHVuiI8ZY5uJWX4VzEF8-FP10MT1xwk/view?usp=sharing)
