# Verificador de Vazamento de Email e Senha

Este container verifica se uma senha e um e-mail foram comprometidos usando fontes públicas.

## Verificações:

- Senha: Have I Been Pwned
- E-mail: Cybernews
- E-mail: Mozilla Monitor
- E-mail: F-Secure

## Como usar

### 1. Build

```bash
docker build -t vazamento-check .
