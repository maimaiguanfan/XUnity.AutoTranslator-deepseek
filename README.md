# XUnity.AutoTranslator-deepseek

本项目通过调用腾讯的DeepSeek V3 API，实现Unity游戏中日文文本的自动翻译。

## 准备工作

### 1. 获取API密钥
- 访问[腾讯云API控制台](https://console.cloud.tencent.com/lkeap/api)申请DeepSeek的API密钥（限时免费）。
- 也可以使用其他平台提供的DeepSeek API。

### 2. 安装依赖
确保已安装以下软件和库：
- **XUnity.AutoTranslator**
- **Python 3.x**

安装必要的Python库：
```bash
pip install Flask gevent openai
```

### 3. 配置API
克隆本项目后，修改deepseekv3.py中的`api_key`配置部分：
```python
client = OpenAI(
    api_key="sk-XXXXXXXXXXXXXXXXXXXXXX",  # 替换为您的API密钥
    base_url=Base_url,  # API请求基础URL
)
```

### 4. 自定义API配置
如果使用其他云厂商的API和模型，请修改以下配置：
```python
# API配置参数
Base_url = "https://api.lkeap.cloud.tencent.com/v1"  # OpenAI API请求地址
Model_Type = "deepseek-v3"  # 使用的模型类型
```

## 启动项目

### 1. 启动Python脚本
确保Python脚本成功启动，命令行应显示：
```
服务器在 http://127.0.0.1:4000 上启动
```

### 2. 配置XUnity.AutoTranslator
修改XUnity.AutoTranslator插件的配置文件`AutoTranslatorConfig.ini`或`Config.ini`：
```ini
[Service]
Endpoint=CustomTranslate

[Custom]
Url=http://127.0.0.1:4000/translate
```

## 参考项目
- [XUnity.AutoTranslator-Sakura](https://github.com/as176590811/XUnity.AutoTranslator-Sakura)

---

通过以上步骤，您可以轻松实现Unity游戏中日文文本的自动翻译。如有问题，请参考相关文档或联系开发者。
