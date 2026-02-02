import os
import glob
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Configuration
CONTENT_DIR = "content"
OUTPUT_DIR = "."
TEMPLATES_DIR = "templates"
STATIC_DIR = "static"

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def build():
    # Load templates
    post_template = env.get_template("post.html")
    index_template = env.get_template("index.html")

    posts = []

    # Process posts
    post_files = glob.glob(os.path.join(CONTENT_DIR, "posts", "*.md"))
    for file_path in post_files:
        post = frontmatter.load(file_path)
        html_content = markdown.markdown(post.content)

        # Get metadata
        title = post.get("title", "Untitled")
        date = post.get("date", datetime.now())
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                pass  # Keep as string or handle error

        slug = os.path.splitext(os.path.basename(file_path))[0]
        url = f"{slug}.html"

        post_data = {"title": title, "date": date, "content": html_content, "url": url}
        posts.append(post_data)

        # Render post
        output_path = os.path.join(OUTPUT_DIR, url)
        with open(output_path, "w") as f:
            f.write(post_template.render(post=post_data))

    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x["date"], reverse=True)

    # Process index.md
    index_content = ""
    index_title = "Home"
    index_file = os.path.join(CONTENT_DIR, "index.md")
    if os.path.exists(index_file):
        post = frontmatter.load(index_file)
        index_content = markdown.markdown(post.content)
        index_title = post.get("title", index_title)

    # Render index
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w") as f:
        f.write(
            index_template.render(posts=posts, content=index_content, title=index_title)
        )

    print(f"Build complete! Generated {len(posts)} posts.")


if __name__ == "__main__":
    build()
