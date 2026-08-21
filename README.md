# Livraria — projeto pronto

Projeto baseado no material enviado: API REST com Django/DRF, autenticação SimpleJWT,
models Categoria, Editora, Autor, Livro, User, Compra e ItensCompra, Admin, Swagger e
um frontend Vue 3.

## Backend

```bash
cd backend
cp .env.example .env
pdm install
pdm run migrate
pdm run dev
```

A API ficará em `http://127.0.0.1:8000/api/`.

Swagger: `http://127.0.0.1:8000/api/swagger/`
Admin: `http://127.0.0.1:8000/admin/`

Para criar o administrador:

```bash
pdm run superuser
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

O frontend usa `http://127.0.0.1:8000/api` como backend.


## Compras com itens aninhados

O endpoint `POST /api/compras/` aceita uma compra com vários itens:

```json
{
  "usuario": 1,
  "itens": [
    {"livro": 1, "quantidade": 1},
    {"livro": 2, "quantidade": 2}
  ]
}
```

A criação é feita por `CompraCreateUpdateSerializer`, que cria a compra e seus `ItensCompra` dentro de uma transação atômica.

## Admin pronto

Depois de instalar as dependências e aplicar as migrações, execute:

```bash
pdm run python manage.py migrate
pdm run python manage.py setup_admin
```

Acesso ao Admin:

- E-mail: `a@a.com`
- Senha: `teste.123`
- URL: `/admin/`
