import numpy as np
from sklearn.ensemble import RandomForestClassifier

class WastewaterQualityModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.is_trained = False

    def train(self):
        # Example synthetic training data (you can replace with real sensor data)
        # features: [turbidity, pH, TDS, temperature]
        X = np.array([
            [5, 7.0, 300, 25],   # cleanish greywater
            [20, 6.5, 600, 28],  # medium
            [50, 6.0, 1000, 30], # dirty
            [8, 7.2, 350, 24],   # high reuse
            [30, 6.8, 800, 29],  # medium
            [70, 5.8, 1500, 32], # poor
        ])

        # labels: 0 = High quality, 1 = Medium, 2 = Low
        y = np.array([0, 1, 2, 0, 1, 2])

        self.model.fit(X, y)
        self.is_trained = True

    def predict_quality(self, turbidity, pH, tds, temp):
        if not self.is_trained:
            self.train()

        x = np.array([[turbidity, pH, tds, temp]])
        prediction = self.model.predict(x)[0]
        return prediction


def generate_water_recommendation(quality_label):
    if quality_label == 0:
        return "Water quality is good. You can safely reuse it for gardening, toilet flushing, and general cleaning."
    elif quality_label == 1:
        return "Water quality is moderate. Basic filtration is recommended before reuse for cleaning or irrigation."
    else:
        return "Water quality is low. Treatment (sedimentation + filtration) is required before reuse."
