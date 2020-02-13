import logging
import os


LOG_FORMAT = '[%(levelname)s] %(asctime)s\t%(message)s'
LOG_STORE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "result.log")
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler(LOG_STORE_FILE)
fh.setLevel(logging.ERROR)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter(LOG_FORMAT)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
log.addHandler(fh)
log.addHandler(ch)


if __name__ == '__main__':
    log.error("test")
