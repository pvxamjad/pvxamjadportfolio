from django.shortcuts import render,redirect
from portfolio.models import protfolio,Contact
from django.contrib import messages
import requests
from datetime import datetime

def main(request):

    data = protfolio.objects.all().order_by('-id')

    return render(request , 'index.html' ,{"data":data})

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=data)

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        number = request.POST.get('phone', '').strip()
        message = request.POST.get('comment', '').strip()

        # Basic validation
        if not name or not email or not message:
            messages.error(request, "Name, Email, and Message are required.")
            return redirect('/#contact')

        if number and not number.isdigit():
            messages.error(request, "Phone number should contain only digits.")
            return redirect('/#contact')
        
        now = datetime.now()
        formatted_datetime = now.strftime('%Y-%m-%d %I:%M:%S %p')

                # Send Telegram notification
        telegram_message = f"📩 *New Contact Form Submission*\n\n" \
                           f"🕒 Date & Time: {formatted_datetime}\n\n" \
                           f"👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {number}\n📝 Message: {message}"
        send_telegram_message(telegram_message)

        # Save to database
        Contact.objects.create(name=name, email=email, number=number, message=message)


        messages.success(request, "Your message has been sent successfully!")
        return redirect('/#contact')
    

TELEGRAM_BOT_TOKEN = "7275203631:AAFF_sdtbHmBo2Uq6Qt03m8U-h4T1edMfxI" 
TELEGRAM_CHAT_ID = "644097305" 

