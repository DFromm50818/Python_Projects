# Schritt 1: Importieren der benötigten Bibliotheken
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Schritt 2: Daten generieren (hier verwenden wir zufällige Daten)
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1)

# Schritt 3: Modell initialisieren und trainieren
model = LinearRegression()
model.fit(X, y)

# Schritt 4: Vorhersagen treffen
X_test = np.array([[5]])  # Testdatenpunkt
predicted_y = model.predict(X_test)

# Schritt 5: Ergebnisse anzeigen
print("Vorhergesagter Wert für X_test:", predicted_y)

# Schritt 6: Visualisierung der Daten und der Regressionslinie
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.scatter(X_test, predicted_y, color='green', marker='o', s=200)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Lineare Regression')
plt.show()