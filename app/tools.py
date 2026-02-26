from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader


class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads and extracts summarized text from a financial PDF document."

    def _run(self, file_path: str) -> str:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        full_text = ""
        for doc in documents:
            full_text += doc.page_content + "\n"

        # 🔥 TOKEN SAFETY LIMIT
        MAX_CHARS = 8000   # Safe for 8k–10k token models
        if len(full_text) > MAX_CHARS:
            full_text = full_text[:MAX_CHARS]

        return full_text.strip()