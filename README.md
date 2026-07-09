# Thiago Kodama - Site Flask

Site simples em Python Flask com a imagem principal na home.

## Rodar localmente

```bash
pip install -r requirements.txt
python start.py
```

Abra: `http://localhost:8080`

## Subir no Railway

1. Suba estes arquivos no GitHub.
2. No Railway, crie um novo projeto conectado ao repositório.
3. O Railway vai detectar Python e iniciar com:

```bash
python start.py
```

Este projeto lê a variável `PORT` automaticamente. Se ela não existir, usa `8080`.

## Arquivos importantes

- `app.py` - aplicação Flask
- `start.py` - inicialização compatível com Railway
- `Procfile` - comando de start
- `static/img/kodama.png` - imagem da home
- `templates/index.html` - página principal
