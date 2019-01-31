import falcon


class ThingsResource(object):
    def on_get(self, req, resp, name=''):
        resp.media = {'name': name}
        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200


things = ThingsResource()
