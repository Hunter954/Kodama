# Site Thiago Kodama - Flask

Site simples em Python Flask com a imagem principal na home.

## Rodar localmente

```bash
pip install -r requirements.txt
python start.py
```

Acesse: `http://localhost:8080`

## Railway

Este projeto foi ajustado para evitar definitivamente o erro:

```txt
Error: '$PORT' is not a valid port number.
```

Correções aplicadas:

- `Dockerfile` usando `ENTRYPOINT ["python", "/app/start.py"]`.
- `railway.json` forçando deploy via Dockerfile.
- `start.py` valida a porta e, se vier literal como `$PORT`, usa `8080`.

### Importante

No Railway, se tiver um Start Command manual antigo nas configurações do serviço, apague ele ou troque para:

```bash
python /app/start.py
```

Mesmo que o Railway tente usar o comando antigo, o `ENTRYPOINT` deste Dockerfile força o app a iniciar pelo `start.py`.
