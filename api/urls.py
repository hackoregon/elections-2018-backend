from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'transactions', views.TransactionsViewSet)
router.register(r'transactiondetail', views.TransactionDetailViewSet)
router.register(r'statementoforg', views.StatementOfOrgViewSet)
router.register(r'payee', views.PayeeViewSet)
router.register(r'electionactivity', views.ElectionActivityViewSet)
router.register(r'donor', views.DonorViewSet)
router.register(r'committeeslist', views.CommitteesListViewSet)
router.register(r'committeehistory', views.CommitteeHistoryViewSet)
router.register(r'ballots', views.BallotsViewSet)

schema_view = get_swagger_view(title="elections API")

urlpatterns = [
    url(r'^schema/', schema_view),
    url(r'^api/', include(router.urls)),
]
