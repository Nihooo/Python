# logging模块 日志操作
import logging

# 日志级别 debug < info < warning < error < critical

# logging.basicConfig(
#     level=logging.DEBUG, # 最低显示级别
#     filename='logger.log', # 生成文件保存信息，默认追加模式
#     filemode='w', # 改变写入模式
#     format="%(asctime)s %(filename)s [%(lineno)d] %(message)s" # 日志格式
# )

# format参数中可能用到的格式化串：
# %(name)s            Logger的名字
# %(levelno)s         数字形式的日志级别
# %(levelname)s       文本形式的日志级别
# %(pathname)s        调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s        调用日志输出函数的模块的文件名
# %(module)s          调用日志输出函数的模块名
# %(funcName)s        调用日志输出函数的函数名
# %(lineno)d          调用日志输出函数的语句所在的代码行
# %(created)f         当前时间，用UNIX标准的表示时间的浮点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d          线程ID。可能没有
# %(threadName)s      线程名。可能没有
# %(process)d         进程ID。可能没有
# %(message)s         用户输出的消息

# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")



# logger对象,尽量用它
'''
def logger():
    loggername = logging.getLogger()
    
    fh = logging.FileHandler('test_log') # 向文件里发送内容
    ch = logging.StreamHandler() # 向屏幕发送内容
    
    fm = logging.Formatter("%(asctime)s %(message)s") # 日志格式
    
    fh.setFormatter(fm) # 设置格式
    ch.setFormatter(fm)
    
    loggername.addHandler(fh)
    loggername.addHandler(ch)
    loggername.setLevel("DEBUG") # 设置级别
    
    return loggername

# 默认为warning开始
logger = logger()

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
'''

'''
logger1 = logging.getLogger('mylogger') # 默认为root，设置子对象mylogger，当其父对象也在工作时，输出时，也会将父对象打印一遍
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO) # mylogger子用户以最后设置为准，而不是分开

fh = logging.FileHandler('test_log_new')  # 向文件里发送内容
ch = logging.StreamHandler()

logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')
'''
