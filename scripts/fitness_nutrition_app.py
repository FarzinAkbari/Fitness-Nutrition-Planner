import joblib

def load_model():
    model = joblib.load('model.pkl')
    return model

def predict_calories_needed(model, age, weight, height):
    prediction = model.predict([[age, weight, height]])
    return prediction[0]

if __name__ == "__main__":
    age = float(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    model = load_model()
    calories_needed = predict_calories_needed(model, age, weight, height)
    print(f"Calories needed: {calories_needed}")
~                                                                                                     ~                                                                                                     ~                                                     
