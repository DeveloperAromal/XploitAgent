import os
from langchain_openai import ChatOpenAI
from agent.prompt_builder import FinalReportPrompt
from emailer.send_report import Send_email

def generateReportAndSendMail(receiver_email, target_name="www.example.com", recipient_name="Security Team"):
    load_file = os.path.join("db", "report.md")
    with open(load_file, "r", encoding="utf-8") as f:
        report = f.read()

    llm = ChatOpenAI(
        model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
        base_url="https://openrouter.ai/api/v1",
    )

    prompt = FinalReportPrompt(report)
    get_report = llm.invoke(prompt).content

    app_email = "geethaniya42@gmail.com"
    app_password = "twpeheehhampadva"

    html_content = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Vulnerability Scan Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #ddd;
                padding: 30px;
            }}
            .container {{
                max-width: 700px;
                margin: auto;
                background: #1f1f1f;
                border-radius: 12px;
                padding: 30px;
                box-shadow: 0 0 30px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #fff;
                text-align: center;
            }}
            .summary {{
                background: #2b2b2b;
                padding: 20px;
                border-radius: 8px;
                margin-top: 20px;
            }}
            a.button {{
                display: inline-block;
                background: #3b82f6;
                color: #fff;
                padding: 12px 20px;
                border-radius: 8px;
                text-decoration: none;
                margin-top: 20px;
            }}
            .footer {{
                margin-top: 40px;
                font-size: 12px;
                text-align: center;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://vgvmufmldgmthuoxqrum.supabase.co/storage/v1/object/public/xploitagent-bucket//file_00000000413061f78631d52252e1aeab-removebg-preview.png" style="display: block; margin: 0 auto; width: 150px;" />
            <h1>🔐 Vulnerability Scan Report</h1>
            <p>Dear <strong>{recipient_name}</strong>,</p>
            <p>The vulnerability scan for <strong>{target_name}</strong> has been successfully completed. Below is a summary generated using AI:</p>

            <div class="summary">
                {get_report}
            </div>

            <p>For detailed analysis, please review the full scan report linked below:</p>
            <a href="#" class="button"> View Full Report</a>

            <div class="footer">
                <p>&copy; 2025 XploitAgent. All rights reserved.</p>
                <p>Need help? Contact support at xploitagent@example.com</p>
            </div>
        </div>
    </body>
    </html>
    """

    Send_email(
        receiver_email,
        subject=" Vulnerability Scan Report – XploitAgent",
        html_content=html_content,
        app_email=app_email,
        app_password=app_password
    )
