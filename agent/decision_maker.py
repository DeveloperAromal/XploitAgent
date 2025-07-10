from langchain.callbacks.base import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_core.documents import Document
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType
from langchain.agents import initialize_agent

import os
from dotenv import load_dotenv
from utils.log import logReport
from colorama import Fore, Style

from agent.prompt_builder import SiteBaseAnalyserPrompt, PlanBuilderPrompt, AttackExecutorPrompt
from agent.peneteration_tools import all_tools
from agent.peneteration_tools import Nmap, ScanHeaders, SqlInjection, Xss 
from utils.extract_urls_from_list import extract_urls_from_text


load_dotenv()

class ToolOutputLogger(BaseCallbackHandler):
    def __init__(self):
        super().__init__()
        self.tool_outputs = []

    def on_tool_end(self, tool_output: str, **kwargs):
        self.tool_outputs.append(tool_output)


def clean_and_label_docs(documents):
    cleaned_docs = []

    for doc in documents:
        content = doc.page_content.strip()

        if "<html" in content or "<!DOCTYPE html" in content:
            labeled = f"=== HTML SOURCE CODE ===\n{content}"
        elif "Presence of" in content or "detected" in content:
            labeled = f"=== STACK INFORMATION ===\n{content}"
        elif "https://" in content:
            labeled = f"=== SUBDOMAINS & Routes FOUND ===\n{content}"
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
    
    filtered_docs = [doc for doc in docs if doc.metadata["source"].endswith(("target_html.txt", "target_stack_data.txt", "valid_subdomains.txt", "endpoints.txt"))]
    document = filtered_docs
    
    
    combined = clean_and_label_docs(document)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents([Document(page_content=combined)])
    chain = load_qa_chain(llm, chain_type="stuff")
    
    
    
    prompt = SiteBaseAnalyserPrompt()
    
    
    
    result = chain.invoke({"input_documents":splitter, "question": prompt})
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

    prompt = PlanBuilderPrompt()

    print("[*] Invoking LLM to generate plan...")
    plan = chain.invoke({"input_documents": documents, "question": prompt})
    print("[+] Plan generation complete.\n")

    save_file = os.path.join("db", "plan.md")
       
    with open(save_file, "w") as f:
         f.write(plan["output_text"])
    

    print("========== GENERATED ATTACK PLAN ==========")
    print(plan["output_text"])
    print("===========================================")
    
    
    
def attack_target():
    load_data = os.path.join("db", "plan.md")
    save_file = os.path.join("db", "report.md")

    if not os.path.exists(load_data):
        print("[-] Plan file not found!")
        return

    llm = ChatOpenAI(
        model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
        base_url="https://openrouter.ai/api/v1",
    )

  
    memory = ConversationBufferMemory(memory_key="chat_history")
    tool_logger = ToolOutputLogger()

    agent = initialize_agent(
        tools=all_tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        callbacks=[tool_logger],  
        handle_parsing_errors=True,
        max_iterations=30,
        max_execution_time=300,
    )

    with open(load_data, "r", encoding="utf-8", errors="ignore") as f:
        plan = f.read()

    prompt = f"{plan}\n\nExecute the above attack plan step-by-step."

    print("[*] Running agent on attack plan...")
    result = agent.run(prompt)  # run agent on the plan prompt

    # Write agent final output + all captured tool outputs to report file
    with open(save_file, "w", encoding="utf-8") as f:
        f.write("\n\n===== AGENT FINAL OUTPUT =====\n")
        f.write(result)
        f.write("\n\n===== TOOL OUTPUTS =====\n")
        for output in tool_logger.tool_outputs:
            f.write(output + "\n\n")

    print("[+] Attack completed. Results saved to db/report.md")