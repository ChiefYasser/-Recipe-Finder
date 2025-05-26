from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.db.models import Q

from datetime import date

def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query)
        )
    else:
        contacts = Contact.objects.all()

    today = date.today()
    birthdays_today = contacts.filter(birthday__month=today.month, birthday__day=today.day)

    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts,
        'birthdays_today': birthdays_today,
    })


def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        birthday = request.POST.get('birthday') or None
        address = request.POST.get('address') or None  # ✅ Get address

        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            birthday=birthday,
            address=address  # ✅ Save address
        )
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_form.html')

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.birthday = request.POST.get('birthday') or None
        contact.address = request.POST.get('address') or None  # ✅ Update address

        contact.save()
        return redirect('contact_list')

    return render(request, 'contacts/contact_form.html', {'contact': contact})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})

