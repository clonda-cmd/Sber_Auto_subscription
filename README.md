🚀 Прогнозирование целевого действия пользователя
https://img.shields.io/badge/python-3.8+-blue.svg
https://img.shields.io/badge/CatBoost-latest-orange.svg
https://img.shields.io/badge/FastAPI-0.68+-green.svg
https://img.shields.io/badge/license-MIT-blue.svg

Сервис для предсказания совершения пользователем целевого действия на основе данных о визитах и поведении.

📊 Метрика качества
ROC-AUC ≈ 0.65 — модель успешно предсказывает факт совершения целевого действия

📋 Содержание
Описание задачи

Глоссарий

Архитектура решения

Установка и запуск

API Endpoints

Примеры запросов

Структура проекта

Технологии

🎯 Описание задачи
Разработана модель машинного обучения для прогнозирования вероятности совершения пользователем целевого действия (оформление заявки или заказ звонка) на основе данных о визите:

Источники трафика (utm_*)

Характеристики устройства (device_*)

Географические данные (geo_*)

Поведенческие паттерны

Вход: атрибуты визита пользователя
Выход: бинарный прогноз (0/1) и вероятность целевого действия

📚 Глоссарий
🎯 Целевое действие
События, свидетельствующие о заинтересованности пользователя:

sub_car_claim_click — клик по заявке на авто

sub_car_claim_submit_click — отправка заявки

sub_open_dialog_click — открытие диалога

sub_custom_question_submit_click — отправка вопроса

sub_call_number_click — клик по номеру телефона

sub_callback_submit_click — заказ обратного звонка

sub_submit_success — успешная отправка

sub_car_request_submit_click — запрос по авто

📈 CR (Conversion Rate)
Конверсия из визита (session_id) в целевое действие. При наличии нескольких целевых действий в рамках одного визита — считается как одно.

🌿 Органический трафик
Визиты с utm_medium в:

organic

referral

(none)

💰 Платный трафик
Весь неорганический трафик (все остальные utm_medium).

📱 Реклама в соцсетях
Визиты с utm_source:

QxAxdyPLuQMEcrdZWdWb

MvfHsxITijuriZxsqZqt

ISrKoXQCxqqYvAZICvjs

IZEXUFLARCUMynmHNBGo

PlbkrSYoHuZBWfYjYnfw

gVRrcxiDQubJiljoTbGm

🏗 Архитектура решения
text
┌─────────────────────────────────────────────────────────────┐
│                     Входные данные                          │
│  (utm_*, device_*, geo_*, visit_date, visit_time, ...)      │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Preprocessing Pipeline                         │
│  • Обработка пропусков                                      │
│  • Кодирование категориальных признаков                     │
│  • Обработка неизвестных значений                           │
│  • Генерация новых признаков                                │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   CatBoost Classifier                       │
│              (обучен на исторических данных)                │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     Выходные данные                         │
│          • prediction: 0/1                                  │
│          • probability: 0.00 - 1.00                         │
└─────────────────────────────────────────────────────────────┘


Тело запроса:

json
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
Успешный ответ:

json
{
  "success": true,
  "prediction": 0,
  "probability": 0.0091,
  "timestamp": "2026-07-14T15:30:45.123456"
}
Ответ с ошибкой:

json
{
  "success": false,
  "error": "Missing required field: visit_date",
  "timestamp": "2026-07-14T15:30:45.123456"
}
Пакетный запрос
POST /predict_batch

json
{
  "data": [
    {
      "visit_number": 1,
      "visit_date": "2021-06-15",
      "utm_source": "google",
      ...
    },
    {
      "visit_number": 2,
      "visit_date": "2021-06-16",
      "utm_source": "facebook",
      ...
    }
  ]
}



Реализация      
✅ Полный preprocessing pipeline

✅ Обработка пропусков и неизвестных значений

✅ Поддержка JSON API

✅ Сохранение модели в .cbm (CatBoost)

✅ Сохранение конфигурации в .json

