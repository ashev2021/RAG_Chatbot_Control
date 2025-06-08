# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# near your other COPY lines



# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt \
 && pip install -U langchain-openai \
 && pip install -U langchain-community

# Expose Gradio default port
EXPOSE 7860

# Run the app
CMD ["python", "main.py"]
