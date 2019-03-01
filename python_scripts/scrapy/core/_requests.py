import requests
import datetime, time
import copy
from random import randint
import os
from utils.file_handle import mkdir_if_not_existed, get_url_path_info, get_vedio_url_path_info

from http import cookiejar  
class BlockAll(cookiejar.CookiePolicy):
	return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
	netscape = True
	rfc2965 = hide_cookie2 = False

class RequestTemplete(object):

	def __init__(self):
		self.session = requests.Session()
		self.session.cookies.set_policy(BlockAll())
		self.datas = {}
		self.params ={}
		self.files = {}
		self.url = ''
		self.host = '127.0.0.1'
		self.port = '80'
		
		self.verify = False
		self.method = 'get'
		self.proxies = ''
		self.cookies = ''
		self.headers = ''
		self.img_save_path = ''

	
	def set_url(self,dns,url):
		self.url = dns + "/" + url

	def set_proxies(self,proxies):
		if not proxies:
			self.proxies = {
			  'http' : 'socks5://192.168.10.20:1080',
			  'https': 'socks5://192.168.10.20:1080'
			}
		else:
			self.proxies = proxies
	def set_proxies_disable(self, url_strval="192.168.10.230"):
		'''
		session = requests.Session()
		session.trust_env = False
		os.environ['NO_PROXY'] = 'stackoverflow.com'
		response = requests.get('http://www.stackoverflow.com')
		'''
		import os
		os.environ['NO_PROXY'] = url_strval

	def set_cookies(self, cookies=None):
		self.auto_headers_info = importModule(self.auto_header_file)
		if not cookies:

			self.cookies = None
		elif cookies == "default":
			key = "cookies"
			if not self.auto_headers_info and (key not in self.auto_headers_info):
				self.cookies = {"uid":"ChQA/Fmk9+tpkFsrBCvgAg=="}
			else:
				self.cookies = self.auto_headers_info[key]
		else:
			self.cookies = cookies
		  
	def set_params(self,param):
		self.params = param

	def set_verify(self,bverify):
		self.verify = bverify

	def set_method(self,method):
		self.method = method

	def set_logpath(self,logpath):
		self.logpath = logpath

	def set_request_retry(self,url,count_number=3):
		request_retry = requests.adapters.HTTPAdapter(max_retries=count_number)
		self.session.mount(url,request_retry)

	# def response_encoding(self, response):
	# 	if response.encoding == 'ISO-8859-1' and not 'ISO-8859-1' in response.headers.get('content-type', ''):
	#         encodings = requests.utils.get_encodings_from_content(response.content)  #re.compile(r'<meta.*?charset  #源代码没有利用这个方法
	#         if encodings:
	#             response.encoding = encodings[0]
	#         else:
	#             response.encoding = response.apparent_encoding  #models.py  chardet.detect(self.content)['encoding'] 消耗计算 # resp.text >>> if self.encoding is None: encoding = self.apparent_encoding
 #        return response

	def post(self):
		try:
			self.set_proxies_disable()
			starttime = datetime.datetime.now()
			self.set_request_retry(self.url)
			response = self.session.post(self.url,data=self.params,
				headers=self.headers,cookies=self.cookies,verify=self.verify,timeout=30)
			endtime = datetime.datetime.now()
			responsetime = (endtime - starttime).microseconds	
		except TimeoutError:
			 print(TimeoutError)
		return response

	def get(self):
		try:
			self.set_proxies_disable()
			starttime = datetime.datetime.now()
			self.set_request_retry(self.url)
			# print("cookies:   ",self.cookies)
			response = self.session.get(url=self.url,params=self.params,\
				headers=self.headers,cookies=self.cookies,verify=self.verify,timeout=30)
			endtime = datetime.datetime.now()
			responsetime = (endtime - starttime).microseconds

		except TimeoutError:
			 print(TimeoutError)
		return response

	def _req(self):
		# print("method",self.method)
		if 'get' == self.method:
			return self.get()
		elif 'post' == self.method:
			return self.post()

	def set_headers(self,headers=None):
		self.auto_headers_info = importModule(self.auto_header_file)

		if not headers:
			self.headers = None
		elif headers == "default":
			# print("222:",headers)
			key = "headers"
			if not self.auto_headers_info and (key not in self.auto_headers_info):
				self.headers = {

					#生产机的header
					"Host": "api.crazysales.com.au",
					"Connection": "keep-alive",
					"Accept": "application/json",
					"X-Requested-With": "XMLHttpRequest",
					"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; Samsung Galaxy S6 - 7.1.0 - API 25 - 1440x2560 Build/NMF26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Html5Plus/1.0",
					"Content-Type": "application/json",
					"Accept-Encoding": "gzip, deflate",
					"Accept-Language": "en-US"
					# "Host": "192.168.10.230",
					# "Connection": "keep-alive",
					
					# "Accept": "application/json",
					# "X-Requested-With": "XMLHttpRequest",
					# "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Google Nexus 6P - 7.0.0 - API 24 - 1440x2560 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.91 Mobile Safari/537.36 Html5Plus/1.0",
					# "Content-Type": "application/json",
					# "Accept-Encoding": "gzip, deflate",
					# "Accept-Language": "en-US"
				}
			else:
				self.headers = self.auto_headers_info[key]
		# elif isinstance(headers, dict):
		else:
			self.headers = headers

		# self.generate_headers()
		
	__user_agents = (
		"Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.5.22 Version/10.50",
		"Mozilla/6.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:2.0.0.0) Gecko/20061028 Firefox/3.0",
		"Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
		"Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/13.0.1",
		"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0",
		"Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9",
		"Lynx/2.8.8dev.3 libwww-FM/2.14 SSL-MM/1.4.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11",
		"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
		"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
		"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
		"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
		"Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)",
		"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
		"Mozilla/5.0 (PLAYSTATION 3; 3.55)",
		"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
		"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
		"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
		"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
		"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
		"Mozilla/5.0 (Linux; Android 7.1.1; Samsung Galaxy S6 - 7.1.0 - API 25 - 1440x2560 Build/NMF26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Html5Plus/1.0"
	)

	def generate_user_agent(self):
		"""
		:returns: A valid user agent string, randomly chosen from a predefined list.
		:rtype: str
		"""
		return self.__user_agents[randint(0, len(self.__user_agents) - 1)]

	def generate_headers(self):

		__user_agents = self.generate_user_agent()
		self.set_headers_user_agent(__user_agents)

	def set_headers_user_agent(self, user_agent):
		if not self.headers:
			self.headers = {}
		__user_agents_key = 'User-Agent'
		self.headers[__user_agents_key] = user_agent


	def get_csrf_token_from_text(self, str_data):

		csrf_key = "csrf-token"
		len_csrf_key = len(csrf_key) + 1

		index = str_data.find(csrf_key) 
		if -1 != index:
			index +=  len_csrf_key 
			new_str = str_data[index:index + 100 ]
			new_str = new_str.strip()
			new_str = new_str.split(" ")[0]
			new_str = new_str.replace("\n", "").replace(">", "").replace("content", "").replace("=", "").replace("\"","")
			return new_str.strip()

	def get_token_from_usr(self, str_data):


		csrf_key = "_token"
		len_csrf_key = len(csrf_key) + 1

		index = str_data.find(csrf_key) 
		if -1 != index:
			index +=  len_csrf_key 
			new_str = str_data[index:index + 100 ]

			new_str = new_str.strip()
			new_str = new_str.split(" ")[0]
			new_str = new_str.replace("\n", "").replace(">", "").replace("value", "").replace("=", "").replace("\"","").replace(":","")
			qoute_index = new_str.find(",")
			if qoute_index != -1:
				new_str = new_str[:qoute_index]
			return new_str.strip()

	def get_token(self, url):
		response =self.session.get(url, verify=False, timeout=30)
		return self.get_token_from_usr(response.text)

	def get_headers_info_by_homepage(self, url, path):
		# file_path = _base_path_config_obj.auto_headers
		import requests, codecs
		# session = requests.Session()
		response =self.session.get(url, verify=False, timeout=30)
		# print(type(response.text))
		csrf_token = self.get_csrf_token_from_text(response.text)
		# print(csrf_token)

		data = {}
		if url.find("https") != -1:
			host = url[8:]
		else:
			host = url[7:]
		if response.status_code == 200:
			data['headers'] = response.headers

			cookies = response.cookies.items()
			cookies_str = ""
			for key, value in cookies:
				cookies_str += key + "=" + value + ";"
			data['headers'] = {
				"Accept-Encoding": "gzip, deflate, br",
				"Accept": "application/json, text/html, */*",
				"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
				"Connection": "keep-alive",
				"Content-Type": "application/json;charset=UTF-8",
				"X-Requested-With": "XMLHttpRequest",
				"X-XSRF-TOKEN": response.cookies['XSRF-TOKEN'],
				"X-CSRF-TOKEN": csrf_token,
				"Cookie": cookies_str,
				"Host": host,
				"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
			}
		
		data['cookies'] = cookies
		self.headers = data['headers']
		# self.cookies = data['cookies']
		with codecs.open(path, 'w' ,'utf-8') as fjson:
			write_contents = """
auto_headers = %s
""" % (data)
			fjson.write(write_contents)



	def get_cookies_keys(self):
		# print("cookie before: ", self.reqObj.session.cookies.keys())
		# print("cookie after: ", self.reqObj.session.cookies.clear())
		return self.session.cookies.keys()

	def clear_all_cookies(self):
		# print("cookie before: ", self.reqObj.session.cookies.keys())
		self.session.cookies.clear()

	def get_img(self, args):
		(img_url, file_name) = args
		# raise Exception(img_url)
		try:
			print("[infos]Will download img: %s" % img_url)
			self.generate_headers()
			img = requests.get(img_url.strip(), headers=self.headers)
			
			mkdir_if_not_existed(file_name)
			
			import codecs
			with codecs.open(file_name, 'wb') as file_bj:
				print("[infos]save file in ", file_name)
				file_bj.write(img.content)
			print("[infos]Finish download img: %s" % img_url)
			return file_name
		except Exception as e:
			raise e

	def download_img(self, img_url, img_type=0, thred=2):
		# raise Exception(img_url, img_type)
		result = ''
		from multiprocessing.dummy import Pool as ThreadPool
		
		if not img_url:
			raise Exception(img_url)
			return 
		img_urls = []
		if isinstance(img_url, list):
			img_urls = img_url
		elif isinstance(img_url,str):
			path, fname, ext_name = get_url_path_info(img_url)
			path = os.path.join('.', path, fname + ext_name)
			img_urls.append((img_url, path))

		if len(img_urls) > 4:
			thred = thred * 2 
		if thred >= 2:
			thred = 2
		pool = ThreadPool(thred)  # 同时开启 10 个线程
		if img_type == 0:
		
			result = pool.map(self.get_img, img_urls)
			print("[infos]pool path ", result)
			# pool.close()
			# pool.join()
		elif img_type == 1:
			result = pool.map(self.get_vedio, img_urls)
		pool.close()
		pool.join()

		print("[infos]pool path ", result)
		

	def get_vedio(self, args):
		(img_url, file_name) = args
		try:
			# raise Exception(img_url)
			print("[infos]Will download img: %s" % img_url)
			self.generate_headers()
			img = requests.get(img_url.strip(), headers=self.headers, stream=True)
			mkdir_if_not_existed(file_name)
			import codecs
			with codecs.open(file_name, 'wb') as file_bj:
				for chunk in img.iter_content(chunk_size=1024 * 1024):
					if chunk:
						file_bj.write(chunk)
				print("[infos]save file in ", file_name)
				# file_bj.write(img.content)
			print("[infos]Finish download img: %s" % img_url)
			return file_name
		except Exception as e:
			raise e



		


