BOT_NAME = 'buildzoom'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

IMAGES_STORE = 'image'

COMMANDS_MODULE = 'commands'

EXTENSIONS = {
   'extensions.ConnectionExtension.ConnectionExtension': 1
}

ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'pipelines.BuildzoomPipeline.BuildzoomPipeline': 2,
}