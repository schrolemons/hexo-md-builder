"""Check skill files without installing runtime dependencies or executing user tasks."""
import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[2]
errors = []
ignored = {'.git', 'node_modules', '__pycache__', '.venv', 'output', 'dist'}
for required in ['README.md', 'SKILL.md']:
    if not (root / required).is_file():
        errors.append(f'Missing entry: {required}')
counts = {'markdown': 0, 'json': 0, 'python': 0}
for file in root.rglob('*'):
    if not file.is_file() or any(p in ignored for p in file.relative_to(root).parts):
        continue
    relative = file.relative_to(root).as_posix()
    try:
        if file.suffix == '.json':
            json.loads(file.read_text(encoding='utf-8-sig'))
            counts['json'] += 1
        elif file.suffix == '.py':
            ast.parse(file.read_text(encoding='utf-8-sig'), filename=relative)
            counts['python'] += 1
        elif file.suffix.lower() == '.md':
            counts['markdown'] += 1
            text = re.sub(r'(?ms)^```.*?^```[^\n]*$', '', file.read_text(encoding='utf-8'))
            text = re.sub(r'`+[^`\n]*`+', '', text)
            for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', text):
                target = target.strip().split(' "', 1)[0].strip('<>')
                if not target or target.startswith('#') or urlsplit(target).scheme:
                    continue
                local = unquote(target.split('#', 1)[0].split('?', 1)[0])
                if not local:
                    continue
                resolved = (file.parent / local).resolve()
                if not resolved.is_relative_to(root):
                    errors.append(f'{relative}: link leaves repository: {target}')
                elif not resolved.exists():
                    errors.append(f'{relative}: missing link target: {target}')
    except (ValueError, SyntaxError, UnicodeError) as error:
        errors.append(f'{relative}: {error}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Repository checks passed: ' + ', '.join(f'{k}={v}' for k, v in counts.items()))
