#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, time, hmac, uuid, urllib, base64, hashlib

from urllib import request, parse, error
import circumstances_config


#DEFAULT_HOST = 'api.highdax.com'

#DEFAULT_HOST = 'api.dev2.highdax.com'
import global_variable


def _get_config():
    #"dev2","matrix"
    config=circumstances_config.config_init_(global_variable.cir_var)
    return config

DEFAULT_HOST =_get_config().get("host")
print (DEFAULT_HOST)

class ApiClient(object):

    def __init__(self, api_key, api_secret, host=None, https=True, timeout=10, enable_debug=False):
        print("test:"+DEFAULT_HOST)
        self._api_key = api_key
        self._api_secret = api_secret.encode('utf-8')
        self._host = (host or DEFAULT_HOST).lower()
        self._protocol =_get_config().get("protocol") if https else 'http'
        self._timeout = timeout
        self._debug = enable_debug




    def _hostname(self):
        n = self._host.find(':')
        if n > 0:
            return self._host[:n]
        return self._host

    def get(self, path, **params):
        return self._http('GET', path, params, None)

    def post(self, path,pram, obj=None):
        data = json.dumps(obj) if obj is not None else None
        #print(data)
        #print(self._http('POST', path,{"withdrawAddressId":86,"amount":0.1,"currency":"ETC"},data))
        return self._http('POST', path, pram, data)

    def _http(self, method, path, params, data):
        print("params",params)
        # build payload:
        param_list = ['%s=%s' % (k, v) for k, v in params.items()]
        param_list.sort()
        payload = [method, self._hostname(), path, '&'.join(param_list)]
        headers = {
            'API-Key': self._api_key,
            'API-Signature-Method': 'HmacSHA256',
            'API-Signature-Version': '1',
            'API-Timestamp': str(int(time.time() * 1000))
        }
        if method == 'POST' and path.startswith('/v1/trade/'):
            headers['API-Unique-ID'] = uuid.uuid4().hex
        headers_list = ['%s: %s' % (k.upper(), v) for k, v in headers.items()]
        headers_list.sort()
        payload.extend(headers_list)
        payload.append(data if data else '')
        payload_str = '\n'.join(payload)
        # signature:
        sign = hmac.new(self._api_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        self.debug('payload:\n----\n' + payload_str + '----\nsignature: ' + sign)
        headers['API-Signature'] = sign
        # build request:
        if data:
            data = data.encode('utf-8')
        else:
            data = None
        url = '%s://%s%s?%s' % (self._protocol, self._host, path, parse.urlencode(params))
        print("yyyyyyy",path)
        self.debug('%s: %s' % (method, url))
        #print(url)
        req = request.Request(url, data=data, method=method)
        print(url)
        #print(req.host)
        for k, v in headers.items():
            req.add_header(k, v)
        if data:
            req.add_header('Content-Type', 'application/json')
        try:
            with request.urlopen(req, timeout=self._timeout) as f:
                s = f.read()
                r = json.loads(s.decode('utf-8'), object_hook=lambda d: Dict(**d))
                self.debug(json.dumps(r))
                return r
        except error.HTTPError as err:
            s = err.read()
            self.debug(s)
            return json.loads(s.decode('utf-8'), object_hook=lambda d: Dict(**d))

    def debug(self, msg):
        if self._debug:
            print(msg)

class ApiError(Exception):
    pass

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
# { "apiKey": "AAAAAKCNRDM8rTtvC7XXZUTX", "apiSecret": "WB90xv248qq6ytkk" },



