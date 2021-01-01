"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

*TL;DR
Provides a centralized entry point that controls and manages request handling.
"""


class MobileView:
    def show_index_page(self):
        print("Displaying mobile index page")


class TabletView:
    def show_index_page(self):
        print("Displaying tablet index page")


class Dispatcher:
    def __init__(self):
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()

    def dispatch(self, request):
        if request.type == Request.mobile_type:
            self.mobile_view.show_index_page()
        elif request.type == Request.tablet_type:
            self.tablet_view.show_index_page()
        else:
            print("Cannot dispatch the request")


class RequestController:
    """ front controller """

    def __init__(self):
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request):
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print("request must be a Request object")


class Request:
    """ request """

    mobile_type = "mobile"
    tablet_type = "tablet"

    def __init__(self, request):
        self.type = None
        request = request.lower()
        if request == self.mobile_type:
            self.type = self.mobile_type
        elif request == self.tablet_type:
            self.type = self.tablet_type


def main():
    """
    >>> front_controller = RequestController()

    >>> front_controller.dispatch_request(Request('mobile'))
    Displaying mobile index page

    >>> front_controller.dispatch_request(Request('tablet'))
    Displaying tablet index page

    >>> front_controller.dispatch_request(Request('desktop'))
    Cannot dispatch the request

    >>> front_controller.dispatch_request('mobile')
    request must be a Request object
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
