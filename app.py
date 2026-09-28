import streamlit as st
import ollama

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff, #f8faff);
    }

    /* Main title */
    .main-title {
        text-align: center;
        color: #4f46e5;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Question label */
    label {
        color: #334155 !important;
        font-weight: 600 !important;
    }

    /* Text input */
    .stTextInput input {
        border: 2px solid #c7d2fe;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
        background-color: white;
    }

    .stTextInput input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 8px rgba(99, 102, 241, 0.25);
    }

    /* Button */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        font-size: 18px;
        font-weight: 600;
        padding: 12px;
        border: none;
        margin-top: 10px;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        color: white;
    }

    /* AI response box */
    .response-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #6366f1;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-top: 20px;
        color: #334155;
        font-size: 17px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 40px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">🤖 Friendly AI Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask anything and get a simple, friendly answer ✨</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT ----------------

question = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)


# ---------------- AI BUTTON ----------------

if st.button("✨ Ask AI"):

    if question.strip() == "":
        st.warning("⚠️ Please enter a question first.")

    else:

        with st.spinner("🤔 AI is thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a friendly and funny AI assistant.

Explain things in simple language.

Be helpful and encouraging.
"""
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        st.markdown(
            '<h3 style="color:#4f46e5;">💡 AI Response</h3>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="response-box">{answer}</div>',
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">Powered by Ollama • Built with Streamlit 🚀</div>',
    unsafe_allow_html=True
)