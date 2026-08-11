=== [1] CHANGELOG.md ===
FILE: CHANGELOG.md:1-6

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

----------------------------------------------------------------------

=== [2] Changelog > [UNRELEASED] ===
FILE: CHANGELOG.md:7-16

## [UNRELEASED]

### Removed

* Drop support for Python 3.8

### Added

* Expose `FunctionAuth` from the public API. (#3699)

----------------------------------------------------------------------

=== [3] Changelog > 0.28.1 (6th December, 2024) ===
FILE: CHANGELOG.md:17-20

## 0.28.1 (6th December, 2024)

* Fix SSL case where `verify=False` together with client side certificates.

----------------------------------------------------------------------

=== [4] Changelog > 0.28.0 (28th November, 2024) ===
FILE: CHANGELOG.md:21-48

## 0.28.0 (28th November, 2024)

Be aware that the default *JSON request bodies now use a more compact representation*. This is generally considered a prefered style, tho may require updates to test suites.

The 0.28 release includes a limited set of deprecations...

**Deprecations**:

We are working towards a simplified SSL configuration API.

*For users of the standard `verify=True` or `verify=False` cases, or `verify=<ssl_context>` case this should require no changes. The following cases have been deprecated...*

* The `verify` argument as a string argument is now deprecated and will raise warnings.
* The `cert` argument is now deprecated and will raise warnings.

Our revised [SSL documentation](docs/advanced/ssl.md) covers how to implement the same behaviour with a more constrained API.

**The following changes are also included**:

* The deprecated `proxies` argument has now been removed.
* The deprecated `app` argument has now been removed.
* JSON request bodies use a compact representation. (#3363)
* Review URL percent escape sets, based on WHATWG spec. (#3371, #3373)
* Ensure `certifi` and `httpcore` are only imported if required. (#3377)
* Treat `socks5h` as a valid proxy scheme. (#3178)
* Cleanup `Request()` method signature in line with `client.request()` and `httpx.request()`. (#3378)
* Bugfix: When passing `params={}`, always strictly update rather than merge with an existing querystring. (#3364)

----------------------------------------------------------------------

=== [5] Changelog > 0.27.2 (27th August, 2024) ===
FILE: CHANGELOG.md:49-54

## 0.27.2 (27th August, 2024)

### Fixed

* Reintroduced supposedly-private `URLTypes` shortcut. (#2673)

----------------------------------------------------------------------

=== [6] Changelog > 0.27.1 (27th August, 2024) ===
FILE: CHANGELOG.md:55-65

## 0.27.1 (27th August, 2024)

### Added

* Support for `zstd` content decoding using the python `zstandard` package is added. Installable using `httpx[zstd]`. (#3139)

### Fixed

* Improved error messaging for `InvalidURL` exceptions. (#3250)
* Fix `app` type signature in `ASGITransport`. (#3109)

----------------------------------------------------------------------

=== [7] Changelog > 0.27.0 (21st February, 2024) ===
FILE: CHANGELOG.md:66-76

## 0.27.0 (21st February, 2024)

### Deprecated

* The `app=...` shortcut has been deprecated. Use the explicit style of `transport=httpx.WSGITransport()` or `transport=httpx.ASGITransport()` instead.

### Fixed

* Respect the `http1` argument while configuring proxy transports. (#3023)
* Fix RFC 2069 mode digest authentication. (#3045)

----------------------------------------------------------------------

=== [8] Changelog > 0.26.0 (20th December, 2023) ===
FILE: CHANGELOG.md:77-94

## 0.26.0 (20th December, 2023)

### Added

* The `proxy` argument was added. You should use the `proxy` argument instead of the deprecated `proxies`, or use `mounts=` for more complex configurations. (#2879)

### Deprecated

* The `proxies` argument is now deprecated. It will still continue to work, but it will be removed in the future. (#2879)

### Fixed

* Fix cases of double escaping of URL path components. Allow / as a safe character in the query portion. (#2990)
* Handle `NO_PROXY` envvar cases when a fully qualified URL is supplied as the value. (#2741)
* Allow URLs where username or password contains unescaped '@'. (#2986)
* Ensure ASGI `raw_path` does not include URL query component. (#2999)
* Ensure `Response.iter_text()` cannot yield empty strings. (#2998)

----------------------------------------------------------------------

=== [9] Changelog > 0.25.2 (24th November, 2023) ===
FILE: CHANGELOG.md:95-100

## 0.25.2 (24th November, 2023)

### Added

* Add missing type hints to few `__init__()` methods. (#2938)

----------------------------------------------------------------------

=== [10] Changelog > 0.25.1 (3rd November, 2023) ===
FILE: CHANGELOG.md:101-111

## 0.25.1 (3rd November, 2023)

### Added

* Add support for Python 3.12. (#2854)
* Add support for httpcore 1.0 (#2885)

### Fixed

* Raise `ValueError` on `Response.encoding` being set after `Response.text` has been accessed. (#2852)

----------------------------------------------------------------------

=== [11] Changelog > 0.25.0 (11th September, 2023) ===
FILE: CHANGELOG.md:112-131

## 0.25.0 (11th September, 2023)

### Removed

* Drop support for Python 3.7. (#2813)

### Added

* Support HTTPS proxies. (#2845)
* Change the type of `Extensions` from `Mapping[Str, Any]` to `MutableMapping[Str, Any]`. (#2803)
* Add `socket_options` argument to `httpx.HTTPTransport` and `httpx.AsyncHTTPTransport` classes. (#2716)
* The `Response.raise_for_status()` method now returns the response instance. For example: `data = httpx.get('...').raise_for_status().json()`. (#2776)

### Fixed

* Return `500` error response instead of exceptions when `raise_app_exceptions=False` is set on `ASGITransport`. (#2669)
* Ensure all `WSGITransport` environs have a `SERVER_PROTOCOL`. (#2708)
* Always encode forward slashes as `%2F` in query parameters (#2723)
* Use Mozilla documentation instead of `httpstatuses.com` for HTTP error reference (#2768)

----------------------------------------------------------------------

=== [12] Changelog > 0.24.1 (17th May, 2023) ===
FILE: CHANGELOG.md:132-146

## 0.24.1 (17th May, 2023)

### Added

* Provide additional context in some `InvalidURL` exceptions. (#2675)

### Fixed

* Fix optional percent-encoding behaviour. (#2671)
* More robust checking for opening upload files in binary mode. (#2630)
* Properly support IP addresses in `NO_PROXY` environment variable. (#2659)
* Set default file for `NetRCAuth()` to `None` to use the stdlib default. (#2667)
* Set logging request lines to INFO level for async requests, in line with sync requests. (#2656)
* Fix which gen-delims need to be escaped for path/query/fragment components in URL. (#2701)

----------------------------------------------------------------------

=== [13] Changelog > 0.24.0 (6th April, 2023) ===
FILE: CHANGELOG.md:147-159

## 0.24.0 (6th April, 2023)

### Changed

* The logging behaviour has been changed to be more in-line with other standard Python logging usages. We no longer have a custom `TRACE` log level, and we no longer use the `HTTPX_LOG_LEVEL` environment variable to auto-configure logging. We now have a significant amount of `DEBUG` logging available at the network level. Full documentation is available at https://www.python-httpx.org/logging/ (#2547, encode/httpcore#648)
* The `Response.iter_lines()` method now matches the stdlib behaviour and does not include the newline characters. It also resolves a performance issue. (#2423)
* Query parameter encoding switches from using + for spaces and %2F for forward slash, to instead using %20 for spaces and treating forward slash as a safe, unescaped character. This differs from `requests`, but is in line with browser behavior in Chrome, Safari, and Firefox. Both options are RFC valid. (#2543)
* NetRC authentication is no longer automatically handled, but is instead supported by an explicit `httpx.NetRCAuth()` authentication class. See the documentation at https://www.python-httpx.org/advanced/authentication/#netrc-authentication (#2525)

### Removed

* The `rfc3986` dependancy has been removed. (#2252)

----------------------------------------------------------------------

=== [14] Changelog > 0.23.3 (4th January, 2023) ===
FILE: CHANGELOG.md:160-165

## 0.23.3 (4th January, 2023)

### Fixed

* Version 0.23.2 accidentally included stricter type checking on query parameters. This shouldn've have been included in a minor version bump, and is now reverted. (#2523, #2539)

----------------------------------------------------------------------

=== [15] Changelog > 0.23.2 (2nd January, 2023) ===
FILE: CHANGELOG.md:166-177

## 0.23.2 (2nd January, 2023)

### Added

* Support digest auth nonce counting to avoid multiple auth requests. (#2463)

### Fixed

* Multipart file uploads where the file length cannot be determine now use chunked transfer encoding, rather than loading the entire file into memory in order to determine the `Content-Length`. (#2382)
* Raise `TypeError` if content is passed a dict-instance. (#2495)
* Partially revert the API breaking change in 0.23.1, which removed `RawURL`. We continue to expose a `url.raw` property which is now a plain named-tuple. This API is still expected to be deprecated, but we will do so with a major version bump. (#2481)

----------------------------------------------------------------------

=== [16] Changelog > 0.23.1 (18th November, 2022) ===
FILE: CHANGELOG.md:178-201

## 0.23.1 (18th November, 2022)

**Note**: The 0.23.1 release should have used a proper version bump, rather than a minor point release.
There are API surface area changes that may affect some users.
See the "Removed" section of these release notes for details.

### Added

* Support for Python 3.11. (#2420)
* Allow setting an explicit multipart boundary in `Content-Type` header. (#2278)
* Allow `tuple` or `list` for multipart values, not just `list`. (#2355)
* Allow `str` content for multipart upload files. (#2400)
* Support connection upgrades. See https://www.encode.io/httpcore/extensions/#upgrade-requests

### Fixed

* Don't drop empty query parameters. (#2354)

### Removed

* Upload files *must* always be opened in binary mode. (#2400)
* Drop `.read`/`.aread` from `SyncByteStream`/`AsyncByteStream`. (#2407)
* Drop `RawURL`. (#2241)

----------------------------------------------------------------------

=== [17] Changelog > 0.23.0 (23rd May, 2022) ===
FILE: CHANGELOG.md:202-221

## 0.23.0 (23rd May, 2022)

### Changed

* Drop support for Python 3.6. (#2097)
* Use `utf-8` as the default character set, instead of falling back to `charset-normalizer` for auto-detection. To enable automatic character set detection, see [the documentation](https://www.python-httpx.org/advanced/text-encodings/#using-auto-detection). (#2165)

### Fixed

* Fix `URL.copy_with` for some oddly formed URL cases. (#2185)
* Digest authentication should use case-insensitive comparison for determining which algorithm is being used. (#2204)
* Fix console markup escaping in command line client. (#1866)
* When files are used in multipart upload, ensure we always seek to the start of the file. (#2065)
* Ensure that `iter_bytes` never yields zero-length chunks. (#2068)
* Preserve `Authorization` header for redirects that are to the same origin, but are an `http`-to-`https` upgrade. (#2074)
* When responses have binary output, don't print the output to the console in the command line client. Use output like `<16086 bytes of binary data>` instead. (#2076)
* Fix display of `--proxies` argument in the command line client help. (#2125)
* Close responses when task cancellations occur during stream reading. (#2156)
* Fix type error on accessing `.request` on `HTTPError` exceptions. (#2158)

----------------------------------------------------------------------

=== [18] Changelog > 0.22.0 (26th January, 2022) ===
FILE: CHANGELOG.md:222-233

## 0.22.0 (26th January, 2022)

### Added

* Support for [the SOCKS5 proxy protocol](https://www.python-httpx.org/advanced/proxies/#socks) via [the `socksio` package](https://github.com/sethmlarson/socksio). (#2034)
* Support for custom headers in multipart/form-data requests (#1936)

### Fixed

* Don't perform unreliable close/warning on `__del__` with unclosed clients. (#2026)
* Fix `Headers.update(...)` to correctly handle repeated headers (#2038)

----------------------------------------------------------------------

=== [19] Changelog > 0.21.3 (6th January, 2022) ===
FILE: CHANGELOG.md:234-239

## 0.21.3 (6th January, 2022)

### Fixed

* Fix streaming uploads using `SyncByteStream` or `AsyncByteStream`. Regression in 0.21.2. (#2016)

----------------------------------------------------------------------

=== [20] Changelog > 0.21.2 (5th January, 2022) ===
FILE: CHANGELOG.md:240-246

## 0.21.2 (5th January, 2022)

### Fixed

* HTTP/2 support for tunnelled proxy cases. (#2009)
* Improved the speed of large file uploads. (#1948)

----------------------------------------------------------------------

=== [21] Changelog > 0.21.1 (16th November, 2021) ===
FILE: CHANGELOG.md:247-252

## 0.21.1 (16th November, 2021)

### Fixed

* The `response.url` property is now correctly annotated as `URL`, instead of `Optional[URL]`. (#1940)

----------------------------------------------------------------------

=== [22] Changelog > 0.21.0 (15th November, 2021) ===
FILE: CHANGELOG.md:253-270

## 0.21.0 (15th November, 2021)

The 0.21.0 release integrates against a newly redesigned `httpcore` backend.

Both packages ought to automatically update to the required versions, but if you are
seeing any issues, you should ensure that you have `httpx==0.21.*` and `httpcore==0.14.*` installed.

### Added

* The command-line client will now display connection information when `-v/--verbose` is used.
* The command-line client will now display server certificate information when `-v/--verbose` is used.
* The command-line client is now able to properly detect if the outgoing request
should be formatted as HTTP/1.1 or HTTP/2, based on the result of the HTTP/2 negotiation.

### Removed

* Curio support is no longer currently included. Please get in touch if you require this, so that we can assess priorities.

----------------------------------------------------------------------

=== [23] Changelog > 0.20.0 (13th October, 2021) ===
FILE: CHANGELOG.md:271-337

## 0.20.0 (13th October, 2021)

The 0.20.0 release adds an integrated command-line client, and also includes some
design changes. The most notable of these is that redirect responses are no longer
automatically followed, unless specifically requested.

This design decision prioritises a more explicit approach to redirects, in order
to avoid code that unintentionally issues multiple requests as a result of
misconfigured URLs.

For example, previously a client configured to send requests to `http://api.github.com/`
would end up sending every API request twice, as each request would be redirected to `https://api.github.com/`.

If you do want auto-redirect behaviour, you can enable this either by configuring
the client instance with `Client(follow_redirects=True)`, or on a per-request
basis, with `.get(..., follow_redirects=True)`.

This change is a classic trade-off between convenience and precision, with no "right"
answer. See [discussion #1785](https://github.com/encode/httpx/discussions/1785) for more
context.

The other major design change is an update to the Transport API, which is the low-level
interface against which requests are sent. Previously this interface used only primitive
datastructures, like so...

```python
(status_code, headers, stream, extensions) = transport.handle_request(method, url, headers, stream, extensions)
try
    ...
finally:
    stream.close()
```

Now the interface is much simpler...

```python
response = transport.handle_request(request)
try
    ...
finally:
    response.close()
```

### Changed

* The `allow_redirects` flag is now `follow_redirects` and defaults to `False`.
* The `raise_for_status()` method will now raise an exception for any responses
  except those with 2xx status codes. Previously only 4xx and 5xx status codes
  would result in an exception.
* The low-level transport API changes to the much simpler `response = transport.handle_request(request)`.
* The `client.send()` method no longer accepts a `timeout=...` argument, but the
  `client.build_request()` does. This required by the signature change of the
  Transport API. The request timeout configuration is now stored on the request
  instance, as `request.extensions['timeout']`.

### Added

* Added the `httpx` command-line client.
* Response instances now include `.is_informational`, `.is_success`, `.is_redirect`, `.is_client_error`, and `.is_server_error`
  properties for checking 1xx, 2xx, 3xx, 4xx, and 5xx response types. Note that the behaviour of `.is_redirect` is slightly different in that it now returns True for all 3xx responses, in order to allow for a consistent set of properties onto the different HTTP status code types. The `response.has_redirect_location` location may be used to determine responses with properly formed URL redirects.

### Fixed

* `response.iter_bytes()` no longer raises a ValueError when called on a response with no content. (Pull #1827)
* The `'wsgi.error'` configuration now defaults to `sys.stderr`, and is corrected to be a `TextIO` interface, not a `BytesIO` interface. Additionally, the WSGITransport now accepts a `wsgi_error` configuration. (Pull #1828)
* Follow the WSGI spec by properly closing the iterable returned by the application. (Pull #1830)

----------------------------------------------------------------------

=== [24] Changelog > 0.19.0 (19th August, 2021) ===
FILE: CHANGELOG.md:338-351

## 0.19.0 (19th August, 2021)

### Added

* Add support for `Client(allow_redirects=<bool>)`. (Pull #1790)
* Add automatic character set detection, when no `charset` is included in the response `Content-Type` header. (Pull #1791)

### Changed

* Event hooks are now also called for any additional redirect or auth requests/responses. (Pull #1806)
* Strictly enforce that upload files must be opened in binary mode. (Pull #1736)
* Strictly enforce that client instances can only be opened and closed once, and cannot be re-opened. (Pull #1800)
* Drop `mode` argument from `httpx.Proxy(..., mode=...)`. (Pull #1795)

----------------------------------------------------------------------

=== [25] Changelog > 0.18.2 (17th June, 2021) ===
FILE: CHANGELOG.md:352-364

## 0.18.2 (17th June, 2021)

### Added

* Support for Python 3.10. (Pull #1687)
* Expose `httpx.USE_CLIENT_DEFAULT`, used as the default to `auth` and `timeout` parameters in request methods. (Pull #1634)
* Support [HTTP/2 "prior knowledge"](https://python-hyper.org/projects/hyper-h2/en/v2.3.1/negotiating-http2.html#prior-knowledge), using `httpx.Client(http1=False, http2=True)`. (Pull #1624)

### Fixed

* Clean up some cases where warnings were being issued. (Pull #1687)
* Prefer Content-Length over Transfer-Encoding: chunked for content=<file-like> cases. (Pull #1619)

----------------------------------------------------------------------

=== [26] Changelog > 0.18.1 (29th April, 2021) ===
FILE: CHANGELOG.md:365-376

## 0.18.1 (29th April, 2021)

### Changed

* Update brotli support to use the `brotlicffi` package (Pull #1605)
* Ensure that `Request(..., stream=...)` does not auto-generate any headers on the request instance. (Pull #1607)

### Fixed

* Pass through `timeout=...` in top-level httpx.stream() function. (Pull #1613)
* Map httpcore transport close exceptions to httpx exceptions. (Pull #1606)

----------------------------------------------------------------------

=== [27] Changelog > 0.18.0 (27th April, 2021) ===
FILE: CHANGELOG.md:377-418

## 0.18.0 (27th April, 2021)

The 0.18.x release series formalises our low-level Transport API, introducing the base classes `httpx.BaseTransport` and `httpx.AsyncBaseTransport`.

See the "[Custom transports](https://www.python-httpx.org/advanced/transports/#custom-transports)" documentation and the [`httpx.BaseTransport.handle_request()`](https://github.com/encode/httpx/blob/397aad98fdc8b7580a5fc3e88f1578b4302c6382/httpx/_transports/base.py#L77-L147) docstring for more complete details on implementing custom transports.

Pull request #1522 includes a checklist of differences from the previous `httpcore` transport API, for developers implementing custom transports.

The following API changes have been issuing deprecation warnings since 0.17.0 onwards, and are now fully deprecated...

* You should now use httpx.codes consistently instead of httpx.StatusCodes.
* Use limits=... instead of pool_limits=....
* Use proxies={"http://": ...} instead of proxies={"http": ...} for scheme-specific mounting.

### Changed

* Transport instances now inherit from `httpx.BaseTransport` or `httpx.AsyncBaseTransport`,
  and should implement either the `handle_request` method or `handle_async_request` method. (Pull #1522, #1550)
* The `response.ext` property and `Response(ext=...)` argument are now named `extensions`. (Pull #1522)
* The recommendation to not use `data=<bytes|str|bytes (a)iterator>` in favour of `content=<bytes|str|bytes (a)iterator>` has now been escalated to a deprecation warning. (Pull #1573)
* Drop `Response(on_close=...)` from API, since it was a bit of leaking implementation detail. (Pull #1572)
* When using a client instance, cookies should always be set on the client, rather than on a per-request basis. We prefer enforcing a stricter API here because it provides clearer expectations around cookie persistence, particularly when redirects occur. (Pull #1574)
* The runtime exception `httpx.ResponseClosed` is now named `httpx.StreamClosed`. (#1584)
* The `httpx.QueryParams` model now presents an immutable interface. There is a discussion on [the design and motivation here](https://github.com/encode/httpx/discussions/1599). Use `client.params = client.params.merge(...)` instead of `client.params.update(...)`. The basic query manipulation methods are `query.set(...)`, `query.add(...)`, and `query.remove()`. (#1600)

### Added

* The `Request` and `Response` classes can now be serialized using pickle. (#1579)
* Handle `data={"key": [None|int|float|bool]}` cases. (Pull #1539)
* Support `httpx.URL(**kwargs)`, for example `httpx.URL(scheme="https", host="www.example.com", path="/')`, or `httpx.URL("https://www.example.com/", username="tom@gmail.com", password="123 456")`. (Pull #1601)
* Support `url.copy_with(params=...)`. (Pull #1601)
* Add `url.params` parameter, returning an immutable `QueryParams` instance. (Pull #1601)
* Support query manipulation methods on the URL class. These are `url.copy_set_param()`, `url.copy_add_param()`, `url.copy_remove_param()`, `url.copy_merge_params()`. (Pull #1601)
* The `httpx.URL` class now performs port normalization, so `:80` ports are stripped from `http` URLs and `:443` ports are stripped from `https` URLs. (Pull #1603)
* The `URL.host` property returns unicode strings for internationalized domain names. The `URL.raw_host` property returns byte strings with IDNA escaping applied. (Pull #1590)

### Fixed

* Fix Content-Length for cases of `files=...` where unicode string is used as the file content. (Pull #1537)
* Fix some cases of merging relative URLs against `Client(base_url=...)`. (Pull #1532)
* The `request.content` attribute is now always available except for streaming content, which requires an explicit `.read()`. (Pull #1583)

----------------------------------------------------------------------

=== [28] Changelog > 0.17.1 (March 15th, 2021) ===
FILE: CHANGELOG.md:419-425

## 0.17.1 (March 15th, 2021)

### Fixed

* Type annotation on `CertTypes` allows `keyfile` and `password` to be optional. (Pull #1503)
* Fix httpcore pinned version. (Pull #1495)

----------------------------------------------------------------------

=== [29] Changelog > 0.17.0 (February 28th, 2021) ===
FILE: CHANGELOG.md:426-446

## 0.17.0 (February 28th, 2021)

### Added

* Add `httpx.MockTransport()`, allowing to mock out a transport using pre-determined responses. (Pull #1401, Pull #1449)
* Add `httpx.HTTPTransport()` and `httpx.AsyncHTTPTransport()` default transports. (Pull #1399)
* Add mount API support, using `httpx.Client(mounts=...)`. (Pull #1362)
* Add `chunk_size` parameter to `iter_raw()`, `iter_bytes()`, `iter_text()`. (Pull #1277)
* Add `keepalive_expiry` parameter to `httpx.Limits()` configuration. (Pull #1398)
* Add repr to `httpx.Cookies` to display available cookies. (Pull #1411)
* Add support for `params=<tuple>` (previously only `params=<list>` was supported). (Pull #1426)

### Fixed

* Add missing `raw_path` to ASGI scope. (Pull #1357)
* Tweak `create_ssl_context` defaults to use `trust_env=True`. (Pull #1447)
* Properly URL-escape WSGI `PATH_INFO`. (Pull #1391)
* Properly set default ports in WSGI transport. (Pull #1469)
* Properly encode slashes when using `base_url`. (Pull #1407)
* Properly map exceptions in `request.aclose()`. (Pull #1465)

----------------------------------------------------------------------

=== [30] Changelog > 0.16.1 (October 8th, 2020) ===
FILE: CHANGELOG.md:447-453

## 0.16.1 (October 8th, 2020)

### Fixed

* Support literal IPv6 addresses in URLs. (Pull #1349)
* Force lowercase headers in ASGI scope dictionaries. (Pull #1351)

----------------------------------------------------------------------

=== [31] Changelog > 0.16.0 (October 6th, 2020) ===
FILE: CHANGELOG.md:454-466

## 0.16.0 (October 6th, 2020)

### Changed

* Preserve HTTP header casing. (Pull #1338, encode/httpcore#216, python-hyper/h11#104)
* Drop `response.next()` and `response.anext()` methods in favour of `response.next_request` attribute. (Pull #1339)
* Closed clients now raise a runtime error if attempting to send a request. (Pull #1346)

### Added

* Add Python 3.9 to officially supported versions.
* Type annotate `__enter__`/`__exit__`/`__aenter__`/`__aexit__` in a way that supports subclasses of `Client` and `AsyncClient`. (Pull #1336)

----------------------------------------------------------------------

=== [32] Changelog > 0.15.5 (October 1st, 2020) ===
FILE: CHANGELOG.md:467-472

## 0.15.5 (October 1st, 2020)

### Added

* Add `response.next_request` (Pull #1334)

----------------------------------------------------------------------

=== [33] Changelog > 0.15.4 (September 25th, 2020) ===
FILE: CHANGELOG.md:473-482

## 0.15.4 (September 25th, 2020)

### Added

* Support direct comparisons between `Headers` and dicts or lists of two-tuples. Eg. `assert response.headers == {"Content-Length": 24}` (Pull #1326)

### Fixed

* Fix automatic `.read()` when `Response` instances are created with `content=<str>` (Pull #1324)

----------------------------------------------------------------------

=== [34] Changelog > 0.15.3 (September 24th, 2020) ===
FILE: CHANGELOG.md:483-488

## 0.15.3 (September 24th, 2020)

### Fixed

* Fixed connection leak in async client due to improper closing of response streams. (Pull #1316)

----------------------------------------------------------------------

=== [35] Changelog > 0.15.2 (September 23nd, 2020) ===
FILE: CHANGELOG.md:489-495

## 0.15.2 (September 23nd, 2020)

### Fixed

* Fixed `response.elapsed` property. (Pull #1313)
* Fixed client authentication interaction with `.stream()`. (Pull #1312)

----------------------------------------------------------------------

=== [36] Changelog > 0.15.1 (September 23nd, 2020) ===
FILE: CHANGELOG.md:496-501

## 0.15.1 (September 23nd, 2020)

### Fixed

* ASGITransport now properly applies URL decoding to the `path` component, as-per the ASGI spec. (Pull #1307)

----------------------------------------------------------------------

=== [37] Changelog > 0.15.0 (September 22nd, 2020) ===
FILE: CHANGELOG.md:502-544

## 0.15.0 (September 22nd, 2020)

### Added

* Added support for curio. (Pull https://github.com/encode/httpcore/pull/168)
* Added support for event hooks. (Pull #1246)
* Added support for authentication flows which require either sync or async I/O. (Pull #1217)
* Added support for monitoring download progress with `response.num_bytes_downloaded`. (Pull #1268)
* Added `Request(content=...)` for byte content, instead of overloading `Request(data=...)` (Pull #1266)
* Added support for all URL components as parameter names when using `url.copy_with(...)`. (Pull #1285)
* Neater split between automatically populated headers on `Request` instances, vs default `client.headers`. (Pull #1248)
* Unclosed `AsyncClient` instances will now raise warnings if garbage collected. (Pull #1197)
* Support `Response(content=..., text=..., html=..., json=...)` for creating usable response instances in code. (Pull #1265, #1297)
* Support instantiating requests from the low-level transport API. (Pull #1293)
* Raise errors on invalid URL types. (Pull #1259)

### Changed

* Cleaned up expected behaviour for URL escaping. `url.path` is now URL escaped. (Pull #1285)
* Cleaned up expected behaviour for bytes vs str in URL components. `url.userinfo` and `url.query` are not URL escaped, and so return bytes. (Pull #1285)
* Drop `url.authority` property in favour of `url.netloc`, since "authority" was semantically incorrect. (Pull #1285)
* Drop `url.full_path` property in favour of `url.raw_path`, for better consistency with other parts of the API. (Pull #1285)
* No longer use the `chardet` library for auto-detecting charsets, instead defaulting to a simpler approach when no charset is specified. (#1269)

### Fixed

* Swapped ordering of redirects and authentication flow. (Pull #1267)
* `.netrc` lookups should use host, not host+port. (Pull #1298)

### Removed

* The `URLLib3Transport` class no longer exists. We've published it instead as an example of [a custom transport class](https://gist.github.com/florimondmanca/d56764d78d748eb9f73165da388e546e). (Pull #1182)
* Drop `request.timer` attribute, which was being used internally to set `response.elapsed`. (Pull #1249)
* Drop `response.decoder` attribute, which was being used internally. (Pull #1276)
* `Request.prepare()` is now a private method. (Pull #1284)
* The `Headers.getlist()` method had previously been deprecated in favour of `Headers.get_list()`. It is now fully removed.
* The `QueryParams.getlist()` method had previously been deprecated in favour of `QueryParams.get_list()`. It is now fully removed.
* The `URL.is_ssl` property had previously been deprecated in favour of `URL.scheme == "https"`. It is now fully removed.
* The `httpx.PoolLimits` class had previously been deprecated in favour of `httpx.Limits`. It is now fully removed.
* The `max_keepalive` setting had previously been deprecated in favour of the more explicit `max_keepalive_connections`. It is now fully removed.
* The verbose `httpx.Timeout(5.0, connect_timeout=60.0)` style had previously been deprecated in favour of `httpx.Timeout(5.0, connect=60.0)`. It is now fully removed.
* Support for instantiating a timeout config missing some defaults, such as `httpx.Timeout(connect=60.0)`, had previously been deprecated in favour of enforcing a more explicit style, such as `httpx.Timeout(5.0, connect=60.0)`. This is now strictly enforced.

----------------------------------------------------------------------

=== [38] Changelog > 0.14.3 (September 2nd, 2020) ===
FILE: CHANGELOG.md:545-556

## 0.14.3 (September 2nd, 2020)

### Added

* `http.Response()` may now be instantiated without a `request=...` parameter. Useful for some unit testing cases. (Pull #1238)
* Add `103 Early Hints` and `425 Too Early` status codes. (Pull #1244)

### Fixed

* `DigestAuth` now handles responses that include multiple 'WWW-Authenticate' headers. (Pull #1240)
* Call into transport `__enter__`/`__exit__` or `__aenter__`/`__aexit__` when client is used in a context manager style. (Pull #1218)

----------------------------------------------------------------------

=== [39] Changelog > 0.14.2 (August 24th, 2020) ===
FILE: CHANGELOG.md:557-575

## 0.14.2 (August 24th, 2020)

### Added

* Support `client.get(..., auth=None)` to bypass the default authentication on a clients. (Pull #1115)
* Support `client.auth = ...` property setter. (Pull #1185)
* Support `httpx.get(..., proxies=...)` on top-level request functions. (Pull #1198)
* Display instances with nicer import styles. (Eg. <httpx.ReadTimeout ...>) (Pull #1155)
* Support `cookies=[(key, value)]` list-of-two-tuples style usage. (Pull #1211)

### Fixed

* Ensure that automatically included headers on a request may be modified. (Pull #1205)
* Allow explicit `Content-Length` header on streaming requests. (Pull #1170)
* Handle URL quoted usernames and passwords properly. (Pull #1159)
* Use more consistent default for `HEAD` requests, setting `allow_redirects=True`. (Pull #1183)
* If a transport error occurs while streaming the response, raise an `httpx` exception, not the underlying `httpcore` exception. (Pull #1190)
* Include the underlying `httpcore` traceback, when transport exceptions occur. (Pull #1199)

----------------------------------------------------------------------

=== [40] Changelog > 0.14.1 (August 11th, 2020) ===
FILE: CHANGELOG.md:576-585

## 0.14.1 (August 11th, 2020)

### Added

* The `httpx.URL(...)` class now raises `httpx.InvalidURL` on invalid URLs, rather than exposing the underlying `rfc3986` exception. If a redirect response includes an invalid 'Location' header, then a `RemoteProtocolError` exception is raised, which will be associated with the request that caused it. (Pull #1163)

### Fixed

* Handling multiple `Set-Cookie` headers became broken in the 0.14.0 release, and is now resolved. (Pull #1156)

----------------------------------------------------------------------

=== [41] Changelog > 0.14.0 (August 7th, 2020) ===
FILE: CHANGELOG.md:586-665

## 0.14.0 (August 7th, 2020)

The 0.14 release includes a range of improvements to the public API, intended on preparing for our upcoming 1.0 release.

* Our HTTP/2 support is now fully optional. **You now need to use `pip install httpx[http2]` if you want to include the HTTP/2 dependencies.**
* Our HSTS support has now been removed. Rewriting URLs from `http` to `https` if the host is on the HSTS list can be beneficial in avoiding roundtrips to incorrectly formed URLs, but on balance we've decided to remove this feature, on the principle of least surprise. Most programmatic clients do not include HSTS support, and for now we're opting to remove our support for it.
* Our exception hierarchy has been overhauled. Most users will want to stick with their existing `httpx.HTTPError` usage, but we've got a clearer overall structure now. See https://www.python-httpx.org/exceptions/ for more details.

When upgrading you should be aware of the following public API changes. Note that deprecated usages will currently continue to function, but will issue warnings.

* You should now use `httpx.codes` consistently instead of `httpx.StatusCodes`.
* Usage of `httpx.Timeout()` should now always include an explicit default. Eg. `httpx.Timeout(None, pool=5.0)`.
* When using `httpx.Timeout()`, we now have more concisely named keyword arguments. Eg. `read=5.0`, instead of `read_timeout=5.0`.
* Use `httpx.Limits()` instead of `httpx.PoolLimits()`, and `limits=...` instead of `pool_limits=...`.
* The `httpx.Limits(max_keepalive=...)` argument is now deprecated in favour of a more explicit `httpx.Limits(max_keepalive_connections=...)`.
* Keys used with `Client(proxies={...})` should now be in the style of `{"http://": ...}`, rather than `{"http": ...}`.
* The multidict methods `Headers.getlist()` and `QueryParams.getlist()` are deprecated in favour of more consistent `.get_list()` variants.
* The `URL.is_ssl` property is deprecated in favour of `URL.scheme == "https"`.
* The `URL.join(relative_url=...)` method is now `URL.join(url=...)`. This change does not support warnings for the deprecated usage style.

One notable aspect of the 0.14.0 release is that it tightens up the public API for `httpx`, by ensuring that several internal attributes and methods have now become strictly private.

The following previously had nominally public names on the client, but were all undocumented and intended solely for internal usage. They are all now replaced with underscored names, and should not be relied on or accessed.

These changes should not affect users who have been working from the `httpx` documentation.

* `.merge_url()`, `.merge_headers()`, `.merge_cookies()`, `.merge_queryparams()`
* `.build_auth()`, `.build_redirect_request()`
* `.redirect_method()`, `.redirect_url()`, `.redirect_headers()`, `.redirect_stream()`
* `.send_handling_redirects()`, `.send_handling_auth()`, `.send_single_request()`
* `.init_transport()`, `.init_proxy_transport()`
* `.proxies`, `.transport`, `.netrc`, `.get_proxy_map()`

See pull requests #997, #1065, #1071.

Some areas of API which were already on the deprecation path, and were raising warnings or errors in 0.13.x have now been escalated to being fully removed.

* Drop `ASGIDispatch`, `WSGIDispatch`, which have been replaced by `ASGITransport`, `WSGITransport`.
* Drop `dispatch=...`` on client, which has been replaced by `transport=...``
* Drop `soft_limit`, `hard_limit`, which have been replaced by `max_keepalive` and `max_connections`.
* Drop `Response.stream` and` `Response.raw`, which have been replaced by ``.aiter_bytes` and `.aiter_raw`.
* Drop `proxies=<transport instance>` in favor of `proxies=httpx.Proxy(...)`.

See pull requests #1057, #1058.

### Added

* Added dedicated exception class `httpx.HTTPStatusError` for `.raise_for_status()` exceptions. (Pull #1072)
* Added `httpx.create_ssl_context()` helper function. (Pull #996)
* Support for proxy exclusions like `proxies={"https://www.example.com": None}`. (Pull #1099)
* Support `QueryParams(None)` and `client.params = None`. (Pull #1060)

### Changed

* Use `httpx.codes` consistently in favour of `httpx.StatusCodes` which is placed into deprecation. (Pull #1088)
* Usage of `httpx.Timeout()` should now always include an explicit default. Eg. `httpx.Timeout(None, pool=5.0)`. (Pull #1085)
* Switch to more concise `httpx.Timeout()` keyword arguments. Eg. `read=5.0`, instead of `read_timeout=5.0`. (Pull #1111)
* Use `httpx.Limits()` instead of `httpx.PoolLimits()`, and `limits=...` instead of `pool_limits=...`. (Pull #1113)
* Keys used with `Client(proxies={...})` should now be in the style of `{"http://": ...}`, rather than `{"http": ...}`. (Pull #1127)
* The multidict methods `Headers.getlist` and `QueryParams.getlist` are deprecated in favour of more consistent `.get_list()` variants. (Pull #1089)
* `URL.port` becomes `Optional[int]`. Now only returns a port if one is explicitly included in the URL string. (Pull #1080)
* The `URL(..., allow_relative=[bool])` parameter no longer exists. All URL instances may be relative. (Pull #1073)
* Drop unnecessary `url.full_path = ...` property setter. (Pull #1069)
* The `URL.join(relative_url=...)` method is now `URL.join(url=...)`. (Pull #1129)
* The `URL.is_ssl` property is deprecated in favour of `URL.scheme == "https"`. (Pull #1128)

### Fixed

* Add missing `Response.next()` method. (Pull #1055)
* Ensure all exception classes are exposed as public API. (Pull #1045)
* Support multiple items with an identical field name in multipart encodings. (Pull #777)
* Skip HSTS preloading on single-label domains. (Pull #1074)
* Fixes for `Response.iter_lines()`. (Pull #1033, #1075)
* Ignore permission errors when accessing `.netrc` files. (Pull #1104)
* Allow bare hostnames in `HTTP_PROXY` etc... environment variables. (Pull #1120)
* Settings `app=...` or `transport=...` bypasses any environment based proxy defaults. (Pull #1122)
* Fix handling of `.base_url` when a path component is included in the base URL. (Pull #1130)

---

----------------------------------------------------------------------

=== [42] Changelog > 0.13.3 (May 29th, 2020) ===
FILE: CHANGELOG.md:666-672

## 0.13.3 (May 29th, 2020)

### Fixed

* Include missing keepalive expiry configuration. (Pull #1005)
* Improved error message when URL redirect has a custom scheme. (Pull #1002)

----------------------------------------------------------------------

=== [43] Changelog > 0.13.2 (May 27th, 2020) ===
FILE: CHANGELOG.md:673-680

## 0.13.2 (May 27th, 2020)

### Fixed

* Include explicit "Content-Length: 0" on POST, PUT, PATCH if no request body is used. (Pull #995)
* Add `http2` option to `httpx.Client`. (Pull #982)
* Tighten up API typing in places. (Pull #992, #999)

----------------------------------------------------------------------

=== [44] Changelog > 0.13.1 (May 22nd, 2020) ===
FILE: CHANGELOG.md:681-687

## 0.13.1 (May 22nd, 2020)

### Fixed

* Fix pool options deprecation warning. (Pull #980)
* Include `httpx.URLLib3ProxyTransport` in top-level API. (Pull #979)

----------------------------------------------------------------------

=== [45] Changelog > 0.13.0 (May 22nd, 2020) ===
FILE: CHANGELOG.md:688-726

## 0.13.0 (May 22nd, 2020)

This release switches to `httpcore` for all the internal networking, which means:

* We're using the same codebase for both our sync and async clients.
* HTTP/2 support is now available with the sync client.
* We no longer have a `urllib3` dependency for our sync client, although there is still an *optional* `URLLib3Transport` class.

It also means we've had to remove our UDS support, since maintaining that would have meant having to push back our work towards a 1.0 release, which isn't a trade-off we wanted to make.

We also now have [a public "Transport API"](https://www.python-httpx.org/advanced/transports/#custom-transports), which you can use to implement custom transport implementations against. This formalises and replaces our previously private "Dispatch API".

### Changed

* Use `httpcore` for underlying HTTP transport. Drop `urllib3` requirement. (Pull #804, #967)
* Rename pool limit options from `soft_limit`/`hard_limit` to `max_keepalive`/`max_connections`. (Pull #968)
* The previous private "Dispatch API" has now been promoted to a public "Transport API". When customizing the transport use `transport=...`. The `ASGIDispatch` and `WSGIDispatch` class naming is deprecated in favour of `ASGITransport` and `WSGITransport`. (Pull #963)

### Added

* Added `URLLib3Transport` class for optional `urllib3` transport support. (Pull #804, #963)
* Streaming multipart uploads. (Pull #857)
* Logging via HTTPCORE_LOG_LEVEL and HTTPX_LOG_LEVEL environment variables
and TRACE level logging. (Pull encode/httpcore#79)

### Fixed

* Performance improvement in brotli decoder. (Pull #906)
* Proper warning level of deprecation notice in `Response.stream` and `Response.raw`. (Pull #908)
* Fix support for generator based WSGI apps. (Pull #887)
* Reuse of connections on HTTP/2 in close concurrency situations. (Pull encode/httpcore#81)
* Honor HTTP/2 max concurrent streams settings (Pull encode/httpcore#89, encode/httpcore#90)
* Fix bytes support in multipart uploads. (Pull #974)
* Improve typing support for `files=...`. (Pull #976)

### Removed

* Dropped support for `Client(uds=...)` (Pull #804)

----------------------------------------------------------------------

=== [46] Changelog > 0.13.0.dev2 (May 12th, 2020) ===
FILE: CHANGELOG.md:727-740

## 0.13.0.dev2 (May 12th, 2020)

The 0.13.0.dev2 is a *pre-release* version. To install it, use `pip install httpx --pre`.

### Added

* Logging via HTTPCORE_LOG_LEVEL and HTTPX_LOG_LEVEL environment variables
and TRACE level logging. (HTTPCore Pull #79)

### Fixed

* Reuse of connections on HTTP/2 in close concurrency situations. (HTTPCore Pull #81)
* When using an `app=<ASGI app>` observe neater disconnect behaviour instead of sending empty body messages. (Pull #919)

----------------------------------------------------------------------

=== [47] Changelog > 0.13.0.dev1 (May 6th, 2020) ===
FILE: CHANGELOG.md:741-750

## 0.13.0.dev1 (May 6th, 2020)

The 0.13.0.dev1 is a *pre-release* version. To install it, use `pip install httpx --pre`.

### Fixed

* Passing `http2` flag to proxy dispatchers. (Pull #934)
* Use [`httpcore` v0.8.3](https://github.com/encode/httpcore/releases/tag/0.8.3)
which addresses problems in handling of headers when using proxies.

----------------------------------------------------------------------

=== [48] Changelog > 0.13.0.dev0 (April 30th, 2020) ===
FILE: CHANGELOG.md:751-783

## 0.13.0.dev0 (April 30th, 2020)

The 0.13.0.dev0 is a *pre-release* version. To install it, use `pip install httpx --pre`.

This release switches to `httpcore` for all the internal networking, which means:

* We're using the same codebase for both our sync and async clients.
* HTTP/2 support is now available with the sync client.
* We no longer have a `urllib3` dependency for our sync client, although there is still an *optional* `URLLib3Dispatcher` class.

It also means we've had to remove our UDS support, since maintaining that would have meant having to push back our work towards a 1.0 release, which isn't a trade-off we wanted to make.

### Changed

* Use `httpcore` for underlying HTTP transport. Drop `urllib3` requirement. (Pull #804)

### Added

* Added `URLLib3Dispatcher` class for optional `urllib3` transport support. (Pull #804)
* Streaming multipart uploads. (Pull #857)

### Fixed

* Performance improvement in brotli decoder. (Pull #906)
* Proper warning level of deprecation notice in `Response.stream` and `Response.raw`. (Pull #908)
* Fix support for generator based WSGI apps. (Pull #887)

### Removed

* Dropped support for `Client(uds=...)` (Pull #804)

---

----------------------------------------------------------------------

=== [49] Changelog > 0.12.1 (March 19th, 2020) ===
FILE: CHANGELOG.md:784-789

## 0.12.1 (March 19th, 2020)

### Fixed

* Resolved packaging issue, where additional files were being included.

----------------------------------------------------------------------

=== [50] Changelog > 0.12.0 (March 9th, 2020) ===
FILE: CHANGELOG.md:790-818

## 0.12.0 (March 9th, 2020)

The 0.12 release tightens up the API expectations for `httpx` by switching to private module names to enforce better clarity around public API.

All imports of `httpx` should import from the top-level package only, such as `from httpx import Request`, rather than importing from privately namespaced modules such as `from httpx._models import Request`.

### Added

* Support making response body available to auth classes with `.requires_response_body`. (Pull #803)
* Export `NetworkError` exception. (Pull #814)
* Add support for `NO_PROXY` environment variable. (Pull #835)

### Changed

* Switched to private module names. (Pull #785)
* Drop redirect looping detection and the `RedirectLoop` exception, instead using `TooManyRedirects`. (Pull #819)
* Drop `backend=...` parameter on `AsyncClient`, in favour of always autodetecting `trio`/`asyncio`. (Pull #791)

### Fixed

* Support basic auth credentials in proxy URLs. (Pull #780)
* Fix `httpx.Proxy(url, mode="FORWARD_ONLY")` configuration. (Pull #788)
* Fallback to setting headers as UTF-8 if no encoding is specified. (Pull #820)
* Close proxy dispatches classes on client close. (Pull #826)
* Support custom `cert` parameters even if `verify=False`. (Pull #796)
* Don't support invalid dict-of-dicts form data in `data=...`. (Pull #811)

---

----------------------------------------------------------------------

=== [51] Changelog > 0.11.1 (January 17th, 2020) ===
FILE: CHANGELOG.md:819-827

## 0.11.1 (January 17th, 2020)

### Fixed

* Fixed usage of `proxies=...` on `Client()`. (Pull #763)
* Support both `zlib` and `deflate` style encodings on `Content-Encoding: deflate`. (Pull #758)
* Fix for streaming a redirect response body with `allow_redirects=False`. (Pull #766)
* Handle redirect with malformed Location headers missing host. (Pull #774)

----------------------------------------------------------------------

=== [52] Changelog > 0.11.0 (January 9th, 2020) ===
FILE: CHANGELOG.md:828-858

## 0.11.0 (January 9th, 2020)

The 0.11 release reintroduces our sync support, so that `httpx` now supports both a standard thread-concurrency API, and an async API.

Existing async `httpx` users that are upgrading to 0.11 should ensure that:

* Async codebases should always use a client instance to make requests, instead of the top-level API.
* The async client is named as `httpx.AsyncClient()`, instead of `httpx.Client()`.
* When instantiating proxy configurations use the `httpx.Proxy()` class, instead of the previous `httpx.HTTPProxy()`. This new configuration class works for configuring both sync and async clients.

We believe the API is now pretty much stable, and are aiming for a 1.0 release sometime on or before April 2020.

### Changed

- Top level API such as `httpx.get(url, ...)`, `httpx.post(url, ...)`, `httpx.request(method, url, ...)` becomes synchronous.
- Added `httpx.Client()` for synchronous clients, with `httpx.AsyncClient` being used for async clients.
- Switched to `proxies=httpx.Proxy(...)` for proxy configuration.
- Network connection errors are wrapped in `httpx.NetworkError`, rather than exposing lower-level exception types directly.

### Removed

- The `request.url.origin` property and `httpx.Origin` class are no longer available.
- The per-request `cert`, `verify`, and `trust_env` arguments are escalated from raising errors if used, to no longer being available. These arguments should be used on a per-client instance instead, or in the top-level API.
- The `stream` argument has escalated from raising an error when used, to no longer being available. Use the `client.stream(...)` or `httpx.stream()` streaming API instead.

### Fixed

- Redirect loop detection matches against `(method, url)` rather than `url`. (Pull #734)

---

----------------------------------------------------------------------

=== [53] Changelog > 0.10.1 (December 31st, 2019) ===
FILE: CHANGELOG.md:859-865

## 0.10.1 (December 31st, 2019)

### Fixed

- Fix issue with concurrent connection acquisition. (Pull #700)
- Fix write error on closing HTTP/2 connections. (Pull #699)

----------------------------------------------------------------------

=== [54] Changelog > 0.10.0 (December 29th, 2019) ===
FILE: CHANGELOG.md:866-893

## 0.10.0 (December 29th, 2019)

The 0.10.0 release makes some changes that will allow us to support both sync and async interfaces.

In particular with streaming responses the `response.read()` method becomes `response.aread()`, and the `response.close()` method becomes `response.aclose()`.

If following redirects explicitly the `response.next()` method becomes `response.anext()`.

### Fixed

- End HTTP/2 streams immediately on no-body requests, rather than sending an empty body message. (Pull #682)
- Improve typing for `Response.request`: switch from `Optional[Request]` to `Request`. (Pull #666)
- `Response.elapsed` now reflects the entire download time. (Pull #687, #692)

### Changed

- Added `AsyncClient` as a synonym for `Client`. (Pull #680)
- Switch to `response.aread()` for conditionally reading streaming responses. (Pull #674)
- Switch to `response.aclose()` and `client.aclose()` for explicit closing. (Pull #674, #675)
- Switch to `response.anext()` for resolving the next redirect response. (Pull #676)

### Removed

- When using a client instance, the per-request usage of `verify`, `cert`, and `trust_env` have now escalated from raising a warning to raising an error. You should set these arguments on the client instead. (Pull #617)
- Removed the undocumented `request.read()`, since end users should not require it.

---

----------------------------------------------------------------------

=== [55] Changelog > 0.9.5 (December 20th, 2019) ===
FILE: CHANGELOG.md:894-903

## 0.9.5 (December 20th, 2019)

### Fixed

- Fix Host header and HSTS rewrites when an explicit `:80` port is included in URL. (Pull #649)
- Query Params on the URL string are merged with any `params=...` argument. (Pull #653)
- More robust behavior when closing connections. (Pull #640)
- More robust behavior when handling HTTP/2 headers with trailing whitespace. (Pull #637)
- Allow any explicit `Content-Type` header to take precedence over the encoding default. (Pull #633)

----------------------------------------------------------------------

=== [56] Changelog > 0.9.4 (December 12th, 2019) ===
FILE: CHANGELOG.md:904-910

## 0.9.4 (December 12th, 2019)

### Fixed

- Added expiry to Keep-Alive connections, resolving issues with acquiring connections. (Pull #627)
- Increased flow control windows on HTTP/2, resolving download speed issues. (Pull #629)

----------------------------------------------------------------------

=== [57] Changelog > 0.9.3 (December 7th, 2019) ===
FILE: CHANGELOG.md:911-916

## 0.9.3 (December 7th, 2019)

### Fixed

- Fixed HTTP/2 with autodetection backend. (Pull #614)

----------------------------------------------------------------------

=== [58] Changelog > 0.9.2 (December 7th, 2019) ===
FILE: CHANGELOG.md:917-920

## 0.9.2 (December 7th, 2019)

* Released due to packaging build artifact.

----------------------------------------------------------------------

=== [59] Changelog > 0.9.1 (December 6th, 2019) ===
FILE: CHANGELOG.md:921-924

## 0.9.1 (December 6th, 2019)

* Released due to packaging build artifact.

----------------------------------------------------------------------

=== [60] Changelog > 0.9.0 (December 6th, 2019) ===
FILE: CHANGELOG.md:925-966

## 0.9.0 (December 6th, 2019)

The 0.9 releases brings some major new features, including:

* A new streaming API.
* Autodetection of either asyncio or trio.
* Nicer timeout configuration.
* HTTP/2 support off by default, but can be enabled.

We've also removed all private types from the top-level package export.

In order to ensure you are only ever working with public API you should make
sure to only import the top-level package eg. `import httpx`, rather than
importing modules within the package.

### Added

- Added concurrency backend autodetection. (Pull #585)
- Added `Client(backend='trio')` and `Client(backend='asyncio')` API. (Pull #585)
- Added `response.stream_lines()` API. (Pull #575)
- Added `response.is_error` API. (Pull #574)
- Added support for `timeout=Timeout(5.0, connect_timeout=60.0)` styles. (Pull #593)

### Fixed

- Requests or Clients with `timeout=None` now correctly always disable timeouts. (Pull #592)
- Request 'Authorization' headers now have priority over `.netrc` authentication info. (Commit 095b691)
- Files without a filename no longer set a Content-Type in multipart data. (Commit ed94950)

### Changed

- Added `httpx.stream()` API. Using `stream=True` now results in a warning. (Pull #600, #610)
- HTTP/2 support is switched to "off by default", but can be enabled explicitly. (Pull #584)
- Switched to `Client(http2=True)` API from `Client(http_versions=["HTTP/1.1", "HTTP/2"])`. (Pull #586)
- Removed all private types from the top-level package export. (Pull #608)
- The SSL configuration settings of `verify`, `cert`, and `trust_env` now raise warnings if used per-request when using a Client instance. They should always be set on the Client instance itself. (Pull #597)
- Use plain strings "TUNNEL_ONLY" or "FORWARD_ONLY" on the HTTPProxy `proxy_mode` argument. The `HTTPProxyMode` enum still exists, but its usage will raise warnings. (#610)
- Pool timeouts are now on the timeout configuration, not the pool limits configuration. (Pull #563)
- The timeout configuration is now named `httpx.Timeout(...)`, not `httpx.TimeoutConfig(...)`. The old version currently remains as a synonym for backwards compatibility.  (Pull #591)

---

----------------------------------------------------------------------

=== [61] Changelog > 0.8.0 (November 27, 2019) ===
FILE: CHANGELOG.md:967-974

## 0.8.0 (November 27, 2019)

### Removed

- The synchronous API has been removed, in order to allow us to fundamentally change how we approach supporting both sync and async variants. (See #588 for more details.)

---

----------------------------------------------------------------------

=== [62] Changelog > 0.7.8 (November 17, 2019) ===
FILE: CHANGELOG.md:975-980

## 0.7.8 (November 17, 2019)

### Added

- Add support for proxy tunnels for Python 3.6 + asyncio. (Pull #521)

----------------------------------------------------------------------

=== [63] Changelog > 0.7.7 (November 15, 2019) ===
FILE: CHANGELOG.md:981-991

## 0.7.7 (November 15, 2019)

### Fixed

- Resolve an issue with cookies behavior on redirect requests. (Pull #529)

### Added

- Add request/response DEBUG logs. (Pull #502)
- Use TRACE log level for low level info. (Pull #500)

----------------------------------------------------------------------

=== [64] Changelog > 0.7.6 (November 2, 2019) ===
FILE: CHANGELOG.md:992-1004

## 0.7.6 (November 2, 2019)

### Removed

- Drop `proxies` parameter from the high-level API. (Pull #485)

### Fixed

- Tweak multipart files: omit null filenames, add support for `str` file contents. (Pull #482)
- Cache NETRC authentication per-client. (Pull #400)
- Rely on `getproxies` for all proxy environment variables. (Pull #470)
- Wait for the `asyncio` stream to close when closing a connection. (Pull #494)

----------------------------------------------------------------------

=== [65] Changelog > 0.7.5 (October 10, 2019) ===
FILE: CHANGELOG.md:1005-1024

## 0.7.5 (October 10, 2019)

### Added

- Allow lists of values to be passed to `params`. (Pull #386)
- `ASGIDispatch`, `WSGIDispatch` are now available in the `httpx.dispatch` namespace. (Pull #407)
- `HTTPError` is now available in the `httpx` namespace.  (Pull #421)
- Add support for `start_tls()` to the Trio concurrency backend. (Pull #467)

### Fixed

- Username and password are no longer included in the `Host` header when basic authentication
  credentials are supplied via the URL. (Pull #417)

### Removed

- The `.delete()` function no longer has `json`, `data`, or `files` parameters
  to match the expected semantics of the `DELETE` method. (Pull #408)
- Removed the `trio` extra. Trio support is detected automatically. (Pull #390)

----------------------------------------------------------------------

=== [66] Changelog > 0.7.4 (September 25, 2019) ===
FILE: CHANGELOG.md:1025-1039

## 0.7.4 (September 25, 2019)

### Added

- Add Trio concurrency backend. (Pull #276)
- Add `params` parameter to `Client` for setting default query parameters. (Pull #372)
- Add support for `SSL_CERT_FILE` and `SSL_CERT_DIR` environment variables. (Pull #307)
- Add debug logging to calls into ASGI apps. (Pull #371)
- Add debug logging to SSL configuration. (Pull #378)

### Fixed

- Fix a bug when using `Client` without timeouts in Python 3.6. (Pull #383)
- Propagate `Client` configuration to HTTP proxies. (Pull #377)

----------------------------------------------------------------------

=== [67] Changelog > 0.7.3 (September 20, 2019) ===
FILE: CHANGELOG.md:1040-1062

## 0.7.3 (September 20, 2019)

### Added

- HTTP Proxy support. (Pulls #259, #353)
- Add Digest authentication. (Pull #332)
- Add `.build_request()` method to `Client` and `AsyncClient`. (Pull #319)
- Add `.elapsed` property on responses. (Pull #351)
- Add support for `SSLKEYLOGFILE` in Python 3.8b4+. (Pull #301)

### Removed

- Drop NPN support for HTTP version negotiation. (Pull #314)

### Fixed

- Fix distribution of type annotations for mypy (Pull #361).
- Set `Host` header when redirecting cross-origin. (Pull #321)
- Drop `Content-Length` headers on `GET` redirects. (Pull #310)
- Raise `KeyError` if header isn't found in `Headers`. (Pull #324)
- Raise `NotRedirectResponse` in `response.next()` if there is no redirection to perform. (Pull #297)
- Fix bug in calculating the HTTP/2 maximum frame size. (Pull #153)

----------------------------------------------------------------------

=== [68] Changelog > 0.7.2 (August 28, 2019) ===
FILE: CHANGELOG.md:1063-1073

## 0.7.2 (August 28, 2019)

- Enforce using `httpx.AsyncioBackend` for the synchronous client. (Pull #232)
- `httpx.ConnectionPool` will properly release a dropped connection. (Pull #230)
- Remove the `raise_app_exceptions` argument from `Client`. (Pull #238)
- `DecodeError` will no longer be raised for an empty body encoded with Brotli. (Pull #237)
- Added `http_versions` parameter to `Client`. (Pull #250)
- Only use HTTP/1.1 on short-lived connections like `httpx.get()`. (Pull #284)
- Convert `Client.cookies` and `Client.headers` when set as a property. (Pull #274)
- Setting `HTTPX_DEBUG=1` enables debug logging on all requests. (Pull #277)

----------------------------------------------------------------------

=== [69] Changelog > 0.7.1 (August 18, 2019) ===
FILE: CHANGELOG.md:1074-1077

## 0.7.1 (August 18, 2019)

- Include files with source distribution to be installable. (Pull #233)

----------------------------------------------------------------------

=== [70] Changelog > 0.7.0 (August 17, 2019) ===
FILE: CHANGELOG.md:1078-1098

## 0.7.0 (August 17, 2019)

- Add the `trust_env` property to `BaseClient`. (Pull #187)
- Add the `links` property to `BaseResponse`. (Pull #211)
- Accept `ssl.SSLContext` instances into `SSLConfig(verify=...)`. (Pull #215)
- Add `Response.stream_text()` with incremental encoding detection. (Pull #183)
- Properly updated the `Host` header when a redirect changes the origin. (Pull #199)
- Ignore invalid `Content-Encoding` headers. (Pull #196)
- Use `~/.netrc` and `~/_netrc` files by default when `trust_env=True`. (Pull #189)
- Create exception base class `HTTPError` with `request` and `response` properties. (Pull #162)
- Add HSTS preload list checking within `BaseClient` to upgrade HTTP URLs to HTTPS. (Pull #184)
- Switch IDNA encoding from IDNA 2003 to IDNA 2008. (Pull #161)
- Expose base classes for alternate concurrency backends. (Pull #178)
- Improve Multipart parameter encoding. (Pull #167)
- Add the `headers` property to `BaseClient`. (Pull #159)
- Add support for Google's `brotli` library. (Pull #156)
- Remove deprecated TLS versions (TLSv1 and TLSv1.1) from default `SSLConfig`. (Pull #155)
- Fix `URL.join(...)` to work similarly to RFC 3986 URL joining. (Pull #144)

---

----------------------------------------------------------------------

=== [71] Changelog > 0.6.8 (July 25, 2019) ===
FILE: CHANGELOG.md:1099-1109

## 0.6.8 (July 25, 2019)

- Check for disconnections when searching for an available
  connection in `ConnectionPool.keepalive_connections` (Pull #145)
- Allow string comparison for `URL` objects (Pull #139)
- Add HTTP status codes 418 and 451 (Pull #135)
- Add support for client certificate passwords (Pull #118)
- Enable post-handshake client cert authentication for TLSv1.3 (Pull #118)
- Disable using `commonName` for hostname checking for OpenSSL 1.1.0+ (Pull #118)
- Detect encoding for `Response.json()` (Pull #116)

----------------------------------------------------------------------

=== [72] Changelog > 0.6.7 (July 8, 2019) ===
FILE: CHANGELOG.md:1110-1113

## 0.6.7 (July 8, 2019)

- Check for connection aliveness on re-acquisition (Pull #111)

----------------------------------------------------------------------

=== [73] Changelog > 0.6.6 (July 3, 2019) ===
FILE: CHANGELOG.md:1114-1118

## 0.6.6 (July 3, 2019)

- Improve `USER_AGENT` (Pull #110)
- Add `Connection: keep-alive` by default to HTTP/1.1 connections. (Pull #110)

----------------------------------------------------------------------

=== [74] Changelog > 0.6.5 (June 27, 2019) ===
FILE: CHANGELOG.md:1119-1123

## 0.6.5 (June 27, 2019)

- Include `Host` header by default. (Pull #109)
- Improve HTTP protocol detection. (Pull #107)

----------------------------------------------------------------------

=== [75] Changelog > 0.6.4 (June 25, 2019) ===
FILE: CHANGELOG.md:1124-1127

## 0.6.4 (June 25, 2019)

- Implement read and write timeouts (Pull #104)

----------------------------------------------------------------------

=== [76] Changelog > 0.6.3 (June 24, 2019) ===
FILE: CHANGELOG.md:1128-1131

## 0.6.3 (June 24, 2019)

- Handle early connection closes (Pull #103)

----------------------------------------------------------------------

=== [77] Changelog > 0.6.2 (June 23, 2019) ===
FILE: CHANGELOG.md:1132-1135

## 0.6.2 (June 23, 2019)

- Use urllib3's `DEFAULT_CIPHERS` for the `SSLConfig` object. (Pull #100)

----------------------------------------------------------------------

=== [78] Changelog > 0.6.1 (June 21, 2019) ===
FILE: CHANGELOG.md:1136-1139

## 0.6.1 (June 21, 2019)

- Add support for setting a `base_url` on the `Client`.

----------------------------------------------------------------------

=== [79] Changelog > 0.6.0 (June 21, 2019) ===
FILE: CHANGELOG.md:1140-1142

## 0.6.0 (June 21, 2019)

- Honor `local_flow_control_window` for HTTP/2 connections (Pull #98)

----------------------------------------------------------------------

=== [80] LICENSE.md ===
FILE: LICENSE.md:1-12

Copyright © 2019, [Encode OSS Ltd](https://www.encode.io/).
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

----------------------------------------------------------------------

=== [81] README.md ===
FILE: README.md:1-58

<p align="center">
  <a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/butterfly.png" alt='HTTPX'></a>
</p>

<p align="center"><strong>HTTPX</strong> <em>- A next-generation HTTP client for Python.</em></p>

<p align="center">
<a href="https://github.com/encode/httpx/actions">
    <img src="https://github.com/encode/httpx/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/httpx/">
    <img src="https://badge.fury.io/py/httpx.svg" alt="Package version">
</a>
</p>

HTTPX is a fully featured HTTP client library for Python 3. It includes **an integrated command line client**, has support for both **HTTP/1.1 and HTTP/2**, and provides both **sync and async APIs**.

---

Install HTTPX using pip:

```shell
$ pip install httpx
```

Now, let's get started:

```pycon
>>> import httpx
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

Or, using the command-line client.

```shell
$ pip install 'httpx[cli]'  # The command line client is an optional dependency.
```

Which now allows us to use HTTPX directly from the command-line...

<p align="center">
  <img width="700" src="docs/img/httpx-help.png" alt='httpx --help'>
</p>

Sending a request...

<p align="center">
  <img width="700" src="docs/img/httpx-request.png" alt='httpx http://httpbin.org/json'>
</p>

----------------------------------------------------------------------

=== [82] Features ===
FILE: README.md:59-89

## Features

HTTPX builds on the well-established usability of `requests`, and gives you:

* A broadly [requests-compatible API](https://www.python-httpx.org/compatibility/).
* An integrated command-line client.
* HTTP/1.1 [and HTTP/2 support](https://www.python-httpx.org/http2/).
* Standard synchronous interface, but with [async support if you need it](https://www.python-httpx.org/async/).
* Ability to make requests directly to [WSGI applications](https://www.python-httpx.org/advanced/transports/#wsgi-transport) or [ASGI applications](https://www.python-httpx.org/advanced/transports/#asgi-transport).
* Strict timeouts everywhere.
* Fully type annotated.
* 100% test coverage.

Plus all the standard features of `requests`...

* International Domains and URLs
* Keep-Alive & Connection Pooling
* Sessions with Cookie Persistence
* Browser-style SSL Verification
* Basic/Digest Authentication
* Elegant Key/Value Cookies
* Automatic Decompression
* Automatic Content Decoding
* Unicode Response Bodies
* Multipart File Uploads
* HTTP(S) Proxy Support
* Connection Timeouts
* Streaming Downloads
* .netrc Support
* Chunked Requests

----------------------------------------------------------------------

=== [83] Installation ===
FILE: README.md:90-105

## Installation

Install with pip:

```shell
$ pip install httpx
```

Or, to include the optional HTTP/2 support, use:

```shell
$ pip install httpx[http2]
```

HTTPX requires Python 3.9+.

----------------------------------------------------------------------

=== [84] Documentation ===
FILE: README.md:106-117

## Documentation

Project documentation is available at [https://www.python-httpx.org/](https://www.python-httpx.org/).

For a run-through of all the basics, head over to the [QuickStart](https://www.python-httpx.org/quickstart/).

For more advanced topics, see the [Advanced Usage](https://www.python-httpx.org/advanced/) section, the [async support](https://www.python-httpx.org/async/) section, or the [HTTP/2](https://www.python-httpx.org/http2/) section.

The [Developer Interface](https://www.python-httpx.org/api/) provides a comprehensive API reference.

To find out about tools that integrate with HTTPX, see [Third Party Packages](https://www.python-httpx.org/third_party_packages/).

----------------------------------------------------------------------

=== [85] Contribute ===
FILE: README.md:118-121

## Contribute

If you want to contribute with HTTPX check out the [Contributing Guide](https://www.python-httpx.org/contributing/) to learn how to start.

----------------------------------------------------------------------

=== [86] Dependencies ===
FILE: README.md:122-147

## Dependencies

The HTTPX project relies on these excellent libraries:

* `httpcore` - The underlying transport implementation for `httpx`.
  * `h11` - HTTP/1.1 support.
* `certifi` - SSL certificates.
* `idna` - Internationalized domain name support.
* `sniffio` - Async library autodetection.

As well as these optional installs:

* `h2` - HTTP/2 support. *(Optional, with `httpx[http2]`)*
* `socksio` - SOCKS proxy support. *(Optional, with `httpx[socks]`)*
* `rich` - Rich terminal support. *(Optional, with `httpx[cli]`)*
* `click` - Command line client support. *(Optional, with `httpx[cli]`)*
* `brotli` or `brotlicffi` - Decoding for "brotli" compressed responses. *(Optional, with `httpx[brotli]`)*
* `zstandard` - Decoding for "zstd" compressed responses. *(Optional, with `httpx[zstd]`)*

A huge amount of credit is due to `requests` for the API layout that
much of this work follows, as well as to `urllib3` for plenty of design
inspiration around the lower-level networking details.

---

<p align="center"><i>HTTPX is <a href="https://github.com/encode/httpx/blob/master/LICENSE.md">BSD licensed</a> code.<br/>Designed & crafted with care.</i><br/>&mdash; 🦋 &mdash;</p>

----------------------------------------------------------------------

=== [87] docs\api.md ===
FILE: docs\api.md:1-2

# Developer Interface

----------------------------------------------------------------------

=== [88] Developer Interface > Helper Functions ===
FILE: docs\api.md:3-37

## Helper Functions

!!! note
    Only use these functions if you're testing HTTPX in a console
    or making a small number of requests. Using a `Client` will
    enable HTTP/2 and connection pooling for more efficient and
    long-lived connections.

::: httpx.request
    :docstring:

::: httpx.get
    :docstring:

::: httpx.options
    :docstring:

::: httpx.head
    :docstring:

::: httpx.post
    :docstring:

::: httpx.put
    :docstring:

::: httpx.patch
    :docstring:

::: httpx.delete
    :docstring:

::: httpx.stream
    :docstring:

----------------------------------------------------------------------

=== [89] Developer Interface > `Client` ===
FILE: docs\api.md:38-43

## `Client`

::: httpx.Client
    :docstring:
    :members: headers cookies params auth request get head options post put patch delete stream build_request send close

----------------------------------------------------------------------

=== [90] Developer Interface > `AsyncClient` ===
FILE: docs\api.md:44-50

## `AsyncClient`

::: httpx.AsyncClient
    :docstring:
    :members: headers cookies params auth request get head options post put patch delete stream build_request send aclose

----------------------------------------------------------------------

=== [91] Developer Interface > `Response` ===
FILE: docs\api.md:51-89

## `Response`

*An HTTP response.*

* `def __init__(...)`
* `.status_code` - **int**
* `.reason_phrase` - **str**
* `.http_version` - `"HTTP/2"` or `"HTTP/1.1"`
* `.url` - **URL**
* `.headers` - **Headers**
* `.content` - **bytes**
* `.text` - **str**
* `.encoding` - **str**
* `.is_redirect` - **bool**
* `.request` - **Request**
* `.next_request` - **Optional[Request]**
* `.cookies` - **Cookies**
* `.history` - **List[Response]**
* `.elapsed` - **[timedelta](https://docs.python.org/3/library/datetime.html)**
  * The amount of time elapsed between sending the request and calling `close()` on the corresponding response received for that request.
  [total_seconds()](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds) to correctly get
  the total elapsed seconds.
* `def .raise_for_status()` - **Response**
* `def .json()` - **Any**
* `def .read()` - **bytes**
* `def .iter_raw([chunk_size])` - **bytes iterator**
* `def .iter_bytes([chunk_size])` - **bytes iterator**
* `def .iter_text([chunk_size])` - **text iterator**
* `def .iter_lines()` - **text iterator**
* `def .close()` - **None**
* `def .next()` - **Response**
* `def .aread()` - **bytes**
* `def .aiter_raw([chunk_size])` - **async bytes iterator**
* `def .aiter_bytes([chunk_size])` - **async bytes iterator**
* `def .aiter_text([chunk_size])` - **async text iterator**
* `def .aiter_lines()` - **async text iterator**
* `def .aclose()` - **None**
* `def .anext()` - **Response**

----------------------------------------------------------------------

=== [92] Developer Interface > `Request` ===
FILE: docs\api.md:90-106

## `Request`

*An HTTP request. Can be constructed explicitly for more control over exactly
what gets sent over the wire.*

```pycon
>>> request = httpx.Request("GET", "https://example.org", headers={'host': 'example.org'})
>>> response = client.send(request)
```

* `def __init__(method, url, [params], [headers], [cookies], [content], [data], [files], [json], [stream])`
* `.method` - **str**
* `.url` - **URL**
* `.content` - **byte**, **byte iterator**, or **byte async iterator**
* `.headers` - **Headers**
* `.cookies` - **Cookies**

----------------------------------------------------------------------

=== [93] Developer Interface > `URL` ===
FILE: docs\api.md:107-130

## `URL`

*A normalized, IDNA supporting URL.*

```pycon
>>> url = URL("https://example.org/")
>>> url.host
'example.org'
```

* `def __init__(url, **kwargs)`
* `.scheme` - **str**
* `.authority` - **str**
* `.host` - **str**
* `.port` - **int**
* `.path` - **str**
* `.query` - **str**
* `.raw_path` - **str**
* `.fragment` - **str**
* `.is_ssl` - **bool**
* `.is_absolute_url` - **bool**
* `.is_relative_url` - **bool**
* `def .copy_with([scheme], [authority], [path], [query], [fragment])` - **URL**

----------------------------------------------------------------------

=== [94] Developer Interface > `Headers` ===
FILE: docs\api.md:131-143

## `Headers`

*A case-insensitive multi-dict.*

```pycon
>>> headers = Headers({'Content-Type': 'application/json'})
>>> headers['content-type']
'application/json'
```

* `def __init__(self, headers, encoding=None)`
* `def copy()` - **Headers**

----------------------------------------------------------------------

=== [95] Developer Interface > `Cookies` ===
FILE: docs\api.md:144-162

## `Cookies`

*A dict-like cookie store.*

```pycon
>>> cookies = Cookies()
>>> cookies.set("name", "value", domain="example.org")
```

* `def __init__(cookies: [dict, Cookies, CookieJar])`
* `.jar` - **CookieJar**
* `def extract_cookies(response)`
* `def set_cookie_header(request)`
* `def set(name, value, [domain], [path])`
* `def get(name, [domain], [path])`
* `def delete(name, [domain], [path])`
* `def clear([domain], [path])`
* *Standard mutable mapping interface*

----------------------------------------------------------------------

=== [96] Developer Interface > `Proxy` ===
FILE: docs\api.md:163-176

## `Proxy`

*A configuration of the proxy server.*

```pycon
>>> proxy = Proxy("http://proxy.example.com:8030")
>>> client = Client(proxy=proxy)
```

* `def __init__(url, [ssl_context], [auth], [headers])`
* `.url` - **URL**
* `.auth` - **tuple[str, str]**
* `.headers` - **Headers**
* `.ssl_context` - **SSLContext**

----------------------------------------------------------------------

=== [97] docs\async.md ===
FILE: docs\async.md:1-12

# Async Support

HTTPX offers a standard synchronous API by default, but also gives you
the option of an async client if you need it.

Async is a concurrency model that is far more efficient than multi-threading,
and can provide significant performance benefits and enable the use of
long-lived network connections such as WebSockets.

If you're working with an async web framework then you'll also want to use an
async client for sending outgoing HTTP requests.

----------------------------------------------------------------------

=== [98] Async Support > Making Async requests ===
FILE: docs\async.md:13-27

## Making Async requests

To make asynchronous requests, you'll need an `AsyncClient`.

```pycon
>>> async with httpx.AsyncClient() as client:
...     r = await client.get('https://www.example.com/')
...
>>> r
<Response [200 OK]>
```

!!! tip
    Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.9+ with `python -m asyncio` to try this code interactively, as they support executing `async`/`await` expressions in the console.

----------------------------------------------------------------------

=== [99] Async Support > API Differences ===
FILE: docs\async.md:28-130

## API Differences

If you're using an async client then there are a few bits of API that
use async methods.

### Making requests

The request methods are all async, so you should use `response = await client.get(...)` style for all of the following:

* `AsyncClient.get(url, ...)`
* `AsyncClient.options(url, ...)`
* `AsyncClient.head(url, ...)`
* `AsyncClient.post(url, ...)`
* `AsyncClient.put(url, ...)`
* `AsyncClient.patch(url, ...)`
* `AsyncClient.delete(url, ...)`
* `AsyncClient.request(method, url, ...)`
* `AsyncClient.send(request, ...)`

### Opening and closing clients

Use `async with httpx.AsyncClient()` if you want a context-managed client...

```python
async with httpx.AsyncClient() as client:
    ...
```

!!! warning
    In order to get the most benefit from connection pooling, make sure you're not instantiating multiple client instances - for example by using `async with` inside a "hot loop". This can be achieved either by having a single scoped client that's passed throughout wherever it's needed, or by having a single global client instance.

Alternatively, use `await client.aclose()` if you want to close a client explicitly:

```python
client = httpx.AsyncClient()
...
await client.aclose()
```

### Streaming responses

The `AsyncClient.stream(method, url, ...)` method is an async context block.

```pycon
>>> client = httpx.AsyncClient()
>>> async with client.stream('GET', 'https://www.example.com/') as response:
...     async for chunk in response.aiter_bytes():
...         ...
```

The async response streaming methods are:

* `Response.aread()` - For conditionally reading a response inside a stream block.
* `Response.aiter_bytes()` - For streaming the response content as bytes.
* `Response.aiter_text()` - For streaming the response content as text.
* `Response.aiter_lines()` - For streaming the response content as lines of text.
* `Response.aiter_raw()` - For streaming the raw response bytes, without applying content decoding.
* `Response.aclose()` - For closing the response. You don't usually need this, since `.stream` block closes the response automatically on exit.

For situations when context block usage is not practical, it is possible to enter "manual mode" by sending a [`Request` instance](advanced/clients.md#request-instances) using `client.send(..., stream=True)`.

Example in the context of forwarding the response to a streaming web endpoint with [Starlette](https://www.starlette.io):

```python
import httpx
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse

client = httpx.AsyncClient()

async def home(request):
    req = client.build_request("GET", "https://www.example.com/")
    r = await client.send(req, stream=True)
    return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))
```

!!! warning
    When using this "manual streaming mode", it is your duty as a developer to make sure that `Response.aclose()` is called eventually. Failing to do so would leave connections open, most likely resulting in resource leaks down the line.

### Streaming requests

When sending a streaming request body with an `AsyncClient` instance, you should use an async bytes generator instead of a bytes generator:

```python
async def upload_bytes():
    ...  # yield byte content

await client.post(url, content=upload_bytes())
```

### Explicit transport instances

When instantiating a transport instance directly, you need to use `httpx.AsyncHTTPTransport`.

For instance:

```pycon
>>> import httpx
>>> transport = httpx.AsyncHTTPTransport(retries=1)
>>> async with httpx.AsyncClient(transport=transport) as client:
>>>     ...
```

----------------------------------------------------------------------

=== [100] Async Support > Supported async environments ===
FILE: docs\async.md:131-191

## Supported async environments

HTTPX supports either `asyncio` or `trio` as an async environment.

It will auto-detect which of those two to use as the backend
for socket operations and concurrency primitives.

### [AsyncIO](https://docs.python.org/3/library/asyncio.html)

AsyncIO is Python's [built-in library](https://docs.python.org/3/library/asyncio.html)
for writing concurrent code with the async/await syntax.

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)

asyncio.run(main())
```

### [Trio](https://github.com/python-trio/trio)

Trio is [an alternative async library](https://trio.readthedocs.io/en/stable/),
designed around the [the principles of structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency).

```python
import httpx
import trio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)

trio.run(main)
```

!!! important
    The `trio` package must be installed to use the Trio backend.


### [AnyIO](https://github.com/agronholm/anyio)

AnyIO is an [asynchronous networking and concurrency library](https://anyio.readthedocs.io/) that works on top of either `asyncio` or `trio`. It blends in with native libraries of your chosen backend (defaults to `asyncio`).

```python
import httpx
import anyio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)

anyio.run(main, backend='trio')
```

----------------------------------------------------------------------

=== [101] Async Support > Calling into Python Web Apps ===
FILE: docs\async.md:192-194

## Calling into Python Web Apps

For details on calling directly into ASGI applications, see [the `ASGITransport` docs](../advanced/transports#asgitransport).

----------------------------------------------------------------------

=== [102] docs\code_of_conduct.md ===
FILE: docs\code_of_conduct.md:1-6

# Code of Conduct

We expect contributors to our projects and online spaces to follow [the Python Software Foundation’s Code of Conduct](https://www.python.org/psf/conduct/).

The Python community is made up of members from around the globe with a diverse set of skills, personalities, and experiences. It is through these differences that our community experiences great successes and continued growth. When you're working with members of the community, this Code of Conduct will help steer your interactions and keep Python a positive, successful, and growing community.

----------------------------------------------------------------------

=== [103] Code of Conduct > Our Community ===
FILE: docs\code_of_conduct.md:7-20

## Our Community

Members of the Python community are **open, considerate, and respectful**. Behaviours that reinforce these values contribute to a positive environment, and include:

* **Being open.** Members of the community are open to collaboration, whether it's on PEPs, patches, problems, or otherwise.
* **Focusing on what is best for the community.** We're respectful of the processes set forth in the community, and we work within them.
* **Acknowledging time and effort.** We're respectful of the volunteer efforts that permeate the Python community. We're thoughtful when addressing the efforts of others, keeping in mind that often times the labor was completed simply for the good of the community.
* **Being respectful of differing viewpoints and experiences.** We're receptive to constructive comments and criticism, as the experiences and skill sets of other members contribute to the whole of our efforts.
* **Showing empathy towards other community members.** We're attentive in our communications, whether in person or online, and we're tactful when approaching differing views.
* **Being considerate.** Members of the community are considerate of their peers -- other Python users.
* **Being respectful.** We're respectful of others, their positions, their skills, their commitments, and their efforts.
* **Gracefully accepting constructive criticism.** When we disagree, we are courteous in raising our issues.
* **Using welcoming and inclusive language.** We're accepting of all who wish to take part in our activities, fostering an environment where anyone can participate and everyone can make a difference.

----------------------------------------------------------------------

=== [104] Code of Conduct > Our Standards ===
FILE: docs\code_of_conduct.md:21-24

## Our Standards

Every member of our community has the right to have their identity respected. The Python community is dedicated to providing a positive experience for everyone, regardless of age, gender identity and expression, sexual orientation, disability, physical appearance, body size, ethnicity, nationality, race, or religion (or lack thereof), education, or socio-economic status.

----------------------------------------------------------------------

=== [105] Code of Conduct > Inappropriate Behavior ===
FILE: docs\code_of_conduct.md:25-47

## Inappropriate Behavior

Examples of unacceptable behavior by participants include:

* Harassment of any participants in any form
* Deliberate intimidation, stalking, or following
* Logging or taking screenshots of online activity for harassment purposes
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Violent threats or language directed against another person
* Incitement of violence or harassment towards any individual, including encouraging a person to commit suicide or to engage in self-harm
* Creating additional online accounts in order to harass another person or circumvent a ban
* Sexual language and imagery in online communities or in any conference venue, including talks
* Insults, put downs, or jokes that are based upon stereotypes, that are exclusionary, or that hold others up for ridicule
* Excessive swearing
* Unwelcome sexual attention or advances
* Unwelcome physical contact, including simulated physical contact (eg, textual descriptions like "hug" or "backrub") without consent or after a request to stop
* Pattern of inappropriate social contact, such as requesting/assuming inappropriate levels of intimacy with others
* Sustained disruption of online community discussions, in-person presentations, or other in-person events
* Continued one-on-one communication after requests to cease
* Other conduct that is inappropriate for a professional audience including people of many different backgrounds

Community members asked to stop any inappropriate behavior are expected to comply immediately.

----------------------------------------------------------------------

=== [106] Code of Conduct > Enforcement ===
FILE: docs\code_of_conduct.md:48-56

## Enforcement

We take Code of Conduct violations seriously, and will act to ensure our spaces are welcoming, inclusive, and professional environments to communicate in.

If you need to raise a Code of Conduct report, you may do so privately by email to tom@tomchristie.com.

Reports will be treated confidentially.

Alternately you may [make a report to the Python Software Foundation](https://www.python.org/psf/conduct/reporting/).

----------------------------------------------------------------------

=== [107] docs\compatibility.md ===
FILE: docs\compatibility.md:1-7

# Requests Compatibility Guide

HTTPX aims to be broadly compatible with the `requests` API, although there are a
few design differences in places.

This documentation outlines places where the API differs...

----------------------------------------------------------------------

=== [108] Requests Compatibility Guide > Redirects ===
FILE: docs\compatibility.md:8-27

## Redirects

Unlike `requests`, HTTPX does **not follow redirects by default**.

We differ in behaviour here [because auto-redirects can easily mask unnecessary network
calls being made](https://github.com/encode/httpx/discussions/1785).

You can still enable behaviour to automatically follow redirects, but you need to
do so explicitly...

```python
response = client.get(url, follow_redirects=True)
```

Or else instantiate a client, with redirect following enabled by default...

```python
client = httpx.Client(follow_redirects=True)
```

----------------------------------------------------------------------

=== [109] Requests Compatibility Guide > Client instances ===
FILE: docs\compatibility.md:28-41

## Client instances

The HTTPX equivalent of `requests.Session` is `httpx.Client`.

```python
session = requests.Session(**kwargs)
```

is generally equivalent to

```python
client = httpx.Client(**kwargs)
```

----------------------------------------------------------------------

=== [110] Requests Compatibility Guide > Request URLs ===
FILE: docs\compatibility.md:42-47

## Request URLs

Accessing `response.url` will return a `URL` instance, rather than a string.

Use `str(response.url)` if you need a string instance.

----------------------------------------------------------------------

=== [111] Requests Compatibility Guide > Determining the next redirect request ===
FILE: docs\compatibility.md:48-69

## Determining the next redirect request

The `requests` library exposes an attribute `response.next`, which can be used to obtain the next redirect request.

```python
session = requests.Session()
request = requests.Request("GET", ...).prepare()
while request is not None:
    response = session.send(request, allow_redirects=False)
    request = response.next
```

In HTTPX, this attribute is instead named `response.next_request`. For example:

```python
client = httpx.Client()
request = client.build_request("GET", ...)
while request is not None:
    response = client.send(request)
    request = response.next_request
```

----------------------------------------------------------------------

=== [112] Requests Compatibility Guide > Request Content ===
FILE: docs\compatibility.md:70-91

## Request Content

For uploading raw text or binary content we prefer to use a `content` parameter,
in order to better separate this usage from the case of uploading form data.

For example, using `content=...` to upload raw content:

```python
# Uploading text, bytes, or a bytes iterator.
httpx.post(..., content=b"Hello, world")
```

And using `data=...` to send form data:

```python
# Uploading form data.
httpx.post(..., data={"message": "Hello, world"})
```

Using the `data=<text/byte content>` will raise a deprecation warning,
and is expected to be fully removed with the HTTPX 1.0 release.

----------------------------------------------------------------------

=== [113] Requests Compatibility Guide > Upload files ===
FILE: docs\compatibility.md:92-97

## Upload files

HTTPX strictly enforces that upload files must be opened in binary mode, in order
to avoid character encoding issues that can result from attempting to upload files
opened in text mode.

----------------------------------------------------------------------

=== [114] Requests Compatibility Guide > Content encoding ===
FILE: docs\compatibility.md:98-102

## Content encoding

HTTPX uses `utf-8` for encoding `str` request bodies. For example, when using `content=<str>` the request body will be encoded to `utf-8` before being sent over the wire. This differs from Requests which uses `latin1`. If you need an explicit encoding, pass encoded bytes explicitly, e.g. `content=<str>.encode("latin1")`.
For response bodies, assuming the server didn't send an explicit encoding then HTTPX will do its best to figure out an appropriate encoding. HTTPX makes a guess at the encoding to use for decoding the response using `charset_normalizer`. Fallback to that or any content with less than 32 octets will be decoded using `utf-8` with the `error="replace"` decoder strategy.

----------------------------------------------------------------------

=== [115] Requests Compatibility Guide > Cookies ===
FILE: docs\compatibility.md:103-122

## Cookies

If using a client instance, then cookies should always be set on the client rather than on a per-request basis.

This usage is supported:

```python
client = httpx.Client(cookies=...)
client.post(...)
```

This usage is **not** supported:

```python
client = httpx.Client()
client.post(..., cookies=...)
```

We prefer enforcing a stricter API here because it provides clearer expectations around cookie persistence, particularly when redirects occur.

----------------------------------------------------------------------

=== [116] Requests Compatibility Guide > Status Codes ===
FILE: docs\compatibility.md:123-128

## Status Codes

In our documentation we prefer the uppercased versions, such as `codes.NOT_FOUND`, but also provide lower-cased versions for API compatibility with `requests`.

Requests includes various synonyms for status codes that HTTPX does not support.

----------------------------------------------------------------------

=== [117] Requests Compatibility Guide > Streaming responses ===
FILE: docs\compatibility.md:129-147

## Streaming responses

HTTPX provides a `.stream()` interface rather than using `stream=True`. This ensures that streaming responses are always properly closed outside of the stream block, and makes it visually clearer at which points streaming I/O APIs may be used with a response.

For example:

```python
with httpx.stream("GET", "https://www.example.com") as response:
    ...
```

Within a `stream()` block request data is made available with:

* `.iter_bytes()` - Instead of `response.iter_content()`
* `.iter_text()` - Instead of `response.iter_content(decode_unicode=True)`
* `.iter_lines()` - Corresponding to `response.iter_lines()`
* `.iter_raw()` - Use this instead of `response.raw`
* `.read()` - Read the entire response body, making `response.text` and `response.content` available.

----------------------------------------------------------------------

=== [118] Requests Compatibility Guide > Timeouts ===
FILE: docs\compatibility.md:148-157

## Timeouts

HTTPX defaults to including reasonable [timeouts](quickstart.md#timeouts) for all network operations, while Requests has no timeouts by default.

To get the same behavior as Requests, set the `timeout` parameter to `None`:

```python
httpx.get('https://www.example.com', timeout=None)
```

----------------------------------------------------------------------

=== [119] Requests Compatibility Guide > Proxy keys ===
FILE: docs\compatibility.md:158-171

## Proxy keys

HTTPX uses the mounts argument for HTTP proxying and transport routing.
It can do much more than proxies and allows you to configure more than just the proxy route.
For more detailed documentation, see [Mounting Transports](advanced/transports.md#mounting-transports).

When using `httpx.Client(mounts={...})` to map to a selection of different transports, we use full URL schemes, such as `mounts={"http://": ..., "https://": ...}`.

This is different to the `requests` usage of `proxies={"http": ..., "https": ...}`.

This change is for better consistency with more complex mappings, that might also include domain names, such as `mounts={"all://": ..., httpx.HTTPTransport(proxy="all://www.example.com": None})` which maps all requests onto a proxy, except for requests to "www.example.com" which have an explicit exclusion.

Also note that `requests.Session.request(...)` allows a `proxies=...` parameter, whereas `httpx.Client.request(...)` does not allow `mounts=...`.

----------------------------------------------------------------------

=== [120] Requests Compatibility Guide > SSL configuration ===
FILE: docs\compatibility.md:172-177

## SSL configuration

When using a `Client` instance, the ssl configurations should always be passed on client instantiation, rather than passed to the request method.

If you need more than one different SSL configuration, you should use different client instances for each SSL configuration.

----------------------------------------------------------------------

=== [121] Requests Compatibility Guide > Request body on HTTP methods ===
FILE: docs\compatibility.md:178-191

## Request body on HTTP methods

The HTTP `GET`, `DELETE`, `HEAD`, and `OPTIONS` methods are specified as not supporting a request body. To stay in line with this, the `.get`, `.delete`, `.head` and `.options` functions do not support `content`, `files`, `data`, or `json` arguments.

If you really do need to send request data using these http methods you should use the generic `.request` function instead.

```python
httpx.request(
  method="DELETE",
  url="https://www.example.com/",
  content=b'A request body on a DELETE request.'
)
```

----------------------------------------------------------------------

=== [122] Requests Compatibility Guide > Checking for success and failure responses ===
FILE: docs\compatibility.md:192-195

## Checking for success and failure responses

We don't support `response.is_ok` since the naming is ambiguous there, and might incorrectly imply an equivalence to `response.status_code == codes.OK`. Instead we provide the `response.is_success` property, which can be used to check for a 2xx response.

----------------------------------------------------------------------

=== [123] Requests Compatibility Guide > Request instantiation ===
FILE: docs\compatibility.md:196-201

## Request instantiation

There is no notion of [prepared requests](https://requests.readthedocs.io/en/stable/user/advanced/#prepared-requests) in HTTPX. If you need to customize request instantiation, see [Request instances](advanced/clients.md#request-instances).

Besides, `httpx.Request()` does not support the `auth`, `timeout`, `follow_redirects`, `mounts`, `verify` and `cert` parameters. However these are available in `httpx.request`, `httpx.get`, `httpx.post` etc., as well as on [`Client` instances](advanced/clients.md#client-instances).

----------------------------------------------------------------------

=== [124] Requests Compatibility Guide > Mocking ===
FILE: docs\compatibility.md:202-205

## Mocking

If you need to mock HTTPX the same way that test utilities like `responses` and `requests-mock` does for `requests`, see [RESPX](https://github.com/lundberg/respx).

----------------------------------------------------------------------

=== [125] Requests Compatibility Guide > Caching ===
FILE: docs\compatibility.md:206-209

## Caching

If you use `cachecontrol` or `requests-cache` to add HTTP Caching support to the `requests` library, you can use [Hishel](https://hishel.com) for HTTPX.

----------------------------------------------------------------------

=== [126] Requests Compatibility Guide > Networking layer ===
FILE: docs\compatibility.md:210-215

## Networking layer

`requests` defers most of its HTTP networking code to the excellent [`urllib3` library](https://urllib3.readthedocs.io/en/latest/).

On the other hand, HTTPX uses [HTTPCore](https://github.com/encode/httpcore) as its core HTTP networking layer, which is a different project than `urllib3`.

----------------------------------------------------------------------

=== [127] Requests Compatibility Guide > Query Parameters ===
FILE: docs\compatibility.md:216-221

## Query Parameters

`requests` omits `params` whose values are `None` (e.g. `requests.get(..., params={"foo": None})`). This is not supported by HTTPX.

For both query params (`params=`) and form data (`data=`), `requests` supports sending a list of tuples (e.g. `requests.get(..., params=[('key1', 'value1'), ('key1', 'value2')])`). This is not supported by HTTPX. Instead, use a dictionary with lists as values. E.g.: `httpx.get(..., params={'key1': ['value1', 'value2']})` or with form data: `httpx.post(..., data={'key1': ['value1', 'value2']})`.

----------------------------------------------------------------------

=== [128] Requests Compatibility Guide > Event Hooks ===
FILE: docs\compatibility.md:222-229

## Event Hooks

`requests` allows event hooks to mutate `Request` and `Response` objects. See [examples](https://requests.readthedocs.io/en/master/user/advanced/#event-hooks) given in the documentation for `requests`.

In HTTPX, event hooks may access properties of requests and responses, but event hook callbacks cannot mutate the original request/response.

If you are looking for more control, consider checking out [Custom Transports](advanced/transports.md#custom-transports).

----------------------------------------------------------------------

=== [129] Requests Compatibility Guide > Exceptions and Errors ===
FILE: docs\compatibility.md:230-232

## Exceptions and Errors

`requests` exception hierarchy is slightly different to the `httpx` exception hierarchy. `requests` exposes a top level `RequestException`, where as `httpx` exposes a top level `HTTPError`. see the exceptions exposes in requests [here](https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/). See the `httpx` error hierarchy [here](https://www.python-httpx.org/exceptions/).

----------------------------------------------------------------------

=== [130] docs\contributing.md ===
FILE: docs\contributing.md:1-11

# Contributing

Thank you for being interested in contributing to HTTPX.
There are many ways you can contribute to the project:

- Try HTTPX and [report bugs/issues you find](https://github.com/encode/httpx/issues/new)
- [Implement new features](https://github.com/encode/httpx/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [Review Pull Requests of others](https://github.com/encode/httpx/pulls)
- Write documentation
- Participate in discussions

----------------------------------------------------------------------

=== [131] Contributing > Reporting Bugs or Other Issues ===
FILE: docs\contributing.md:12-39

## Reporting Bugs or Other Issues

Found something that HTTPX should support?
Stumbled upon some unexpected behaviour?

Contributions should generally start out with [a discussion](https://github.com/encode/httpx/discussions).
Possible bugs may be raised as a "Potential Issue" discussion, feature requests may
be raised as an "Ideas" discussion. We can then determine if the discussion needs
to be escalated into an "Issue" or not, or if we'd consider a pull request.

Try to be more descriptive as you can and in case of a bug report,
provide as much information as possible like:

- OS platform
- Python version
- Installed dependencies and versions (`python -m pip freeze`)
- Code snippet
- Error traceback

You should always try to reduce any examples to the *simplest possible case*
that demonstrates the issue.

Some possibly useful tips for narrowing down potential issues...

- Does the issue exist on HTTP/1.1, or HTTP/2, or both?
- Does the issue exist with `Client`, `AsyncClient`, or both?
- When using `AsyncClient` does the issue exist when using `asyncio` or `trio`, or both?

----------------------------------------------------------------------

=== [132] Contributing > Development ===
FILE: docs\contributing.md:40-58

## Development

To start developing HTTPX create a **fork** of the
[HTTPX repository](https://github.com/encode/httpx) on GitHub.

Then clone your fork with the following command replacing `YOUR-USERNAME` with
your GitHub username:

```shell
$ git clone https://github.com/YOUR-USERNAME/httpx
```

You can now install the project and its dependencies using:

```shell
$ cd httpx
$ scripts/install
```

----------------------------------------------------------------------

=== [133] Contributing > Testing and Linting ===
FILE: docs\contributing.md:59-93

## Testing and Linting

We use custom shell scripts to automate testing, linting,
and documentation building workflow.

To run the tests, use:

```shell
$ scripts/test
```

!!! warning
    The test suite spawns testing servers on ports **8000** and **8001**.
    Make sure these are not in use, so the tests can run properly.

Any additional arguments will be passed to `pytest`. See the [pytest documentation](https://docs.pytest.org/en/latest/how-to/usage.html) for more information.

For example, to run a single test script:

```shell
$ scripts/test tests/test_multipart.py
```

To run the code auto-formatting:

```shell
$ scripts/lint
```

Lastly, to run code checks separately (they are also run as part of `scripts/test`), run:

```shell
$ scripts/check
```

----------------------------------------------------------------------

=== [134] Contributing > Documenting ===
FILE: docs\contributing.md:94-103

## Documenting

Documentation pages are located under the `docs/` folder.

To run the documentation site locally (useful for previewing changes), use:

```shell
$ scripts/docs
```

----------------------------------------------------------------------

=== [135] Contributing > Resolving Build / CI Failures ===
FILE: docs\contributing.md:104-152

## Resolving Build / CI Failures

Once you've submitted your pull request, the test suite will automatically run, and the results will show up in GitHub.
If the test suite fails, you'll want to click through to the "Details" link, and try to identify why the test suite failed.

<p align="center" style="margin: 0 0 10px">
  <img src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/gh-actions-fail.png" alt='Failing PR commit status'>
</p>

Here are some common ways the test suite can fail:

### Check Job Failed

<p align="center" style="margin: 0 0 10px">
  <img src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/gh-actions-fail-check.png" alt='Failing GitHub action lint job'>
</p>

This job failing means there is either a code formatting issue or type-annotation issue.
You can look at the job output to figure out why it's failed or within a shell run:

```shell
$ scripts/check
```

It may be worth it to run `$ scripts/lint` to attempt auto-formatting the code
and if that job succeeds commit the changes.

### Docs Job Failed

This job failing means the documentation failed to build. This can happen for
a variety of reasons like invalid markdown or missing configuration within `mkdocs.yml`.

### Python 3.X Job Failed

<p align="center" style="margin: 0 0 10px">
  <img src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/gh-actions-fail-test.png" alt='Failing GitHub action test job'>
</p>

This job failing means the unit tests failed or not all code paths are covered by unit tests.

If tests are failing you will see this message under the coverage report:

`=== 1 failed, 435 passed, 1 skipped, 1 xfailed in 11.09s ===`

If tests succeed but coverage doesn't reach our current threshold, you will see this
message under the coverage report:

`FAIL Required test coverage of 100% not reached. Total coverage: 99.00%`

----------------------------------------------------------------------

=== [136] Contributing > Releasing ===
FILE: docs\contributing.md:153-181

## Releasing

*This section is targeted at HTTPX maintainers.*

Before releasing a new version, create a pull request that includes:

- **An update to the changelog**:
    - We follow the format from [keepachangelog](https://keepachangelog.com/en/1.0.0/).
    - [Compare](https://github.com/encode/httpx/compare/) `master` with the tag of the latest release, and list all entries that are of interest to our users:
        - Things that **must** go in the changelog: added, changed, deprecated or removed features, and bug fixes.
        - Things that **should not** go in the changelog: changes to documentation, tests or tooling.
        - Try sorting entries in descending order of impact / importance.
        - Keep it concise and to-the-point. 🎯
- **A version bump**: see `__version__.py`.

For an example, see [#1006](https://github.com/encode/httpx/pull/1006).

Once the release PR is merged, create a
[new release](https://github.com/encode/httpx/releases/new) including:

- Tag version like `0.13.3`.
- Release title `Version 0.13.3`
- Description copied from the changelog.

Once created this release will be automatically uploaded to PyPI.

If something goes wrong with the PyPI job the release can be published using the
`scripts/publish` script.

----------------------------------------------------------------------

=== [137] Contributing > Development proxy setup ===
FILE: docs\contributing.md:182-232

## Development proxy setup

To test and debug requests via a proxy it's best to run a proxy server locally.
Any server should do but HTTPCore's test suite uses
[`mitmproxy`](https://mitmproxy.org/) which is written in Python, it's fully
featured and has excellent UI and tools for introspection of requests.

You can install `mitmproxy` using `pip install mitmproxy` or [several
other ways](https://docs.mitmproxy.org/stable/overview-installation/).

`mitmproxy` does require setting up local TLS certificates for HTTPS requests,
as its main purpose is to allow developers to inspect requests that pass through
it. We can set them up follows:

1. [`pip install trustme-cli`](https://github.com/sethmlarson/trustme-cli/).
2. `trustme-cli -i example.org www.example.org`, assuming you want to test
connecting to that domain, this will create three files: `server.pem`,
`server.key` and `client.pem`.
3. `mitmproxy` requires a PEM file that includes the private key and the
certificate so we need to concatenate them:
`cat server.key server.pem > server.withkey.pem`.
4. Start the proxy server `mitmproxy --certs server.withkey.pem`, or use the
[other mitmproxy commands](https://docs.mitmproxy.org/stable/) with different
UI options.

At this point the server is ready to start serving requests, you'll need to
configure HTTPX as described in the
[proxy section](https://www.python-httpx.org/advanced/proxies/#http-proxies) and
the [SSL certificates section](https://www.python-httpx.org/advanced/ssl/),
this is where our previously generated `client.pem` comes in:

```python
ctx = ssl.create_default_context(cafile="/path/to/client.pem")
client = httpx.Client(proxy="http://127.0.0.1:8080/", verify=ctx)
```

Note, however, that HTTPS requests will only succeed to the host specified
in the SSL/TLS certificate we generated, HTTPS requests to other hosts will
raise an error like:

```
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate
verify failed: Hostname mismatch, certificate is not valid for
'duckduckgo.com'. (_ssl.c:1108)
```

If you want to make requests to more hosts you'll need to regenerate the
certificates and include all the hosts you intend to connect to in the
seconds step, i.e.

`trustme-cli -i example.org www.example.org duckduckgo.com www.duckduckgo.com`

----------------------------------------------------------------------

=== [138] docs\environment_variables.md ===
FILE: docs\environment_variables.md:1-10

# Environment Variables

The HTTPX library can be configured via environment variables.
Environment variables are used by default. To ignore environment variables, `trust_env` has to be set `False`. There are two ways to set `trust_env` to disable environment variables:

* On the client via `httpx.Client(trust_env=False)`.
* Using the top-level API, such as `httpx.get("<url>", trust_env=False)`.

Here is a list of environment variables that HTTPX recognizes and what function they serve:

----------------------------------------------------------------------

=== [139] Environment Variables > Proxies ===
FILE: docs\environment_variables.md:11-54

## Proxies

The environment variables documented below are used as a convention by various HTTP tooling, including:

* [cURL](https://github.com/curl/curl/blob/master/docs/MANUAL.md#environment-variables)
* [requests](https://github.com/psf/requests/blob/master/docs/user/advanced.rst#proxies)

For more information on using proxies in HTTPX, see [HTTP Proxying](advanced/proxies.md#http-proxying).

### `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`

Valid values: A URL to a proxy

`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` set the proxy to be used for `http`, `https`, or all requests respectively.

```bash
export HTTP_PROXY=http://my-external-proxy.com:1234

# This request will be sent through the proxy
python -c "import httpx; httpx.get('http://example.com')"

# This request will be sent directly, as we set `trust_env=False`
python -c "import httpx; httpx.get('http://example.com', trust_env=False)"

```

### `NO_PROXY`

Valid values: a comma-separated list of hostnames/urls

`NO_PROXY` disables the proxy for specific urls

```bash
export HTTP_PROXY=http://my-external-proxy.com:1234
export NO_PROXY=http://127.0.0.1,python-httpx.org

# As in the previous example, this request will be sent through the proxy
python -c "import httpx; httpx.get('http://example.com')"

# These requests will be sent directly, bypassing the proxy
python -c "import httpx; httpx.get('http://127.0.0.1:5000/my-api')"
python -c "import httpx; httpx.get('https://www.python-httpx.org')"
```

----------------------------------------------------------------------

=== [140] Environment Variables > `SSL_CERT_FILE` ===
FILE: docs\environment_variables.md:55-68

## `SSL_CERT_FILE`

Valid values: a filename

If this environment variable is set then HTTPX will load
CA certificate from the specified file instead of the default
location.

Example:

```console
SSL_CERT_FILE=/path/to/ca-certs/ca-bundle.crt python -c "import httpx; httpx.get('https://example.com')"
```

----------------------------------------------------------------------

=== [141] Environment Variables > `SSL_CERT_DIR` ===
FILE: docs\environment_variables.md:69-79

## `SSL_CERT_DIR`

Valid values: a directory following an [OpenSSL specific layout](https://www.openssl.org/docs/manmaster/man3/SSL_CTX_load_verify_locations.html).

If this environment variable is set and the directory follows an [OpenSSL specific layout](https://www.openssl.org/docs/manmaster/man3/SSL_CTX_load_verify_locations.html) (ie. you ran `c_rehash`) then HTTPX will load CA certificates from this directory instead of the default location.

Example:

```console
SSL_CERT_DIR=/path/to/ca-certs/ python -c "import httpx; httpx.get('https://example.com')"
```

----------------------------------------------------------------------

=== [142] docs\exceptions.md ===
FILE: docs\exceptions.md:1-6

# Exceptions

This page lists exceptions that may be raised when using HTTPX.

For an overview of how to work with HTTPX exceptions, see [Exceptions (Quickstart)](quickstart.md#exceptions).

----------------------------------------------------------------------

=== [143] Exceptions > The exception hierarchy ===
FILE: docs\exceptions.md:7-39

## The exception hierarchy

* HTTPError
    * RequestError
        * TransportError
            * TimeoutException
                * ConnectTimeout
                * ReadTimeout
                * WriteTimeout
                * PoolTimeout
            * NetworkError
                * ConnectError
                * ReadError
                * WriteError
                * CloseError
            * ProtocolError
                * LocalProtocolError
                * RemoteProtocolError
            * ProxyError
            * UnsupportedProtocol
        * DecodingError
        * TooManyRedirects
    * HTTPStatusError
* InvalidURL
* CookieConflict
* StreamError
    * StreamConsumed
    * ResponseNotRead
    * RequestNotRead
    * StreamClosed

---

----------------------------------------------------------------------

=== [144] Exceptions > Exception classes ===
FILE: docs\exceptions.md:40-124

## Exception classes

::: httpx.HTTPError
    :docstring:

::: httpx.RequestError
    :docstring:

::: httpx.TransportError
    :docstring:

::: httpx.TimeoutException
    :docstring:

::: httpx.ConnectTimeout
    :docstring:

::: httpx.ReadTimeout
    :docstring:

::: httpx.WriteTimeout
    :docstring:

::: httpx.PoolTimeout
    :docstring:

::: httpx.NetworkError
    :docstring:

::: httpx.ConnectError
    :docstring:

::: httpx.ReadError
    :docstring:

::: httpx.WriteError
    :docstring:

::: httpx.CloseError
    :docstring:

::: httpx.ProtocolError
    :docstring:

::: httpx.LocalProtocolError
    :docstring:

::: httpx.RemoteProtocolError
    :docstring:

::: httpx.ProxyError
    :docstring:

::: httpx.UnsupportedProtocol
    :docstring:

::: httpx.DecodingError
    :docstring:

::: httpx.TooManyRedirects
    :docstring:

::: httpx.HTTPStatusError
    :docstring:

::: httpx.InvalidURL
    :docstring:

::: httpx.CookieConflict
    :docstring:

::: httpx.StreamError
    :docstring:

::: httpx.StreamConsumed
    :docstring:

::: httpx.StreamClosed
    :docstring:

::: httpx.ResponseNotRead
    :docstring:

::: httpx.RequestNotRead
    :docstring:

----------------------------------------------------------------------

=== [145] docs\http2.md ===
FILE: docs\http2.md:1-18

# HTTP/2

HTTP/2 is a major new iteration of the HTTP protocol, that provides a far more
efficient transport, with potential performance benefits. HTTP/2 does not change
the core semantics of the request or response, but alters the way that data is
sent to and from the server.

Rather than the text format that HTTP/1.1 uses, HTTP/2 is a binary format.
The binary format provides full request and response multiplexing, and efficient
compression of HTTP headers. The stream multiplexing means that where HTTP/1.1
requires one TCP stream for each concurrent request, HTTP/2 allows a single TCP
stream to handle multiple concurrent requests.

HTTP/2 also provides support for functionality such as response prioritization,
and server push.

For a comprehensive guide to HTTP/2 you may want to check out "[http2 explained](https://http2-explained.haxx.se/)".

----------------------------------------------------------------------

=== [146] HTTP/2 > Enabling HTTP/2 ===
FILE: docs\http2.md:19-53

## Enabling HTTP/2

When using the `httpx` client, HTTP/2 support is not enabled by default, because
HTTP/1.1 is a mature, battle-hardened transport layer, and our HTTP/1.1
implementation may be considered the more robust option at this point in time.
It is possible that a future version of `httpx` may enable HTTP/2 support by default.

If you're issuing highly concurrent requests you might want to consider
trying out our HTTP/2 support. You can do so by first making sure to install
the optional HTTP/2 dependencies...

```shell
$ pip install httpx[http2]
```

And then instantiating a client with HTTP/2 support enabled:

```python
client = httpx.AsyncClient(http2=True)
...
```

You can also instantiate a client as a context manager, to ensure that all
HTTP connections are nicely scoped, and will be closed once the context block
is exited.

```python
async with httpx.AsyncClient(http2=True) as client:
    ...
```

HTTP/2 support is available on both `Client` and `AsyncClient`, although it's
typically more useful in async contexts if you're issuing lots of concurrent
requests.

----------------------------------------------------------------------

=== [147] HTTP/2 > Inspecting the HTTP version ===
FILE: docs\http2.md:54-68

## Inspecting the HTTP version

Enabling HTTP/2 support on the client does not *necessarily* mean that your
requests and responses will be transported over HTTP/2, since both the client
*and* the server need to support HTTP/2. If you connect to a server that only
supports HTTP/1.1 the client will use a standard HTTP/1.1 connection instead.

You can determine which version of the HTTP protocol was used by examining
the `.http_version` property on the response.

```python
client = httpx.AsyncClient(http2=True)
response = await client.get(...)
print(response.http_version)  # "HTTP/1.0", "HTTP/1.1", or "HTTP/2".
```

----------------------------------------------------------------------

=== [148] docs\index.md ===
FILE: docs\index.md:1-63

<p align="center" style="margin: 0 0 10px">
  <img width="350" height="208" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/butterfly.png" alt='HTTPX'>
</p>

<h1 align="center" style="font-size: 3rem; margin: -15px 0">
HTTPX
</h1>

---

<div align="center">
<p>
<a href="https://github.com/encode/httpx/actions">
    <img src="https://github.com/encode/httpx/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/httpx/">
    <img src="https://badge.fury.io/py/httpx.svg" alt="Package version">
</a>
</p>

<em>A next-generation HTTP client for Python.</em>
</div>

HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

---

Install HTTPX using pip:

```shell
$ pip install httpx
```

Now, let's get started:

```pycon
>>> import httpx
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

Or, using the command-line client.

```shell
# The command line client is an optional dependency.
$ pip install 'httpx[cli]'
```

Which now allows us to use HTTPX directly from the command-line...

![httpx --help](img/httpx-help.png)

Sending a request...

![httpx http://httpbin.org/json](img/httpx-request.png)

----------------------------------------------------------------------

=== [149] The command line client is an optional dependency. > Features ===
FILE: docs\index.md:64-93

## Features

HTTPX builds on the well-established usability of `requests`, and gives you:

* A broadly [requests-compatible API](compatibility.md).
* Standard synchronous interface, but with [async support if you need it](async.md).
* HTTP/1.1 [and HTTP/2 support](http2.md).
* Ability to make requests directly to [WSGI applications](advanced/transports.md#wsgi-transport) or [ASGI applications](advanced/transports.md#asgi-transport).
* Strict timeouts everywhere.
* Fully type annotated.
* 100% test coverage.

Plus all the standard features of `requests`...

* International Domains and URLs
* Keep-Alive & Connection Pooling
* Sessions with Cookie Persistence
* Browser-style SSL Verification
* Basic/Digest Authentication
* Elegant Key/Value Cookies
* Automatic Decompression
* Automatic Content Decoding
* Unicode Response Bodies
* Multipart File Uploads
* HTTP(S) Proxy Support
* Connection Timeouts
* Streaming Downloads
* .netrc Support
* Chunked Requests

----------------------------------------------------------------------

=== [150] The command line client is an optional dependency. > Documentation ===
FILE: docs\index.md:94-104

## Documentation

For a run-through of all the basics, head over to the [QuickStart](quickstart.md).

For more advanced topics, see the **Advanced** section,
the [async support](async.md) section, or the [HTTP/2](http2.md) section.

The [Developer Interface](api.md) provides a comprehensive API reference.

To find out about tools that integrate with HTTPX, see [Third Party Packages](third_party_packages.md).

----------------------------------------------------------------------

=== [151] The command line client is an optional dependency. > Dependencies ===
FILE: docs\index.md:105-127

## Dependencies

The HTTPX project relies on these excellent libraries:

* `httpcore` - The underlying transport implementation for `httpx`.
  * `h11` - HTTP/1.1 support.
* `certifi` - SSL certificates.
* `idna` - Internationalized domain name support.
* `sniffio` - Async library autodetection.

As well as these optional installs:

* `h2` - HTTP/2 support. *(Optional, with `httpx[http2]`)*
* `socksio` - SOCKS proxy support. *(Optional, with `httpx[socks]`)*
* `rich` - Rich terminal support. *(Optional, with `httpx[cli]`)*
* `click` - Command line client support. *(Optional, with `httpx[cli]`)*
* `brotli` or `brotlicffi` - Decoding for "brotli" compressed responses. *(Optional, with `httpx[brotli]`)*
* `zstandard` - Decoding for "zstd" compressed responses. *(Optional, with `httpx[zstd]`)*

A huge amount of credit is due to `requests` for the API layout that
much of this work follows, as well as to `urllib3` for plenty of design
inspiration around the lower-level networking details.

----------------------------------------------------------------------

=== [152] The command line client is an optional dependency. > Installation ===
FILE: docs\index.md:128-150

## Installation

Install with pip:

```shell
$ pip install httpx
```

Or, to include the optional HTTP/2 support, use:

```shell
$ pip install httpx[http2]
```

To include the optional brotli and zstandard decoders support, use:

```shell
$ pip install httpx[brotli,zstd]
```

HTTPX requires Python 3.9+

[sync-support]: https://github.com/encode/httpx/issues/572

----------------------------------------------------------------------

=== [153] docs\logging.md ===
FILE: docs\logging.md:1-81

# Logging

If you need to inspect the internal behaviour of `httpx`, you can use Python's standard logging to output information about the underlying network behaviour.

For example, the following configuration...

```python
import logging
import httpx

logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)

httpx.get("https://www.example.com")
```

Will send debug level output to the console, or wherever `stdout` is directed too...

```
DEBUG [2024-09-28 17:27:40] httpcore.connection - connect_tcp.started host='www.example.com' port=443 local_address=None timeout=5.0 socket_options=None
DEBUG [2024-09-28 17:27:41] httpcore.connection - connect_tcp.complete return_value=<httpcore._backends.sync.SyncStream object at 0x101f1e8e0>
DEBUG [2024-09-28 17:27:41] httpcore.connection - start_tls.started ssl_context=SSLContext(verify=True) server_hostname='www.example.com' timeout=5.0
DEBUG [2024-09-28 17:27:41] httpcore.connection - start_tls.complete return_value=<httpcore._backends.sync.SyncStream object at 0x1020f49a0>
DEBUG [2024-09-28 17:27:41] httpcore.http11 - send_request_headers.started request=<Request [b'GET']>
DEBUG [2024-09-28 17:27:41] httpcore.http11 - send_request_headers.complete
DEBUG [2024-09-28 17:27:41] httpcore.http11 - send_request_body.started request=<Request [b'GET']>
DEBUG [2024-09-28 17:27:41] httpcore.http11 - send_request_body.complete
DEBUG [2024-09-28 17:27:41] httpcore.http11 - receive_response_headers.started request=<Request [b'GET']>
DEBUG [2024-09-28 17:27:41] httpcore.http11 - receive_response_headers.complete return_value=(b'HTTP/1.1', 200, b'OK', [(b'Content-Encoding', b'gzip'), (b'Accept-Ranges', b'bytes'), (b'Age', b'407727'), (b'Cache-Control', b'max-age=604800'), (b'Content-Type', b'text/html; charset=UTF-8'), (b'Date', b'Sat, 28 Sep 2024 13:27:42 GMT'), (b'Etag', b'"3147526947+gzip"'), (b'Expires', b'Sat, 05 Oct 2024 13:27:42 GMT'), (b'Last-Modified', b'Thu, 17 Oct 2019 07:18:26 GMT'), (b'Server', b'ECAcc (dcd/7D43)'), (b'Vary', b'Accept-Encoding'), (b'X-Cache', b'HIT'), (b'Content-Length', b'648')])
INFO [2024-09-28 17:27:41] httpx - HTTP Request: GET https://www.example.com "HTTP/1.1 200 OK"
DEBUG [2024-09-28 17:27:41] httpcore.http11 - receive_response_body.started request=<Request [b'GET']>
DEBUG [2024-09-28 17:27:41] httpcore.http11 - receive_response_body.complete
DEBUG [2024-09-28 17:27:41] httpcore.http11 - response_closed.started
DEBUG [2024-09-28 17:27:41] httpcore.http11 - response_closed.complete
DEBUG [2024-09-28 17:27:41] httpcore.connection - close.started
DEBUG [2024-09-28 17:27:41] httpcore.connection - close.complete
```

Logging output includes information from both the high-level `httpx` logger, and the network-level `httpcore` logger, which can be configured separately.

For handling more complex logging configurations you might want to use the dictionary configuration style...

```python
import logging.config
import httpx

LOGGING_CONFIG = {
    "version": 1,
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "http",
            "stream": "ext://sys.stderr"
        }
    },
    "formatters": {
        "http": {
            "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    'loggers': {
        'httpx': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'httpcore': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
httpx.get('https://www.example.com')
```

The exact formatting of the debug logging may be subject to change across different versions of `httpx` and `httpcore`. If you need to rely on a particular format it is recommended that you pin installation of these packages to fixed versions.

----------------------------------------------------------------------

=== [154] docs\quickstart.md ===
FILE: docs\quickstart.md:1-31

# QuickStart

First, start by importing HTTPX:

```pycon
>>> import httpx
```

Now, let’s try to get a webpage.

```pycon
>>> r = httpx.get('https://httpbin.org/get')
>>> r
<Response [200 OK]>
```

Similarly, to make an HTTP POST request:

```pycon
>>> r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
```

The PUT, DELETE, HEAD, and OPTIONS requests all follow the same style:

```pycon
>>> r = httpx.put('https://httpbin.org/put', data={'key': 'value'})
>>> r = httpx.delete('https://httpbin.org/delete')
>>> r = httpx.head('https://httpbin.org/get')
>>> r = httpx.options('https://httpbin.org/get')
```

----------------------------------------------------------------------

=== [155] QuickStart > Passing Parameters in URLs ===
FILE: docs\quickstart.md:32-57

## Passing Parameters in URLs

To include URL query parameters in the request, use the `params` keyword:

```pycon
>>> params = {'key1': 'value1', 'key2': 'value2'}
>>> r = httpx.get('https://httpbin.org/get', params=params)
```

To see how the values get encoding into the URL string, we can inspect the
resulting URL that was used to make the request:

```pycon
>>> r.url
URL('https://httpbin.org/get?key2=value2&key1=value1')
```

You can also pass a list of items as a value:

```pycon
>>> params = {'key1': 'value1', 'key2': ['value2', 'value3']}
>>> r = httpx.get('https://httpbin.org/get', params=params)
>>> r.url
URL('https://httpbin.org/get?key1=value1&key2=value2&key2=value3')
```

----------------------------------------------------------------------

=== [156] QuickStart > Response Content ===
FILE: docs\quickstart.md:58-91

## Response Content

HTTPX will automatically handle decoding the response content into Unicode text.

```pycon
>>> r = httpx.get('https://www.example.org/')
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

You can inspect what encoding will be used to decode the response.

```pycon
>>> r.encoding
'UTF-8'
```

In some cases the response may not contain an explicit encoding, in which case HTTPX
will attempt to automatically determine an encoding to use.

```pycon
>>> r.encoding
None
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

If you need to override the standard behaviour and explicitly set the encoding to
use, then you can do that too.

```pycon
>>> r.encoding = 'ISO-8859-1'
```

----------------------------------------------------------------------

=== [157] QuickStart > Binary Response Content ===
FILE: docs\quickstart.md:92-113

## Binary Response Content

The response content can also be accessed as bytes, for non-text responses:

```pycon
>>> r.content
b'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

Any `gzip` and `deflate` HTTP response encodings will automatically
be decoded for you. If `brotlipy` is installed, then the `brotli` response
encoding will be supported. If `zstandard` is installed, then `zstd`
response encodings will also be supported.

For example, to create an image from binary data returned by a request, you can use the following code:

```pycon
>>> from PIL import Image
>>> from io import BytesIO
>>> i = Image.open(BytesIO(r.content))
```

----------------------------------------------------------------------

=== [158] QuickStart > JSON Response Content ===
FILE: docs\quickstart.md:114-123

## JSON Response Content

Often Web API responses will be encoded as JSON.

```pycon
>>> r = httpx.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...' ...  }}]
```

----------------------------------------------------------------------

=== [159] QuickStart > Custom Headers ===
FILE: docs\quickstart.md:124-133

## Custom Headers

To include additional headers in the outgoing request, use the `headers` keyword argument:

```pycon
>>> url = 'https://httpbin.org/headers'
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> r = httpx.get(url, headers=headers)
```

----------------------------------------------------------------------

=== [160] QuickStart > Sending Form Encoded Data ===
FILE: docs\quickstart.md:134-171

## Sending Form Encoded Data

Some types of HTTP requests, such as `POST` and `PUT` requests, can include data
in the request body. One common way of including that is as form-encoded data,
which is used for HTML forms.

```pycon
>>> data = {'key1': 'value1', 'key2': 'value2'}
>>> r = httpx.post("https://httpbin.org/post", data=data)
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```

Form encoded data can also include multiple values from a given key.

```pycon
>>> data = {'key1': ['value1', 'value2']}
>>> r = httpx.post("https://httpbin.org/post", data=data)
>>> print(r.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
```

----------------------------------------------------------------------

=== [161] QuickStart > Sending Multipart File Uploads ===
FILE: docs\quickstart.md:172-226

## Sending Multipart File Uploads

You can also upload files, using HTTP multipart encoding:

```pycon
>>> with open('report.xls', 'rb') as report_file:
...     files = {'upload-file': report_file}
...     r = httpx.post("https://httpbin.org/post", files=files)
>>> print(r.text)
{
  ...
  "files": {
    "upload-file": "<... binary content ...>"
  },
  ...
}
```

You can also explicitly set the filename and content type, by using a tuple
of items for the file value:

```pycon
>>> with open('report.xls', 'rb') as report_file:
...     files = {'upload-file': ('report.xls', report_file, 'application/vnd.ms-excel')}
...     r = httpx.post("https://httpbin.org/post", files=files)
>>> print(r.text)
{
  ...
  "files": {
    "upload-file": "<... binary content ...>"
  },
  ...
}
```

If you need to include non-file data fields in the multipart form, use the `data=...` parameter:

```pycon
>>> data = {'message': 'Hello, world!'}
>>> with open('report.xls', 'rb') as report_file:
...     files = {'file': report_file}
...     r = httpx.post("https://httpbin.org/post", data=data, files=files)
>>> print(r.text)
{
  ...
  "files": {
    "file": "<... binary content ...>"
  },
  "form": {
    "message": "Hello, world!",
  },
  ...
}
```

----------------------------------------------------------------------

=== [162] QuickStart > Sending JSON Encoded Data ===
FILE: docs\quickstart.md:227-250

## Sending JSON Encoded Data

Form encoded data is okay if all you need is a simple key-value data structure.
For more complicated data structures you'll often want to use JSON encoding instead.

```pycon
>>> data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
>>> r = httpx.post("https://httpbin.org/post", json=data)
>>> print(r.text)
{
  ...
  "json": {
    "boolean": true,
    "integer": 123,
    "list": [
      "a",
      "b",
      "c"
    ]
  },
  ...
}
```

----------------------------------------------------------------------

=== [163] QuickStart > Sending Binary Request Data ===
FILE: docs\quickstart.md:251-263

## Sending Binary Request Data

For other encodings, you should use the `content=...` parameter, passing
either a `bytes` type or a generator that yields `bytes`.

```pycon
>>> content = b'Hello, world'
>>> r = httpx.post("https://httpbin.org/post", content=content)
```

You may also want to set a custom `Content-Type` header when uploading
binary data.

----------------------------------------------------------------------

=== [164] QuickStart > Response Status Codes ===
FILE: docs\quickstart.md:264-307

## Response Status Codes

We can inspect the HTTP status code of the response:

```pycon
>>> r = httpx.get('https://httpbin.org/get')
>>> r.status_code
200
```

HTTPX also includes an easy shortcut for accessing status codes by their text phrase.

```pycon
>>> r.status_code == httpx.codes.OK
True
```

We can raise an exception for any responses which are not a 2xx success code:

```pycon
>>> not_found = httpx.get('https://httpbin.org/status/404')
>>> not_found.status_code
404
>>> not_found.raise_for_status()
Traceback (most recent call last):
  File "/Users/tomchristie/GitHub/encode/httpcore/httpx/models.py", line 837, in raise_for_status
    raise HTTPStatusError(message, response=self)
httpx._exceptions.HTTPStatusError: 404 Client Error: Not Found for url: https://httpbin.org/status/404
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
```

Any successful response codes will return the `Response` instance rather than raising an exception.

```pycon
>>> r.raise_for_status()
```

The method returns the response instance, allowing you to use it inline. For example:

```pycon
>>> r = httpx.get('...').raise_for_status()
>>> data = httpx.get('...').raise_for_status().json()
```

----------------------------------------------------------------------

=== [165] QuickStart > Response Headers ===
FILE: docs\quickstart.md:308-338

## Response Headers

The response headers are available as a dictionary-like interface.

```pycon
>>> r.headers
Headers({
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
})
```

The `Headers` data type is case-insensitive, so you can use any capitalization.

```pycon
>>> r.headers['Content-Type']
'application/json'

>>> r.headers.get('content-type')
'application/json'
```

Multiple values for a single response header are represented as a single comma-separated value, as per [RFC 7230](https://tools.ietf.org/html/rfc7230#section-3.2):

> A recipient MAY combine multiple header fields with the same field name into one “field-name: field-value” pair, without changing the semantics of the message, by appending each subsequent field-value to the combined field value in order, separated by a comma.

----------------------------------------------------------------------

=== [166] QuickStart > Streaming Responses ===
FILE: docs\quickstart.md:339-386

## Streaming Responses

For large downloads you may want to use streaming responses that do not load the entire response body into memory at once.

You can stream the binary content of the response...

```pycon
>>> with httpx.stream("GET", "https://www.example.com") as r:
...     for data in r.iter_bytes():
...         print(data)
```

Or the text of the response...

```pycon
>>> with httpx.stream("GET", "https://www.example.com") as r:
...     for text in r.iter_text():
...         print(text)
```

Or stream the text, on a line-by-line basis...

```pycon
>>> with httpx.stream("GET", "https://www.example.com") as r:
...     for line in r.iter_lines():
...         print(line)
```

HTTPX will use universal line endings, normalising all cases to `\n`.

In some cases you might want to access the raw bytes on the response without applying any HTTP content decoding. In this case any content encoding that the web server has applied such as `gzip`, `deflate`, `brotli`, or `zstd` will
not be automatically decoded.

```pycon
>>> with httpx.stream("GET", "https://www.example.com") as r:
...     for chunk in r.iter_raw():
...         print(chunk)
```

If you're using streaming responses in any of these ways then the `response.content` and `response.text` attributes will not be available, and will raise errors if accessed. However you can also use the response streaming functionality to conditionally load the response body:

```pycon
>>> with httpx.stream("GET", "https://www.example.com") as r:
...     if int(r.headers['Content-Length']) < TOO_LONG:
...         r.read()
...         print(r.text)
```

----------------------------------------------------------------------

=== [167] QuickStart > Cookies ===
FILE: docs\quickstart.md:387-417

## Cookies

Any cookies that are set on the response can be easily accessed:

```pycon
>>> r = httpx.get('https://httpbin.org/cookies/set?chocolate=chip')
>>> r.cookies['chocolate']
'chip'
```

To include cookies in an outgoing request, use the `cookies` parameter:

```pycon
>>> cookies = {"peanut": "butter"}
>>> r = httpx.get('https://httpbin.org/cookies', cookies=cookies)
>>> r.json()
{'cookies': {'peanut': 'butter'}}
```

Cookies are returned in a `Cookies` instance, which is a dict-like data structure
with additional API for accessing cookies by their domain or path.

```pycon
>>> cookies = httpx.Cookies()
>>> cookies.set('cookie_on_domain', 'hello, there!', domain='httpbin.org')
>>> cookies.set('cookie_off_domain', 'nope.', domain='example.org')
>>> r = httpx.get('http://httpbin.org/cookies', cookies=cookies)
>>> r.json()
{'cookies': {'cookie_on_domain': 'hello, there!'}}
```

----------------------------------------------------------------------

=== [168] QuickStart > Redirection and History ===
FILE: docs\quickstart.md:418-450

## Redirection and History

By default, HTTPX will **not** follow redirects for all HTTP methods, although
this can be explicitly enabled.

For example, GitHub redirects all HTTP requests to HTTPS.

```pycon
>>> r = httpx.get('http://github.com/')
>>> r.status_code
301
>>> r.history
[]
>>> r.next_request
<Request('GET', 'https://github.com/')>
```

You can modify the default redirection handling with the `follow_redirects` parameter:

```pycon
>>> r = httpx.get('http://github.com/', follow_redirects=True)
>>> r.url
URL('https://github.com/')
>>> r.status_code
200
>>> r.history
[<Response [301 Moved Permanently]>]
```

The `history` property of the response can be used to inspect any followed redirects.
It contains a list of any redirect responses that were followed, in the order
in which they were made.

----------------------------------------------------------------------

=== [169] QuickStart > Timeouts ===
FILE: docs\quickstart.md:451-471

## Timeouts

HTTPX defaults to including reasonable timeouts for all network operations,
meaning that if a connection is not properly established then it should always
raise an error rather than hanging indefinitely.

The default timeout for network inactivity is five seconds. You can modify the
value to be more or less strict:

```pycon
>>> httpx.get('https://github.com/', timeout=0.001)
```

You can also disable the timeout behavior completely...

```pycon
>>> httpx.get('https://github.com/', timeout=None)
```

For advanced timeout management, see [Timeout fine-tuning](advanced/timeouts.md#fine-tuning-the-configuration).

----------------------------------------------------------------------

=== [170] QuickStart > Authentication ===
FILE: docs\quickstart.md:472-494

## Authentication

HTTPX supports Basic and Digest HTTP authentication.

To provide Basic authentication credentials, pass a 2-tuple of
plaintext `str` or `bytes` objects as the `auth` argument to the request
functions:

```pycon
>>> httpx.get("https://example.com", auth=("my_user", "password123"))
```

To provide credentials for Digest authentication you'll need to instantiate
a `DigestAuth` object with the plaintext username and password as arguments.
This object can be then passed as the `auth` argument to the request methods
as above:

```pycon
>>> auth = httpx.DigestAuth("my_user", "password123")
>>> httpx.get("https://example.com", auth=auth)
<Response [200 OK]>
```

----------------------------------------------------------------------

=== [171] QuickStart > Exceptions ===
FILE: docs\quickstart.md:495-547

## Exceptions

HTTPX will raise exceptions if an error occurs.

The most important exception classes in HTTPX are `RequestError` and `HTTPStatusError`.

The `RequestError` class is a superclass that encompasses any exception that occurs
while issuing an HTTP request. These exceptions include a `.request` attribute.

```python
try:
    response = httpx.get("https://www.example.com/")
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")
```

The `HTTPStatusError` class is raised by `response.raise_for_status()` on responses which are not a 2xx success code.
These exceptions include both a `.request` and a `.response` attribute.

```python
response = httpx.get("https://www.example.com/")
try:
    response.raise_for_status()
except httpx.HTTPStatusError as exc:
    print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
```

There is also a base class `HTTPError` that includes both of these categories, and can be used
to catch either failed requests, or 4xx and 5xx responses.

You can either use this base class to catch both categories...

```python
try:
    response = httpx.get("https://www.example.com/")
    response.raise_for_status()
except httpx.HTTPError as exc:
    print(f"Error while requesting {exc.request.url!r}.")
```

Or handle each case explicitly...

```python
try:
    response = httpx.get("https://www.example.com/")
    response.raise_for_status()
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")
except httpx.HTTPStatusError as exc:
    print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
```

For a full list of available exceptions, see [Exceptions (API Reference)](exceptions.md).

----------------------------------------------------------------------

=== [172] docs\third_party_packages.md ===
FILE: docs\third_party_packages.md:1-6

# Third Party Packages

As HTTPX usage grows, there is an expanding community of developers building tools and libraries that integrate with HTTPX, or depend on HTTPX. Here are some of them.

<!-- NOTE: Entries are alphabetised. -->

----------------------------------------------------------------------

=== [173] Third Party Packages > Plugins ===
FILE: docs\third_party_packages.md:7-74

## Plugins

### Hishel

[GitHub](https://github.com/karpetrosyan/hishel) - [Documentation](https://hishel.com/)

An elegant HTTP Cache implementation for HTTPX and HTTP Core.

### HTTPX-Auth

[GitHub](https://github.com/Colin-b/httpx_auth) - [Documentation](https://colin-b.github.io/httpx_auth/)

Provides authentication classes to be used with HTTPX's [authentication parameter](advanced/authentication.md#customizing-authentication).

### httpx-caching

[Github](https://github.com/johtso/httpx-caching)

This package adds caching functionality to HTTPX

### httpx-secure

[GitHub](https://github.com/Zaczero/httpx-secure)

Drop-in SSRF protection for httpx with DNS caching and custom validation support.

### httpx-socks

[GitHub](https://github.com/romis2012/httpx-socks)

Proxy (HTTP, SOCKS) transports for httpx.

### httpx-sse

[GitHub](https://github.com/florimondmanca/httpx-sse)

Allows consuming Server-Sent Events (SSE) with HTTPX.

### httpx-retries

[GitHub](https://github.com/will-ockmore/httpx-retries) - [Documentation](https://will-ockmore.github.io/httpx-retries/)

A retry layer for HTTPX.

### httpx-ws

[GitHub](https://github.com/frankie567/httpx-ws) - [Documentation](https://frankie567.github.io/httpx-ws/)

WebSocket support for HTTPX.

### pytest-HTTPX

[GitHub](https://github.com/Colin-b/pytest_httpx) - [Documentation](https://colin-b.github.io/pytest_httpx/)

Provides a [pytest](https://docs.pytest.org/en/latest/) fixture to mock HTTPX within test cases.

### RESPX

[GitHub](https://github.com/lundberg/respx) - [Documentation](https://lundberg.github.io/respx/)

A utility for mocking out HTTPX.

### rpc.py

[Github](https://github.com/abersheeran/rpc.py) - [Documentation](https://github.com/abersheeran/rpc.py#rpcpy)

A fast and powerful RPC framework based on ASGI/WSGI. Use HTTPX as the client of the RPC service.

----------------------------------------------------------------------

=== [174] Third Party Packages > Libraries with HTTPX support ===
FILE: docs\third_party_packages.md:75-100

## Libraries with HTTPX support

### Authlib

[GitHub](https://github.com/lepture/authlib) - [Documentation](https://docs.authlib.org/en/latest/)

A python library for building OAuth and OpenID Connect clients and servers. Includes an [OAuth HTTPX client](https://docs.authlib.org/en/latest/client/httpx.html).

### Gidgethub

[GitHub](https://github.com/brettcannon/gidgethub) - [Documentation](https://gidgethub.readthedocs.io/en/latest/index.html)

An asynchronous GitHub API library. Includes [HTTPX support](https://gidgethub.readthedocs.io/en/latest/httpx.html).

### httpdbg

[GitHub](https://github.com/cle-b/httpdbg) - [Documentation](https://httpdbg.readthedocs.io/)

A tool for python developers to easily debug the HTTP(S) client requests in a python program.

### VCR.py

[GitHub](https://github.com/kevin1024/vcrpy) - [Documentation](https://vcrpy.readthedocs.io/)

Record and repeat requests.

----------------------------------------------------------------------

=== [175] Third Party Packages > Gists ===
FILE: docs\third_party_packages.md:101-107

## Gists

### urllib3-transport

[GitHub](https://gist.github.com/florimondmanca/d56764d78d748eb9f73165da388e546e)

This public gist provides an example implementation for a [custom transport](advanced/transports.md#custom-transports) implementation on top of the battle-tested [`urllib3`](https://urllib3.readthedocs.io) library.

----------------------------------------------------------------------

=== [176] docs\troubleshooting.md ===
FILE: docs\troubleshooting.md:1-4

# Troubleshooting

This page lists some common problems or issues you could encounter while developing with HTTPX, as well as possible solutions.

----------------------------------------------------------------------

=== [177] Troubleshooting > Proxies ===
FILE: docs\troubleshooting.md:5-63

## Proxies

---

### "`The handshake operation timed out`" on HTTPS requests when using a proxy

**Description**: When using a proxy and making an HTTPS request, you see an exception looking like this:

```console
httpx.ProxyError: _ssl.c:1091: The handshake operation timed out
```

**Similar issues**: [encode/httpx#1412](https://github.com/encode/httpx/issues/1412), [encode/httpx#1433](https://github.com/encode/httpx/issues/1433)

**Resolution**: it is likely that you've set up your proxies like this...

```python
mounts = {
  "http://": httpx.HTTPTransport(proxy="http://myproxy.org"),
  "https://": httpx.HTTPTransport(proxy="https://myproxy.org"),
}
```

Using this setup, you're telling HTTPX to connect to the proxy using HTTP for HTTP requests, and using HTTPS for HTTPS requests.

But if you get the error above, it is likely that your proxy doesn't support connecting via HTTPS. Don't worry: that's a [common gotcha](advanced/proxies.md#http-proxies).

Change the scheme of your HTTPS proxy to `http://...` instead of `https://...`:

```python
mounts = {
  "http://": httpx.HTTPTransport(proxy="http://myproxy.org"),
  "https://": httpx.HTTPTransport(proxy="http://myproxy.org"),
}
```

This can be simplified to:

```python
proxy = "http://myproxy.org"
with httpx.Client(proxy=proxy) as client:
  ...
```

For more information, see [Proxies: FORWARD vs TUNNEL](advanced/proxies.md#forward-vs-tunnel).

---

### Error when making requests to an HTTPS proxy

**Description**: your proxy _does_ support connecting via HTTPS, but you are seeing errors along the lines of...

```console
httpx.ProxyError: [SSL: PRE_MAC_LENGTH_TOO_LONG] invalid alert (_ssl.c:1091)
```

**Similar issues**: [encode/httpx#1424](https://github.com/encode/httpx/issues/1424).

**Resolution**: HTTPX does not properly support HTTPS proxies at this time. If that's something you're interested in having, please see [encode/httpx#1434](https://github.com/encode/httpx/issues/1434) and consider lending a hand there.

----------------------------------------------------------------------

=== [178] docs\advanced\authentication.md ===
FILE: docs\advanced\authentication.md:1-16

Authentication can either be included on a per-request basis...

```pycon
>>> auth = httpx.BasicAuth(username="username", password="secret")
>>> client = httpx.Client()
>>> response = client.get("https://www.example.com/", auth=auth)
```

Or configured on the client instance, ensuring that all outgoing requests will include authentication credentials...

```pycon
>>> auth = httpx.BasicAuth(username="username", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://www.example.com/")
```

----------------------------------------------------------------------

=== [179] Basic authentication ===
FILE: docs\advanced\authentication.md:17-28

## Basic authentication

HTTP basic authentication is an unencrypted authentication scheme that uses a simple encoding of the username and password in the request `Authorization` header. Since it is unencrypted it should typically only be used over `https`, although this is not strictly enforced.

```pycon
>>> auth = httpx.BasicAuth(username="finley", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://httpbin.org/basic-auth/finley/secret")
>>> response
<Response [200 OK]>
```

----------------------------------------------------------------------

=== [180] Digest authentication ===
FILE: docs\advanced\authentication.md:29-42

## Digest authentication

HTTP digest authentication is a challenge-response authentication scheme. Unlike basic authentication it provides encryption, and can be used over unencrypted `http` connections. It requires an additional round-trip in order to negotiate the authentication. 

```pycon
>>> auth = httpx.DigestAuth(username="olivia", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://httpbin.org/digest-auth/auth/olivia/secret")
>>> response
<Response [200 OK]>
>>> response.history
[<Response [401 UNAUTHORIZED]>]
```

----------------------------------------------------------------------

=== [181] NetRC authentication ===
FILE: docs\advanced\authentication.md:43-86

## NetRC authentication

HTTPX can be configured to use [a `.netrc` config file](https://everything.curl.dev/usingcurl/netrc) for authentication.

The `.netrc` config file allows authentication credentials to be associated with specified hosts. When a request is made to a host that is found in the netrc file, the username and password will be included using HTTP basic authentication.

Example `.netrc` file:

```
machine example.org
login example-username
password example-password

machine python-httpx.org
login other-username
password other-password
```

Some examples of configuring `.netrc` authentication with `httpx`.

Use the default `.netrc` file in the users home directory:

```pycon
>>> auth = httpx.NetRCAuth()
>>> client = httpx.Client(auth=auth)
```

Use an explicit path to a `.netrc` file:

```pycon
>>> auth = httpx.NetRCAuth(file="/path/to/.netrc")
>>> client = httpx.Client(auth=auth)
```

Use the `NETRC` environment variable to configure a path to the `.netrc` file,
or fallback to the default.

```pycon
>>> auth = httpx.NetRCAuth(file=os.environ.get("NETRC"))
>>> client = httpx.Client(auth=auth)
```

The `NetRCAuth()` class uses [the `netrc.netrc()` function from the Python standard library](https://docs.python.org/3/library/netrc.html). See the documentation there for more details on exceptions that may be raised if the `.netrc` file is not found, or cannot be parsed.

----------------------------------------------------------------------

=== [182] Custom authentication schemes ===
FILE: docs\advanced\authentication.md:87-232

## Custom authentication schemes

When issuing requests or instantiating a client, the `auth` argument can be used to pass an authentication scheme to use. The `auth` argument may be one of the following...

* A two-tuple of `username`/`password`, to be used with basic authentication.
* An instance of `httpx.BasicAuth()`, `httpx.DigestAuth()`, or `httpx.NetRCAuth()`.
* A callable, accepting a request and returning an authenticated request instance.
* An instance of subclasses of `httpx.Auth`.

The most involved of these is the last, which allows you to create authentication flows involving one or more requests. A subclass of `httpx.Auth` should implement `def auth_flow(request)`, and yield any requests that need to be made...

```python
class MyCustomAuth(httpx.Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        # Send the request, with a custom `X-Authentication` header.
        request.headers['X-Authentication'] = self.token
        yield request
```

If the auth flow requires more than one request, you can issue multiple yields, and obtain the response in each case...

```python
class MyCustomAuth(httpx.Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
      response = yield request
      if response.status_code == 401:
          # If the server issues a 401 response then resend the request,
          # with a custom `X-Authentication` header.
          request.headers['X-Authentication'] = self.token
          yield request
```

Custom authentication classes are designed to not perform any I/O, so that they may be used with both sync and async client instances. If you are implementing an authentication scheme that requires the request body, then you need to indicate this on the class using a `requires_request_body` property.

You will then be able to access `request.content` inside the `.auth_flow()` method.

```python
class MyCustomAuth(httpx.Auth):
    requires_request_body = True

    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
      response = yield request
      if response.status_code == 401:
          # If the server issues a 401 response then resend the request,
          # with a custom `X-Authentication` header.
          request.headers['X-Authentication'] = self.sign_request(...)
          yield request

    def sign_request(self, request):
        # Create a request signature, based on `request.method`, `request.url`,
        # `request.headers`, and `request.content`.
        ...
```

Similarly, if you are implementing a scheme that requires access to the response body, then use the `requires_response_body` property.   You will then be able to access response body properties and methods such as `response.content`, `response.text`, `response.json()`, etc.

```python
class MyCustomAuth(httpx.Auth):
    requires_response_body = True

    def __init__(self, access_token, refresh_token, refresh_url):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_url = refresh_url

    def auth_flow(self, request):
        request.headers["X-Authentication"] = self.access_token
        response = yield request

        if response.status_code == 401:
            # If the server issues a 401 response, then issue a request to
            # refresh tokens, and resend the request.
            refresh_response = yield self.build_refresh_request()
            self.update_tokens(refresh_response)

            request.headers["X-Authentication"] = self.access_token
            yield request

    def build_refresh_request(self):
        # Return an `httpx.Request` for refreshing tokens.
        ...

    def update_tokens(self, response):
        # Update the `.access_token` and `.refresh_token` tokens
        # based on a refresh response.
        data = response.json()
        ...
```

If you _do_ need to perform I/O other than HTTP requests, such as accessing a disk-based cache, or you need to use concurrency primitives, such as locks, then you should override `.sync_auth_flow()` and `.async_auth_flow()` (instead of `.auth_flow()`). The former will be used by `httpx.Client`, while the latter will be used by `httpx.AsyncClient`.

```python
import asyncio
import threading
import httpx


class MyCustomAuth(httpx.Auth):
    def __init__(self):
        self._sync_lock = threading.RLock()
        self._async_lock = asyncio.Lock()

    def sync_get_token(self):
        with self._sync_lock:
            ...

    def sync_auth_flow(self, request):
        token = self.sync_get_token()
        request.headers["Authorization"] = f"Token {token}"
        yield request

    async def async_get_token(self):
        async with self._async_lock:
            ...

    async def async_auth_flow(self, request):
        token = await self.async_get_token()
        request.headers["Authorization"] = f"Token {token}"
        yield request
```

If you only want to support one of the two methods, then you should still override it, but raise an explicit `RuntimeError`.

```python
import httpx
import sync_only_library


class MyCustomAuth(httpx.Auth):
    def sync_auth_flow(self, request):
        token = sync_only_library.get_token(...)
        request.headers["Authorization"] = f"Token {token}"
        yield request

    async def async_auth_flow(self, request):
        raise RuntimeError("Cannot use a sync authentication class with httpx.AsyncClient")
```

----------------------------------------------------------------------

=== [183] docs\advanced\clients.md ===
FILE: docs\advanced\clients.md:1-3

!!! hint
    If you are coming from Requests, `httpx.Client()` is what you can use instead of `requests.Session()`.

----------------------------------------------------------------------

=== [184] Why use a Client? ===
FILE: docs\advanced\clients.md:4-31

## Why use a Client?

!!! note "TL;DR"
    If you do anything more than experimentation, one-off scripts, or prototypes, then you should use a `Client` instance.

**More efficient usage of network resources**

When you make requests using the top-level API as documented in the [Quickstart](../quickstart.md) guide, HTTPX has to establish a new connection _for every single request_ (connections are not reused). As the number of requests to a host increases, this quickly becomes inefficient.

On the other hand, a `Client` instance uses [HTTP connection pooling](https://en.wikipedia.org/wiki/HTTP_persistent_connection). This means that when you make several requests to the same host, the `Client` will reuse the underlying TCP connection, instead of recreating one for every single request.

This can bring **significant performance improvements** compared to using the top-level API, including:

- Reduced latency across requests (no handshaking).
- Reduced CPU usage and round-trips.
- Reduced network congestion.

**Extra features**

`Client` instances also support features that aren't available at the top-level API, such as:

- Cookie persistence across requests.
- Applying configuration across all outgoing requests.
- Sending requests through HTTP proxies.
- Using [HTTP/2](../http2.md).

The other sections on this page go into further detail about what you can do with a `Client` instance.

----------------------------------------------------------------------

=== [185] Usage ===
FILE: docs\advanced\clients.md:32-50

## Usage

The recommended way to use a `Client` is as a context manager. This will ensure that connections are properly cleaned up when leaving the `with` block:

```python
with httpx.Client() as client:
    ...
```

Alternatively, you can explicitly close the connection pool without block-usage using `.close()`:

```python
client = httpx.Client()
try:
    ...
finally:
    client.close()
```

----------------------------------------------------------------------

=== [186] Making requests ===
FILE: docs\advanced\clients.md:51-75

## Making requests

Once you have a `Client`, you can send requests using `.get()`, `.post()`, etc. For example:

```pycon
>>> with httpx.Client() as client:
...     r = client.get('https://example.com')
...
>>> r
<Response [200 OK]>
```

These methods accept the same arguments as `httpx.get()`, `httpx.post()`, etc. This means that all features documented in the [Quickstart](../quickstart.md) guide are also available at the client level.

For example, to send a request with custom headers:

```pycon
>>> with httpx.Client() as client:
...     headers = {'X-Custom': 'value'}
...     r = client.get('https://example.com', headers=headers)
...
>>> r.request.headers['X-Custom']
'value'
```

----------------------------------------------------------------------

=== [187] Sharing configuration across requests ===
FILE: docs\advanced\clients.md:76-91

## Sharing configuration across requests

Clients allow you to apply configuration to all outgoing requests by passing parameters to the `Client` constructor.

For example, to apply a set of custom headers _on every request_:

```pycon
>>> url = 'http://httpbin.org/headers'
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> with httpx.Client(headers=headers) as client:
...     r = client.get(url)
...
>>> r.json()['headers']['User-Agent']
'my-app/0.0.1'
```

----------------------------------------------------------------------

=== [188] Merging of configuration ===
FILE: docs\advanced\clients.md:92-127

## Merging of configuration

When a configuration option is provided at both the client-level and request-level, one of two things can happen:

- For headers, query parameters and cookies, the values are combined together. For example:

```pycon
>>> headers = {'X-Auth': 'from-client'}
>>> params = {'client_id': 'client1'}
>>> with httpx.Client(headers=headers, params=params) as client:
...     headers = {'X-Custom': 'from-request'}
...     params = {'request_id': 'request1'}
...     r = client.get('https://example.com', headers=headers, params=params)
...
>>> r.request.url
URL('https://example.com?client_id=client1&request_id=request1')
>>> r.request.headers['X-Auth']
'from-client'
>>> r.request.headers['X-Custom']
'from-request'
```

- For all other parameters, the request-level value takes priority. For example:

```pycon
>>> with httpx.Client(auth=('tom', 'mot123')) as client:
...     r = client.get('https://example.com', auth=('alice', 'ecila123'))
...
>>> _, _, auth = r.request.headers['Authorization'].partition(' ')
>>> import base64
>>> base64.b64decode(auth)
b'alice:ecila123'
```

If you need finer-grained control on the merging of client-level and request-level parameters, see [Request instances](#request-instances).

----------------------------------------------------------------------

=== [189] Other Client-only configuration options ===
FILE: docs\advanced\clients.md:128-145

## Other Client-only configuration options

Additionally, `Client` accepts some configuration options that aren't available at the request level.

For example, `base_url` allows you to prepend an URL to all outgoing requests:

```pycon
>>> with httpx.Client(base_url='http://httpbin.org') as client:
...     r = client.get('/headers')
...
>>> r.request.url
URL('http://httpbin.org/headers')
```

For a list of all available client parameters, see the [`Client`](../api.md#client) API reference.

---

----------------------------------------------------------------------

=== [190] Request instances ===
FILE: docs\advanced\clients.md:146-178

## Request instances

For maximum control on what gets sent over the wire, HTTPX supports building explicit [`Request`](../api.md#request) instances:

```python
request = httpx.Request("GET", "https://example.com")
```

To dispatch a `Request` instance across to the network, create a [`Client` instance](#client-instances) and use `.send()`:

```python
with httpx.Client() as client:
    response = client.send(request)
    ...
```

If you need to mix client-level and request-level options in a way that is not supported by the default [Merging of parameters](#merging-of-parameters), you can use `.build_request()` and then make arbitrary modifications to the `Request` instance. For example:

```python
headers = {"X-Api-Key": "...", "X-Client-ID": "ABC123"}

with httpx.Client(headers=headers) as client:
    request = client.build_request("GET", "https://api.example.com")

    print(request.headers["X-Client-ID"])  # "ABC123"

    # Don't send the API key for this particular request.
    del request.headers["X-Api-Key"]

    response = client.send(request)
    ...
```

----------------------------------------------------------------------

=== [191] Monitoring download progress ===
FILE: docs\advanced\clients.md:179-233

## Monitoring download progress

If you need to monitor download progress of large responses, you can use response streaming and inspect the `response.num_bytes_downloaded` property.

This interface is required for properly determining download progress, because the total number of bytes returned by `response.content` or `response.iter_content()` will not always correspond with the raw content length of the response if HTTP response compression is being used.

For example, showing a progress bar using the [`tqdm`](https://github.com/tqdm/tqdm) library while a response is being downloaded could be done like this…

```python
import tempfile

import httpx
from tqdm import tqdm

with tempfile.NamedTemporaryFile() as download_file:
    url = "https://speed.hetzner.de/100MB.bin"
    with httpx.stream("GET", url) as response:
        total = int(response.headers["Content-Length"])

        with tqdm(total=total, unit_scale=True, unit_divisor=1024, unit="B") as progress:
            num_bytes_downloaded = response.num_bytes_downloaded
            for chunk in response.iter_bytes():
                download_file.write(chunk)
                progress.update(response.num_bytes_downloaded - num_bytes_downloaded)
                num_bytes_downloaded = response.num_bytes_downloaded
```

![tqdm progress bar](../img/tqdm-progress.gif)

Or an alternate example, this time using the [`rich`](https://github.com/willmcgugan/rich) library…

```python
import tempfile
import httpx
import rich.progress

with tempfile.NamedTemporaryFile() as download_file:
    url = "https://speed.hetzner.de/100MB.bin"
    with httpx.stream("GET", url) as response:
        total = int(response.headers["Content-Length"])

        with rich.progress.Progress(
            "[progress.percentage]{task.percentage:>3.0f}%",
            rich.progress.BarColumn(bar_width=None),
            rich.progress.DownloadColumn(),
            rich.progress.TransferSpeedColumn(),
        ) as progress:
            download_task = progress.add_task("Download", total=total)
            for chunk in response.iter_bytes():
                download_file.write(chunk)
                progress.update(download_task, completed=response.num_bytes_downloaded)
```

![rich progress bar](../img/rich-progress.gif)

----------------------------------------------------------------------

=== [192] Monitoring upload progress ===
FILE: docs\advanced\clients.md:234-265

## Monitoring upload progress

If you need to monitor upload progress of large responses, you can use request content generator streaming.

For example, showing a progress bar using the [`tqdm`](https://github.com/tqdm/tqdm) library.

```python
import io
import random

import httpx
from tqdm import tqdm


def gen():
    """
    this is a complete example with generated random bytes.
    you can replace `io.BytesIO` with real file object.
    """
    total = 32 * 1024 * 1024  # 32m
    with tqdm(ascii=True, unit_scale=True, unit='B', unit_divisor=1024, total=total) as bar:
        with io.BytesIO(random.randbytes(total)) as f:
            while data := f.read(1024):
                yield data
                bar.update(len(data))


httpx.post("https://httpbin.org/post", content=gen())
```

![tqdm progress bar](../img/tqdm-progress.gif)

----------------------------------------------------------------------

=== [193] Multipart file encoding ===
FILE: docs\advanced\clients.md:266-328

## Multipart file encoding

As mentioned in the [quickstart](../quickstart.md#sending-multipart-file-uploads)
multipart file encoding is available by passing a dictionary with the
name of the payloads as keys and either tuple of elements or a file-like object or a string as values.

```pycon
>>> with open('report.xls', 'rb') as report_file:
...     files = {'upload-file': ('report.xls', report_file, 'application/vnd.ms-excel')}
...     r = httpx.post("https://httpbin.org/post", files=files)
>>> print(r.text)
{
  ...
  "files": {
    "upload-file": "<... binary content ...>"
  },
  ...
}
```

More specifically, if a tuple is used as a value, it must have between 2 and 3 elements:

- The first element is an optional file name which can be set to `None`.
- The second element may be a file-like object or a string which will be automatically
encoded in UTF-8.
- An optional third element can be used to specify the
[MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_Types)
of the file being uploaded. If not specified HTTPX will attempt to guess the MIME type based
on the file name, with unknown file extensions defaulting to "application/octet-stream".
If the file name is explicitly set to `None` then HTTPX will not include a content-type
MIME header field.

```pycon
>>> files = {'upload-file': (None, 'text content', 'text/plain')}
>>> r = httpx.post("https://httpbin.org/post", files=files)
>>> print(r.text)
{
  ...
  "files": {},
  "form": {
    "upload-file": "text-content"
  },
  ...
}
```

!!! tip
    It is safe to upload large files this way. File uploads are streaming by default, meaning that only one chunk will be loaded into memory at a time.

 Non-file data fields can be included in the multipart form using by passing them to `data=...`.

You can also send multiple files in one go with a multiple file field form.
To do that, pass a list of `(field, <file>)` items instead of a dictionary, allowing you to pass multiple items with the same `field`.
For instance this request sends 2 files, `foo.png` and `bar.png` in one request on the `images` form field:

```pycon
>>> with open('foo.png', 'rb') as foo_file, open('bar.png', 'rb') as bar_file:
...     files = [
...         ('images', ('foo.png', foo_file, 'image/png')),
...         ('images', ('bar.png', bar_file, 'image/png')),
...     ]
...     r = httpx.post("https://httpbin.org/post", files=files)
```

----------------------------------------------------------------------

=== [194] docs\advanced\event-hooks.md ===
FILE: docs\advanced\event-hooks.md:1-65

HTTPX allows you to register "event hooks" with the client, that are called
every time a particular type of event takes place.

There are currently two event hooks:

* `request` - Called after a request is fully prepared, but before it is sent to the network. Passed the `request` instance.
* `response` - Called after the response has been fetched from the network, but before it is returned to the caller. Passed the `response` instance.

These allow you to install client-wide functionality such as logging, monitoring or tracing.

```python
def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = httpx.Client(event_hooks={'request': [log_request], 'response': [log_response]})
```

You can also use these hooks to install response processing code, such as this
example, which creates a client instance that always raises `httpx.HTTPStatusError`
on 4xx and 5xx responses.

```python
def raise_on_4xx_5xx(response):
    response.raise_for_status()

client = httpx.Client(event_hooks={'response': [raise_on_4xx_5xx]})
```

!!! note
    Response event hooks are called before determining if the response body
    should be read or not.

    If you need access to the response body inside an event hook, you'll
    need to call `response.read()`, or for AsyncClients, `response.aread()`.

The hooks are also allowed to modify `request` and `response` objects.

```python
def add_timestamp(request):
    request.headers['x-request-timestamp'] = datetime.now(tz=datetime.utc).isoformat()

client = httpx.Client(event_hooks={'request': [add_timestamp]})
```

Event hooks must always be set as a **list of callables**, and you may register
multiple event hooks for each type of event.

As well as being able to set event hooks on instantiating the client, there
is also an `.event_hooks` property, that allows you to inspect and modify
the installed hooks.

```python
client = httpx.Client()
client.event_hooks['request'] = [log_request]
client.event_hooks['response'] = [log_response, raise_on_4xx_5xx]
```

!!! note
    If you are using HTTPX's async support, then you need to be aware that
    hooks registered with `httpx.AsyncClient` MUST be async functions,
    rather than plain functions.

----------------------------------------------------------------------

=== [195] docs\advanced\extensions.md ===
FILE: docs\advanced\extensions.md:1-31

# Extensions

Request and response extensions provide a untyped space where additional information may be added.

Extensions should be used for features that may not be available on all transports, and that do not fit neatly into [the simplified request/response model](https://www.encode.io/httpcore/extensions/) that the underlying `httpcore` package uses as its API.

Several extensions are supported on the request:

```python
# Request timeouts actually implemented as an extension on
# the request, ensuring that they are passed throughout the
# entire call stack.
client = httpx.Client()
response = client.get(
    "https://www.example.com",
    extensions={"timeout": {"connect": 5.0}}
)
response.request.extensions["timeout"]
{"connect": 5.0}
```

And on the response:

```python
client = httpx.Client()
response = client.get("https://www.example.com")
print(response.extensions["http_version"])  # b"HTTP/1.1"
# Other server responses could have been
# b"HTTP/0.9", b"HTTP/1.0", or b"HTTP/1.1"
```

----------------------------------------------------------------------

=== [196] Extensions > Request Extensions ===
FILE: docs\advanced\extensions.md:32-181

## Request Extensions

### `"trace"`

The trace extension allows a callback handler to be installed to monitor the internal
flow of events within the underlying `httpcore` transport.

The simplest way to explain this is with an example:

```python
import httpx

def log(event_name, info):
    print(event_name, info)

client = httpx.Client()
response = client.get("https://www.example.com/", extensions={"trace": log})
# connection.connect_tcp.started {'host': 'www.example.com', 'port': 443, 'local_address': None, 'timeout': None}
# connection.connect_tcp.complete {'return_value': <httpcore.backends.sync.SyncStream object at 0x1093f94d0>}
# connection.start_tls.started {'ssl_context': <ssl.SSLContext object at 0x1093ee750>, 'server_hostname': b'www.example.com', 'timeout': None}
# connection.start_tls.complete {'return_value': <httpcore.backends.sync.SyncStream object at 0x1093f9450>}
# http11.send_request_headers.started {'request': <Request [b'GET']>}
# http11.send_request_headers.complete {'return_value': None}
# http11.send_request_body.started {'request': <Request [b'GET']>}
# http11.send_request_body.complete {'return_value': None}
# http11.receive_response_headers.started {'request': <Request [b'GET']>}
# http11.receive_response_headers.complete {'return_value': (b'HTTP/1.1', 200, b'OK', [(b'Age', b'553715'), (b'Cache-Control', b'max-age=604800'), (b'Content-Type', b'text/html; charset=UTF-8'), (b'Date', b'Thu, 21 Oct 2021 17:08:42 GMT'), (b'Etag', b'"3147526947+ident"'), (b'Expires', b'Thu, 28 Oct 2021 17:08:42 GMT'), (b'Last-Modified', b'Thu, 17 Oct 2019 07:18:26 GMT'), (b'Server', b'ECS (nyb/1DCD)'), (b'Vary', b'Accept-Encoding'), (b'X-Cache', b'HIT'), (b'Content-Length', b'1256')])}
# http11.receive_response_body.started {'request': <Request [b'GET']>}
# http11.receive_response_body.complete {'return_value': None}
# http11.response_closed.started {}
# http11.response_closed.complete {'return_value': None}
```

The `event_name` and `info` arguments here will be one of the following:

* `{event_type}.{event_name}.started`, `<dictionary of keyword arguments>`
* `{event_type}.{event_name}.complete`, `{"return_value": <...>}`
* `{event_type}.{event_name}.failed`, `{"exception": <...>}`

Note that when using async code the handler function passed to `"trace"` must be an `async def ...` function.

The following event types are currently exposed...

**Establishing the connection**

* `"connection.connect_tcp"`
* `"connection.connect_unix_socket"`
* `"connection.start_tls"`

**HTTP/1.1 events**

* `"http11.send_request_headers"`
* `"http11.send_request_body"`
* `"http11.receive_response"`
* `"http11.receive_response_body"`
* `"http11.response_closed"`

**HTTP/2 events**

* `"http2.send_connection_init"`
* `"http2.send_request_headers"`
* `"http2.send_request_body"`
* `"http2.receive_response_headers"`
* `"http2.receive_response_body"`
* `"http2.response_closed"`

The exact set of trace events may be subject to change across different versions of `httpcore`. If you need to rely on a particular set of events it is recommended that you pin installation of the package to a fixed version.

### `"sni_hostname"`

The server's hostname, which is used to confirm the hostname supplied by the SSL certificate.

If you want to connect to an explicit IP address rather than using the standard DNS hostname lookup, then you'll need to use this request extension.

For example:

``` python
# Connect to '185.199.108.153' but use 'www.encode.io' in the Host header,
# and use 'www.encode.io' when SSL verifying the server hostname.
client = httpx.Client()
headers = {"Host": "www.encode.io"}
extensions = {"sni_hostname": "www.encode.io"}
response = client.get(
    "https://185.199.108.153/path",
    headers=headers,
    extensions=extensions
)
```

### `"timeout"`

A dictionary of `str: Optional[float]` timeout values.

May include values for `'connect'`, `'read'`, `'write'`, or `'pool'`.

For example:

```python
# Timeout if a connection takes more than 5 seconds to established, or if
# we are blocked waiting on the connection pool for more than 10 seconds.
client = httpx.Client()
response = client.get(
    "https://www.example.com",
    extensions={"timeout": {"connect": 5.0, "pool": 10.0}}
)
```

This extension is how the `httpx` timeouts are implemented, ensuring that the timeout values are associated with the request instance and passed throughout the stack. You shouldn't typically be working with this extension directly, but use the higher level `timeout` API instead.

### `"target"`

The target that is used as [the HTTP target instead of the URL path](https://datatracker.ietf.org/doc/html/rfc2616#section-5.1.2).

This enables support constructing requests that would otherwise be unsupported.

* URL paths with non-standard escaping applied.
* Forward proxy requests using an absolute URI.
* Tunneling proxy requests using `CONNECT` with hostname as the target.
* Server-wide `OPTIONS *` requests.

Some examples:

Using the 'target' extension to send requests without the standard path escaping rules...

```python
# Typically a request to "https://www.example.com/test^path" would
# connect to "www.example.com" and send an HTTP/1.1 request like...
#
# GET /test%5Epath HTTP/1.1
#
# Using the target extension we can include the literal '^'...
#
# GET /test^path HTTP/1.1
#
# Note that requests must still be valid HTTP requests.
# For example including whitespace in the target will raise a `LocalProtocolError`.
extensions = {"target": b"/test^path"}
response = httpx.get("https://www.example.com", extensions=extensions)
```

The `target` extension also allows server-wide `OPTIONS *` requests to be constructed...

```python
# This will send the following request...
#
# CONNECT * HTTP/1.1
extensions = {"target": b"*"}
response = httpx.request("CONNECT", "https://www.example.com", extensions=extensions)
```

----------------------------------------------------------------------

=== [197] Extensions > Response Extensions ===
FILE: docs\advanced\extensions.md:182-242

## Response Extensions

### `"http_version"`

The HTTP version, as bytes. Eg. `b"HTTP/1.1"`.

When using HTTP/1.1 the response line includes an explicit version, and the value of this key could feasibly be one of `b"HTTP/0.9"`, `b"HTTP/1.0"`, or `b"HTTP/1.1"`.

When using HTTP/2 there is no further response versioning included in the protocol, and the value of this key will always be `b"HTTP/2"`.

### `"reason_phrase"`

The reason-phrase of the HTTP response, as bytes. For example `b"OK"`. Some servers may include a custom reason phrase, although this is not recommended.

HTTP/2 onwards does not include a reason phrase on the wire.

When no key is included, a default based on the status code may be used.

### `"stream_id"`

When HTTP/2 is being used the `"stream_id"` response extension can be accessed to determine the ID of the data stream that the response was sent on.

### `"network_stream"`

The `"network_stream"` extension allows developers to handle HTTP `CONNECT` and `Upgrade` requests, by providing an API that steps outside the standard request/response model, and can directly read or write to the network.

The interface provided by the network stream:

* `read(max_bytes, timeout = None) -> bytes`
* `write(buffer, timeout = None)`
* `close()`
* `start_tls(ssl_context, server_hostname = None, timeout = None) -> NetworkStream`
* `get_extra_info(info) -> Any`

This API can be used as the foundation for working with HTTP proxies, WebSocket upgrades, and other advanced use-cases.

See the [network backends documentation](https://www.encode.io/httpcore/network-backends/) for more information on working directly with network streams.

**Extra network information**

The network stream abstraction also allows access to various low-level information that may be exposed by the underlying socket:

```python
response = httpx.get("https://www.example.com")
network_stream = response.extensions["network_stream"]

client_addr = network_stream.get_extra_info("client_addr")
server_addr = network_stream.get_extra_info("server_addr")
print("Client address", client_addr)
print("Server address", server_addr)
```

The socket SSL information is also available through this interface, although you need to ensure that the underlying connection is still open, in order to access it...

```python
with httpx.stream("GET", "https://www.example.com") as response:
    network_stream = response.extensions["network_stream"]

    ssl_object = network_stream.get_extra_info("ssl_object")
    print("TLS version", ssl_object.version())
```

----------------------------------------------------------------------

=== [198] docs\advanced\proxies.md ===
FILE: docs\advanced\proxies.md:1-7

HTTPX supports setting up [HTTP proxies](https://en.wikipedia.org/wiki/Proxy_server#Web_proxy_servers) via the `proxy` parameter to be passed on client initialization or top-level API functions like `httpx.get(..., proxy=...)`.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Open_proxy_h2g2bob.svg/480px-Open_proxy_h2g2bob.svg.png"/>
    <figcaption><em>Diagram of how a proxy works (source: Wikipedia). The left hand side "Internet" blob may be your HTTPX client requesting <code>example.com</code> through a proxy.</em></figcaption>
</div>

----------------------------------------------------------------------

=== [199] HTTP Proxies ===
FILE: docs\advanced\proxies.md:8-37

## HTTP Proxies

To route all traffic (HTTP and HTTPS) to a proxy located at `http://localhost:8030`, pass the proxy URL to the client...

```python
with httpx.Client(proxy="http://localhost:8030") as client:
    ...
```

For more advanced use cases, pass a mounts `dict`. For example, to route HTTP and HTTPS requests to 2 different proxies, respectively located at `http://localhost:8030`, and `http://localhost:8031`, pass a `dict` of proxy URLs:

```python
proxy_mounts = {
    "http://": httpx.HTTPTransport(proxy="http://localhost:8030"),
    "https://": httpx.HTTPTransport(proxy="http://localhost:8031"),
}

with httpx.Client(mounts=proxy_mounts) as client:
    ...
```

For detailed information about proxy routing, see the [Routing](#routing) section.

!!! tip "Gotcha"
    In most cases, the proxy URL for the `https://` key _should_ use the `http://` scheme (that's not a typo!).

    This is because HTTP proxying requires initiating a connection with the proxy server. While it's possible that your proxy supports doing it via HTTPS, most proxies only support doing it via HTTP.

    For more information, see [FORWARD vs TUNNEL](#forward-vs-tunnel).

----------------------------------------------------------------------

=== [200] Authentication ===
FILE: docs\advanced\proxies.md:38-46

## Authentication

Proxy credentials can be passed as the `userinfo` section of the proxy URL. For example:

```python
with httpx.Client(proxy="http://username:password@localhost:8030") as client:
    ...
```

----------------------------------------------------------------------

=== [201] Proxy mechanisms ===
FILE: docs\advanced\proxies.md:47-67

## Proxy mechanisms

!!! note
    This section describes **advanced** proxy concepts and functionality.

### FORWARD vs TUNNEL

In general, the flow for making an HTTP request through a proxy is as follows:

1. The client connects to the proxy (initial connection request).
2. The proxy transfers data to the server on your behalf.

How exactly step 2/ is performed depends on which of two proxying mechanisms is used:

* **Forwarding**: the proxy makes the request for you, and sends back the response it obtained from the server.
* **Tunnelling**: the proxy establishes a TCP connection to the server on your behalf, and the client reuses this connection to send the request and receive the response. This is known as an [HTTP Tunnel](https://en.wikipedia.org/wiki/HTTP_tunnel). This mechanism is how you can access websites that use HTTPS from an HTTP proxy (the client "upgrades" the connection to HTTPS by performing the TLS handshake with the server over the TCP connection provided by the proxy).

### Troubleshooting proxies

If you encounter issues when setting up proxies, please refer to our [Troubleshooting guide](../troubleshooting.md#proxies).

----------------------------------------------------------------------

=== [202] SOCKS ===
FILE: docs\advanced\proxies.md:68-83

## SOCKS

In addition to HTTP proxies, `httpcore` also supports proxies using the SOCKS protocol.
This is an optional feature that requires an additional third-party library be installed before use.

You can install SOCKS support using `pip`:

```shell
$ pip install httpx[socks]
```

You can now configure a client to make requests via a proxy using the SOCKS protocol:

```python
httpx.Client(proxy='socks5://user:pass@host:port')
```

----------------------------------------------------------------------

=== [203] docs\advanced\resource-limits.md ===
FILE: docs\advanced\resource-limits.md:1-13

You can control the connection pool size using the `limits` keyword
argument on the client. It takes instances of `httpx.Limits` which define:

- `max_keepalive_connections`, number of allowable keep-alive connections, or `None` to always
allow. (Defaults 20)
- `max_connections`, maximum number of allowable connections, or `None` for no limits.
(Default 100)
- `keepalive_expiry`, time limit on idle keep-alive connections in seconds, or `None` for no limits. (Default 5)

```python
limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
client = httpx.Client(limits=limits)
```

----------------------------------------------------------------------

=== [204] docs\advanced\ssl.md ===
FILE: docs\advanced\ssl.md:1-89

When making a request over HTTPS, HTTPX needs to verify the identity of the requested host. To do this, it uses a bundle of SSL certificates (a.k.a. CA bundle) delivered by a trusted certificate authority (CA).

### Enabling and disabling verification

By default httpx will verify HTTPS connections, and raise an error for invalid SSL cases...

```pycon
>>> httpx.get("https://expired.badssl.com/")
httpx.ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:997)
```

You can disable SSL verification completely and allow insecure requests...

```pycon
>>> httpx.get("https://expired.badssl.com/", verify=False)
<Response [200 OK]>
```

### Configuring client instances

If you're using a `Client()` instance you should pass any `verify=<...>` configuration when instantiating the client.

By default the [certifi CA bundle](https://certifiio.readthedocs.io/en/latest/) is used for SSL verification.

For more complex configurations you can pass an [SSL Context](https://docs.python.org/3/library/ssl.html) instance...

```python
import certifi
import httpx
import ssl

# This SSL context is equivalent to the default `verify=True`.
ctx = ssl.create_default_context(cafile=certifi.where())
client = httpx.Client(verify=ctx)
```

Using [the `truststore` package](https://truststore.readthedocs.io/) to support system certificate stores...

```python
import ssl
import truststore
import httpx

# Use system certificate stores.
ctx = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client = httpx.Client(verify=ctx)
```

Loding an alternative certificate verification store using [the standard SSL context API](https://docs.python.org/3/library/ssl.html)...

```python
import httpx
import ssl

# Use an explicitly configured certificate store.
ctx = ssl.create_default_context(cafile="path/to/certs.pem")  # Either cafile or capath.
client = httpx.Client(verify=ctx)
```

### Client side certificates

Client side certificates allow a remote server to verify the client. They tend to be used within private organizations to authenticate requests to remote servers.

You can specify client-side certificates, using the [`.load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain) API...

```python
ctx = ssl.create_default_context()
ctx.load_cert_chain(certfile="path/to/client.pem")  # Optionally also keyfile or password.
client = httpx.Client(verify=ctx)
```

### Working with `SSL_CERT_FILE` and `SSL_CERT_DIR`

`httpx` does respect the `SSL_CERT_FILE` and `SSL_CERT_DIR` environment variables by default. For details, refer to [the section on the environment variables page](../environment_variables.md#ssl_cert_file).

### Making HTTPS requests to a local server

When making requests to local servers, such as a development server running on `localhost`, you will typically be using unencrypted HTTP connections.

If you do need to make HTTPS connections to a local server, for example to test an HTTPS-only service, you will need to create and use your own certificates. Here's one way to do it...

1. Use [trustme](https://github.com/python-trio/trustme) to generate a pair of server key/cert files, and a client cert file.
2. Pass the server key/cert files when starting your local server. (This depends on the particular web server you're using. For example, [Uvicorn](https://www.uvicorn.org) provides the `--ssl-keyfile` and `--ssl-certfile` options.)
3. Configure `httpx` to use the certificates stored in `client.pem`.

```python
ctx = ssl.create_default_context(cafile="client.pem")
client = httpx.Client(verify=ctx)
```

----------------------------------------------------------------------

=== [205] docs\advanced\text-encodings.md ===
FILE: docs\advanced\text-encodings.md:1-6

When accessing `response.text`, we need to decode the response bytes into a unicode text representation.

By default `httpx` will use `"charset"` information included in the response `Content-Type` header to determine how the response bytes should be decoded into text.

In cases where no charset information is included on the response, the default behaviour is to assume "utf-8" encoding, which is by far the most widely used text encoding on the internet.

----------------------------------------------------------------------

=== [206] Instantiate a client with the default configuration. > Using the default encoding ===
FILE: docs\advanced\text-encodings.md:7-24

## Using the default encoding

To understand this better let's start by looking at the default behaviour for text decoding...

```python
import httpx
# Instantiate a client with the default configuration.
client = httpx.Client()
# Using the client...
response = client.get(...)
print(response.encoding)  # This will either print the charset given in
                          # the Content-Type charset, or else "utf-8".
print(response.text)  # The text will either be decoded with the Content-Type
                      # charset, or using "utf-8".
```

This is normally absolutely fine. Most servers will respond with a properly formatted Content-Type header, including a charset encoding. And in most cases where no charset encoding is included, UTF-8 is very likely to be used, since it is so widely adopted.

----------------------------------------------------------------------

=== [207] Instantiate a client with the default configuration. > Using an explicit encoding ===
FILE: docs\advanced\text-encodings.md:25-40

## Using an explicit encoding

In some cases we might be making requests to a site where no character set information is being set explicitly by the server, but we know what the encoding is. In this case it's best to set the default encoding explicitly on the client.

```python
import httpx
# Instantiate a client with a Japanese character set as the default encoding.
client = httpx.Client(default_encoding="shift-jis")
# Using the client...
response = client.get(...)
print(response.encoding)  # This will either print the charset given in
                          # the Content-Type charset, or else "shift-jis".
print(response.text)  # The text will either be decoded with the Content-Type
                      # charset, or using "shift-jis".
```

----------------------------------------------------------------------

=== [208] Instantiate a client with the default configuration. > Using auto-detection ===
FILE: docs\advanced\text-encodings.md:41-75

## Using auto-detection

In cases where the server is not reliably including character set information, and where we don't know what encoding is being used, we can enable auto-detection to make a best-guess attempt when decoding from bytes to text.

To use auto-detection you need to set the `default_encoding` argument to a callable instead of a string. This callable should be a function which takes the input bytes as an argument and returns the character set to use for decoding those bytes to text.

There are two widely used Python packages which both handle this functionality:

* [`chardet`](https://chardet.readthedocs.io/) - This is a well established package, and is a port of [the auto-detection code in Mozilla](https://www-archive.mozilla.org/projects/intl/chardet.html).
* [`charset-normalizer`](https://charset-normalizer.readthedocs.io/) - A newer package, motivated by `chardet`, with a different approach.

Let's take a look at installing autodetection using one of these packages...

```shell
$ pip install httpx
$ pip install chardet
```

Once `chardet` is installed, we can configure a client to use character-set autodetection.

```python
import httpx
import chardet

def autodetect(content):
    return chardet.detect(content).get("encoding")

# Using a client with character-set autodetection enabled.
client = httpx.Client(default_encoding=autodetect)
response = client.get(...)
print(response.encoding)  # This will either print the charset given in
                          # the Content-Type charset, or else the auto-detected
                          # character set.
print(response.text)
```

----------------------------------------------------------------------

=== [209] docs\advanced\timeouts.md ===
FILE: docs\advanced\timeouts.md:1-5

HTTPX is careful to enforce timeouts everywhere by default.

The default behavior is to raise a `TimeoutException` after 5 seconds of
network inactivity.

----------------------------------------------------------------------

=== [210] Using the top-level API: > Setting and disabling timeouts ===
FILE: docs\advanced\timeouts.md:6-29

## Setting and disabling timeouts

You can set timeouts for an individual request:

```python
# Using the top-level API:
httpx.get('http://example.com/api/v1/example', timeout=10.0)

# Using a client instance:
with httpx.Client() as client:
    client.get("http://example.com/api/v1/example", timeout=10.0)
```

Or disable timeouts for an individual request:

```python
# Using the top-level API:
httpx.get('http://example.com/api/v1/example', timeout=None)

# Using a client instance:
with httpx.Client() as client:
    client.get("http://example.com/api/v1/example", timeout=None)
```

----------------------------------------------------------------------

=== [211] Using the top-level API: > Setting a default timeout on a client ===
FILE: docs\advanced\timeouts.md:30-40

## Setting a default timeout on a client

You can set a timeout on a client instance, which results in the given
`timeout` being used as the default for requests made with this client:

```python
client = httpx.Client()              # Use a default 5s timeout everywhere.
client = httpx.Client(timeout=10.0)  # Use a default 10s timeout everywhere.
client = httpx.Client(timeout=None)  # Disable all timeouts by default.
```

----------------------------------------------------------------------

=== [212] Using the top-level API: > Fine tuning the configuration ===
FILE: docs\advanced\timeouts.md:41-71

## Fine tuning the configuration

HTTPX also allows you to specify the timeout behavior in more fine grained detail.

There are four different types of timeouts that may occur. These are **connect**,
**read**, **write**, and **pool** timeouts.

* The **connect** timeout specifies the maximum amount of time to wait until
a socket connection to the requested host is established. If HTTPX is unable to connect
within this time frame, a `ConnectTimeout` exception is raised.
* The **read** timeout specifies the maximum duration to wait for a chunk of
data to be received (for example, a chunk of the response body). If HTTPX is
unable to receive data within this time frame, a `ReadTimeout` exception is raised.
* The **write** timeout specifies the maximum duration to wait for a chunk of
data to be sent (for example, a chunk of the request body). If HTTPX is unable
to send data within this time frame, a `WriteTimeout` exception is raised.
* The **pool** timeout specifies the maximum duration to wait for acquiring
a connection from the connection pool. If HTTPX is unable to acquire a connection
within this time frame, a `PoolTimeout` exception is raised. A related
configuration here is the maximum number of allowable connections in the
connection pool, which is configured by the `limits` argument.

You can configure the timeout behavior for any of these values...

```python
# A client with a 60s timeout for connecting, and a 10s timeout elsewhere.
timeout = httpx.Timeout(10.0, connect=60.0)
client = httpx.Client(timeout=timeout)

response = client.get('http://example.com/')
```

----------------------------------------------------------------------

=== [213] docs\advanced\transports.md ===
FILE: docs\advanced\transports.md:1-4

HTTPX's `Client` also accepts a `transport` argument. This argument allows you
to provide a custom Transport object that will be used to perform the actual
sending of the requests.

----------------------------------------------------------------------

=== [214] HTTP Transport ===
FILE: docs\advanced\transports.md:5-37

## HTTP Transport

For some advanced configuration you might need to instantiate a transport
class directly, and pass it to the client instance. One example is the
`local_address` configuration which is only available via this low-level API.

```pycon
>>> import httpx
>>> transport = httpx.HTTPTransport(local_address="0.0.0.0")
>>> client = httpx.Client(transport=transport)
```

Connection retries are also available via this interface. Requests will be retried the given number of times in case an `httpx.ConnectError` or an `httpx.ConnectTimeout` occurs, allowing smoother operation under flaky networks. If you need other forms of retry behaviors, such as handling read/write errors or reacting to `503 Service Unavailable`, consider general-purpose tools such as [tenacity](https://github.com/jd/tenacity).

```pycon
>>> import httpx
>>> transport = httpx.HTTPTransport(retries=1)
>>> client = httpx.Client(transport=transport)
```

Similarly, instantiating a transport directly provides a `uds` option for
connecting via a Unix Domain Socket that is only available via this low-level API:

```pycon
>>> import httpx
>>> # Connect to the Docker API via a Unix Socket.
>>> transport = httpx.HTTPTransport(uds="/var/run/docker.sock")
>>> client = httpx.Client(transport=transport)
>>> response = client.get("http://docker/info")
>>> response.json()
{"ID": "...", "Containers": 4, "Images": 74, ...}
```

----------------------------------------------------------------------

=== [215] Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4". > WSGI Transport ===
FILE: docs\advanced\transports.md:38-85

## WSGI Transport

You can configure an `httpx` client to call directly into a Python web application using the WSGI protocol.

This is particularly useful for two main use-cases:

* Using `httpx` as a client inside test cases.
* Mocking out external services during tests or in dev or staging environments.

### Example

Here's an example of integrating against a Flask application:

```python
from flask import Flask
import httpx


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

transport = httpx.WSGITransport(app=app)
with httpx.Client(transport=transport, base_url="http://testserver") as client:
    r = client.get("/")
    assert r.status_code == 200
    assert r.text == "Hello World!"
```

### Configuration

For some more complex cases you might need to customize the WSGI transport. This allows you to:

* Inspect 500 error responses rather than raise exceptions by setting `raise_app_exceptions=False`.
* Mount the WSGI application at a subpath by setting `script_name` (WSGI).
* Use a given client address for requests by setting `remote_addr` (WSGI).

For example:

```python
# Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4".
transport = httpx.WSGITransport(app=app, remote_addr="1.2.3.4")
with httpx.Client(transport=transport, base_url="http://testserver") as client:
    ...
```

----------------------------------------------------------------------

=== [216] Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4". > ASGI Transport ===
FILE: docs\advanced\transports.md:86-148

## ASGI Transport

You can configure an `httpx` client to call directly into an async Python web application using the ASGI protocol.

This is particularly useful for two main use-cases:

* Using `httpx` as a client inside test cases.
* Mocking out external services during tests or in dev or staging environments.

### Example

Let's take this Starlette application as an example:

```python
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def hello(request):
    return HTMLResponse("Hello World!")


app = Starlette(routes=[Route("/", hello)])
```

We can make requests directly against the application, like so:

```python
transport = httpx.ASGITransport(app=app)

async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
    r = await client.get("/")
    assert r.status_code == 200
    assert r.text == "Hello World!"
```

### Configuration

For some more complex cases you might need to customise the ASGI transport. This allows you to:

* Inspect 500 error responses rather than raise exceptions by setting `raise_app_exceptions=False`.
* Mount the ASGI application at a subpath by setting `root_path`.
* Use a given client address for requests by setting `client`.

For example:

```python
# Instantiate a client that makes ASGI requests with a client IP of "1.2.3.4",
# on port 123.
transport = httpx.ASGITransport(app=app, client=("1.2.3.4", 123))
async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
    ...
```

See [the ASGI documentation](https://asgi.readthedocs.io/en/latest/specs/www.html#connection-scope) for more details on the `client` and `root_path` keys.

### ASGI startup and shutdown

It is not in the scope of HTTPX to trigger ASGI lifespan events of your app.

However it is suggested to use `LifespanManager` from [asgi-lifespan](https://github.com/florimondmanca/asgi-lifespan#usage) in pair with `AsyncClient`.

----------------------------------------------------------------------

=== [217] Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4". > Custom transports ===
FILE: docs\advanced\transports.md:149-245

## Custom transports

A transport instance must implement the low-level Transport API which deals
with sending a single request, and returning a response. You should either
subclass `httpx.BaseTransport` to implement a transport to use with `Client`,
or subclass `httpx.AsyncBaseTransport` to implement a transport to
use with `AsyncClient`.

At the layer of the transport API we're using the familiar `Request` and
`Response` models.

See the `handle_request` and `handle_async_request` docstrings for more details
on the specifics of the Transport API.

A complete example of a custom transport implementation would be:

```python
import json
import httpx

class HelloWorldTransport(httpx.BaseTransport):
    """
    A mock transport that always returns a JSON "Hello, world!" response.
    """

    def handle_request(self, request):
        return httpx.Response(200, json={"text": "Hello, world!"})
```

Or this example, which uses a custom transport and `httpx.Mounts` to always redirect `http://` requests.

```python
class HTTPSRedirect(httpx.BaseTransport):
    """
    A transport that always redirects to HTTPS.
    """
    def handle_request(self, request):
        url = request.url.copy_with(scheme="https")
        return httpx.Response(303, headers={"Location": str(url)})

# A client where any `http` requests are always redirected to `https`
transport = httpx.Mounts({
    'http://': HTTPSRedirect()
    'https://': httpx.HTTPTransport()
})
client = httpx.Client(transport=transport)
```

A useful pattern here is custom transport classes that wrap the default HTTP implementation. For example...

```python
class DebuggingTransport(httpx.BaseTransport):
    def __init__(self, **kwargs):
        self._wrapper = httpx.HTTPTransport(**kwargs)

    def handle_request(self, request):
        print(f">>> {request}")
        response = self._wrapper.handle_request(request)
        print(f"<<< {response}")
        return response

    def close(self):
        self._wrapper.close()

transport = DebuggingTransport()
client = httpx.Client(transport=transport)
```

Here's another case, where we're using a round-robin across a number of different proxies...

```python
class ProxyRoundRobin(httpx.BaseTransport):
    def __init__(self, proxies, **kwargs):
        self._transports = [
            httpx.HTTPTransport(proxy=proxy, **kwargs)
            for proxy in proxies
        ]
        self._idx = 0

    def handle_request(self, request):
        transport = self._transports[self._idx]
        self._idx = (self._idx + 1) % len(self._transports)
        return transport.handle_request(request)

    def close(self):
        for transport in self._transports:
            transport.close()

proxies = [
    httpx.Proxy("http://127.0.0.1:8081"),
    httpx.Proxy("http://127.0.0.1:8082"),
    httpx.Proxy("http://127.0.0.1:8083"),
]
transport = ProxyRoundRobin(proxies=proxies)
client = httpx.Client(transport=transport)
```

----------------------------------------------------------------------

=== [218] Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4". > Mock transports ===
FILE: docs\advanced\transports.md:246-270

## Mock transports

During testing it can often be useful to be able to mock out a transport,
and return pre-determined responses, rather than making actual network requests.

The `httpx.MockTransport` class accepts a handler function, which can be used
to map requests onto pre-determined responses:

```python
def handler(request):
    return httpx.Response(200, json={"text": "Hello, world!"})


# Switch to a mock transport, if the TESTING environment variable is set.
if os.environ.get('TESTING', '').upper() == "TRUE":
    transport = httpx.MockTransport(handler)
else:
    transport = httpx.HTTPTransport()

client = httpx.Client(transport=transport)
```

For more advanced use-cases you might want to take a look at either [the third-party
mocking library, RESPX](https://lundberg.github.io/respx/), or the [pytest-httpx library](https://github.com/Colin-b/pytest_httpx).

----------------------------------------------------------------------

=== [219] Instantiate a client that makes WSGI requests with a client IP of "1.2.3.4". > Mounting transports ===
FILE: docs\advanced\transports.md:271-454

## Mounting transports

You can also mount transports against given schemes or domains, to control
which transport an outgoing request should be routed via, with [the same style
used for specifying proxy routing](#routing).

```python
import httpx

class HTTPSRedirectTransport(httpx.BaseTransport):
    """
    A transport that always redirects to HTTPS.
    """

    def handle_request(self, method, url, headers, stream, extensions):
        scheme, host, port, path = url
        if port is None:
            location = b"https://%s%s" % (host, path)
        else:
            location = b"https://%s:%d%s" % (host, port, path)
        stream = httpx.ByteStream(b"")
        headers = [(b"location", location)]
        extensions = {}
        return 303, headers, stream, extensions


# A client where any `http` requests are always redirected to `https`
mounts = {'http://': HTTPSRedirectTransport()}
client = httpx.Client(mounts=mounts)
```

A couple of other sketches of how you might take advantage of mounted transports...

Disabling HTTP/2 on a single given domain...

```python
mounts = {
    "all://": httpx.HTTPTransport(http2=True),
    "all://*example.org": httpx.HTTPTransport()
}
client = httpx.Client(mounts=mounts)
```

Mocking requests to a given domain:

```python
# All requests to "example.org" should be mocked out.
# Other requests occur as usual.
def handler(request):
    return httpx.Response(200, json={"text": "Hello, World!"})

mounts = {"all://example.org": httpx.MockTransport(handler)}
client = httpx.Client(mounts=mounts)
```

Adding support for custom schemes:

```python
# Support URLs like "file:///Users/sylvia_green/websites/new_client/index.html"
mounts = {"file://": FileSystemTransport()}
client = httpx.Client(mounts=mounts)
```

### Routing

HTTPX provides a powerful mechanism for routing requests, allowing you to write complex rules that specify which transport should be used for each request.

The `mounts` dictionary maps URL patterns to HTTP transports. HTTPX matches requested URLs against URL patterns to decide which transport should be used, if any. Matching is done from most specific URL patterns (e.g. `https://<domain>:<port>`) to least specific ones (e.g. `https://`).

HTTPX supports routing requests based on **scheme**, **domain**, **port**, or a combination of these.

### Wildcard routing

Route everything through a transport...

```python
mounts = {
    "all://": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

### Scheme routing

Route HTTP requests through one transport, and HTTPS requests through another...

```python
mounts = {
    "http://": httpx.HTTPTransport(proxy="http://localhost:8030"),
    "https://": httpx.HTTPTransport(proxy="http://localhost:8031"),
}
```

### Domain routing

Proxy all requests on domain "example.com", let other requests pass through...

```python
mounts = {
    "all://example.com": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

Proxy HTTP requests on domain "example.com", let HTTPS and other requests pass through...

```python
mounts = {
    "http://example.com": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

Proxy all requests to "example.com" and its subdomains, let other requests pass through...

```python
mounts = {
    "all://*example.com": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

Proxy all requests to strict subdomains of "example.com", let "example.com" and other requests pass through...

```python
mounts = {
    "all://*.example.com": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

### Port routing

Proxy HTTPS requests on port 1234 to "example.com"...

```python
mounts = {
    "https://example.com:1234": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

Proxy all requests on port 1234...

```python
mounts = {
    "all://*:1234": httpx.HTTPTransport(proxy="http://localhost:8030"),
}
```

### No-proxy support

It is also possible to define requests that _shouldn't_ be routed through the transport.

To do so, pass `None` as the proxy URL. For example...

```python
mounts = {
    # Route requests through a proxy by default...
    "all://": httpx.HTTPTransport(proxy="http://localhost:8031"),
    # Except those for "example.com".
    "all://example.com": None,
}
```

### Complex configuration example

You can combine the routing features outlined above to build complex proxy routing configurations. For example...

```python
mounts = {
    # Route all traffic through a proxy by default...
    "all://": httpx.HTTPTransport(proxy="http://localhost:8030"),
    # But don't use proxies for HTTPS requests to "domain.io"...
    "https://domain.io": None,
    # And use another proxy for requests to "example.com" and its subdomains...
    "all://*example.com": httpx.HTTPTransport(proxy="http://localhost:8031"),
    # And yet another proxy if HTTP is used,
    # and the "internal" subdomain on port 5550 is requested...
    "http://internal.example.com:5550": httpx.HTTPTransport(proxy="http://localhost:8032"),
}
```

### Environment variables

There are also environment variables that can be used to control the dictionary of the client mounts. 
They can be used to configure HTTP proxying for clients.

See documentation on [`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`](../environment_variables.md#http_proxy-https_proxy-all_proxy)
and [`NO_PROXY`](../environment_variables.md#no_proxy) for more information.

----------------------------------------------------------------------

