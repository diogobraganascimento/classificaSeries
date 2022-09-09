# Classifica Series

---

### Site para catalogar e classificar as series assistidas.

---

### Tecnologias utilizadas: 

|descrição | versão | documentação                                    |
|----------|--------|-------------------------------------------------|
|python | 3.10.7 | https://www.python.org/                         | 
|Flask | 2.0.2  | https://flask.palletsprojects.com/en/2.2.x/     |
|Flask-Mysqldb | 0.2.0 | https://flask-mysqldb.readthedocs.io/en/latest/ |

---
### Instalação:
> Criar ambiente virtual:<br>
> python3 -m venv 'nome_do_ambiente';

> Ativar o ambiente: <br>
> windows: 'nome_do_ambiente'\Scripts\activate <br>
> Linux ou Mac: source 'nome_do_ambiente'/bin/activate

> Instalar as dependências: <br>
> pip install -r requirements.txt


---
Ajustes no código HTML
> title: Coloca o primeiro caracter em maiúscola;

> upper: Colocal os caracteres em caixa alta;

>round: Arredonda os números;

>trim: Remover espaços do início e do fim do texto;

>default('texto exibido por padrão'): Quando queremos mostrar algo, caso a variável esteja vazia ou nula;

---

#### classificaSerie
- static
  - reset.css
  - style.css
- templates
  - list.html
  - login.html
  - novo.html
  - template.html
- cassificaSeries.py
- dao.py - 'data access object'
- prepara_banco
- README.md
- requirementes.txt

---

Fonte de conhecimento:
Alura - alura.com.br