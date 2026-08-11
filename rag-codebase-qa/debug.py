import inspect, sys
sys.path.append('retrieve')
from retrieve.retriever import retrieve
print(inspect.signature(retrieve))