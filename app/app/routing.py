from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from notifier import consumers

# This will replace the default django application in wsgi.py
# Now the application will pass through a router, which will
# determine if a request has to be passed to a websocket
# or HTTP protocol. Websocket will map to consumers
# as HTTP maps to views.  If HTTP is not defined, it will use the
# default django http routes to views
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/", consumers.AsyncChatConsumer),
            # path("ws/2", consumers.AnotherAsyncChatConsumer),
        ])
    )
})
