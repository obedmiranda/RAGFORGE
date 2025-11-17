from langchain_community.document_loaders import TextLoader
def load_text(path: str):
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()
