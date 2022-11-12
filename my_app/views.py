from django.contrib import messages
from django.shortcuts import render

from my_app.models import Cellphone, Computer, Accessorie
from my_app.forms import CellphoneForm, ComputerForm, AccessorieForm

def create_cellphones(request):
    if request.method == "POST":
        cellphone_form = CellphoneForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if cellphone_form.is_valid():
            data = cellphone_form.cleaned_data
            actual_objects = Cellphone.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                cellphone = Cellphone(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                cellphone.save()
                messages.success(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"cellphone": Cellphone.objects.all()},
                template_name="my_app/cellphone_list.html",
            )

    cellphone_form = CellphoneForm(request.POST)
    context_dict = {"form": cellphone_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/cellphone_form.html",
    )

def cellphones(request):
    return render(
        request=request,
        context={"cellphones": Cellphone.objects.all()},
        template_name="my_app/cellphone_list.html",
    )

def create_computers(request):
    if request.method == "POST":
        computer_form = ComputerForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if computer_form.is_valid():
            data = computer_form.cleaned_data
            actual_objects = Computer.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Computer {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                computer = Computer(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                computer.save()
                messages.success(
                    request,
                    f"Computer {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"computer": Computer.objects.all()},
                template_name="my_app/computer_list.html",
            )

    computer_form = ComputerForm(request.POST)
    context_dict = {"form": computer_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/computer_form.html",
    )

def computers(request):
    return render(
        request=request,
        context={"computers": Computer.objects.all()},
        template_name="my_app/computer_list.html",
    )

def create_accessories(request):
    if request.method == "POST":
        accessorie_form = AccessorieForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if accessorie_form.is_valid():
            data = accessorie_form.cleaned_data
            actual_objects = Accessorie.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Accessorie {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                accessorie = Accessorie(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                accessorie.save()
                messages.success(
                    request,
                    f"Accessorie {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"accessorie": Accessorie.objects.all()},
                template_name="my_app/accessorie_list.html",
            )

    accessorie_form = AccessorieForm(request.POST)
    context_dict = {"form": accessorie_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/accessorie_form.html",
    )

def accessories(request):
    return render(
        request=request,
        context={"accessories": Accessorie.objects.all()},
        template_name="my_app/accessorie_list.html",
    )
    
    
def test():
    pass 
