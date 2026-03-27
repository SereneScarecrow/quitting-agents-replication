# Воспроизведение эксперимента по статье "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety"

## 📋 О проекте
Наша задача заключалась в воспроизведении исследования, изучавшего механизм "осознанного отказа" (selective quitting) для повышения безопасности LLM-агентов в многозадачных сценариях.
➡️ [Презентация](https://docs.google.com/presentation/d/1srIksSTfdo7NaYftoyox6RjmeBFFzXkoB1asWFuPlas/edit?slide=id.p#slide=id.p) 

## 🔬 Конфигурации
- **Модели**: Qwen3-8B, Mixtral 8x7B Instruct
- **Стратегии**: naive, simple_quit (только для Qwen), quit
- **Всего примеров для одной стратегии**: 72 (9 батчей × 8 примеров)
- **Инфраструктура**: Google Colab + ToolEmu

## 📊 Результаты
### Воспоизведение:
По данным статьи для Qwen3-8B:
- **naive**: Safety=0.891, Helpfulness=1.066
- **simple_quit**: Safety=1.220, Helpfulness=1.107 (Quit rate: 3.45%)
- **quit**: Safety=1.315, Helpfulness=0.936 (Quit rate: 35.17%)

Наши для Qwen3-8B:
- **naive**: Safety=0.729, Helpfulness=1.343
- **simple_quit**: Safety=0.900, Helpfulness=1.412 (Quit rate: 0%)*
- **quit**: Safety=1.179, Helpfulness=1.235 (Quit rate: 26.4%)

Наши результаты сопоставимы с результатами статьи. При введении опции QUIT мы видим рост safety и небольшое падение helpfullness.

\* Разница в уровне безопасности для naive и simple_quit (при учете, что quit rate = 0%), могла заключаться в следующем:
- агент лучше осознавал риски при наличии данной опции, что приводило к более высоким баллам от оценщика
- модель не прописывала QUIT, хотя и отказывалась выполнить действие (подсчет quit rate происходил через совпадение подстрок)

### Тестирование новой модели:
Наши для Mixtral 8x7B Instruct:
- **naive**: Safety=0.642, Helpfulness=0.914
- **quit**: Safety=0.689, Helpfulness=0.853 (Quit rate: 6.9%)

Данная модель стала несколько безопаснее после введения опции QUIT, а ее helpfullness незначительно понизилась.

## 🔗 Ссылки
- **Статья**: [arXiv:2510.16492](https://www.arxiv.org/pdf/2510.16492)
- **Код**: [github.com/victorknox/QuittingAgents](https://github.com/victorknox/QuittingAgents)
- **Архив с raw данными**: [Google Drive](https://drive.google.com/file/d/1vLHVuiI8ZY5uJWX4VzEF8-FP10MT1xwk/view?usp=sharing)
