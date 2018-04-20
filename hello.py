from flask import Flask  # 导入Flask类，这个类的实例将会是我们的WSGI类
app = Flask(__name__)


@app.route('/')  # 使用route装饰器告诉Flask什么样的url触发我们的函数
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run()  # 使用run函数来让应用运行在本地服务器上

