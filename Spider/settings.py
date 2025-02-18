# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_test (+http://www.yourdomain.com)'weibo_spider

DOWNLOAD_DELAY = 10
TIME_DELAY = 30

# Pipelines config
ITEM_PIPELINES = {'Spider.pipelines.ScrapyWeiboPipeline': 300}


# MySql configuration
MYSQL_HOST = "localhost"
USER_NAME = "root"
PASSWORD = ""
DATABASE = "sina"
SQL_PATH = "Spider/mysql/mysql_init.sql"


