from api.utils.order_utility import get_order_summary
from rest_framework import status, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Customer, Order, OrderItem, Tracking
from .serializers import (OrderItemSerializer, OrderSerializer,
                          TrackingSerializer)


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stock to be viewed or edited.
    """
    queryset = OrderItem.objects.all().order_by('-id')
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tag to be viewed or edited.
    """
    admin_actions = [
        'On Hold', 'Confirmed',
        'Rejected', 'Packed', 'Dispatched',
        'Out for delivery', 'Delivered'
    ]
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-date_created')
        if self.request.user.is_staff is False:
            customer = Customer.objects.get(user=self.request.user)
            queryset = Order.objects.filter(
                customer=customer).order_by('-date_created')
        return queryset


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_history(request, orderId):
    try:
        queryset = Tracking.objects.filter(
            order_id=orderId).order_by('-event_date')
        serializer = TrackingSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_summary(request):
    try:
        queryset = Order.objects.order_by('-date_created')
        serializer = OrderSerializer(queryset, many=True)
        summary_data = get_order_summary(serializer.data)
        return Response(summary_data)

    except Exception as e:
        print(e)
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
