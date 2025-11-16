# 🎓 Gerador de Planos de Aula com IA

Aplicação simples em **Streamlit + LangChain + OpenAI** para gerar planos de aula personalizados utilizando um modelo de linguagem.

## 🚀 Funcionalidades

- Seleção de tema da aula  
- Nível de ensino  
- Duração da aula  
- Metodologia pedagógica  
- Elemento adicional (ex.: inclusão, tecnologia, engajamento)  
- Geração de plano de aula estruturado em **Markdown**  
- Download do plano em arquivo `.md`

## 🧱 Tecnologias

- Python  
- Streamlit  
- LangChain (langchain-core + langchain-openai)  
- OpenAI API  

## ⚙️ Como rodar localmente

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPO.git
   cd SEU_REPO
  ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua chave da OpenAI:**

   * Copie o arquivo `config-example.yaml` para `config.yaml`
   * Edite o `config.yaml` e coloque sua chave:

     ```yaml
     OPENAI_API_KEY: "SUA_CHAVE_AQUI"
     ```

5. **Rode a aplicação:**

   ```bash
   streamlit run app.py
   ```

6. **Acesse no navegador:**
   [http://localhost:8501](http://localhost:8501)

---

## 📌 Observações

* Não suba sua chave de API para o GitHub (o arquivo `config.yaml` já está no `.gitignore`).
* Este projeto foi criado para fins de estudo em GenAI com LangChain.
