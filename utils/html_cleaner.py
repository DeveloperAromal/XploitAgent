import re
import os


def clean_html(content: str, filename="target_html.txt", folder="db"):

    pattern = r'\s*(class|style)="[^"]*"|<!--.*?-->'
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(cleaned_content)

    print(f"✅ Cleaned content saved to: {file_path}")


# content = ""
# with open("db/target_html.txt") as html_content:
#     content = html_content.read()

# clean_html(content, filename="target_html.txt")
