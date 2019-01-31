import falcon


class ThingsResource(object):
    def on_get(self, req, resp, name='I am Version 2'):
        resp.media = {'version': name}
        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200


things = ThingsResource()


