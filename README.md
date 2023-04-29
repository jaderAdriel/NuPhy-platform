# Plataforma xxxxxx

## Como usar o venv (ambiente virtual)

O venv é uma ferramenta integrada do Python que permite criar ambientes virtuais isolados para o desenvolvimento de projetos Python. Isso permite que você instale pacotes Python em um ambiente isolado, evitando conflitos com outras versões do Python e outros projetos Python em seu sistema.

### Criando um novo ambiente virtual

Para criar um novo ambiente virtual, abra o terminal ou o prompt de comando e navegue até o diretório onde deseja criar o ambiente virtual. Em seguida, execute o seguinte comando:

```
python -m nome_do_ambiente
```

Isso criará um novo ambiente virtual com o nome nome_do_ambiente . Para ativar o ambiente virtual, execute o seguinte comando:

#### No Windows:


```
nome_do_ambiente\Scripts\activate.bat
```

#### No Unix ou Linux:


```
source nome_do_ambiente/bin/activate
```


O `nome_do_ambiente` é o nome que você escolheu para o ambiente virtual.

Depois de ativar o ambiente virtual, você verá o nome do ambiente virtual no prompt de comando.

### Instalando dependências de um projeto Python

Com o ambiente virtual ativado, você pode instalar as dependências de um projeto Python usando o arquivo `requirements.txt`. O arquivo `requirements.txt` é um arquivo de texto simples que lista as dependências do projeto, uma em cada linha.

Para instalar as dependências, certifique-se de estar no diretório raiz do projeto e execute o seguinte comando:

```
pip install -r requirements.txt
```


Isso instalará todas as dependências do projeto listadas no arquivo `requirements.txt`.

### Desativando o ambiente virtual

Para desativar o ambiente virtual, basta executar o seguinte comando:


```
deactivate
```


Isso desativará o ambiente virtual e retornará ao ambiente padrão do Python.

## Gerenciamento de pacotes com o pip

O pip é um gerenciador de pacotes para Python que permite instalar, gerenciar e atualizar pacotes de terceiros para o seu projeto Python. Neste repositório, você aprenderá como usar o pip para gerenciar pacotes em Python.

### Instalação do pip

Antes de usar o pip, você precisa instalá-lo em seu sistema. Se você já tem o Python instalado em seu sistema, provavelmente já tem o pip instalado. Você pode verificar se o pip está instalado em seu sistema executando o seguinte comando:

```
pip --version
```
Se o pip estiver instalado, você verá a versão do pip que está sendo executada em seu sistema. Caso contrário, você pode instalar o pip executando o seguinte comando:

```
sudo apt-get install python-pip
```

### Instalação de pacotes

Para instalar um pacote usando o pip, execute o seguinte comando:
```
pip install <pacote>
```

Por exemplo, para instalar o pacote "numpy", execute o seguinte comando:

pip install numpy

### Atualização de pacotes

Para atualizar um pacote usando o pip, execute o seguinte comando:

pip install --upgrade <pacote>

Por exemplo, para atualizar o pacote "numpy", execute o seguinte comando:

pip install --upgrade numpy

### Remoção de pacotes

Para remover um pacote usando o pip, execute o seguinte comando:

```
pip uninstall <pacote>
```

Por exemplo, para remover o pacote "numpy", execute o seguinte comando:

pip uninstall numpy

### Listagem de pacotes instalados

Para listar todos os pacotes instalados em seu ambiente Python, execute o seguinte comando:

```
pip list
```

### Criação de um arquivo requirements.txt

Para gerenciar as dependências do seu projeto usando o pip, você pode criar um arquivo requirements.txt que lista todos os pacotes que seu projeto precisa para ser executado. Você pode criar um arquivo requirements.txt a partir dos pacotes instalados em seu ambiente Python executando o seguinte comando:

```
pip freeze > requirements.txt
```

Isso criará um arquivo requirements.txt que lista todos os pacotes instalados em seu ambiente Python. Você pode editar este arquivo manualmente para adicionar ou remover pacotes, se necessário.


## Equipe

- [**Anna Julya Santos Cruz**](https://github.com/JulyaCruz)
- [**Jader Adriel Miranda Souza**](https://github.com/jaderAdriel)
- [**Kleberson Fialho Baleeiro**](https://github.com/klebersonfialhobaleeiro)
- [**Reinaldo Soares Assunção Junior**](https://github.com/reinaldo-a)
