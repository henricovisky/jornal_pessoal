import sys
import json
import datetime
import subprocess
import os

def add_post(title, content_input):
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(repo_dir, "historico.json")
    
    # Se content_input for um caminho para arquivo existente, lê o arquivo
    if os.path.isfile(content_input):
        with open(content_input, 'r', encoding='utf-8') as f:
            html_content = f.read().strip()
    else:
        html_content = content_input
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    data["posts"].insert(0, {
        "date": date_str,
        "title": title,
        "content": html_content
    })
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    subprocess.run(["git", "add", "historico.json"], cwd=repo_dir)
    subprocess.run(["git", "commit", "-m", f"Auto-post: {title}"], cwd=repo_dir)
    subprocess.run(["git", "push", "origin", "master"], cwd=repo_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 add_post.py 'Título' 'Conteúdo em HTML ou caminho para arquivo'")
        sys.exit(1)
    
    title = sys.argv[1]
    # Se houver múltiplos argumentos e não for arquivo, junta para recuperar corte acidental do bash
    if len(sys.argv) > 3 and not os.path.isfile(sys.argv[2]):
        content = " ".join(sys.argv[2:])
    else:
        content = sys.argv[2]
        
    add_post(title, content)
