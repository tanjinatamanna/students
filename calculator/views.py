from django.shortcuts import render

def index(request):
    result = None
    expression = ""

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        try:
            # calculate result using Python's eval()
            result = eval(expression)
        except Exception:
            result = "Error"

    return render(request, "calculator/index.html", {
        "result": result,
        "expression": expression
    })
















