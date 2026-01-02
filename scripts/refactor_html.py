import os
import re

def refactor_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for <pre><code start
        if '<pre><code' in line:
            # Found the start of a target block
            # Determine indentation from this line for the wrapper div
            indent_match = re.match(r'\s*', line)
            indent = indent_match.group(0) if indent_match else ''
            
            group_lines = [line]
            current_idx = i + 1
            
            # Handle multi-line <pre> block if needed
            if '</pre>' not in line:
                while current_idx < len(lines):
                    l = lines[current_idx]
                    group_lines.append(l)
                    current_idx += 1
                    if '</pre>' in l:
                        break
            
            # Now look for consecutive <explainer-cont> blocks
            while current_idx < len(lines):
                # We need to handle potential whitespace/comments between blocks if appropriate,
                # but "right after" usually implies structure. 
                # We will skip empty lines to find the next tag.
                look_ahead_idx = current_idx
                temp_buffer = []
                found_explainer = False
                
                while look_ahead_idx < len(lines):
                    la_line = lines[look_ahead_idx]
                    if not la_line.strip():
                        temp_buffer.append(la_line)
                        look_ahead_idx += 1
                    elif la_line.strip().startswith('<explainer-cont>'):
                        found_explainer = True
                        break
                    else:
                        break
                
                if found_explainer:
                    # Add the empty lines we skipped
                    group_lines.extend(temp_buffer)
                    current_idx = look_ahead_idx
                    
                    # Consume the explainer-cont block
                    while current_idx < len(lines):
                        el = lines[current_idx]
                        group_lines.append(el)
                        current_idx += 1
                        if '</explainer-cont>' in el:
                            break
                else:
                    # Next content is not an explainer, stop looking
                    break
            
            # Wrap the identified group
            new_lines.append(f'{indent}<div class="code-cont">\n')
            new_lines.extend(group_lines)
            new_lines.append(f'{indent}</div>\n')
            
            i = current_idx
        else:
            new_lines.append(line)
            i += 1
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    target_dir = '/home/leon/forsirano-ucenje/lessons/osnove'
    files = [f for f in os.listdir(target_dir) if f.endswith('.html')]
    # files = ['string.html'] # Uncomment to test specific file first if needed manually
    
    for filename in files:
        filepath = os.path.join(target_dir, filename)
        refactor_file(filepath)

if __name__ == '__main__':
    main()
