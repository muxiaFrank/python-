#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/12 下午12:54 
"""

import logging
import re
import time

import requests
from requests import Request, Response
from requests.exceptions import (InvalidSchema, InvalidURL, MissingSchema,
                                 RequestException)

def request(method, url, **kwargs):
    """
    Constructs and sends a :py:class:`requests.Request`.
    Returns :py:class:`requests.Response` object.

    :param method:
        method for the new :class:`Request` object.
    :param url:
        URL for the new :class:`Request` object.
    :param params: (optional)
        Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional)
        Dictionary or bytes to send in the body of the :class:`Request`.
    :param headers: (optional)
        Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional)
        Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional)
        Dictionary of ``'filename': file-like-objects`` for multipart encoding upload.
    :param auth: (optional)
        Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional)
        How long to wait for the server to send data before giving up, as a float, or \
        a (`connect timeout, read timeout <user/advanced.html#timeouts>`_) tuple.
        :type timeout: float or tuple
    :param allow_redirects: (optional)
        Set to True by default.
    :type allow_redirects: bool
    :param proxies: (optional)
        Dictionary mapping protocol to the URL of the proxy.
    :param stream: (optional)
        whether to immediately download the response content. Defaults to ``False``.
    :param verify: (optional)
        if ``True``, the SSL cert will be verified. A CA_BUNDLE path can also be provided.
    :param cert: (optional)
        if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    """

    # prepend url with hostname unless it's already an absolute URL

    logging.info(" Start to {method} {url}".format(method=method, url=url))
    logging.debug(" kwargs: {kwargs}".format(kwargs=kwargs))
    # store meta data that is used when reporting the request to locust's statistics
    request_meta = {}

    # set up pre_request hook for attaching meta data to the request object
    request_meta["method"] = method
    request_meta["start_time"] = time.time()

    if "HttpNtlmAuth" in kwargs:
        from requests_ntlm import HttpNtlmAuth
        auth_account = kwargs.pop("HttpNtlmAuth")
        kwargs["auth"] = HttpNtlmAuth(
            auth_account["username"], auth_account["password"])

    response = self._send_request_safe_mode(method, url, **kwargs)
    request_meta["url"] = (response.history and response.history[0] or response) \
        .request.path_url

    # record the consumed time
    request_meta["response_time"] = int((time.time() - request_meta["start_time"]) * 1000)

    # get the length of the content, but if the argument stream is set to True, we take
    # the size from the content-length header, in order to not trigger fetching of the body
    if kwargs.get("stream", False):
        request_meta["content_size"] = int(response.headers.get("content-length") or 0)
    else:
        request_meta["content_size"] = len(response.content or "")

    request_meta["request_headers"] = response.request.headers
    request_meta["request_body"] = response.request.body
    request_meta["status_code"] = response.status_code
    request_meta["response_headers"] = response.headers
    request_meta["response_content"] = response.content

    logging.debug(" response: {response}".format(response=request_meta))

    try:
        response.raise_for_status()
    except RequestException as e:
        logging.error(" Failed to {method} {url}! exception msg: {exception}".format(
            method=method, url=url, exception=str(e)))
    else:
        logging.info(
            """ status_code: {}, response_time: {} ms, response_length: {} bytes, headers: {} """ \
                .format(request_meta["status_code"], request_meta["response_time"], \
                        request_meta["content_size"], request_meta["request_headers"]))

    return response