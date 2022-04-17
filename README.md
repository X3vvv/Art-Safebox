# Art-Safebox

COMP3334 Computer Security Group Project

# TODO

1. 确保所有数据库命令都在`DBmanager`中实现，常用的数据库操作可以利用各个 model 中的 db 类变打包作为 model 的方法，从而被调用。
2. ~~完成 Controller.sign_in() 的实现~~
3. 实现 User.is_online()
4. 完成 Controller.init()
5. 完成 Controller.\_find_transactionon()
6. 完成 Collection.updata_db()
7. 完成 DBmanager.getxx_by_id() 到生成对应实例的过程
8. 优化 Controller.init_user_list() 等 init 函数，目前每初始化一个用户需要调两次数据库
9. 数据库语法优化解决报错：[参考](https://stackoverflow.com/questions/45575608/python-sqlite-operationalerror-near-s-syntax-error)

#

# ERROR

1. DBmanager.update_collection()，使用后 price 和 user_id 顺序会交换
2. DBmanager 的 transactions 多了一个参数 NULL

# 系统设计详情（部分内容已过时）

Web Client

-   html: 首页（未登录/已登陆）；登录；注册；个人主页；其他人主页；消息页；
-   css: bootstramp5
-   javasript: ID, PWD -- post/get ID, PWD
-   TOKEN - expire_time

Web Server:

-   Django web framework/HTTPS
-   OpenSLL set TLS1.3
-   mkcert fake CA
-   POST/GET -> JSON

ITERATION TYPE:

-   SIGNUP {'USER_ID', 'TOKEN'} <- FAILED+MSG/PRIV_KEY POST
-   SIGNIN {'USER_ID', 'PRIV_KEY', 'TOKEN'} <- FAILED+MSG/OK POST
-   UPLOAD {'COLLECTION_ID', 'SOURCE', 'TOKEN'} <- FAILED+MSG/OK POST
-   BUY {'COLLECTION_ID', 'USER_ID', 'TOKEN'} <- FAILED+MSG/OK POST
-   RESPONCE {'timestamp', 'status': [accept/refuse], 'TOKEN', 'PRIV_KEY'} <- FAILED+MSG/OK POST
-   RECHARGE {'USER_ID', 'AMOUNT', 'TOKEN'} <- FAILED+MSG/OK POST
-   DOWNLOAD {'COLLECTION_ID', 'TOKEN', 'PRIV_KEY'} <- FAILED/OK POST

Database Entity
User:

-   USER_ID
-   PUB_KEY
-   VALIDATION_FILE
-   BALANCE
-   TRANSECTION <- BLOB <- JSON DICT{'timestamp', type' [request, notice], 'content', 'artwork-id', 'requestee_id', 'requestor_id', 'status': [accept/reject/pending], 'AMOUNT': 10}

Collection:

-   collection_id
-   owner_id
-   encrypted_content
-   preview
-   price += 1 当销售之后
-   status: "PENDING", "CONFIRMED"

# reference

-   [Python Notebook 不同文件互相引用](https://www.jianshu.com/p/4850ad2a8516)
-   [中泰证券 NFT 技术分析](https://dfscdn.dfcfw.com/download/A2_cms_f_20220216123508144922&direct=1&abc3847.pdf)
