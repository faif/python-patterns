"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

*TL;DR
Provides a centralized entry point that controls and manages request handling.
"""

from __future__ import annotations

from typing import Any


class MobileView:
    def show_index_page(self) -> None:
        print("Displaying mobile index page")


class TabletView:
    def show_index_page(self) -> None:
        print("Displaying tablet index page")


class Dispatcher:
    def __init__(self) -> None:
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()

    def dispatch(self, request: Request) -> None:
        """
        This function is used to dispatch the request based on the type of device.
        If it is a mobile, then mobile view will be called and if it is a tablet,
        then tablet view will be called.
        Otherwise, an error message will be printed saying that cannot dispatch the request.
        """
        if request.type == Request.mobile_type:
            self.mobile_view.show_index_page()
        elif request.type == Request.tablet_type:
            self.tablet_view.show_index_page()
        else:
            print("Cannot dispatch the request")


class RequestController:
    """front controller"""

    def __init__(self) -> None:
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request: Any) -> None:
        """
        This function takes a request object and sends it to the dispatcher.
        """
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print("request must be a Request object")


class Request:
    """request"""

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
