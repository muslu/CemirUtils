import json

from urllib import request, parse


class CemirUtils:
    def __init__(self):
        self.default_headers = {"User-Agent": "CemirUtils"}

    def http_send_request(self, url, method='GET', headers=None, data=None, destination=None):
        """
        Send an HTTP request to the given URL with the specified method, headers, and data.
        If destination is provided, download the file to the destination path.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()
        try:
            req = request.Request(url, headers=headers or self.default_headers, method=method, data=data)
            with request.urlopen(req) as response:
                content = response.read()
                result = {
                    "url": url,
                    "method": method,
                    "headers": dict(response.headers),
                    "content": "Binary data (PDF, image, etc.)"
                }
                if destination:
                    with open(destination, 'wb') as f:
                        f.write(content)
                    result["saved_to"] = destination
                return json.dumps(result, indent=4)
        except Exception as e:
            return f"Failed to send request to {url}, error: {str(e)}"


    def http_get(self, url, params=None, headers=None, verify_ssl=True):
        """
        GET isteği gönderir.

        Parametreler:
        url (str): İstek URL'si.
        params (dict): URL parametreleri.
        headers (dict): İstek başlıkları.
        verify_ssl (bool): SSL doğrulama kontrolü.

        Dönüş:
        dict, str: JSON yanıtı veya düz metin.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()

        if params:
            url += '?' + parse.urlencode(params)

        req = request.Request(url, headers=headers)
        response = request.urlopen(req, timeout=10, context=None if verify_ssl else request._create_unverified_context())
        content = response.read().decode('utf-8')

        if 'application/json' in response.getheader('Content-Type'):
            return json.loads(content)
        else:
            return content

    def http_post(self, url, data=None, headers=None, verify_ssl=True):
        """
        POST isteği gönderir.

        Parametreler:
        url (str): İstek URL'si.
        data (dict): Gönderilecek veri.
        headers (dict): İstek başlıkları.
        verify_ssl (bool): SSL doğrulama kontrolü.

        Dönüş:
        dict, str: JSON yanıtı veya düz metin.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()

        if data:
            data = parse.urlencode(data).encode('utf-8')

        req = request.Request(url, data=data, headers=headers, method='POST')
        response = request.urlopen(req, timeout=10, context=None if verify_ssl else request._create_unverified_context())
        content = response.read().decode('utf-8')

        if 'application/json' in response.getheader('Content-Type'):
            return json.loads(content)
        else:
            return content

    def http_put(self, url, data=None, headers=None, verify_ssl=True):
        """
        PUT isteği gönderir.

        Parametreler:
        url (str): İstek URL'si.
        data (dict): Gönderilecek veri.
        headers (dict): İstek başlıkları.
        verify_ssl (bool): SSL doğrulama kontrolü.

        Dönüş:
        dict, str: JSON yanıtı veya düz metin.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()

        if data:
            data = parse.urlencode(data).encode('utf-8')

        req = request.Request(url, data=data, headers=headers, method='PUT')
        response = request.urlopen(req, timeout=10, context=None if verify_ssl else request._create_unverified_context())
        content = response.read().decode('utf-8')

        if 'application/json' in response.getheader('Content-Type'):
            return json.loads(content)
        else:
            return content

    def http_delete(self, url, headers=None, verify_ssl=True):
        """
        DELETE isteği gönderir.

        Parametreler:
        url (str): İstek URL'si.
        headers (dict): İstek başlıkları.
        verify_ssl (bool): SSL doğrulama kontrolü.

        Dönüş:
        dict, str: JSON yanıtı veya düz metin.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()

        req = request.Request(url, headers=headers, method='DELETE')
        response = request.urlopen(req, timeout=10, context=None if verify_ssl else request._create_unverified_context())
        content = response.read().decode('utf-8')

        if 'application/json' in response.getheader('Content-Type'):
            return json.loads(content)
        else:
            return content

    def http_patch(self, url, data=None, headers=None, verify_ssl=True):
        """
        PATCH isteği gönderir.

        Parametreler:
        url (str): İstek URL'si.
        data (dict): Gönderilecek veri.
        headers (dict): İstek başlıkları.
        verify_ssl (bool): SSL doğrulama kontrolü.

        Dönüş:
        dict, str: JSON yanıtı veya düz metin.
        """
        if headers is None or "User-Agent" not in headers:
            headers = self.default_headers.copy()

        if data:
            data = parse.urlencode(data).encode('utf-8')

        req = request.Request(url, data=data, headers=headers, method='PATCH')
        response = request.urlopen(req, timeout=10, context=None if verify_ssl else request._create_unverified_context())
        content = response.read().decode('utf-8')

        if 'application/json' in response.getheader('Content-Type'):
            return json.loads(content)
        else:
            return content


cemir_utils = CemirUtils()


headers = {"Authorization": "Bearer token123"}
print(cemir_utils.http_send_request("http://0.0.0.0:8000/", method='GET', headers=headers))
# print(cemir_utils.http_send_request("https://jsonplaceholder.typicode.com/posts/1", method='GET', headers=headers))
# print(cemir_utils.http_send_request("https://pdfobject.com/pdf/sample.pdf", method='GET', destination='downloaded_file.pdf'))

