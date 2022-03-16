from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_animation import AnimationView
from web.views_board import BoardView
from web.views_comedy import ComedyView
from web.views_description import DescriptionView
from web.views_documentary import DocumentaryView
from web.views_fantasy import FantasyView
from web.views_horror import HorrorView
from web.views_mystery import MysteryView
from web.views_romance import RomanceView
from web.views_sf import SFView
from web.views_thriller import ThrillerView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(RomanceView);
urlpatterns.register(FantasyView);
urlpatterns.register(ThrillerView);
urlpatterns.register(ComedyView);
urlpatterns.register(SFView);
urlpatterns.register(HorrorView);
urlpatterns.register(MysteryView);
urlpatterns.register(DocumentaryView);
urlpatterns.register(AnimationView);
urlpatterns.register(DescriptionView);
urlpatterns.register(BoardView);

