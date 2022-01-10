from django.shortcuts import render
from rest_framework import generics
from core.models import Home, Services, UpcomingEvent, Structure, POs, AC, PMY, \
                        NLM, UBA, Awards, Reports, ActivityCalendar, \
                            Assets, VT, Sapling, BDC, Camp, Seminar, Others
from core.serializers import HomeSerializer, ServiceSerializer, UpcomingEventSerializer, \
                                StructureSerializer, POSerializer, ACSerializer, PMYSerializer, \
                                 NLMSerializer, UBASerializer,\
                                AwardsSerializer, ReportSerializer, ActivityCalendarSerializer, \
                                AssetSerializer, VTSerializer, SaplingSerializer, BDCSerializer, \
                                CampSerializer, SeminarSerializer, OtherSerializer

class HomeListView(generics.ListAPIView):
    """API view for Home"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class ServiceListView(generics.ListAPIView):
    """API view for """
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class UpcomingEventListView(generics.ListAPIView):
    """API view for upcoming events"""
    queryset = UpcomingEvent.objects.all()
    serializer_class = UpcomingEventSerializer

class StructureListView(generics.ListAPIView):
    """API view for upcoming events"""
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class POListView(generics.ListAPIView):
    """API view for PO"""
    queryset = POs.objects.all()
    serializer_class = POSerializer

class ACListView(generics.ListAPIView):
    """API view for AC"""
    queryset = AC.objects.all()
    serializer_class = ACSerializer

class PMYListView(generics.ListAPIView):
    """API view for PMY"""
    queryset = PMY.objects.all()
    serializer_class = PMYSerializer

# class DLListView(generics.ListAPIView):
#     """API view for DL"""
#     queryset = DL.objects.all()
#     serializer_class = DLSerializer

class NLMListView(generics.ListAPIView):
    """API view for NLM"""
    queryset = NLM.objects.all()
    serializer_class = NLMSerializer

# class SBMListView(generics.ListAPIView):
#     """API view for """
#     queryset = SBM.objects.all()
#     serializer_class = SBMSerializer

class UBAListView(generics.ListAPIView):
    """API view for UBA"""
    queryset = UBA.objects.all()
    serializer_class = UBASerializer

class AwardsListView(generics.ListAPIView):
    """API view for Awards"""
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class ReportListView(generics.ListAPIView):
    """API view for Reports"""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

class ActivityCalendarListView(generics.ListAPIView):
    """API view for Activity Calendar"""
    queryset = ActivityCalendar.objects.all()
    serializer_class = ActivityCalendarSerializer

class AssetListView(generics.ListAPIView):
    """API view for Assets"""
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer

class VTListView(generics.ListAPIView):
    """API view for VT"""
    queryset = VT.objects.all()
    serializer_class = VTSerializer

class SaplingListView(generics.ListAPIView):
    """API view for Sapling"""
    queryset = Sapling.objects.all()
    serializer_class = SaplingSerializer

class BDCListView(generics.ListAPIView):
    """API view for BDC"""
    queryset = BDC.objects.all()
    serializer_class = BDCSerializer

class CampListView(generics.ListAPIView):
    """API view for Camp"""
    queryset = Camp.objects.all()
    serializer_class = CampSerializer

class SeminarListView(generics.ListAPIView):
    """API view for Seminar"""
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer

class OtherListView(generics.ListAPIView):
    """API view for Seminar"""
    queryset = Others.objects.all()
    serializer_class = OtherSerializer