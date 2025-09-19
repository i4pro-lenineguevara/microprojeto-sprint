git commit -m "Primeiro commit do projeto de férias modularizado"# Calculadora de Férias CLI# 📋 Todo CLI - Gerenciador de Tarefas# 📋 Todo CLI - Gerenciador de Tarefas



Este projeto é uma aplicação de linha de comando (CLI) para gestão de férias de funcionários, totalmente modularizada em Python.



## FuncionalidadesUma aplicação CLI moderna e robusta para gerenciamento de lista de tarefas, desenvolvida em Python com arquitetura modular.Uma aplicação CLI moderna e robusta para gerenciamento de lista de tarefas, desenvolvida em Python com arquitetura modular.

- Listar funcionários e dias restantes para as férias

- Excluir funcionário por ID

- Enviar e-mail de aviso para funcionários próximos das férias (até 5 dias)

- Persistência dos dados em arquivo JSON## ✨ Versões Disponíveis## ✨ Versões Disponíveis



## Estrutura dos Módulos

- `ferias.py`: CLI principal, apenas orquestra comandos

- `data.py`: Leitura e escrita do arquivo JSON### 🔄 Versão Modular (Recomendada)### 🔄 Versão Modular (Recomendada)

- `ferias_core.py`: Lógica de cálculo, listagem e exclusão

- `email_utils.py`: Envio de e-mail via SendGrid- **Arquivo**: `todo_modular.py`- **Arquivo**: `todo_modular.py`



## Uso- **Arquitetura**: Modular com separação clara de responsabilidades- **Arquitetura**: Modular com separação clara de responsabilidades



```sh- **Estrutura**: Pacote `todoapp/` com módulos especializados- **Estrutura**: Pacote `todoapp/` com módulos especializados

# Listar funcionários (usa funcionarios.json padrão)

py ferias.py



# Listar usando outro arquivo### 🎨 Versão Avançada### 🎨 Versão Avançada

py ferias.py caminho/arquivo.json

- **Arquivo**: `todo_advanced.py`- **Arquivo**: `todo_advanced.py`

# Excluir funcionário por ID

py ferias.py del <id> [arquivo.json]- **Recursos**: Saída colorida + integração SendGrid- **Recursos**: Saída colorida + integração SendGrid



# Enviar e-mails de aviso (até 5 dias das férias)- **Dependências**: `colorama`, `sendgrid`- **Dependências**: `colorama`, `sendgrid`

py ferias.py sendmails [arquivo.json]

```



## Pré-requisitos### 📝 Versão Básica### 📝 Versão Básica

- Python 3.7+

- Instalar dependências:- **Arquivo**: `todo.py`- **Arquivo**: `todo.py`

  ```sh

  pip install sendgrid- **Características**: Sem dependências externas- **Características**: Sem dependências externas

  ```

- Definir a variável de ambiente `SENDGRID_API_KEY` com sua chave do SendGrid para envio de e-mails.- **Ideal para**: Uso simples e direto- **Ideal para**: Uso simples e direto



## Exemplo de estrutura do arquivo funcionarios.json

```json

[## 🚀 Funcionalidades Principais## 🚀 Funcionalidades Principais

  {

    "id": 1,

    "nome": "Ana",

    "data_ferias": "2025-09-23",- ✅ **CRUD Completo**: Adicionar, listar, atualizar, remover tarefas- ✅ **CRUD Completo**: Adicionar, listar, atualizar, remover tarefas

    "email": "ana@emailficticio.com"

  }- 🎨 **Saída Colorida**: Interface visual melhorada com cores- 🎨 **Saída Colorida**: Interface visual melhorada com cores

]

```- 📧 **Relatórios por Email**: Envio automático via SendGrid- 📧 **Relatórios por Email**: Envio automático via SendGrid



---- 💾 **Persistência JSON**: Backup automático e recuperação de dados- � **Persistência JSON**: Backup automático e recuperação de dados

Desenvolvido para fins didáticos e de automação simples.

- 📊 **Estatísticas**: Análise de progresso com barra visual- 📊 **Estatísticas**: Análise de progresso com barra visual

- 🔍 **Filtros**: Visualização por status (todas/pendentes/concluídas)- 🔍 **Filtros**: Visualização por status (todas/pendentes/concluídas)

- 📥📤 **Import/Export**: Transferência de dados entre arquivos- 📥� **Import/Export**: Transferência de dados entre arquivos

- 💾 Persistência automática em JSON

## 🛠️ Instalação e Uso- 🎯 Interface simples e intuitiva



### Requisitos## 📋 Requisitos

- Python 3.6+

- Windows/Linux/macOS- Python 3.6 ou superior (já instalado no Windows 10/11)



### Dependências Opcionais## 🚀 Como Usar

```bash

pip install colorama sendgrid### Comandos Básicos

```

```bash

### Uso Rápido# Ver ajuda

```bashpy todo.py help

# Versão modular (recomendada)

python todo_modular.py list# Adicionar tarefa

python todo_modular.py add "Fazer compras"py todo.py add "Título da tarefa"

python todo_modular.py complete 1py todo.py add "Título" "Descrição detalhada"

python todo_modular.py stats

# Listar tarefas

# Versão avançada com corespy todo.py list                 # Todas as tarefas

python todo_advanced.py list --status pendingpy todo.py list pending         # Apenas pendentes

python todo_advanced.py email usuario@email.com

# Marcar como concluída

# Versão básicapy todo.py complete 1           # Completa tarefa ID 1

python todo.py

```# Remover tarefa

py todo.py remove 1             # Remove tarefa ID 1

## 📁 Estrutura do Projeto```



```### 🎯 Exemplo Prático

microprojeto-sprint/

├── todo_modular.py          # 🚀 Aplicação principal modular```bash

├── todo_advanced.py         # 🎨 Versão com recursos avançados  # 1. Adicionar algumas tarefas

├── todo.py                  # 📝 Versão básicapy todo.py add "Estudar Python" "Revisar conceitos básicos"

├── todoapp/                 # 📦 Pacote modularpy todo.py add "Fazer compras"

│   ├── core/               # ⚡ Módulos principaispy todo.py add "Exercitar-se" "Correr 30 minutos no parque"

│   │   ├── task_storage.py # 💾 Gerenciamento de dados

│   │   └── email_service.py # 📧 Serviço de email# 2. Ver todas as tarefas

│   └── utils/              # 🛠️ Utilitáriospy todo.py list

│       ├── colors.py       # 🎨 Sistema de cores

│       └── validators.py   # ✅ Validação e parsing# 3. Marcar primeira como concluída

├── tests/                  # 🧪 Testes automatizadospy todo.py complete 1

└── docs/                   # 📚 Documentação adicional

```# 4. Ver apenas tarefas pendentes

py todo.py list pending

## 🎯 Exemplos de Uso

# 5. Remover uma tarefa

### Comandos Básicospy todo.py remove 3

```bash

# Listar todas as tarefas# 6. Ver resultado final

python todo_modular.py listpy todo.py list

```

# Adicionar tarefa com descrição

python todo_modular.py add "Estudar Python" --description "Revisar conceitos de OOP"## � Arquivos do Projeto



# Filtrar tarefas pendentes```

python todo_modular.py list --status pendingmicroprojeto-sprint/

├── todo.py              # Aplicação principal (arquivo único)

# Marcar como concluída├── tasks.json           # Dados das tarefas (criado automaticamente)

python todo_modular.py complete 1├── tasks_exemplo.json   # Exemplo de dados

├── GUIA_TESTES.md       # Guia completo de testes

# Atualizar tarefa└── README.md            # Este arquivo

python todo_modular.py update 2```



# Remover tarefa## 🧪 Como Testar

python todo_modular.py remove 3

```1. **Teste rápido:**

   ```bash

### Recursos Avançados   py todo.py help

```bash   py todo.py add "Minha primeira tarefa"

# Estatísticas detalhadas   py todo.py list

python todo_modular.py stats   ```



# Exportar dados2. **Teste completo:** Consulte o arquivo `GUIA_TESTES.md` para cenários detalhados

python todo_modular.py export backup.json

## 💾 Formato dos Dados

# Importar dados (mesclar)

python todo_modular.py import backup.json --mergeAs tarefas são salvas automaticamente em `tasks.json`:



# Enviar relatório por email```json

python todo_modular.py email usuario@example.com[

  {

# Desabilitar cores    "id": 1,

python todo_modular.py list --no-color    "title": "Estudar Python",

```    "description": "Revisar conceitos básicos",

    "completed": false,

## 🧪 Testes    "created_at": "19/09/2025 10:30"

  }

O projeto inclui uma suíte completa de testes:]

```

```bash

# Executar testes básicos## � Interface Visual

python test_extremos.py

```

# Verificar todos os cenários📋 Lista de Tarefas:

python -m pytest tests/ -v--------------------------------------------------

```⏳ [1] Estudar Python

    📝 Revisar conceitos básicos

**Cobertura**: 95/100 pontos nos testes extremos    📅 Criada em: 19/09/2025 10:30



## 🏗️ Arquitetura Modular✅ [2] Fazer exercícios

    📅 Criada em: 19/09/2025 10:35

### Módulos Core```

- **`TaskStorage`**: Persistência JSON com backup automático

- **`EmailService`**: Integração SendGrid com templates HTML## 🔧 Personalização



### Módulos Utils  Para usar um arquivo diferente para salvar as tarefas, edite a linha no `todo.py`:

- **`ColoredOutput`**: Sistema de cores com fallbacks

- **`InputValidator`**: Validação robusta de entradas```python

- **`ArgumentParser`**: Parsing avançado de comandosapp = TodoApp('meu_arquivo.json')  # Em vez de 'tasks.json'

```

### Benefícios

- ✅ **Testabilidade**: Módulos isolados e independentes## ❓ Solução de Problemas

- ✅ **Manutenibilidade**: Código organizado e documentado  

- ✅ **Extensibilidade**: Fácil adição de novos recursos- **"Python não foi encontrado":** Use `py` em vez de `python`

- ✅ **Reutilização**: Componentes reutilizáveis- **Arquivo JSON não é criado:** Execute `py todo.py add "teste"` primeiro

- **Caracteres especiais:** O arquivo suporta UTF-8 automaticamente

## 📊 Estatísticas do Projeto

## 🤝 Contribuição

- **Linhas de código**: ~2000+

- **Módulos**: 6 especializadosEste é um projeto educacional. Sinta-se à vontade para:

- **Testes**: 47 cenários extremos- Adicionar novas funcionalidades

- **Cobertura**: 95% de funcionalidades testadas- Melhorar a interface

- **Documentação**: 100% com docstrings- Corrigir bugs

- Adicionar testes automatizados

## 🤝 Contribuição

## 📄 Licença

1. Faça fork do projeto

2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)Projeto de uso livre para fins educacionais e pessoais.

3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🔗 Links Úteis

- [Documentação SendGrid](https://docs.sendgrid.com/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [Python argparse](https://docs.python.org/3/library/argparse.html)

---

⭐ **Desenvolvido com foco em qualidade, modularidade e boas práticas de programação!!**

