# 🛒 Sistema de Controle de Estoque - Loja X

Este projeto é um sistema simples de **controle de estoque em Python**, voltado para prática de programação com modularização, validação de dados e organização de arquivos.

O sistema permite o **cadastro de usuários**, **login com verificação**, e o gerenciamento de produtos com funcionalidades como **cadastro, edição, exclusão e visualização** do estoque.

---

## 📌 Funcionalidades

- Cadastro de novos usuários
- Login com validação e limite de tentativas
- Menu principal e menu do estoque separados
- Cadastro de produtos com validações
- Edição e exclusão de produtos cadastrados
- Visualização do estoque formatada
- Modularização com organização clara por responsabilidade

---

## 🗂 Estrutura de Pastas
AV02 - Loja Online/ │ 
├── Estoque/ 
│ ├── CadastroProduto.py 
│ ├── EditarEstoque.py 
│ ├── ExcluirProduto.py 
│ ├── MenuEstoque.py 
│ └── OpcoesEditar.py 
├── Validacoes/ 
│ ├── ValidacaoLogin.py 
│ ├── ValidacaoNome.py 
│ ├── ValidacaoPreco.py
│ └── ValidacaoQuantidade.py
├── CadastroUsuario.py 
├── main.py 
└── README.md

---

## Tecnologias Utilizadas

Python 3
Estrutura modular com múltiplos arquivos .py
Tratamento de exceções com try/except
Validações manuais de entrada de dados

## Validações Importantes
Usuários:
    Apenas letras e números (sem espaços no início/fim).
    Senha com no mínimo 6 caracteres.
Produtos:
    Nome: apenas letras e espaços (ex: "ARROZ INTEGRAL").
    Preço: número float maior que zero.
    Quantidade: número inteiro e positivo.
Erros comuns tratados:
    Entrada com vírgula ao invés de ponto em valores monetários
    Caracteres inválidos no nome
    Espaços vazios
    Tipos errados em campos de número

## Autores
Nome: Ana Luiza Almeida e Wagner Lopes
Curso: Sistemas de Informação
Centro Universitario Cesmac
Projeto acadêmico de avaliação contínua (AV02) - Programação II

## ▶️ Como Executar

1. Verifique se você possui o **Python 3.x** instalado.
2. Clone ou baixe este repositório.
3. No terminal, navegue até a pasta do projeto.
4. Execute o arquivo principal:

```bash
python main.py