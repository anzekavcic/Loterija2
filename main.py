#!/usr/bin/env python
import os
import jinja2
import webapp2
from random import randint


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):

        return self.render_template("hello.html",)

class LotoHandler(MainHandler):
    def get(self):

        view_vars = {
            "loto1": randint(1, 40),
            "loto2": randint(1, 40),
            "loto3": randint(1, 40),
            "loto4": randint(1, 40),
            "loto5": randint(1, 40),
            "loto6": randint(1, 40),
            "loto7": randint(1, 40),
            "loto8": randint(1, 40),
        }
        return self.render_template("loto.html", view_vars)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route("/loto", LotoHandler)
], debug=True)