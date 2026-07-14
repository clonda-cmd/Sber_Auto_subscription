# congig.py
from pathlib import Path
import pandas as pd

class Config:
    """Класс конфигурации"""

    BASE_DIR = Path(__file__).resolve().parent

    # ----- ПУТИ -----
    PATHS = {
        'sessions': BASE_DIR / 'data' / 'ga_sessions.csv',
        'hits': BASE_DIR / 'data' / 'ga_hits.csv'
    }

    # ----- МОДЕЛЬ -----
    MODEL_PATH = BASE_DIR / 'model' / 'catboost_model.cbm'
    MODEL_CONFIG_PATH = BASE_DIR / 'model' / 'model_config.json'
    
    # ----- ВОСПРОИЗВОДИМОСТЬ -----
    RANDOM_STATE = 42

    # ----- ТАРГЕТ -----
    TARGET_ACTIONS = ['sub_car_claim_click',  # клик по оформлению заявки на авто
                      'sub_car_claim_submit_click',  # отправка заявки на авто
                      'sub_open_dialog_click',  # открытие диалога
                      'sub_custom_question_submit_click',  # отправка вопроса
                      'sub_call_number_click',  # клик по номеру телефона
                      'sub_callback_submit_click',  # отправка заявки на обратный звонок
                      'sub_submit_success',  # успешная отправка
                      'sub_car_request_submit_click'  # отправка запроса по авто
                      ]
    
    # ----- Органический трафик -----
    ORGANIC = [
    'organic',
    'referral',
    '(none)'
    ]
    
    # ----- Реклама в социальных сетях -----
    SOCIAL_SOURCES = [
    'QxAxdyPLuQMEcrdZWdWb',
    'MvfHsxITijuriZxsqZqt',
    'ISrKoXQCxqqYvAZICvjs',
    'IZEXUFLARCUMynmHNBGo',
    'PlbkrSYoHuZBWfYjYnfw',
    'gVRrcxiDQubJiljoTbGm'
    ]

# ----- ПРИЗНАКИ -----
    FEATURES = [
        "visit_number",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_adcontent",
        "utm_keyword",
        "device_category",
        "device_os",
        "device_brand",
        "device_browser",
        "geo_country",
        "geo_city",
        "hour",
        "weekday",
        "is_organic",
        "is_social",
    ]


    CAT_FEATURES = [
        'utm_source',
        'utm_medium',
        'utm_campaign',
        'utm_adcontent',
        'utm_keyword',
        'device_category',
        'device_os',
        'device_brand',
        'device_browser',
        'geo_country',
        'geo_city'
    ]

    NUM_FEATURES = [
        'visit_number',
        'hour',
        'weekday',
        'is_organic',
        'is_social'
    ]

    # Колонки для удаления
    DROP_COLUMNS = [
        'session_id',
        'client_id',
        'visit_date',
        'visit_time',
        'device_screen_resolution'
    ]

     # ----- ПОРОГ  -----
    THRESHOLD = 0.70  
    

    
config = Config() 