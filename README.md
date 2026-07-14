Задача:

- Научитесь предсказывать совершение целевого действия
(ориентировочное значение ROC-AUC ~ 0.65) — факт совершения
пользователем целевого действия.
- Упакуйте получившуюся модель в сервис, который будет брать на
вход все атрибуты, типа utm_*, device_*, geo_*, и отдавать на выход
0/1 (1 — если пользователь совершит любое целевое действие).


Глоссарий:

**Целевое действие** — события типа «Оставить заявку» и «Заказать звонок»
(ga_hits.event_action in ['sub_car_claim_click', 'sub_car_claim_submit_click',
'sub_open_dialog_click', 'sub_custom_question_submit_click',
'sub_call_number_click', 'sub_callback_submit_click', 'sub_submit_success',
'sub_car_request_submit_click']).

**CR (Conversion Rate)** — показатель конверсии из визита (уникальный
session_id) в любое целевое действие в рамках одного визита (в случае
наличия >1 целевого действия — считать все как одно).

**Органический трафик** — все визиты с ga_sessions.utm_medium in ('organic',
'referral', '(none)').

**Платный трафик** — весь неорганический трафик.

**Информация про марку и модель авто** — содержится в ga_hits.hit_page_path.

**Реклама в социальных сетях** — все визиты с ga_sessions.utm_source in
('QxAxdyPLuQMEcrdZWdWb', 'MvfHsxITijuriZxsqZqt', 'ISrKoXQCxqqYvAZICvjs',
IZEXUFLARCUMynmHNBGo', 'PlbkrSYoHuZBWfYjYnfw',
'gVRrcxiDQubJiljoTbGm').


Данные:

**ga_sessions** *(одна строка = один визит на сайт)*
Описание атрибутов:
- session_id — ID визита;
- client_id — ID посетителя;
- visit_date — дата визита;
- visit_time — время визита;
- visit_number — порядковый номер визита клиента;
- utm_source — канал привлечения;
- utm_medium — тип привлечения;
- utm_campaign — рекламная кампания;
- utm_keyword — ключевое слово;
- device_category — тип устройства;
- device_os — ОС устройства;
- device_brand — марка устройства;
- device_model — модель устройства;
- device_screen_resolution — разрешение экрана;
- device_brand — марка устройства;
- device_model — модель устройства;
- device_screen_resolution — разрешение экрана;
- device_browser — браузер;
- geo_country — страна;
- geo_city — город.

**ga_hits** *(одна строка = одно событие в рамках одного визита на сайт)*
Описание атрибутов:
- session_id — ID визита;
- hit_date — дата события;
- hit_time — время события;
- hit_number — порядковый номер события в рамках сессии;
- hit_type — тип события;
- hit_referer — источник события;
- hit_page_path — страница события;
- event_category — тип действия;
- event_action — действие;
- event_label — тег действия;
- event_value — значение результата действия.              
  

==============================================================
=============================================

  *Использован CatBoost*      
  *Реализован preprocessing pipeline*      
  *Обработка пропусков и неизвестных значений*      
  *Поддержка JSON API*      
  *Сохранение модели в .cbm*      
  *Сохранение конфигурации в .json*            

==============================================================
=============================================
1. Установка зависимостей
   

- pip install -r requirements.txt

2. Запуск API

- python app.py

http://localhost:8000


3. Запрос

Json      
{      
  "data": {      
    "visit_number": 1,      
    "visit_date": "2021-06-15",      
    "visit_time": "14:30:25",      
    "utm_source": "google",      
    "utm_medium": "organic",      
    "utm_campaign": "campaign1",      
    "utm_adcontent": "ad1",      
    "utm_keyword": "car",      
    "device_category": "mobile",      
    "device_os": "Android",      
    "device_brand": "Samsung",      
    "device_browser": "Chrome",      
    "geo_country": "Russia",      
    "geo_city": "Moscow"      
  }      
}      

4. Ответ      

Json      
{      
  "success": true,      
  "prediction": 0,      
  "probability": 0.0091      
}      
