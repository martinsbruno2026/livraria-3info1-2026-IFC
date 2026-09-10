import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
})

export async function listarCategorias() {
  const { data } = await api.get('/categorias/')
  return data
}

export async function listarEditoras() {
  const { data } = await api.get('/editoras/')
  return data
}

export async function listarAutores() {
  const { data } = await api.get('/autores/')
  return data
}

export async function listarLivros() {
  const { data } = await api.get('/livros/')
  return data
}

export async function login(email, password) {
  const { data } = await api.post('/token/', { email, password })
  localStorage.setItem('access', data.access)
  localStorage.setItem('refresh', data.refresh)
  return data
}

export async function registrar(email, name, password) {
  const { data } = await api.post('/registro/', { email, name, password })
  return data
}

export function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
}

export function autenticado() {
  return !!localStorage.getItem('access')
}

export default api
