import os
import random
from django.shortcuts import render
from django.conf import settings

def store_view(request):
    base_dir = settings.BASE_DIR / 'static' / 'store'
    categories = ['Casual', 'Formal', 'Bohemian', 'Streetwear', 'Athleisure']
    selected_category = request.GET.get('category', 'All')
    selected_gender = request.GET.get('gender', 'All')

    images = []

    for category in categories:
        if selected_category != 'All' and category != selected_category:
            continue

        category_folder = os.path.join(base_dir, category)

        for image_name in os.listdir(category_folder):
            if image_name.startswith('m') or image_name.startswith('f'):
                gender = 'Male' if image_name.startswith('m') else 'Female'
                if selected_gender != 'All' and gender != selected_gender:
                    continue
                
                image_path = os.path.join('store', category, image_name)
                price = round(random.uniform(10.00, 100.00), 2)
                images.append({
                    'category': category,
                    'gender': gender,
                    'image_url': os.path.join(settings.STATIC_URL, image_path),
                    'price': price
                })

    context = {
        'images': images,
        'categories': categories,
        'selected_category': selected_category,
        'selected_gender': selected_gender
    }
    return render(request, 'store/store.html', context)
