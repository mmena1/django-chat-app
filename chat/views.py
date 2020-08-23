from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'chat/index.html')


class RoomView(View):
    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'room_name': kwargs['room_name']
        })