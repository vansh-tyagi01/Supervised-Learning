import pickle

with open('Predict_score.pkl', 'rb') as f:
    model = pickle.load(f)

name = input("Enter your name:")
hours = float(input("Enter your study hour?:"))

prediction = model.predict([[hours]])

print("Name :",name)
print("Hours :",hours)
print(f"Predicted Percentage : {prediction[0]:.2f}%")
