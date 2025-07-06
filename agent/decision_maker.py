from langchain_community.chat_models import ChatOpenAI
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
         model="meta-llama/llama-4-maverick:free",
         base_url="https://openrouter.ai/api/v1",
        #  api_key=os.getenv("OPENROUTER_API_KEY"),
         api_key="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",

    )

    base_analysis_data = os.path.abspath("db")
    
    loader = DirectoryLoader( base_analysis_data, glob="*.txt",loader_cls=TextLoader)
    docs = loader.load()
    
    filtered_docs = [doc for doc in docs if doc.metadata["source"].endswith(("target_html.txt", "target_stack_data.txt", "valid_subdomains.txt"))]

    document = filtered_docs
    
    
    
    combined = clean_and_label_docs(document)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents([Document(page_content=combined)])
    
    chain = load_qa_chain(llm, chain_type="stuff")
    
    
    
    target_html = os.path.join("db", "target_html.txt")
    with open (target_html, "r") as f:
        html_data = f.read()
        
    valid_subdomains = os.path.join("db", "valid_subdomains.txt")
    with open (valid_subdomains, "r") as f:
        subdomain_data = f.read()
    
    stack = os.path.join("db", "target_stack_data.txt")
    with open (stack, "r") as f:
        stackinfo = f.read()
    
    question = (
                f"""
                    You are a skilled offensive security expert with extensive experience in analyzing web applications for vulnerabilities. Your focus is on identifying potential security risks and providing actionable insights for improvement.

                    Your task is to analyze the provided HTML source code and subdomain data from a scanned target. Here are the details you need to cover:  
                    - HTML Source Code: {html_data}  
                    - Subdomain Data: {subdomain_data}  
                    - Stack info: {stackinfo}
                    ---

                    In your analysis, identify:  
                    1. The frontend or backend stack being used (e.g., frameworks like Next.js, APIs, etc.).  
                    2. Specific security vulnerabilities or misconfigurations observed (e.g., IDOR, XSS, etc.) with evidence from the code.  
                    3. Prioritized next steps or potential exploits a pentester should consider based on the findings.  

                    ---

                    Output your findings as a structured vulnerability report with the following sections:  
                    - Stack Identification  
                    - Vulnerability Analysis  
                    - Exploitation Opportunities  
                    - Recommended Next Steps  

                    ---

                    Ensure that your analysis is thorough, focusing on both common and less obvious vulnerabilities. Provide clear evidence from the code where applicable, and detail each vulnerability's potential impact.  

                    ---

                    Constraints: Avoid overly technical jargon that may confuse non-experts, and ensure clarity in your explanations. Focus on practical recommendations rather than theoretical discussions.  
                """
    )
    

    result = chain.run(input_documents=splitter, question=question)

    logReport(f"[+] ==> {result}")
    logReport(f"[+] ==> ---Security vulnerability found---")
    
    save_file = os.path.join("db", "security_vulnerability.md")
       
    with open(save_file, "w") as f:
         f.write(result)
         
         
    print(f"{Fore.GREEN} [+] Process finished {Style.RESET_ALL}")
    print(f"{Fore.YELLOW} [+] Saving file{Style.RESET_ALL}")
         
    return result
