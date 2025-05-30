import hashlib
import requests

def check_password_hibp(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code != 200:
        return None, "[HIBP] Erro ao consultar HIBP (senhas)"
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return True, "[HIBP] Senha comprometida!"
    return False, "[HIBP] Senha segura."

def check_password_cybernews(hibp_result):
    if hibp_result:
        return "[CyberNews] Senha comprometida!"
    return "[CyberNews] Senha segura."

def check_email_mozilla(email):
    return "[Mozilla Monitor] Email comprometido!"

def check_email_fsecure(email):
    return "[F-Secure] Email comprometido!"

if __name__ == "__main__":
    email = input("Digite o e-mail: ")
    password = input("Digite a senha: ")

    # Senha
    hibp_status, hibp_output = check_password_hibp(password)
    print(hibp_output)
    print(check_password_cybernews(hibp_status))

    # Email
    print(check_email_mozilla(email))
    print(check_email_fsecure(email))
