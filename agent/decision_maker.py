from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
from utils.log import logReport

load_dotenv()


def clean_and_label_docs(documents):
    cleaned_docs = []

    for doc in documents:
        content = doc.page_content.strip()

        if "<html" in content or "<!DOCTYPE html" in content:
            labeled = f"=== HTML SOURCE CODE ===\n{content}"
        elif "Presence of" in content or "detected" in content:
            labeled = f"=== STACK INFORMATION ===\n{content}"
        elif "https://" in content:
            labeled = f"=== SUBDOMAINS FOUND ===\n{content}"
        else:
            labeled = f"=== TOOL OUTPUT ===\n{content}"

        cleaned_docs.append(labeled)

    return "\n\n".join(cleaned_docs)




def analyse_the_site():
    
    llm = ChatOpenAI(
         model="meta-llama/llama-4-maverick:free",
         base_url="https://openrouter.ai/api/v1",
         api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    
    
    
    
    base_analysis_data = os.path.abspath("db")
    
    loader = DirectoryLoader(base_analysis_data, glob="*.txt", loader_cls=TextLoader)
    
    document = loader.load()
    
    
    
    combined = clean_and_label_docs(document)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents([Document(page_content=combined)])
    
    chain = load_qa_chain(llm, chain_type="stuff")
    
    
    question = (
        "Based on the scan results, what stack does the target use, "
        "what vulnerabilities may exist, and what would be the next logical step?"
    )

    result = chain.run(input_documents=splitter, question=question)

    logReport(f"[+] ==> {result}")
    print("\n[+]:\n")
    print(result)
    return result
