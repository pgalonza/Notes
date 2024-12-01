---
title: "Arhitecture and Infrastructure"
date: 2024-11-30T17:20:22+03:00
draft: false
description: "Arhitecture and Infrastructure"
summary: ""
---

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
    - Curcuit Breaker


