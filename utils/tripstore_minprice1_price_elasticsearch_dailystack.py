import schedule
import time
import tripstore_minprice1_price_elasticsearch
import tripstore_minprice1_price_busyfilter
import tripstore_minprice1_price_twosigmatest

def job1():
    return tripstore_minprice1_price_elasticsearch.minprice1_elasticsearch()
    # minprice1의 함수를 불러옴

def job2():
    return tripstore_minprice1_price_busyfilter.busy_filter()
    # minprice1의 함수를 불러옴

def job3():
    return tripstore_minprice1_price_twosigmatest.minprice_ts_func_()
    # minprice1의 함수를 불러옴

schedule.every().day.at("10:43").do(job1)
schedule.every().day.at("11:43").do(job2)
schedule.every().day.at("12:44").do(job3)



while True:
    schedule.run_pending()
    time.sleep(1)