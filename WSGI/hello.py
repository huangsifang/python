def application(environ, start_response): # 符合WSGI标准的一个HTTP处理函数
    start_response('200 OK', [('Content-Type', 'text/html')]) # 发送了HTTP响应的Header，注意Header只能发送一次
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# HTTP请求的所有输入信息都可以通过environ获得
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body