#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 09:12
# @Author  : Dirk Zhao
import requests
from utils.log import logger
from utils import data_dist


METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    pass


class HttpClient(object):
    def __init__(self, url, method='GET', headers=None, cookies=None):
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0},请检查传入参数'
                                           .format(self.method))
        self.set_headers(headers)
        self.set_cookies(cookies)
        self.data = None
        self.sign = None
        self.payload = None

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def set_payload(self, datadict):
        self.data = data_dist.get_data(datadict)
        self.sign = data_dist.get_sign(self.data)
        self.payload = data_dist.get_payload(data=self.data, sign=self.sign)

    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(method=self.method, url=self.url,
                                        params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0}{1}'.format(self.method, self.url))
        logger.debug('请求成功：{0}\n{1}'.format(response, response.text))
        return response

    def get(self, params=None, **kwargs):
        response = self.session.request(method='GET', url=self.url,
                                        params=params, **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0}{1}'.format('GET', self.url))
        logger.debug('请求成功：{0}\n{1}'.format(response, response.text))
        return response

    def post(self, **kwargs):
        d = self.payload
        response = self.session.request(method='POST', url=self.url,
                                        data=d, **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0}{1}'.format('POST', self.url))
        logger.debug('请求成功：{0}\n{1}'.format(response, response.text))
        return response
