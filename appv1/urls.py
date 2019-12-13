from rest_framework import routers
from .views import BankViewSet, BranchViewSet

router = routers.DefaultRouter()
router.register(r'bank', BankViewSet)
router.register(r'branches', BranchViewSet)


