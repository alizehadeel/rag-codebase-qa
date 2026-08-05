
import json
from collections import Counter
chunks = [json.loads(l) for l in open('data/chunks.jsonl')]
print('Total:', len(chunks))
print(Counter(c['chunk_type'] for c in chunks))
print(Counter(c['chunk_method'] for c in chunks))

import json, random
chunks = [json.loads(l) for l in open('data/chunks.jsonl')]
for c in random.sample(chunks, 15):
    print('---', c['qualified_name'], f"({c['file_path']}:{c['start_line']}-{c['end_line']})")
    print(c['content'][:300])
    print()
