# MySQL-Force 🔐🐍

Ferramenta simples de **brute force MySQL** desenvolvida em **Python 3**, voltada **exclusivamente para CTFs, laboratórios e ambientes autorizados**.

O script tenta autenticar em um servidor MySQL/MariaDB utilizando um usuário fixo e uma wordlist de senhas, retornando a credencial válida caso encontrada.

---

## ⚠️ Aviso Legal

> Este projeto é destinado **apenas para fins educacionais**, CTFs e ambientes de teste **com autorização explícita**.  
> O uso desta ferramenta contra sistemas sem permissão é **ilegal**.

---

## 🚀 Funcionalidades

- Autenticação MySQL via brute force
- Suporte a argumentos via linha de comando
- Wordlist customizada
- Rate-limit para evitar lock/IDS
- Banner personalizado
- Compatível com MySQL e MariaDB

---

## 📦 Requisitos

- Python **3.x**
- Biblioteca `mysql-connector-python`

Instalação da dependência:
```bash
pip3 install mysql-connector-python
python3 -c "import mysql.connector; print('OK')"
```

## 🛠️ Uso
```bash
python3 mysql-force.py -u <usuario> -w <wordlist> -ip <ip_do_alvo>
```
## 📌 Parâmetros
Opção	Descrição
- -u, --user	Usuário MySQL
- -w, --wordlist	Arquivo de wordlist
- -ip, --ip	IP do servidor MySQL
- -p, --port	Porta MySQL (padrão: 3306)
- -d, --database	Database (opcional)


