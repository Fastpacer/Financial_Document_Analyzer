import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="Financial Document Analyzer", layout="wide")

st.title("📊 Financial Document Analyzer")

uploaded_file = st.file_uploader("Upload Financial PDF", type=["pdf"])
query = st.text_input(
    "Enter Analysis Query",
    value="Provide structured financial insights."
)

if st.button("Analyze Document"):

    if uploaded_file is None:
        st.warning("Please upload a PDF file.")
    else:
        with st.spinner("Analyzing document..."):

            response = requests.post(
                f"{API_BASE_URL}/analyze",
                files={"file": uploaded_file},
                data={"query": query}
            )

            if response.status_code != 200:
                st.error("Error during analysis.")
                st.stop()

            result = response.json()

        st.success("Analysis Completed ✅")

        st.subheader("Record ID")
        st.write(result["record_id"])

        st.subheader("Analysis")
        st.write(result["analysis"])