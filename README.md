# AutoGenTestCase
借助AI大模型帮助生成测试用例

## 项目目录结构
```
AutoGenTestCase/
├── .new_env/
├── __pycache__/
├── hooks/
│   └── __pycache__/
├── img/
├── README.md
├── TESTCASE_READER_SYSTEM_MESSAGE.txt
├── TESTCASE_WRITER_SYSTEM_MESSAGE.txt
├── config.ini
├── llms.py
├── page.py
├── requirements.txt
├── run.py
└── run.spec
```

## 启动步骤
1. 安装依赖：
   ```bash
   uv pip install -r requirements.txt
   ```
2. 配置API Key：
   - 按照下方说明申请DeepSeek和通义千问的API Key
   - 将API Key填写到config.ini文件中
3. 运行程序：
   ```bash
    streamlit run page.py
   ```

## 注意事项
1. 请确保Python版本为3.8或以上
2. 首次使用需要申请API Key并填写到配置文件中
3. 使用前请仔细阅读模型收费标准，避免产生意外费用
4. 建议在虚拟环境中运行本项目

### 打包程序下载地址
https://pan.baidu.com/s/1Cftl4BiWh_reU-oCwW3aMg  提取码：6bwu

### 模型收费情况：
#### DeepSeek申请apikey后需要充值金额才能使用，收费标准比较低2元可以使用上百次不止，放心大胆使用
#### 通义千问申请apikey后会先赠送百万tokens（够用），收费标准也比较低，放心使用

### 申请DeepSeek的apikey
1、链接：https://platform.deepseek.com/api_keys<br>
2、注册账号并登录<br>
3、创建apikey<br>
![image](https://github.com/user-attachments/assets/28310179-7263-4abc-a3e6-6e5599808fe5)


### 申请通义千问的apikey
1、链接：https://bailian.console.aliyun.com/?tab=model#/api-key<br>
2、注册账号并登录（可直接用支付宝账号登录）<br>
3、创建apikey<br>
![image](https://github.com/user-attachments/assets/9e42f4c5-d4c6-4baf-b18e-dc184bb9a507)
