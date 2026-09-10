<script setup>
import { onMounted, ref } from 'vue'
import {
  listarCategorias, listarEditoras, listarAutores, listarLivros,
  login, registrar, logout, autenticado
} from './api'

const aba = ref('livros')
const livros = ref([])
const categorias = ref([])
const editoras = ref([])
const autores = ref([])
const mensagem = ref('')
const carregando = ref(false)

const email = ref('')
const password = ref('')
const nome = ref('')
const modoCadastro = ref(false)

async function carregar() {
  carregando.value = true
  mensagem.value = ''
  try {
    livros.value = await listarLivros()
    categorias.value = await listarCategorias()
    editoras.value = await listarEditoras()
    autores.value = await listarAutores()
  } catch (e) {
    mensagem.value = 'Não foi possível conectar ao backend. Verifique se o Django está rodando.'
  } finally {
    carregando.value = false
  }
}

async function entrar() {
  try {
    await login(email.value, password.value)
    mensagem.value = 'Login realizado.'
    email.value = ''
    password.value = ''
  } catch {
    mensagem.value = 'E-mail ou senha inválidos.'
  }
}

async function cadastrar() {
  try {
    await registrar(email.value, nome.value, password.value)
    mensagem.value = 'Usuário criado. Agora faça o login.'
    modoCadastro.value = false
  } catch (e) {
    mensagem.value = e.response?.data
      ? JSON.stringify(e.response.data)
      : 'Erro ao cadastrar.'
  }
}

function sair() {
  logout()
  mensagem.value = 'Sessão encerrada.'
}
onMounted(carregar)
</script>

<template>
  <header>
    <div>
      <h1>📚 Livraria</h1>
      <p>API Django + frontend Vue 3</p>
    </div>
    <div class="auth">
      <template v-if="!autenticado()">
        <input v-if="modoCadastro" v-model="nome" placeholder="Nome" />
        <input v-model="email" placeholder="E-mail" type="email" />
        <input v-model="password" placeholder="Senha" type="password" />
        <button @click="modoCadastro ? cadastrar() : entrar()">
          {{ modoCadastro ? 'Cadastrar' : 'Entrar' }}
        </button>
        <button class="sec" @click="modoCadastro = !modoCadastro">
          {{ modoCadastro ? 'Já tenho conta' : 'Criar conta' }}
        </button>
      </template>
      <button v-else @click="sair">Sair</button>
    </div>
  </header>

  <main>
    <p v-if="mensagem" class="message">{{ mensagem }}</p>

    <nav>
      <button v-for="item in ['livros','categorias','editoras','autores']"
              :key="item" :class="{ active: aba === item }"
              @click="aba = item">
        {{ item[0].toUpperCase() + item.slice(1) }}
      </button>
    </nav>

    <section v-if="carregando" class="loading">Carregando...</section>

    <section v-else-if="aba === 'livros'" class="grid">
      <article v-for="livro in livros" :key="livro.id" class="card">
        <div class="cover">📖</div>
        <h2>{{ livro.titulo }}</h2>
        <strong>R$ {{ Number(livro.preco).toFixed(2) }}</strong>
        <p>Estoque: {{ livro.quantidade ?? 0 }}</p>
      </article>
      <p v-if="!livros.length">Nenhum livro cadastrado.</p>
    </section>

    <section v-else-if="aba === 'categorias'" class="list">
      <article v-for="item in categorias" :key="item.id">{{ item.descricao }}</article>
    </section>

    <section v-else-if="aba === 'editoras'" class="list">
      <article v-for="item in editoras" :key="item.id">
        <strong>{{ item.nome }}</strong>
        <span>{{ item.cidade || 'Cidade não informada' }}</span>
      </article>
    </section>

    <section v-else class="list">
      <article v-for="item in autores" :key="item.id">
        <strong>{{ item.nome }}</strong>
        <span>{{ item.email || 'E-mail não informado' }}</span>
      </article>
    </section>
  </main>
</template>
