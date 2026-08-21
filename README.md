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
