# XUnity.AutoTranslator-deepseek
调用腾讯的deep seek v3进行Unity游戏日文文本翻译

## 准备
在[腾讯云api](https://console.cloud.tencent.com/lkeap/api)申请deepseek的api（腾讯云deepseek的api限时免费），或者其他平台的deepseek的api

### 安装
安装好XUnity.AutoTranslator和python，

还需要安装：`pip install Flask` ；

还需要安装：`pip install gevent`；

还需要安装：`pip install openai`。

克隆本项目之后，修改其中的api
```
client = OpenAI(
    api_key="sk-XXXXXXXXXXXXXXXXXXXXXX",  # API 密钥，请替换为您自己的 API Key。如何获取 API Key 的指南：https://cloud.tencent.com/document/product/1772/115970
    base_url=Base_url, # API 请求基础 URL，设置为上面配置的 Base_url
)
```


如果你使用的是其他云厂商提供的api和模型，请自行修改Base_url 和 Model_Type 
```
# API 配置参数
Base_url = "https://api.lkeap.cloud.tencent.com/v1"    # OpenAI API 请求地址，这里使用了腾讯云的 API 代理服务
Model_Type =  "deepseek-v3"    # 使用的模型类型，可选项包括"deepseek-v3" 或者其他模型

```
## 启动
1.确保python脚本启动

2.更改XUnity.AutoTranslator插件的AutoTranslatorConfig.ini或者Config.ini文件 

`[Service]
Endpoint=CustomTranslate
`

`[Custom]
Url=http://127.0.0.1:4000/translate
`

### 参考项目链接
`https://github.com/as176590811/XUnity.AutoTranslator-Sakura`
