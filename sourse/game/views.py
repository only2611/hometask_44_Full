from django.shortcuts import render

from game.functions import Game

# Create your views here.
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

        return render(request, "form.html", {"result": result})

    else:
        return render(request, "form.html",)




def history_stat(request):
    pass