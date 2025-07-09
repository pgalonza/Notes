---
title: "Micro services and frontends"
date: 2024-10-02T21:33:00+03:00
draft: false
description: "Microservices and Microfrontends"
---

{{< toc >}}

## MicroFrontends

- Преимущества
    - Организационная гибкость
    - Свобода выбора технологического стека
    - Удобство управления кодовой базой
    - Управляемое масштабирование
    - Отказоустойчивость
    - Time to Market
- Не подходящее решение
    - Простое приложение
    - Ограниченная функциональность
    - Ограниченный ресурс разработки
    - Тесносвязанные компоненты
    - Minimum Viable Produrct или Proof Of Concept
    - Повышенная требовательность к производительности
    - Организационные и культурные ограничения комании
    - Недостаточность инфраструктуры, процессов и инструментов CI/CD
- Компоненты
    - Microfrontend-модули
    - Слой композиции
        - Гибридная
        - Серверная композиция
            - Reverce Proxy(Nginx? HAProxy)
            - Backend for Frontend(BFF)
                - Подготовка данных под клиента
                - Упрощение логики клиента
                - Увеличение производительности
                - Повышение безопасности
            - API Composer
        - Клиентская композиция
            - Single SPA
            - Module Federation
    - Маршрутизация
        - Гибридная
        - На стороне сервера
        - На стороне клиента
        - Динамическая
    - Слой коммуникации
        - API
            - Взаимодействие исключительно с backend
            - Простой обмен данными
            - Высокие требование к производительности и масштабируемости
        - Паттерн  Publisher/Subscriber
            - Отсутсвие прямых зависимостей
            - Еvent-driven architecture
            - Независимое внедрение
        - Global state or Shared state
            - Тесная связь между разными частями приложения
            - Согласованность в разных частях приложения и последовательный пользовательский опыт
            - Слажные требования к управлению состояниями
- Стратегии
    - Вертикальная нарезка
    - Автономность команд
    - Изоляция
- Методы интеграции
    - Build time
        - Упращенное внедрение
        - Тесное взаимодействие функций и компонентов
        - Прозводительность
    - Run time
        - Независимость внедрения модулей
        - Динамическо обновление модулей(Разработка)
        - Масштабирование


## MicroServices

### Monolith separation

- [Patterns](/arhitecture/arhitecture-and-infrastructure/#migration-patterns)
- Road Map
    - Граицы сервисов
    - Методы взаимодействия
        - Синхронное взаимодействие
            - RESTful
            - GRPC
            - OpenAPI
        - Асинхронное взаимодействие
            - Event-Driven Architecture
                1. Анализ домена
                2. Описание доменной модели
                3. Декомпозиция функциональности
                4. Моделирование потоков событий
                5. Моделирование событий
                6. Выбор брокера событий
                7. Реализация и мониторинг
                8. Тестирование и валидация
            - AsyncAPI
    - Управление данными
        - Стратегии обеспечения согласованности данных
            - Конечная согласованность
            - Строгая согласованность
            - Партицирование данных
        - Распределённые транзакции
            - Протокол двухфазной фиксации (2 Phase Commit, 2PC)
            - Паттерн Saga
                - Eventual Consistency
    - Стратегии развёртывания
        - Blue-Green
        - Canary
        - Rolling
    -  Балансировки нагрузки
        - Стратегии
            - Round Robin
            - Least Connections
            - IP Hash, Sticky sessions
            - Weighted Round Robin
            - Random distribution
            - Least Response Time
            - Least Bandwidth
    - Устойчивость к сбоям
    - Масштабируемость
        - Репликация
        - Кэширование
        - Шардирование и партиционирование
            - Партиционирование
                - Вертикальное
                - Горизонтальное
            - Шардирование
                - Хэшированное
                - Диапазонное
                - Динамическое
                - Геошардинг
            - Маршрутизация
                - Средствами СУБД
                - Router-сервис
                - На стороне клиента
    - Безопасность
    - Мониторинг и наблюдение
    - Хранение данных
    - API-менеджмент
    - Тестирование и валидация
    - DevOps-практики
    - Версионирование и совместимость
- Life Cicle
    - Проектирование
    - Разработка
    - Тестирование
    - Развёртывание
    - Мониторинг и поддержка
    - Масштабирование
    - Обновление и улучшение
    - Вывод из эксплуатации


## Patterns

1. Application patterns
    - Database per Service
    - Service per Team
    - Event Sourcing
    - Stream Processing
        - Синхронная микропакетная обработка
        - Асинхронная микропакетная обработка
        - Streaming-модель
        - Модель непрерывного обновления
    - Message Queueing
    - Publish/Subscribe
    - CQRS
        - Commands
        - Queries
        - Реализация
            1. Определение команд и запросов
            2. Реализация моделей данных
            3. Реализация обработчиков команд и запросов
            4. Доработка систем-потребителей для возможности интеграции с различными компонентами для отправки запросов и команд
    - Saga
        - Типы реализации
            - Orchestration
                - Сложные бизнес-процессы
                - Потребность в централизованном управлении
                - Транзакционное согласование
                - Сложная бизнес-логик
            - Choreography
                - Простые взаимодействия
                - Независимые микросервисы
                - В приоритете гибкость и масштабируемость
                - Событийно-ориентированная архитектура
        - Обрабока ошибок и компенсация
            - Компенсационные транзакции
            - Повторные попытки
            - Тайм-ауты и дедлайны
            - Событийно-ориентированная обработка ошибок
            - Системы мониторинга и алертов
        - Реализация
            - Анализ бизнес-процесса и определение шагов Saga
            - Проектирование микросервисов
            - Управление состоянием и взаимодействием микросервисов
            - Реализуйте действия и компенсирующие действия
            - Логирование и мониторинг
            - Тестирование
    - Transactional outbox
    - Transaction log tailing
2. Application infrastructures patterns
    - Distributed Tracing
    - Audit Logging
    - API Gateway
        - Types
            - Монолитный
            - Распределенный
            - Многослойный
            - Serveless
        - Functions
            - Централизация маршрутизации запросов
            - Управление аутентификацией и авторизацией
            - Балансировка нагрузки и распределение трафика
            - Обеспечение безопасности
            - Кэширование запросов
    - Front-to-back
        - Client pull
            - Patterns
                - Short polling
                - Long polling
            - Implementations
                - REST
                - GraphQL
        - Server push
            - Implementations
                - WebSockets
                - Server sent events
                - GraphQL Subscriptions
    - Back-to-back
        - Patterns
            - Request-Response
            - Publish-Subscribe
        - Implementations
            - REST
            - GraphQL
            - gRPC
3. Infrastructures patterns
    - Service Discovery,
    - Service Mesh
    - Service Registry

## Principles

- The Twelve-Factor App
    - Codebase
    - Dependencies
    - Config
    - Backing Services
    - Build, Release, Run
    - Processes
    - Port Binding
    - Concurrency
    - Disposability
    - Dev/Prod Parity
    - Logs
    - Admin Processes
- Lightweight microservices
    - Минимализм
    - Независимость
    - Быстрое время запуска
    - Эффективное использование ресурсов
    - Упрощение зависимостей
    - Обеспечение изоляции
    - Документирование и автоматизация
- DevOps
    - Pipeline as Code
        - Повторяемость
        - Гибкость
        - Версионирование
        - Прозрачность
        - Масштабируемость
        - Подверженность ошибкам
    - Infrastructure as Code
    - CI/CD
        - Continuous Integration
        - Continuous Delivery
        - Continuous Deployment

## Identification, Authentication, Athorization

- SSO(Single Sign-On)
    - OAuth(Open Authorization)
        - Roles
            - Resource owner
            - Resource server
            - Authorization server
            - Client
            - User-agent
        - Storing the refresh tokens
            - Server
            - HTTP-only cookie
            - LocalStorage
            - WebWorker
        - Flow
            - Authorization code
            - Implicit
            - Resource owner password credentials
            - Client credentials
            - Device authorizatio
        - RFC
            - [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)
            - [RFC 6749](https://datatracker.ietf.org/doc/rfc6749/)
    - OpenID Connect
    - SAML(Security Assertion Markup Language)
    - Kerberos