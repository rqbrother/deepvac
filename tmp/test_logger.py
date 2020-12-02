import logging, os
import datetime

def gettime():
    time = (str(datetime.datetime.now())[:-10]).replace(" ", "_").replace(":", "-")
    return time

def main():
    if not os.path.exists('log'):
        os.makedirs('log')

    # logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("RoadParser")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("log/detection.log", mode='w')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug("this is debug ...")
    logger.info('this is info ...')
    logger.error('this is error ...')
    logger.warning('this is warning ...')
    logger.critical("this is critical ...")

    logger2 = logging.getLogger("log2")
    logger2.setLevel(logging.DEBUG)
    handler2 = logging.FileHandler("log/log2.log", mode='w')
    handler2.setLevel(logging.INFO)
    handler2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s %(message)s'))
    logger2.addHandler(handler2)

    logger2.debug("this is debug ...")
    logger2.info('this is info ...')
    logger2.error('this is error ...')
    logger2.warning('this is warning ...')
    logger2.critical("this is critical ...")



if __name__ == "__main__":
    main()