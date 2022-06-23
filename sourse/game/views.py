from django.shortcuts import render

from game.functions import Game

# Create your views here.

history_list = []

def index_view(request):
    if request.method == "POST":
        numbers_str = request.POST.get("numbers")
        nums = numbers_str.split()
        game = Game()
        error = game.validation(nums)
        if error:
            result = error
        else:
            result = game.results()
            history_list.append(f"введены следующие цифры {numbers_str}, а вот результат: {result}")
        return render(request, "form.html", {"result": result, "nums": numbers_str, "secret_numbers": game.secret_numbers})
    else:
        return render(request, "form.html",)




def history_stat(request):
    return render(request, "history.html", {"history_list": history_list})