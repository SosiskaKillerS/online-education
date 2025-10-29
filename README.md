[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=guid+for+project)](https://git.io/typing-svg)
p.s все команды на bash
## venv
Создание и активация .venv 
```bash 
python3 -m venv .venv 
source .venv/bin/activate 
``` 
установка зависимостей для работы с проектом 
```bush 
pip install requirements.txt 
``` 

## database 
Поднятие контейнера
```bush
docker compose -f docker-compose.dev.yaml up --build
```
Заполнение фейковыми данными бд 
```bush
python3 -m app.seed
```

## run project 
```bush
python3 -m app.main
```