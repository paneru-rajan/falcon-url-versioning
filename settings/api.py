from falcon import API
import logging


class API(API):
    def __init__(self, versions=None, **kwargs):
        super().__init__(**kwargs)
        self.versions = versions
        self.auto_route()

    def auto_route(self):
        for version in self.versions:
            try:
                urls = getattr(__import__(version + '.urls').urls, 'urls')
                for route, instance in urls:
                    self.add_route('/{}/{}'.format(version, route.strip().strip('/')), instance)
            except ModuleNotFoundError as e:
                logging.exception(e)
