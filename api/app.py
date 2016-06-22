from os import getcwd

import falcon


class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        path = '{}/static/index.html'.format(getcwd())
        with open(path, 'r') as f:
            resp.body = f.read()


class ExampleResource(object):

    def on_post(self, req, resp):
        """ Handles POST requests """
        try:
            request_body = req.stream.read().decode('utf-8')
            print(request_body)
        except Exception as ex:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'Error'
            )

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = json.dumps({
            'Everything': 'awesome',
            'When': 'now',
            'PartOf': 'team'
        })


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Routes
app.add_route('/', StaticResource())
app.add_route('/example', ExampleResource())


def get_app():
    return app
