from django import forms

class FeedbackForm(forms.Form):
    comfort_level = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], label="Comfort Level")
    fit_sizing_level = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], label="Fit Sizing Level")
    preferred_piece = forms.ChoiceField(choices=[(piece, piece) for piece in [
        "T-shirt", "Suit", "Maxi Dress", "Hoodie", "Leggings", "Jeans", "Blazer", "Embroidered Top", "Joggers", 
        "Sports Bra", "Dress Shirt", "Flowy Skirt", "Graphic Tee", "Track Pants", "Polo Shirt", "Tuxedo", 
        "Fringe Dress", "Sweatshirt", "Yoga Pants", "Casual Dress", "Boho Blouse", "Track Jacket", "Gym Shorts", 
        "Button-up Shirt", "Gown", "Tunic", "Sweatpants", "Running Shoes", "Tank Top", "Evening Dress", "Boho Skirt", 
        "Baseball Cap", "Sweat-wicking Tee", "Shorts", "Cocktail Dress", "Crochet Top", "Snapback", 
        "Compression Leggings", "Henley Shirt", "Suit Dress", "Embroidered Skirt", "Sport Shorts", 
        "Formal Shirt", "Maxi Skirt", "Cargo Pants", "Athletic Jacket"]], label="Preferred Piece")
    design_style = forms.ChoiceField(choices=[(style, style) for style in ["Simple", "Elegant", "Artistic", "Bold Graphics", "Stylish"]], label="Design Style")
    material_quality = forms.ChoiceField(choices=[(quality, quality) for quality in ["Poor", "Average", "Good", "Excellent"]], label="Material Quality")
