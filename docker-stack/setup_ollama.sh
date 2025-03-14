#!/bin/bash

# Pull the Ollama Docker image
docker pull ollama/ollama:latest

# Run the Ollama Docker container with the gemma3:4b model
docker run -d --name ollama \
  -p 11434:11434 \
  ollama/ollama:latest \
  --model gemma3:4b

echo "Ollama container is running and gemma3:4b model is loaded."
