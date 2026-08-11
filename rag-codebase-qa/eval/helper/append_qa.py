import json

new_qa = [
    {
        "question": "how do I configure custom authentication in httpx",
        "expected_files": ["docs/advanced/authentication.md"],
        "expected_qualified_names": ["Custom authentication schemes"],
        "reference_answer": "Subclass httpx.Auth and implement auth_flow(request), yielding the request and receiving responses to handle challenges or attach headers.",
        "question_type": "semantic"
    },
    {
        "question": "how do I fine tune timeout settings for connect, read, write, and pool",
        "expected_files": ["docs/advanced/timeouts.md"],
        "expected_qualified_names": ["Using the top-level API: > Fine tuning the configuration"],
        "reference_answer": "Pass an httpx.Timeout object with specific keyword arguments like Timeout(5.0, connect=10.0, read=2.0) or Timeout(None, read=5.0) to configure granular connect, read, write, and pool timeouts.",
        "question_type": "exact_identifier"
    },
    {
        "question": "how is SSL verification configured or disabled in httpx",
        "expected_files": ["docs/advanced/ssl.md"],
        "expected_qualified_names": ["docs/advanced/ssl.md"],
        "reference_answer": "Pass verify=True (default), verify=False to disable SSL checks, or a path to a custom CA bundle string / ssl.SSLContext object to httpx.Client or httpx.AsyncClient.",
        "question_type": "semantic"
    },
    {
        "question": "how do event hooks work in httpx",
        "expected_files": ["docs/advanced/event-hooks.md"],
        "expected_qualified_names": ["docs/advanced/event-hooks.md"],
        "reference_answer": "Event hooks allow registering callable routines for request and response events on a client via event_hooks={'request': [...], 'response': [...]} to monitor or log HTTP activity.",
        "question_type": "semantic"
    },
    {
        "question": "how do I test a WSGI application using httpx",
        "expected_files": ["docs/advanced/transports.md"],
        "expected_qualified_names": ["Instantiate a client that makes WSGI requests with a client IP of \"1.2.3.4\". > WSGI Transport"],
        "reference_answer": "Use httpx.WSGITransport(app=app) and pass it as the transport parameter to httpx.Client to dispatch requests directly to a WSGI app without network calls.",
        "question_type": "exact_identifier"
    },
    {
        "question": "how do I configure connection pooling and limits in httpx",
        "expected_files": ["docs/advanced/resource-limits.md"],
        "expected_qualified_names": ["docs/advanced/resource-limits.md"],
        "reference_answer": "Configure connection limits by passing an httpx.Limits instance to the client, such as Limits(max_keepalive_connections=20, max_connections=100, keepalive_expiry=5.0).",
        "question_type": "exact_identifier"
    },
    {
        "question": "which environment variables affect SSL certificates in httpx",
        "expected_files": ["docs/environment_variables.md"],
        "expected_qualified_names": ["Environment Variables > `SSL_CERT_FILE`"],
        "reference_answer": "httpx checks SSL_CERT_FILE (pointing to a CA bundle file) and SSL_CERT_DIR (pointing to a CA bundle directory) to customize default SSL certificate authority locations.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what is the exception hierarchy for httpx errors",
        "expected_files": ["docs/exceptions.md"],
        "expected_qualified_names": ["Exceptions > The exception hierarchy"],
        "reference_answer": "All httpx exceptions derive from httpx.HTTPError. Transport/network failures subclass httpx.RequestError (e.g. ConnectError, TimeoutException), while status errors inherit from httpx.HTTPStatusError.",
        "question_type": "semantic"
    },
    {
        "question": "how do I enable HTTP/2 support in httpx",
        "expected_files": ["docs/http2.md"],
        "expected_qualified_names": ["HTTP/2 > Enabling HTTP/2"],
        "reference_answer": "Install the optional h2 package (or pip install httpx[http2]) and set http2=True when instantiating httpx.Client() or httpx.AsyncClient().",
        "question_type": "semantic"
    },
    {
        "question": "how do I enable debug logging for HTTP requests and responses",
        "expected_files": ["docs/logging.md"],
        "expected_qualified_names": ["docs/logging.md"],
        "reference_answer": "Configure Python's standard logging module to set the logger for httpx or httpcore to logging.DEBUG level to log request lines, status codes, and headers.",
        "question_type": "semantic"
    },
    {
        "question": "how do I send form encoded data in a POST request",
        "expected_files": ["docs/quickstart.md"],
        "expected_qualified_names": ["QuickStart > Sending Form Encoded Data"],
        "reference_answer": "Pass a dictionary of form fields to the data argument in httpx.post(url, data={'key': 'value'}) which automatically sets the Content-Type header to application/x-www-form-urlencoded.",
        "question_type": "semantic"
    },
    {
        "question": "how do I upload files in a multipart request",
        "expected_files": ["docs/quickstart.md"],
        "expected_qualified_names": ["QuickStart > Sending Multipart File Uploads"],
        "reference_answer": "Pass a dictionary to the files parameter, e.g. files={'file': open('report.xls', 'rb')} or files={'file': ('file.txt', open('file.txt', 'rb'), 'text/plain')}.",
        "question_type": "semantic"
    },
    {
        "question": "how does text auto-detection work for response content",
        "expected_files": ["docs/advanced/text-encodings.md"],
        "expected_qualified_names": ["Instantiate a client with the default configuration. > Using auto-detection"],
        "reference_answer": "By default httpx uses utf-8 fallback when charset is unspecified; custom auto-detection can be provided by setting default_encoding=chardet.detect or autodetect callback on the client.",
        "question_type": "semantic"
    },
    {
        "question": "how do I monitor download progress when reading a response body",
        "expected_files": ["docs/advanced/clients.md"],
        "expected_qualified_names": ["Monitoring download progress"],
        "reference_answer": "Use client.stream('GET', url) as a context manager and iterate over chunks with response.iter_bytes(), tracking response.num_bytes_downloaded relative to Content-Length.",
        "question_type": "semantic"
    },
    {
        "question": "how do I use SOCKS proxies with httpx",
        "expected_files": ["docs/advanced/proxies.md"],
        "expected_qualified_names": ["SOCKS"],
        "reference_answer": "Install socksio (pip install httpx[socks]) and specify a SOCKS proxy URL such as proxy='socks5://user:pass@host:port' or socks5h:// when initializing httpx.Client.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what are request extensions in httpx",
        "expected_files": ["docs/advanced/extensions.md"],
        "expected_qualified_names": ["Extensions > Request Extensions"],
        "reference_answer": "Extensions are a dictionary attached to a Request object under request.extensions used to pass protocol-level configuration options like timeout or trace down to the transport layer.",
        "question_type": "exact_identifier"
    },
    {
        "question": "what helper functions are provided in httpx's top-level API",
        "expected_files": ["docs/api.md"],
        "expected_qualified_names": ["Developer Interface > Helper Functions"],
        "reference_answer": "httpx provides top-level request functions like httpx.get(), httpx.post(), httpx.put(), httpx.delete(), httpx.patch(), httpx.head(), httpx.options(), httpx.request(), and httpx.stream().",
        "question_type": "exact_identifier"
    },
    {
        "question": "what features does the httpx URL object provide",
        "expected_files": ["docs/api.md"],
        "expected_qualified_names": ["Developer Interface > `URL`"],
        "reference_answer": "The httpx.URL object parses URLs into components (scheme, host, port, path, query, fragment), supports immutability, relative resolution (url.join(...)), and parameter manipulation (url.copy_with(...)).",
        "question_type": "exact_identifier"
    },
    {
        "question": "how does httpx handle cookie storage and manipulation",
        "expected_files": ["docs/api.md"],
        "expected_qualified_names": ["Developer Interface > `Cookies`"],
        "reference_answer": "httpx.Cookies provides a dictionary-like container managing HTTP cookies across requests, supporting domain/path scoping, .set(), .get(), .clear(), and extraction from response headers.",
        "question_type": "semantic"
    }
]

existing = [json.loads(line) for line in open("eval/qa_set.jsonl", encoding="utf-8") if line.strip()]
print(f"Existing count: {len(existing)}")

all_qa = existing + new_qa

with open("eval/qa_set.jsonl", "w", encoding="utf-8") as f:
    for item in all_qa:
        f.write(json.dumps(item) + "\n")

print(f"Successfully wrote {len(all_qa)} questions to eval/qa_set.jsonl")
