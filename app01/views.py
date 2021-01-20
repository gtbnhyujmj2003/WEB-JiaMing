from django.shortcuts import render, HttpResponse

# Create your views here.
def helloA(request):   # HttpResponse
    return HttpResponse("HttpResponse- You are OK-")

def helloB(request):   # Render
    # 使用 templates，要去settings註冊APPs

    # 中間的參數路徑，固定指向 app01/templates 下面，所以前面不用打
    # 第三個參數帶運算後的結果
    return render(request, 'CSS01/main.html', {})

def index(request):
    # 放好CSS檔案到static後，記得要重新設定CSS的路徑
    return render(request, 'CSS01/index.html', {})

