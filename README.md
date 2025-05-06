## Раздел 1. Работа со скриптом 
Скрипт выполняет:
- 5 HTTP-запросов к https://httpstat.us/
- Логирует успешные ответы (1xx, 2xx, 3xx)
- Генерирует исключения для ошибок (4xx, 5xx)

#### Требования:
- Python 3.6+
- Библиотека `requests`

#### Установка:
```Bash
    pip install requests
```

#### Использование:
```Bash
    python3 script.py
```

## Раздел 2. Работа с Docker 

#### Требования
- Docker 20.10+
- Ubuntu 22.04

#### Установка
Сборка образа:

```bash
    docker build -t http_checker .
```

#### Использование
```bash
    docker run --rm http_checker
```
## Раздел 3: Ansible-плейбук

#### Требования
- Ansible 2.9+
- Доступ к целевому хосту (по SSH для удаленного)
- Пользователь `{{ user }}` имеет права sudo на целевом хосте
- Пользователь `{{ user }}`ключен в файл `/etc/sudoers` или группу `sudo`
- Для автоматического выполнения (без ввода пароля) добавьте в `/etc/sudoers`:
    ```bash
    {{ user }} ALL=(ALL) NOPASSWD: ALL
    ```

#### Установка
Установка зависимостей:
```bash
    pip install docker
    ansible-galaxy collection install community.docker
```
Подготовка inventory файла (опционально):
```ini
    [servers]
    server1 ansible_host=<ip адрес сервера>
```
#### Использование
```bash
# Для localhost
ansible-playbook playbook.yml -e "user=$(whoami)"

# Для удаленного хоста
ansible-playbook playbook.yml -i inventory.ini -e "target=server1 user=remote_user"
```

