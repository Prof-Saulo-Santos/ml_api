# Etapa 1: imagem base com Python
FROM python:3.10-slim

# Etapa 2: diretório de trabalho dentro do container
WORKDIR /app

# Etapa 3: copiar os arquivos do projeto
COPY . /app

# Etapa 4: instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: expor a porta usada pela aplicação
EXPOSE 8000

# Etapa 6: comando de inicialização
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
