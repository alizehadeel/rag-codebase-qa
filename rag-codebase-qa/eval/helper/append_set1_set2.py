import json

set1_filename_mention = [
    {
        "question": "what does docs/advanced/proxies.md say about SOCKS proxies",
        "expected_files": ["docs/advanced/proxies.md"],
        "expected_qualified_names": ["SOCKS"],
        "reference_answer": "docs/advanced/proxies.md explains that SOCKS proxy support requires installing socksio (pip install httpx[socks]) and specifying a socks5:// or socks5h:// proxy URL.",
        "question_type": "filename_mention"
    },
    {
        "question": "what does docs/advanced/timeouts.md explain about default client timeouts",
        "expected_files": ["docs/advanced/timeouts.md"],
        "expected_qualified_names": ["Using the top-level API: > Setting a default timeout on a client"],
        "reference_answer": "docs/advanced/timeouts.md states that setting a timeout on an httpx.Client instance uses that timeout as the default for all requests issued by the client.",
        "question_type": "filename_mention"
    },
    {
        "question": "what does docs/async.md specify about supported async environments",
        "expected_files": ["docs/async.md"],
        "expected_qualified_names": ["Async Support > Supported async environments"],
        "reference_answer": "docs/async.md specifies that httpx supports asyncio and trio backends, and works with AnyIO for cross-framework compatibility.",
        "question_type": "filename_mention"
    },
    {
        "question": "what does docs/environment_variables.md describe for SSL_CERT_FILE",
        "expected_files": ["docs/environment_variables.md"],
        "expected_qualified_names": ["Environment Variables > `SSL_CERT_FILE`"],
        "reference_answer": "docs/environment_variables.md describes SSL_CERT_FILE as an environment variable that overrides the default CA certificate bundle path used by httpx for SSL verification.",
        "question_type": "filename_mention"
    },
    {
        "question": "what exceptions are documented in docs/exceptions.md",
        "expected_files": ["docs/exceptions.md"],
        "expected_qualified_names": ["Exceptions > The exception hierarchy"],
        "reference_answer": "docs/exceptions.md documents HTTPError as the base exception class, divided into RequestError for transport/network failures and HTTPStatusError for 4xx/5xx HTTP status responses.",
        "question_type": "filename_mention"
    }
]

set2_no_answer = [
    {
        "question": "does httpx natively support WebSocket connections",
        "expected_files": [],
        "expected_qualified_names": [],
        "reference_answer": "No, httpx does not natively support WebSockets. For WebSocket functionality in httpx-based applications, third-party libraries like httpx-ws should be used.",
        "question_type": "no_answer"
    },
    {
        "question": "does httpx automatically cache HTTP responses out of the box",
        "expected_files": [],
        "expected_qualified_names": [],
        "reference_answer": "No, httpx does not provide built-in HTTP response caching. Third-party extensions such as Hishel provide HTTP caching for httpx.",
        "question_type": "no_answer"
    },
    {
        "question": "does httpx include built-in classes for OAuth2 authentication flows",
        "expected_files": [],
        "expected_qualified_names": [],
        "reference_answer": "No, httpx does not include built-in OAuth1 or OAuth2 authentication flow classes. Third-party libraries like Authlib or httpx-auth should be used for OAuth authentication.",
        "question_type": "no_answer"
    },
    {
        "question": "can httpx make requests to FTP or SFTP servers",
        "expected_files": [],
        "expected_qualified_names": [],
        "reference_answer": "No, httpx only supports HTTP and HTTPS protocols. Attempting to issue a request to an ftp:// URL will raise an UnsupportedProtocol exception.",
        "question_type": "no_answer"
    },
    {
        "question": "does httpx provide built-in HTML parsing or DOM query methods",
        "expected_files": [],
        "expected_qualified_names": [],
        "reference_answer": "No, httpx is exclusively an HTTP client library and does not include built-in HTML parsing or DOM querying features. Developers typically pair httpx with external libraries like BeautifulSoup or selectolax for HTML parsing.",
        "question_type": "no_answer"
    }
]

existing = [json.loads(line) for line in open("eval/qa_set.jsonl", encoding="utf-8") if line.strip()]
print(f"Existing count: {len(existing)}")

all_qa = existing + set1_filename_mention + set2_no_answer

with open("eval/qa_set.jsonl", "w", encoding="utf-8") as f:
    for item in all_qa:
        f.write(json.dumps(item) + "\n")

print(f"Successfully appended 10 items (5 filename_mention + 5 no_answer). Total dataset count: {len(all_qa)}")
