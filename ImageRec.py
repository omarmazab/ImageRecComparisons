import streamlit as st
from models.gemini import analyze_with_gemini
from models.openai_helper import analyze_with_openai
from models.anthropic_helper import analyze_with_anthropic


st.title("Compare Images")

with st.sidebar:

    with st.expander("Anthropic", expanded=False):
        use_anthropic = st.checkbox("Use Anthropic")
        if use_anthropic:
            anthropic_api_key = st.text_input("Anthropic API Key", key="anthtest_api_key", type="password")
            anthropicTemp = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.05, key = "anthropicTemp")


    with st.expander("Gemini", expanded=False):
        use_gemini = st.checkbox("Use Gemini")
        if use_gemini:
            gemini_api_key = st.text_input("Gemini API Key", key="gemtest_api_key", type="password")
            geminiTemp = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.05, key = "geminiTemp")

    with st.expander("OpenAI", expanded=False):
        use_openai = st.checkbox("Use OpenAI")
        if use_openai:
            openai_api_key = st.text_input("Openai API Key", key="gpttest_api_key", type="password")
            openaiTemp = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.05, key = "openaiTemp")
    st.text("Coming soon, Grok, Deepseek")

with st.expander("Upload an Image", expanded=True):
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image_bytes = uploaded_file.read()
        st.image(image_bytes, width=300)

prompt = st.text_input("Instructions (what should the AI do with the image?)",  placeholder="e.g., You are a bike mechanic, help me fix this bike.", value="")


if uploaded_file and prompt:
    if st.button("Analyze Selected Models"):

        if use_gemini and gemini_api_key:
            st.write("### Gemini 2.5 Output:")
            gemini_result = analyze_with_gemini(image_bytes, prompt, gemini_api_key, geminiTemp)
            st.write(gemini_result)
        elif use_gemini and not gemini_api_key:
            st.warning("Gemini selected but no API key provided.")

        if use_openai and openai_api_key:
            st.write("### OpenAI Output:")
            openai_result = analyze_with_openai(image_bytes, prompt, openai_api_key, openaiTemp)
            st.write(openai_result)
        elif use_openai and not openai_api_key:
            st.warning("OpenAI selected but no API key provided.")

        if use_anthropic and anthropic_api_key:
            st.write("### Anthropic Output:")
            anthropic_result = analyze_with_anthropic(image_bytes, prompt, anthropic_api_key, anthropicTemp)
            st.write(anthropic_result)
        elif use_anthropic and not anthropic_api_key:
            st.warning("Anthropic selected but no API key provided.")


