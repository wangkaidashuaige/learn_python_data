import logging,time

class framelog():
    def __init__(self,logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d")
        # 路径需要修改,为罕当前文件夹下
        self.log_path = "D:\\test_UI_project\\log\\"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()

    def log(self):
        return self.logger
if __name__ == '__main__':
    lo = framelog()
    log = lo.log()
    log.info("info")
    log.debug("debug")
    log.error("error")
    log.critical("critical")