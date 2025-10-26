# LangChain Basics

A collection of basic LangChain examples demonstrating integration with different language models including OpenAI GPT-4 and local Ollama models.

## Prerequisites

- OpenAI API key (for OpenAI demos)
- Ollama installed locally (for Gemma demo)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain-basics
```

2. Install required dependencies:
```bash
pip install langchain-openai langchain-ollama langchain-core langchain-google-genai langchain-anthropic langchain-community streamlit
```

## Setup

### OpenAI API Key
Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Ollama Setup
For the Gemma demo, install and run Ollama:
```bash
# Install Ollama (macOS)
brew install ollama 

or 

# Visit the Ollama website for installation instructions
https://ollama.com/

# commands:
# ollama -> see  list of commands
# serve  -> Start ollama
# run    -> run a model (ollama run gemma:2b)
# pull   -> pull a model from registry (ollama pull gemma:2b )
# push   -> push a model to a registry
# list   -> list all models  (ollama list)
# ps     -> list all running models (ollama ps)
# rm     -> remove a model (ollama rm gemma:2b)
```

## Usage

### Using Run Script (Recommended)
Make the script executable and run demos:
```bash
chmod +x run.sh

# To run the OpenAI demo:
./run.sh openai

# To run the Gemma demo:
./run.sh gemma

# To run the Google Gemini demo:
./run.sh google

# To run the Claude demo:
./run.sh claude

# To run the Grok demo:
./run.sh grok

# To run the Llama demo:
./run.sh llama

# To run the Streamlit demo:
./run.sh streamlit

# To run the travel guide demo:
./run.sh travel

# To run the travel guide Llama demo:
./run.sh travel-llama

# To run the LCEL demo:
./run.sh lcel

# To run the sequential chain demo:
./run.sh sequential

# To run the simple sequential chain demo:
./run.sh simple-sequential

# To run the multiple LLMs demo:
./run.sh multiple-llms

# To run the prompt template demo:
./run.sh prompt

# To run the API key test:
./run.sh apitest

# To run the main program:
./run.sh main
```

### Direct Python Execution
Alternatively, run demos directly:
```bash
python models-demo/openai_demo.py     # OpenAI GPT-4 chat demo
python models-demo/gemma_demo.py      # Local Gemma model demo
python models-demo/google_gemini_demo.py  # Google Gemini model demo
python models-demo/anthropic_claude_ai.py  # Anthropic Claude demo
python models-demo/grok_xai_demo.py   # Grok xAI demo
python models-demo/llama_demo.py      # Llama model demo
streamlit run streamlit-demo/streamlit_demo.py  # Web interface
python app-demo/travel_guide_demo.py  # Travel guide demo
python app-demo/travel_guide_llama_demo.py  # Travel guide Llama demo
python chains-demo/lcel_demo.py  # LCEL demo
streamlit run chains-demo/sequential_chain_demo.py  # Sequential chain demo
python chains-demo/simple_sequential_chain_demo.py  # Simple sequential chain demo
python multiple-llms/multiple_llms_demo.py  # Multiple LLMs demo
python prompt-templeate/prompt_template_demo.py  # Prompt template demo
python api-test/api_key_test.py    # API key test
python main.py            # Basic example
```

## Files

- `models-demo/openai_demo.py` - OpenAI GPT-4 integration example
- `models-demo/gemma_demo.py` - Local Ollama Gemma model example
- `models-demo/google_gemini_demo.py` - Google Gemini model integration example
- `models-demo/anthropic_claude_ai.py` - Anthropic Claude model integration example
- `models-demo/grok_xai_demo.py` - Grok xAI model integration example
- `models-demo/llama_demo.py` - Llama model integration example
- `streamlit-demo/streamlit_demo.py` - Web interface using Streamlit
- `app-demo/travel_guide_demo.py` - Travel guide application demo
- `app-demo/travel_guide_llama_demo.py` - Travel guide application with Llama
- `chains-demo/lcel_demo.py` - LCEL demo
- `chains-demo/sequential_chain_demo.py` - Sequential chain demo
- `chains-demo/simple_sequential_chain_demo.py` - Simple sequential chain demo
- `multiple-llms/multiple_llms_demo.py` - Multiple LLMs demo
- `prompt-templeate/prompt_template_demo.py` - Prompt template demonstration
- `api-test/api_key_test.py` - API key testing utility
- `main.py` - Basic Python script template
- `run.sh` - Shell script to run all demos

## Features

- Interactive command-line chat interfaces
- Web-based chat interface with Streamlit
- Support for both cloud (OpenAI) and local (Ollama) models
- Debug mode enabled for development

## Troubleshooting

- Ensure API keys are properly set in environment variables
- Verify Ollama is running for local model demos
- Check internet connection for OpenAI API calls