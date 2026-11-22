"""把已編輯的 content.json 同步成可直接載入的 content.js。
用法：python sync_content.py
"""
import json
from pathlib import Path
folder=Path(__file__).resolve().parent
contents=json.loads((folder/'content.json').read_text(encoding='utf-8'))
assert isinstance(contents.get('chapters'),list) and isinstance(contents.get('lessons'),list) and isinstance(contents.get('stories'),list)
(folder/'content.js').write_text('window.BEAUTY_WORLD = '+json.dumps(contents,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f"已同步 {len(contents['lessons'])} 堂課程至 content.js")
