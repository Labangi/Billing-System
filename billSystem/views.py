from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from .models import User, Training, BillInfo

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def logout(request):
    if "aec" in request.session:
        del request.session["aec"]
    return redirect("index")


def services(request):
    return render(request, "services.html")


def about_us(request):
    return render(request, "about_us.html")


def contact(request):
    return render(request, "contact.html")


def admin_dashboard(request):
    return render(request, "admin.html")


def loginn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        user_obj = User.objects.filter(username=username, pwd=pwd).first()

        if user_obj:
            request.session["aec"] = user_obj.id
            return redirect("admin_dashboard")

    return redirect("index")


def add_customer(request):
    if request.method == "POST":
        User.objects.create(
            username=request.POST.get("username"),
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            pwd=request.POST.get("password"),
            role=request.POST.get("role")
        )
        return redirect("view_users")

    return render(request, "insert.html")


def view_users(request):

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        new_role = request.POST.get("new_role")

        user_obj = get_object_or_404(User, id=user_id)
        user_obj.role = new_role
        user_obj.save()

        return redirect("view_users")

    users = User.objects.all().order_by("-created_at")

    return render(request, "view_users.html", {
        "users": users
    })


def training_bills(request):
    trainings = Training.objects.all().order_by("-id")

    return render(request, "training_bills.html", {
        "trainings": trainings
    })


def reminder(request):

    today = date.today()
    next_7_days = today + timedelta(days=7)

    due_soon_bills = BillInfo.objects.filter(
        due_date__range=[today, next_7_days],
        status="Pending"
    )

    overdue_bills = BillInfo.objects.filter(
        due_date__lt=today,
        status="Pending"
    )

    return render(request, "reminder.html", {
        "due_soon_bills": due_soon_bills,
        "overdue_bills": overdue_bills
    })
