from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from spiders.djursbo_dk_crawler import DjursboDkCrawler

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

runner.crawl(DjursboDkCrawler)

d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
