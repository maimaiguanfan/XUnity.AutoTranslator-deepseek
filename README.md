
# XUnity.AutoTranslator-deepseek

本项目通过调用DeepSeek V3 API，实现Unity游戏中日文文本的自动翻译。

## 分支特性

- **采用流式接收文案，防止说完就撤回。**
- **自动识别文案是否被云服务商和谐。**
- **支持文案被和谐后自动更换云服务商重试。**
- 支持[腾讯云DeepSeek V3](https://console.cloud.tencent.com/lkeap/api)和[原版DeepSeek V3](https://platform.deepseek.com/)。
- 不完全支持[阿里云DeepSeek V3](https://bailian.console.aliyun.com/?tab=model#/api-key)**（未充分测试）**。
- 优化标点符号预处理。
- 删去对译文的重复文字检查功能。
- 删去对译文的日文字符检查功能。
- 调整模型参数；动态调整token上限；调整temperature到更适合做翻译工作的值，让语言更多样、更华丽（有极少数可能出现有不太符合常识的词）

**推荐**：配置翻译时使用的[云服务商的顺序](#jump1)按**首次腾讯云**，**第二、三次原版DeepSeek**。

## 准备工作

### 1. 获取API密钥
- 访问[腾讯云API控制台](https://console.cloud.tencent.com/lkeap/api)或[DeepSeek开放平台](https://platform.deepseek.com/)申请DeepSeek的API密钥。
- 也可以使用其他平台提供的DeepSeek API。

### 2. 安装依赖
确保已安装以下软件和库：
- **XUnity.AutoTranslator**
- **Python 3.x**

安装必要的Python库：

- **Ubuntu24.04**
```bash
sudo apt install python3-flask python3-gevent python3-openai
```
- **其他**
```bash
pip install Flask gevent openai
```

### 3. 修改配置文件
克隆本项目后，取消追踪 `config.json`
```bash
git update-index --assume-unchanged config.json
```
类似的，可以取消追踪 `dictionary.json`
```bash
git update-index --assume-unchanged dictionary.json
```

直接Download本项目者无需进行上述操作。

#### 3.1 配置API
修改 `api_key` 为你的API密钥
```json
    "deepseek": {
      "api_key": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "base_url": "https://api.deepseek.com/v1",
      "model_type": "deepseek-chat"
    }
```

#### 3.2 <span id="jump1">配置使用云服务商的顺序</span>
默认首次翻译时选择腾讯，第二次和第三次选择官网DeepSeek。
```json
  "api_priority": ["tencent", "deepseek", "deepseek"],
```

可自行增加或删减重试的次数，可自行添加其他服务商。

#### 3.3 配置额外提示词
这部分会随着主提示词一起发送给AI。你可以填写任何你想和AI说的，例如游戏包含的角色风格、翻译的格式例外。
```json
  "prompt_user": "格式例外：XXXXXX",
```
#### 3.4 配置字典路径
字典路径 `dict_path` ，建议字典仅用于固定人名、技能名称、物品名称，剩下交给AI自由发挥。
```json
  "dict_path": "./dictionary.json"
```

## 启动项目

### 1. 启动Python脚本
运行方式：
```bash
python run_app.py
```
正确运行时命令行应显示：
```text
[配置重载]config已重新加载，修改时间: xxx xxx
[配置重载]config文件监视器已启动，每 5 秒检查一次更新
[配置重载]dictionary已重新加载，修改时间: xxx xxx，共 xxx 条记录
[配置重载]dictionary文件监视器已启动，每 5 秒检查一次更新
[服务启动]翻译服务在 http://127.0.0.1:4000/translate 上启动
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
