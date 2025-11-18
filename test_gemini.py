# test_gemini.py — final, auto-detect version

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY is not set in .env")
    sys.exit(1)

genai.configure(api_key=api_key)

try:
    print("✅ Connected to Gemini. Fetching available models...\n")
    models = [
        m for m in genai.list_models()
        if "generateContent" in getattr(m, "supported_generation_methods", [])
    ]

    if not models:
        print("❌ No models with generateContent found for this key/project.")
        print("   Check that you created the key in Google AI Studio (not Vertex AI).")
        sys.exit(1)

    print("Available models that support generateContent:")
    for i, m in enumerate(models):
        print(f"{i}: {m.name}")

    # Pick the first available model
    model_name = models[0].name
    print(f"\n➡ Using model: {model_name}\n")

    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Say: Gemini is working.")
    print("✅ Gemini response:\n")
    print(response.text)

except Exception as e:
    print("\n❌ Something went wrong when calling Gemini:\n")
    print(e)
