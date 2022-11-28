import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import quiz.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
   'websocket': URLRouter(
     quiz.routing.websocket_urlpatterns
  )
})
