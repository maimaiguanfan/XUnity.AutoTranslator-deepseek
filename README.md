
# XUnity.AutoTranslator-deepseek

本项目通过调用 DeepSeek V3 API ，实现 Unity 游戏中日文文本的自动翻译。

## 分支特性

- **采用流式接收文案，防止说完就撤回。**
- **自动识别文案是否被云服务商和谐。**
- **支持文案被和谐后自动更换云服务商重试**（[点击](#jump1)查看详情）。
- 支持腾讯云 DeepSeek V3 和官网 DeepSeek V3 。
- 不完全支持阿里云 DeepSeek V3 **（未充分测试）**。
- 实时检测字典变化，无需重启翻译服务即可更新字典。
- 使用单独的 .json 文件存储 API keys，轻度用户无需对代码进行修改。
- 优化标点符号预处理。
- 动态调整每次发送翻译请求时的 token 上限。
- （可能是缺点）删去对译文的重复文字检查功能。
- （可能是缺点）删去对译文的日文字符检查功能。
- 调整模型参数；调整 temperature 到更适合做翻译工作的值，让语言更多样、更华丽（有极少数可能出现有不太符合常识的词。该值过高时，遇到过最离谱的表述是“这块豆腐像脑浆一样嫩滑”）。

## 准备工作

### 1. 获取 API 密钥
- 访问[腾讯云 API 控制台](https://console.cloud.tencent.com/lkeap/api)或[ DeepSeek 开放平台](https://platform.deepseek.com/)申请DeepSeek的API密钥。
- 也可以使用其他平台提供的符合 OpenAI 接口的 API ，例如[阿里云 DeepSeek ](https://bailian.console.aliyun.com/?tab=model#/api-key)。

### 2. 安装依赖
确保已安装以下软件和库：
- **XUnity.AutoTranslator**
- **Python 3.x**

安装必要的 Python 库：

- **Ubuntu24.04**
```bash
sudo apt install python3-flask python3-gevent python3-openai
```
- **其他**
```bash
pip install Flask gevent openai
```

### 3. 修改配置文件

#### 3.1 取消追踪配置文件（可选）
**仅限获取方式为 `git clone` 者**

取消追踪 `config.json`
```bash
git update-index --assume-unchanged config.json
```
类似的，可以取消追踪 `dictionary.json`
```bash
git update-index --assume-unchanged dictionary.json
```

直接Download本项目者无需进行上述操作。

#### 3.2 配置 API （必须）
修改 `api_key` 为你的API密钥
```json
    "deepseek": {
      "api_key": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "base_url": "https://api.deepseek.com/v1",
      "model_type": "deepseek-chat"
    }
```

#### 3.3 <span id="jump1">配置使用云服务商的顺序（必须）</span>
默认首次翻译时选择腾讯，翻译失败时，第二次选择官网 DeepSeek ，再次失败时第三次选择官网 DeepSeek 。
```json
  "api_priority": ["tencent", "deepseek", "deepseek"],
```

可自行增加或删减重试的次数，例如4次

#### 3.4 配置额外提示词（可选）
这部分会随着主提示词一起发送给 AI 。你可以填写任何你想和AI说的，例如游戏包含的角色风格、翻译的格式例外。
```json
  "prompt_user": "格式例外：XXXXXX",
```
#### 3.5 配置字典（可选）
字典文件 `dictionary.json` 。键为原文，值为译文。
```json
{
  "原文1": "译文1",
  "原文2": "译文2"
}
```
建议仅用于固定人名、地名、技能名称、物品名称，剩下交给AI自由发挥。

## 启动项目

### 1. 启动翻译服务
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
修改XUnity.AutoTranslator插件的配置文件 `AutoTranslatorConfig.ini` 或 `Config.ini` ：
```ini
[Service]
Endpoint=CustomTranslate
```
```ini
[Custom]
Url=http://127.0.0.1:4000/translate
```
如果支持低延迟模式建议打开
```ini
[Custom]
EnableShortDelay=True
```

## 参考项目
- [XUnity.AutoTranslator-Sakura](https://github.com/as176590811/XUnity.AutoTranslator-Sakura)
- [0001lizhubo/XUnity.AutoTranslator-deepseek](https://github.com/0001lizhubo/XUnity.AutoTranslator-deepseek)

---

通过以上步骤，您可以轻松实现 Unity 游戏中日文文本的自动翻译。如有问题，请参考相关文档或联系开发者。
