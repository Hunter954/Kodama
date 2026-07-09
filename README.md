# Site Thiago Kodama

Site simples em Python Flask com a imagem principal na home.

## Rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

Acesse: http://localhost:5000

## Railway

O projeto já inclui `Procfile`, `requirements.txt`, `Dockerfile` e `mise.toml`.

No Railway, basta conectar o repositório do GitHub e fazer deploy.

Observação: o `mise.toml` desativa a validação de atestação do Python para evitar o erro do Railway/Railpack: `No GitHub artifact attestations found for python@3.11.9`.
