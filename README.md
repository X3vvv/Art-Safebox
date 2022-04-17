# Art-Safebox
COMP3334 Computer Security Group Project

# 系统设计详情（部分内容已过时）
Web Client
	- html: 首页（未登录/已登陆）；登录；注册；个人主页；其他人主页；消息页；
	- css: bootstramp5
	- javasript: ID, PWD -- post/get ID, PWD
	- TOKEN - expire_time

Web Server:
	- Django web framework/HTTPS 
	- OpenSLL set TLS1.3
	- mkcert fake CA
	- POST/GET -> JSON

ITERATION TYPE:
	- SIGNUP   {'USER_ID', 'TOKEN'}                                          <- FAILED+MSG/PRIV_KEY   POST
	- SIGNIN   {'USER_ID', 'PRIV_KEY', 'TOKEN'}                              <- FAILED+MSG/OK         POST
	- UPLOAD   {'COLLECTION_ID', 'SOURCE', 'TOKEN'}                          <- FAILED+MSG/OK         POST
	- BUY      {'COLLECTION_ID', 'USER_ID', 'TOKEN'}                         <- FAILED+MSG/OK         POST
	- RESPONCE {'timestamp', 'status': [accept/refuse], 'TOKEN', 'PRIV_KEY'} <- FAILED+MSG/OK         POST
	- RECHARGE {'USER_ID', 'AMOUNT', 'TOKEN'}                			     <- FAILED+MSG/OK         POST
	- DOWNLOAD {'COLLECTION_ID', 'TOKEN', 'PRIV_KEY'}                        <- FAILED/OK             POST

Database Entity
User:
	USER_ID
	PUB_KEY
	VALIDATION_FILE
	BALANCE
	TRANSECTION <- BLOB <- JSON DICT{'timestamp', type' [request, notice], 'content', 'artwork-id', 'requestee_id', 'requestor_id', 'status': [accept/reject/pending], 'AMOUNT': 10}

Collection:
	collection_id
	owner_id
	encrypted_content
	preview
	price += 1 当销售之后
	status: "PENDING", "CONFIRMED"







