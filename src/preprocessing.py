# preprocessing.py
import pandas as pd
from config import Config

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    """
    Обрабатывает входной DataFrame (один или много визитов).
    Возвращает только нужные признаки с пропусками, кодированием и т.д.
    """
    # Копия исходного DataFrame
    df = df.copy()

    required = [
        "visit_number",
        "visit_date",
        "visit_time",
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
        "geo_city"
    ]

    missing = [col for col in required if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    # 1. Генерируем hour и weekday
    visit_datetime = pd.to_datetime(df['visit_date'].astype(str) + ' ' + df['visit_time'].astype(str), errors='coerce')
    df['hour'] = visit_datetime.dt.hour
    df['weekday'] = visit_datetime.dt.dayofweek

    # 3. Органический/соц-трафик
    df['is_organic'] = df['utm_medium'].isin(Config.ORGANIC).astype(int)
    df['is_social'] = df['utm_source'].isin(Config.SOCIAL_SOURCES).astype(int)

    # 4. Категориальные → заполнить 'unknown'
    for col in Config.CAT_FEATURES:
        if col in df.columns:
            df[col] = df[col].fillna('unknown').astype(str)

    # 5. Оставляем только нужные колонки в правильном порядке
    df = df[Config.FEATURES]

    return df