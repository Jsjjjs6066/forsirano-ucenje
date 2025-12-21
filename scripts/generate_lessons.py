import os

# Configuration
SOURCE_DIR = "/home/zlender/forsirano-ucenje"
DEST_DIR = "/home/zlender/forsirano-ucenje/lessons/osnove"
TEMPLATE = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Forsirano učenje</title>
    <link rel="stylesheet" href="/style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css" rel="stylesheet"
        id="theme-style" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism-dark.min.css" rel="stylesheet"
        media="(prefers-color-scheme: dark)" />
    <script src="/scripts/lessons.js"></script>
</head>

<body>
    <header>
        <div id="nav">
            <h1><a href="/index.html" class="nav-link">Uvod</a> / Osnove / {title}</h1>
        </div>
    </header>
    <div id="main">
        <h1>{title}</h1>
{content}
        <button class="complete-button" onclick="completeLesson('{lesson_id}')">
            Završi!
        </button>
    </div>
</body>

</html>"""

FILES = [
    {"src": "2_varijable.py", "title": "Varijable", "id": "varijable"},
    {"src": "3_operatori.py", "title": "Operatori", "id": "operatori"},
    {"src": "4_string.py", "title": "String", "id": "string"},
    {"src": "5_usporedjivanje.py", "title": "Uspoređivanje", "id": "usporedjivanje"},
    {"src": "6_if.py", "title": "If naredba", "id": "if"},
    {"src": "7_input.py", "title": "Input", "id": "input"},
]

def is_diagram(text):
    # Heuristic to detect ASCII diagrams
    if "|" in text or "---" in text or "   " in text:
        return True
    return False

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def format_comment_block(lines):
    if not lines:
        return ""
    text = "\n".join(lines)
    # Check if this block looks like a diagram
    if is_diagram(text):
        # Use simple <p> but with preservation styles as requested "comments as <p>"
        # Using style attribute to ensure whitespace matches the source diagram
        return f'        <p style="white-space: pre-wrap; font-family: monospace;">{escape_html(text)}</p>'
    else:
        # Normal text, join with spaces to reflow, or keep newlines? 
        # Usually comments are discrete lines. Let's keep them as lines but <br> or just let HTML reflow?
        # User said "comments as <p>". Usually this implies text.
        # Let's just join with newlines for now inside the p tag, it will render as space.
        return f'        <p>{escape_html(text)}</p>'

def format_code_block(lines):
    if not lines:
        return ""
    code = "\n".join(lines)
    return f'        <pre><code class="language-python">{escape_html(code)}</code></pre>'

def process_file(file_info):
    src_path = os.path.join(SOURCE_DIR, file_info["src"])
    dest_path = os.path.join(DEST_DIR, file_info["id"] + ".html")
    
    with open(src_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_parts = []
    
    current_block_type = None # 'comment' or 'code'
    buffer = []

    def flush():
        nonlocal current_block_type, buffer
        if not buffer:
            return
        if current_block_type == 'comment':
            html_parts.append(format_comment_block(buffer))
        elif current_block_type == 'code':
            html_parts.append(format_code_block(buffer))
        buffer = []
        current_block_type = None

    for line in lines:
        line_stripped = line.strip()
        
        # Handle empty lines
        if not line_stripped:
            flush()
            continue

        # Check for comments
        # We need to handle inline comments by splitting
        # But first, prioritize full line comments
        if line_stripped.startswith("#"):
            if current_block_type == 'code':
                flush()
            current_block_type = 'comment'
            # Remove the '# ' or '#' prefix
            content = line_stripped[1:]
            if content.startswith(" "):
                content = content[1:]
            
            # Special case: preserve indentation for diagrams
            # If the original line had indentation before #, we ignored it with strip()
            # But inside the comment, we want to keep structure.
            # actually line.find('#') might be better
            
            # Let's re-extract content carefully
            comment_start_index = line.find('#')
            raw_content = line[comment_start_index+1:]
            # If it's a "normal" comment, we strip, but if it's a diagram, we might want to keep spaces?
            # Let's just keep the raw content (swallowing one leading space if present)
            if raw_content.startswith(" "):
                raw_content = raw_content[1:]
            
            # Since we are stripping the line for check, we might lose indentation of the comment itself?
            # Yes. But usually python comments are aligned.
            # Diagram comments like:
            #     #     string
            # have leading spaces after #.
            # The code `raw_content` preserves that.
            
            buffer.append(raw_content.rstrip())
        
        else:
            # Starts with code
            # Check for inline comment
            # Be careful not to split string literals containing #
            # Simple heuristic: split on " # " or "# " if not inside quotes.
            # Writing a full tokenizer is overkill. Let's assume simple cases.
            
            # Simple inline split
            if "  #" in line or " # " in line or line_stripped.endswith("#"):
                 # This is risky for strings like "Hash # tag". 
                 # Given the lesson content, it's mostly simple code.
                 parts = line.split(" #", 1)  # Split on first space-hash
                 if len(parts) > 1:
                     code_part = parts[0]
                     comment_part = parts[1]
                 else:
                     # Maybe no space before hash? "a=1#comment"
                     # The file samples show "  # ..."
                     code_part = line.rstrip()
                     comment_part = None
                     
                     # Let's refine split: search for #
                     # Ignore if it's inside quotes.
                     # Quick hack: assume comments start with "  #" as per PEP8 often, or look at file samples.
                     # 2_varijable.py: `x = 0`, `a = 1 # Cijeli...`
                     # 3_operatori.py: `print(a + b) # Zbrajanje...`
                     
                     if "#" in line:
                         # Find index of #
                         idx = line.find("#")
                         # Verify it's not in a string?
                         # Files are simple. Let's just assume valid inline comments.
                         code_part = line[:idx].rstrip()
                         comment_part = line[idx+1:]
                         if comment_part.startswith(" "):
                             comment_part = comment_part[1:]
                     else:
                        code_part = line.rstrip()
                        comment_part = None
            else:
                code_part = line.rstrip()
                comment_part = None

            if current_block_type == 'comment':
                flush()
            
            current_block_type = 'code'
            if code_part:
                buffer.append(code_part)
            
            if comment_part:
                flush() # Flush the code part
                current_block_type = 'comment'
                buffer.append(comment_part.rstrip())


    flush()
    
    full_html = TEMPLATE.format(title=file_info["title"], content="\n".join(html_parts), lesson_id=file_info["id"])
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated {dest_path}")

if __name__ == "__main__":
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    for file_info in FILES:
        try:
            process_file(file_info)
        except Exception as e:
            print(f"Error processing {file_info['src']}: {e}")
