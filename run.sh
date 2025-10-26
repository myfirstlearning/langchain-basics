#!/bin/bash

case "$1" in
    "openai")
        python models-demo/openai_demo.py
        ;;
    "gemma")
        python models-demo/gemma_demo.py
        ;;
    "google")
        python models-demo/google_gemini_demo.py
        ;;
    "claude")
        python models-demo/anthropic_claude_ai.py
        ;;
    "grok")
        python models-demo/grok_xai_demo.py
        ;;
    "llama")
        python models-demo/llama_demo.py
        ;;
    "streamlit")
        streamlit run streamlit-demo/streamlit_demo.py
        ;;
    "travel")
        python app-demo/travel_guide_demo.py
        ;;
    "travel-llama")
        python app-demo/travel_guide_llama_demo.py
        ;;
    "lcel")
        python chains-demo/lcel_demo.py
        ;;
    "sequential")
        streamlit run chains-demo/sequential_chain_demo.py
        ;;
    "simple-sequential")
        python chains-demo/simple_sequential_chain_demo.py
        ;;
    "multiple-llms")
        python multiple-llms/multiple_llms_demo.py
        ;;
    "prompt")
        python prompt-templeate/prompt_template_demo.py
        ;;
    "apitest")
        python api-test/api_key_test.py
        ;;
    "main")
        python main.py
        ;;
    *)
        echo "Usage: ./run.sh [openai|gemma|google|claude|grok|llama|streamlit|travel|travel-llama|lcel|sequential|simple-sequential|multiple-llms|prompt|apitest|main]"
        ;;
esac