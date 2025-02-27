---
title: "Arhitecture and Infrastructure"
date: 2024-11-30T17:20:22+03:00
draft: false
description: "Arhitecture and Infrastructure"
summary: ""
---

{{< toc >}}

## Cache

- Server
    - Patterns
        - Cache-Aside
            - Advantages
                - Устойчивость к сбоям кеша
                - Модель данных в кеше может отличаться от модели данных в БД
            - Disadvantages
                - Низкая скорость обновления данных
                - Несогласованность данных в кеше с базой данных
        - Read-Through
            - Advantages
                - Меньшая сложность приложения и низкая вероятность ошибок
            - Disadvantages
                - Кеш-промах при первом запросе
                - Ограничения на выбор модели данных в кеше
                - Чувствительность к ошибкам в отличие от Cache-Aside
        - Refresh-ahead
            - Advantages
                - Низкая стоимость чтения данных из БД
                - Согласованность записей кеша, к которым часто обращаются пользователи
                - Высокая чувствительность к задержкам
            - Disadvantages
                - Кеш должен работать без ошибок, поскольку в случае ошибки это будет не сразу определено и приведёт к неконсистентности данных и чтению из базы.
        Write-Through
            - Advantages
                - Данные между кешем и базой данных всегда будут синхронизированы
            - Disadvantages
                - Необходимость ждать, пока кеш обновит базу данных
        - Write-Behind
    - Invalidation
        - Time-based
        - Purge Cache
        - Refresh Cache
        - Time-To-Live(TTL) expiration Cache
        - Key-based
- Client

## HighLoad
- Patterns
    - Backpressure
    - Circuit Breaker

## Observability
- Monitoring
    - USE
        - Utilization
        - Saturation
        - Errors
- 4 Golden Signals
    - Latency
    - Traffic
    - Errors
    - Saturation
- RED
    - Requests Rate
    - Errors
    - Duration

## Сloud computing

- Types
    - Deployment Model
        - Private Cloud
        - Public Cloud
        - Hybrid Cloud
    - Service Model
        - SaaS
        - PaaS
        - IaaS
- Migration
    - 6R Migration Strategy
        1. Retain. Частичная миграция.
        2. Retire. Замена части функциональности облачными решениями.
        3. Rehost or Lift and Shift. Миграция без изменений.
        4. Repurchase or Drop and Shop. Отказ от текущей реализации и полный переход на обланые решения.
        5. Replatform or Lift and Reshape. Минимальные изменения для использования преимуществ облачных решений.
        6. Refactor or Re-architect. Полная переработка текущей реализации под облачные решения.

## AI

1. Формирование бизнес-требований и технологического стека
2. Сбор данных
3. Подготовка данных
4. Анализ данных
5. Моделирование
6. Оценка модели и решения
7. Принятие решений
8. Мониторинг

CRISP-DM

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Data Modeling
5. Evaluation
6. Deployment

