import json

code_qa = [
    {
        "question": "how does Client.build_request construct a Request instance",
        "expected_files": ["httpx/_client.py"],
        "expected_qualified_names": ["BaseClient.build_request"],
        "reference_answer": "Client.build_request merges the request's params, headers, and cookies with client defaults, joins relative URLs with base_url, and creates a Request object.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what is the behavior of Client.send when transmitting a request",
        "expected_files": ["httpx/_client.py"],
        "expected_qualified_names": ["Client.send"],
        "reference_answer": "Client.send sends the Request object as-is without modifying client defaults, manages auth flows, redirects, and streams if stream=True.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what is Client.request equivalent to",
        "expected_files": ["httpx/_client.py"],
        "expected_qualified_names": ["Client.request"],
        "reference_answer": "Client.request is equivalent to first building a request with client.build_request(...) and then sending it with client.send(request, ...).",
        "question_type": "exact_identifier"
    },
    {
        "question": "how does AsyncClient.request handle sending HTTP requests",
        "expected_files": ["httpx/_client.py"],
        "expected_qualified_names": ["AsyncClient.request"],
        "reference_answer": "AsyncClient.request builds a request via client.build_request(...) and asynchronously executes it via await client.send(request, ...).",
        "question_type": "exact_identifier"
    },
    {
        "question": "what exception does Response.raise_for_status raise on 4xx or 5xx responses",
        "expected_files": ["httpx/_models.py"],
        "expected_qualified_names": ["Response.raise_for_status"],
        "reference_answer": "Response.raise_for_status raises an HTTPStatusError if the response has a 4xx client error or 5xx server error status code, returning self if successful.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what is the base class for all HTTP errors in httpx",
        "expected_files": ["httpx/_exceptions.py"],
        "expected_qualified_names": ["HTTPError"],
        "reference_answer": "HTTPError is the base class for RequestError and HTTPStatusError, useful for catching all exceptions raised during requests or raise_for_status().",
        "question_type": "exact_identifier"
    },
    {
        "question": "when is an HTTPStatusError raised in httpx",
        "expected_files": ["httpx/_exceptions.py"],
        "expected_qualified_names": ["HTTPStatusError"],
        "reference_answer": "HTTPStatusError is raised when calling response.raise_for_status() on a response with a 4xx or 5xx HTTP status code, holding request and response attributes.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what is RequestError in httpx",
        "expected_files": ["httpx/_exceptions.py"],
        "expected_qualified_names": ["RequestError"],
        "reference_answer": "RequestError is the base class for all transport and network level exceptions that occur while attempting to issue an HTTP request.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what exception class represents timeout errors in httpx",
        "expected_files": ["httpx/_exceptions.py"],
        "expected_qualified_names": ["TimeoutException"],
        "reference_answer": "TimeoutException is the base class for all timeout-related errors when an operation times out (such as ConnectTimeout, ReadTimeout, or WriteTimeout).",
        "question_type": "exact_identifier"
    },
    {
        "question": "what exception is raised when httpx fails to establish a network connection",
        "expected_files": ["httpx/_exceptions.py"],
        "expected_qualified_names": ["ConnectError"],
        "reference_answer": "ConnectError is a subclass of NetworkError raised when httpx fails to establish a network connection to the target server.",
        "question_type": "exact_identifier"
    }
]

existing = [json.loads(line) for line in open("eval/qa_set.jsonl", encoding="utf-8") if line.strip()]
print(f"Existing QA count: {len(existing)}")

all_qa = existing + code_qa

with open("eval/qa_set.jsonl", "w", encoding="utf-8") as f:
    for item in all_qa:
        f.write(json.dumps(item) + "\n")

print(f"Successfully appended {len(code_qa)} code Q&A pairs. Total count: {len(all_qa)}")
