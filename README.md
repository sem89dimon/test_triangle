# test_triangle


## Для запуска тестов необходимо установить виртуальное окружение:
python - m venv venv
## Активация виртуального окружения
venv\Scripts\activate

## Установить зависимости: 
pip install -r requirements.txt

## Теперь можно запускать тесты:
pytest -sv --alluredir=allure-results

## Для генерации отчета:
allure serve allure-results

