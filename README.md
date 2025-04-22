
# XUnity.AutoTranslator-deepseek

本项目通过调用DeepSeek V3 API，实现Unity游戏中日文文本的自动翻译。

## 分支特性

- **采用流式接收文案，防止说完就撤回。**
- **自动识别文案是否被云服务商和谐。**
- **支持文案被和谐后自动更换云服务商重试。**
- 支持[腾讯云DeepSeek V3]((https://console.cloud.tencent.com/lkeap/api))和[原版DeepSeek V3](https://platform.deepseek.com/)。
- 不完全支持[阿里云DeepSeek V3](https://bailian.console.aliyun.com/?tab=model#/api-key)**（未充分测试）**。
- 优化标点符号预处理。
- 删去对译文的重复文字检查功能。
- 删去对译文的日文字符检查功能。
- 调整模型参数。

个人推荐翻译顺序按首次用腾讯云，第二三次用原版DeepSeek。

## 准备工作

### 1. 获取API密钥
- 访问腾讯云API控制台或DeepSeek开放平台申请DeepSeek的API密钥。
- 也可以使用其他平台提供的DeepSeek API。

### 2. 安装依赖
确保已安装以下软件和库：
- **XUnity.AutoTranslator**
- **Python 3.x**

安装必要的Python库（Ubuntu24.04）：
```bash
sudo apt install python3-flask python3-gevent python3-openai
```
安装必要的Python库（其他）：
```bash
pip install Flask gevent openai
```

### 3. 配置API
克隆本项目后，修改deepseekv3.py中的`api_key`配置部分：
```python
xxxxx_client = OpenAI(
	api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	base_url="https://xxx.xxxxx.com/v1",
)
Model_Type_xxxxx =  "deepseek-xxx"
```
如果使用其他云厂商的API和模型，需要自己修改`base_url`和`Model_Type_xxxxx`

### 4. 配置使用云服务商的顺序
可以自定义首次请求翻译时的云服务商，以及翻译失败后重试的云服务商，例如：
```
API_PRIORITY = ["TENCENT", "DEEPSEEK", "DEEPSEEK"]
```
首次翻译时选择腾讯，第二次和第三次选择官网DeepSeek

### 5. 配置其他
例如字典路径`dict_path`和额外的提示词`prompt_user`，又或者修改使用的模型参数

## 启动项目

### 1. 启动Python脚本
确保Python脚本成功启动，命令行应显示：
```
翻译服务在 http://127.0.0.1:4000/translate 上启动
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
- [0001lizhubo/XUnity.AutoTranslator-deepseek](https://github.com/0001lizhubo/XUnity.AutoTranslator-deepseek)

---

通过以上步骤，您可以轻松实现Unity游戏中日文文本的自动翻译。如有问题，请参考相关文档或联系开发者。
