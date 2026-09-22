import sys
import json
import datetime
import subprocess
import os

def add_post(title, html_content):
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(repo_dir, "historico.json")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    data["posts"].insert(0, {
        "date": date_str,
        "title": title,
        "content": html_content
    })
    
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
        
    subprocess.run(["git", "add", "historico.json"], cwd=repo_dir)
    subprocess.run(["git", "commit", "-m", f"Auto-post: {title}"], cwd=repo_dir)
    subprocess.run(["git", "push", "origin", "master"], cwd=repo_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 add_post.py 'Título' 'Conteúdo em HTML'")
        sys.exit(1)
    
    title = sys.argv[1]
    content = sys.argv[2]
    add_post(title, content)
