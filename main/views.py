from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant
from .forms import ParticipantForm
from django.contrib.auth.hashers import check_password

def secret_santa_view(request):
    participants = Participant.objects.all()
    selected_participant = None
    form = ParticipantForm()

    # Handle the form submission to add a participant
    if request.method == 'POST' and 'join' in request.POST:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secret_santa')  # Reload the page after saving

    # Check if a participant is trying to view their assignment
    elif request.method == 'POST' and 'view_assignment' in request.POST:
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            participant = Participant.objects.get(name=name)
            if check_password(password, participant.password):
                selected_participant = participant
            else:
                selected_participant = "Incorrect password"
        except Participant.DoesNotExist:
            selected_participant = "Participant not found"

    return render(request, 'main/secret_santa.html', {
        'participants': participants,
        'selected_participant': selected_participant,
        'form': form,
    })