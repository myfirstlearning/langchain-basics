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
    "streamlit")
        streamlit run stramlit-demo/streamlit_demo.py
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
        echo "Usage: ./run.sh [openai|gemma|google|streamlit|prompt|apitest|main]"
        ;;
esac