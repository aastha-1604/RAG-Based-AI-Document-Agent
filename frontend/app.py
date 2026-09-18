import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="RAG AI Document Agent",
    page_icon="📄",
    layout="wide"
)


st.title(
    "📄 RAG-Based AI Document Agent"
)

st.write(
    "Upload a PDF and ask questions about it."
)


st.sidebar.header(
    "Document Upload"
)


uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    if st.sidebar.button(
        "Process Document"
    ):

        with st.spinner(
            "Processing PDF..."
        ):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["document_id"] = result["document_id"]

                st.sidebar.success(
                    "Document processed successfully!"
                )

                st.sidebar.write(
                    f"Chunks created: {result['chunks']}"
                )

            else:

                st.sidebar.error(
                    "Error processing document."
                )


st.subheader(
    "Ask your document"
)


question = st.text_input(
    "Enter your question:"
)


if st.button("Ask"):

    if question and "document_id" in st.session_state:

        with st.spinner(
            "Thinking..."
        ):

            response = requests.post(
                f"{API_URL}/ask",
                json={
                    "question": question,
                    "document_id": st.session_state["document_id"]
                }
            )

            if response.status_code == 200:

                result = response.json()

               

                st.subheader(
                    "Answer"
                )

                st.write(
                    result["answer"]
                )

                source = result["source"]

                if source == "document":

                    st.info(
                        "📄 Source: Uploaded Document"
                    )

                else:

                    st.warning(
                        "🌐 Source: Web Search"
                    )

            else:

                st.error(
                    "Unable to generate answer."
                )

    else:

        st.warning(
            "Please enter a question."
        )