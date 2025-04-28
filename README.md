# **GeoRelato**

Relate e visualize problemas urbanos georreferenciados com facilidade.

## **Setup**

### **1. Clonar o Repositório**

Primeiro, clone o repositório do projeto:

```sh
$ git clone https://github.com/klebersonfialhobaleeiro/PIE.git
$ cd PIE
```

### **2. Criar e Ativar o Ambiente Virtual**

Para garantir que as dependências sejam instaladas de forma isolada, crie um ambiente virtual:

```sh
$ python -m venv .venv
```

Ative o ambiente virtual:

- **Windows:**

  ```sh
  $ .venv\Scriptsctivate.bat
  ```

- **Linux/MacOS:**

  ```sh
  $ source .venv/bin/activate
  ```

### **3. Instalar Dependências**

Agora, instale as dependências necessárias para o projeto:

```sh
(.venv) $ pip install -r requirements.txt
```

### **4. Executar as Migrações**

O próximo passo é realizar as migrações para configurar o banco de dados. Execute os seguintes comandos:

```sh
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
```

### **5. Rodar o Servidor de Desenvolvimento**

Agora, você pode rodar o servidor de desenvolvimento para ver a aplicação funcionando. Execute:

```sh
(.venv) $ python manage.py runserver
```
O servidor estará rodando em [http://127.0.0.1:8000](http://127.0.0.1:8000).
