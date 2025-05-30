# Verificador de Vazamento de Email e Senha

Este container verifica se uma senha e um e-mail foram comprometidos usando fontes públicas.

## Verificações:

- Senha: Have I Been Pwned (API pública)
- E-mail: Cybernews (requisição real)
- E-mail: Mozilla Monitor (simulado)
- E-mail: F-Secure (simulado)

## Como usar

### 1. Build

```bash
docker build -t vazamento-check .
