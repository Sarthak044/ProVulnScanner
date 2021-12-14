#!/usr/bin/env python

import requests
import urllib.parse as urlparse
from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.tar_url = url
        self.tar_links = []
        self.ignore = ignore_links
    
    def extract_links(self, url):
        response = requests.get(url)
        return re.findall(f'(?:href=")(.*?)"', response.content.decode(errors = 'ignore'))
    
    def crawl(self, url=None):
        if url is None:
            url = self.tar_url
        href_links = self.extract_links(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]
            
            if self.tar_url in link and link not in self.tar_links and link not in self.ignore:
                self.tar_links.append(link)
                print(link)
                self.crawl(link)
    
    def ex_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, "html.parrser")
        return parsed_html.findAll("form")

    def sub_forms(self, form, value, url):
        action = form.get("action")
        postU = urljoin(url, action)
        method = form.get("method")
        input_list = form.findAll("input")
        post_data = []
        for input in input_list:
            inputN = input.get("name")
            inputT = input.get("type")
            inputV = input.get("value")
            if inputT == 'text':
                inputV = value
            post_data[inputN] = inputV
        if method == "post":
            return self.session.post(postU, data=post_data)
        return self.session.get(postU, params=post_data)
    
    def run_scanner(self):
        for link in self.tar_links:
            forms = self.ex_forms(link)
            for form in forms:
                print("[+] Testing forms in  " + link)
                xssV = self.xssT(form, link)
                if xssV:
                    print("\n\n[***] XSS Discovered in link " + link + "in the following form")
                    print(form)
        
        if "=" in link:
            print("[+] Testing " + link)
            xssV = self.xssT(link)
            if xssV:
                print("\n\n[****] Discovered XSS in " + link)
    
    def xssTL(self, url):
        xssTS = "sCript>alert('test')</scriPt>"
        url = url.replace("=", "=" + xssTS)
        response = self.session.get(url)
 
        return bytes(xssTS, 'utf-8') in response.content
 
    def xssTF(self, form, url):
        xssTS = "<sCript>alert('test')</scriPt>"
        response = self.submit_forms(form, xssTS, url)
        return bytes(xssTS, 'utf-8') in response.content
