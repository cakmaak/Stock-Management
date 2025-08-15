from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Stock
from .models import StockHistory
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required
def proddropdown(request):
    prod = Stock.objects.all()  # Tüm ürünleri çek

    if request.method == "POST":
        # JSON verisini alıyoruz
        import json
        data = json.loads(request.body)

        product_id = data.get("product_id")
        quantity = data.get("quantity")
        date_str = data.get("date")

        try:

           
            product = Stock.objects.get(id=product_id)  # Ürünü bul
            product.miktar += int(quantity)  # Stok miktarını artır
            product.save()  # Güncellenmiş stoğu kaydet

            try:
                date_added = datetime.strptime(date_str, '%Y-%m-%d')  # 'YYYY-MM-DD' formatında alıyoruz
            except ValueError:
                return JsonResponse({"success": False, "error": "Geçersiz tarih formatı!"})


  
    
            quantity = int(quantity)
            movements = "eklendi" if quantity>= 0 else "çikarildi"
            StockHistory.objects.create(
                stock=product,  # Hangi ürün olduğunu belirt
                quantity_added=quantity,  # Eklenen miktar,
                date_added=date_added,
                movements=movements,
                user=request.user

                
                
            )


            messages.success(request, f"{product.name} stoğu güncellendi. Yeni stok: {product.miktar}")

            # AJAX isteğine yanıt olarak JSON döndürüyoruz
            return JsonResponse({"success": True})

        except Stock.DoesNotExist:
            return JsonResponse({"success": False, "error": "Ürün bulunamadı!"})

        except ValueError:
            return JsonResponse({"success": False, "error": "Geçersiz miktar girdiniz!"})

    return render(request, "add.html", {"prod": prod})  # Sayfayı render et

    

def substock(request):
    prod = Stock.objects.all()  # Tüm ürünleri çek

    if request.method == "POST":
        # JSON verisini alıyoruz
        import json
        data = json.loads(request.body)

        product_id = data.get("product_id")
        quantity = data.get("quantity")
        date_str = data.get("date")

        try:

            product = Stock.objects.get(id=product_id)  # Ürünü bul
            product.miktar -= int(quantity)  # Stok miktarını artır
            product.save()  # Güncellenmiş stoğu kaydet
            try:
                date_added = datetime.strptime(date_str, '%Y-%m-%d')  # 'YYYY-MM-DD' formatında alıyoruz
            except ValueError:
                return JsonResponse({"success": False, "error": "Geçersiz tarih formatı!"})

            
            quantity = int(quantity)
            quantity = -abs(quantity)
            movements = "eklendi" if quantity>= 0 else "çikarildi"
           
            StockHistory.objects.create(
                stock=product,  # Hangi ürün olduğunu belirt
                quantity_added=quantity,  # Eklenen miktar,
                date_added=date_added,
                movements=movements

                
                
            )


            messages.success(request, f"{product.name} stoğu güncellendi. Yeni stok: {product.miktar}")

            
            return JsonResponse({"success": True})

        except Stock.DoesNotExist:
            return JsonResponse({"success": False, "error": "Ürün bulunamadı!"})

        except ValueError:
            return JsonResponse({"success": False, "error": "Geçersiz miktar girdiniz!"})

    return render(request, "sub.html", {"prod": prod})  
      
    
    


def liststock(request):
    stocks = Stock.objects.all()
    

    return render(request, 'curstock.html', {'stocks': stocks}) 

def mov(request):
    movements = StockHistory.objects.all().order_by('-date_added')
    return render(request, 'mov.html', {'movements': movements})

@login_required
def index(request):
    return render(request,'index.html')
