# genai---neu

1 - I tested two large models using the Ollama software. First, download Ollama, extract the Ollama software package, and move it to the Applications directory.

2 - Start the local terminal and change the directory to the Applications directory using cd /Applications.

3 - In the command line, enter the following commands to start the models:


Copy code

ollama run llama3
ollama run phi3


4 - reference:


Ollama -from https://github.com/ollama/ollama
Discord

Get up and running with large language models.

macOS
Download

Windows preview
Download

Linux
curl -fsSL https://ollama.com/install.sh | sh
Manual install instructions

Docker
The official Ollama Docker image ollama/ollama is available on Docker Hub.

Libraries
ollama-python
ollama-js
Quickstart
To run and chat with Llama 3:

ollama run llama3
Model library
Ollama supports a list of models available on ollama.com/library

Here are some example models that can be downloaded:

Model	Parameters	Size	Download
Llama 3	8B	4.7GB	ollama run llama3

Llama 3	70B	40GB	ollama run llama3:70b

Phi 3 Mini	3.8B	2.3GB	ollama run phi3

Phi 3 Medium	14B	7.9GB	ollama run phi3:medium

Gemma	2B	1.4GB	ollama run gemma:2b

Gemma	7B	4.8GB	ollama run gemma:7b

Mistral	7B	4.1GB	ollama run mistral

Moondream 2	1.4B	829MB	ollama run moondream

Neural Chat	7B	4.1GB	ollama run neural-chat

Starling	7B	4.1GB	ollama run starling-lm

Code Llama	7B	3.8GB	ollama run codellama

Llama 2 Uncensored	7B	3.8GB	ollama run llama2-uncensored

LLaVA	7B	4.5GB	ollama run llava

Solar	10.7B	6.1GB	ollama run solar

Note: You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

