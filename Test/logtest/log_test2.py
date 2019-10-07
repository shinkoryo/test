import logging

logger = logging.getLogger("logger")    #logger名loggerを取得
logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで

#handler1を作成
handler2 = logging.FileHandler(filename="test1.log")  #handler2はファイル出力
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

#handler2を作成
handler2 = logging.FileHandler(filename="test.log")  #handler2はファイル出力
handler2.setLevel(logging.WARN)     #handler2はLevel.WARN以上
handler2.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

#loggerに2つのハンドラを設定
logger.addHandler(handler1)
logger.addHandler(handler2)

#出力処理
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")