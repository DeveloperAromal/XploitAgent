# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
from utils.log import logReport
from colorama import Fore, Style

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
         model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
         base_url="https://openrouter.ai/api/v1",
         api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    base_analysis_data = os.path.abspath("db")
    
    loader = DirectoryLoader( base_analysis_data, glob="*.txt",loader_cls=TextLoader)
    docs = loader.load()
    
    filtered_docs = [doc for doc in docs if doc.metadata["source"].endswith(("target_html.txt", "target_stack_data.txt", "valid_subdomains.txt"))]

    document = filtered_docs
    
    
    combined = clean_and_label_docs(document)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents([Document(page_content=combined)])
    
    chain = load_qa_chain(llm, chain_type="stuff")
    
    question = (
        "Based on the scan results, what stack does the target use, "
        "what vulnerabilities may exist, and what would be the next logical step?"
    )

    result = chain.invoke({"input_documents":splitter, "question":question})
    data = result["output_text"]
    
    logReport(f"[+] ==> {data}")
    logReport(f"[+] ==> ---Security vulnerability found---")
    
    save_file = os.path.join("db", "security_vulnerability.md")
       
    with open(save_file, "w") as f:
         f.write(result["output_text"])
    
    print(result)
         
    print(f"{Fore.GREEN} [+] Process finished {Style.RESET_ALL}")
    print(f"{Fore.YELLOW} [+] Saving file{Style.RESET_ALL}")
         
    return result


def plan_maker():
    print("[*] Initializing plan maker...")

    vulnerable_report = os.path.join("db", "security_vulnerability.md")
    print(f"[+] Loading vulnerability report from: {vulnerable_report}")

    if not os.path.exists(vulnerable_report):
        print("[-] Report file not found!")
        return
    
    llm = ChatOpenAI(
        model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    print("[+] LLM initialized successfully.")

    with open(vulnerable_report, "r", encoding="utf-8") as f:
        report = f.read()
    print("[+] Vulnerability report loaded into memory.")

    print("[*] Splitting the report into smaller chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(report)
    print(f"[+] Report split into {len(chunks)} chunks.")

    documents = [Document(page_content=chunk) for chunk in chunks]
    print("[+] Converted chunks into LangChain Document objects.")

    print("[*] Loading QA chain with chain_type='stuff'...")
    chain = load_qa_chain(llm, chain_type="stuff")
    print("[+] QA chain loaded successfully.")

    question = (
        """
            You are a professional penetration tester. Analyze the following data which includes:
            - HTML source of the target website
            - Tech stack (e.g. Next.js)
            - Subdomains found
            - Detected tool outputs

            Your task:
            1. Identify the stack and exposed technologies.
            2. List potential vulnerabilities based on the data.
            3. Propose a step-by-step attack plan using: [nmap, leaky header finder, network interceptor].
            4. Justify which tool to use first and why.
            Be as technical and detailed as possible.
        """
    )

    print("[*] Invoking LLM to generate plan...")
    plan = chain.invoke({"input_documents": documents, "question": question})
    print("[+] Plan generation complete.\n")

    save_file = os.path.join("db", "plan.md")
       
    with open(save_file, "w") as f:
         f.write(plan["output_text"])
    

    print("========== GENERATED ATTACK PLAN ==========")
    print(plan["output_text"])
    print("===========================================")