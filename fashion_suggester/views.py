from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
import os
from .models import UserPrediction
import pandas as pd
import joblib
from django.http import JsonResponse



# Define the path to your model
MODEL_PATH = 'models/fashion_model.pkl'

# Load the model at startup
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print('Model loaded successfully.')
    except Exception as e:
        print(f'Error loading model: {str(e)}')
else:
    print('Model file not found.')

def home(request):
    return render(request, 'base/home.html')


@login_required
def dashboard(request):
    form = FeedbackForm()  # Create a new form instance
    return render(request, 'base/dashboard.html', {'form': form})
    
def redirect_to_dashboard(request):
    return redirect('dashboard')


@login_required
def user_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Handle the data as needed, e.g., save to the database
            return redirect('dashboard')  # Redirect after submission
    else:
        form = FeedbackForm()

    return render(request, 'fashion_suggester/feedback_suggestion.html', {'form': form})

@login_required
def feedback_suggestion(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            if model:
                try:
                    # Extract form data
                    data = form.cleaned_data
                    comfort_level = int(data['comfort_level'])
                    fit_sizing_level = int(data['fit_sizing_level'])
                    preferred_piece = data['preferred_piece']
                    design_style = data['design_style']
                    material_quality = data['material_quality']

                    # Print values to the console
                    print(f'Comfort Level: {comfort_level}')
                    print(f'Fit Sizing Level: {fit_sizing_level}')
                    print(f'Preferred Piece: {preferred_piece}')
                    print(f'Design Style: {design_style}')
                    print(f'Material Quality: {material_quality}')

                    # Prepare the data for the model
                    input_data_dict = {
                        'Comfort': [comfort_level],
                        'Fit & Sizing': [fit_sizing_level],
                        'Preferred Pieces': [preferred_piece],
                        'Design & Style': [design_style],
                        'Material Quality': [material_quality],
                    }

                    input_df = pd.DataFrame(input_data_dict)

                    # Get prediction from the model
                    prediction = model.predict(input_df)

                    # Mapping dictionary from numeric label to fashion type name
                    fashion_type_mapping = {
                        0: 'Casual',
                        1: 'Formal',
                        2: 'Bohemian',
                        3: 'Streetwear',
                        4: 'Athleisure'
                    }
                        
                    predicted_fashion_type = fashion_type_mapping.get(prediction[0], 'Unknown')

                    # Return JSON response with the prediction
                    response_data = {'prediction': predicted_fashion_type}
                    return JsonResponse(response_data)

                except Exception as e:
                    print(f'Error during processing: {str(e)}')
                    return JsonResponse({'success': False, 'error': 'An error occurred during processing.'})
            else:
                print('Model is not loaded. Please contact support.')
                return JsonResponse({'success': False, 'error': 'Model not found.'})
        else:
            print('Form is invalid. Please correct the errors and try again.')
            return JsonResponse({'success': False, 'error': 'Form is invalid.'})

    # If not a POST request, initialize an empty form
    form = FeedbackForm()
    return render(request, 'fashion_suggester/feedback_suggestion.html', {'form': form})

