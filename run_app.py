import concurrent.futures  # 导入 concurrent.futures，用于线程池
from flask import Flask, request  # 导入 Flask 库，用于创建 Web 应用，需要安装：pip install Flask
from gevent.pywsgi import WSGIServer  # 导入 gevent 的 WSGIServer，用于提供高性能的异步服务器，需要安装：pip install gevent
from queue import Queue  # 导入 Queue，用于创建线程安全的队列
from translation_service import TranslationService

app = Flask(__name__) # 创建 Flask 应用实例
translation_service = TranslationService()

@app.route('/translate', methods=['GET'])
def translate():
    """同步接口（优化打印逻辑）"""
    text = request.args.get('text')
    
    print(f"\033[36m[原文]\033[0m \033[35m{text}\033[0m")
    
    translation_queue = Queue()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            translation_service.handle_translation,
            text,
            translation_queue
        )
        try:
            future.result(timeout=30)
            result = translation_queue.get()
            
            if result.startswith("[ERROR]"):
                return result, 500
                  
            print(f"\n\033[36m[译文]\033[0m \033[1;32m{result}\n\033[0m")
            return result
            
        except concurrent.futures.TimeoutError:
            return "[ERROR]翻译超时", 500
        except Exception as e:
            return f"[ERROR]系统错误: {str(e)}", 500

def main():
    """
    主函数，启动 Flask 应用和 gevent 服务器。
    """
    print("\033[33m[服务启动]翻译服务在 http://127.0.0.1:4000/translate 上启动\n\033[0m") # 打印服务器启动信息，提示用户访问地址
    http_server = WSGIServer(('127.0.0.1', 4000), app, log=None, error_log=None) # 创建 gevent WSGIServer 实例，监听 127.0.0.1:4000 端口，使用 Flask app 处理请求，禁用访问日志和错误日志 (log=None, error_log=None)
    http_server.serve_forever() # 启动 gevent 服务器，无限循环运行，等待和处理客户端请求

if __name__ == '__main__':
    main() # 当脚本作为主程序运行时，调用 main 函数启动服务器
