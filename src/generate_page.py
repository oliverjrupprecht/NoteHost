from markdown_to_html_node import markdown_to_html_node, extract_title
import os.path

def generate_page(from_path, dest_path, template):
    print(f"generating page {from_path} to {dest_path} from {template}...")

    with open(from_path, "r") as md_file:
        md = md_file.read()

    with open(template, "r") as template_file:
        template = template_file.read()

    print()
    print(md)

    title = extract_title(md)
    html_nodes = markdown_to_html_node(md)
    html = html_nodes.to_html()
    print()
    print(html_nodes)
    print()
    print(html)
    print()

    out = template.replace("{{ Content }}", html)

    print(out)
    print()

    if os.path.exists(dest_path):
        print("path exists, writing...")
        with open(dest_path, "w") as write_file:
            write_file.write(out)

     

    
    
