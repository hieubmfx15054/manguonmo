import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, OptionMenu
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class WaterPotabilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Potability Prediction")

        self.file_path = None
        self.model = None
        self.algorithm_var = StringVar(root)
        self.algorithm_var.set("KNN")

        # Load CSV Button
        Button(root, text="Load CSV File", command=self.load_file).grid(row=0, column=0, pady=10)
        self.file_label = Label(root, text="No file selected")
        self.file_label.grid(row=0, column=1, columnspan=2)

        # Algorithm selection
        Label(root, text="Select Algorithm:").grid(row=1, column=0, pady=10)
        OptionMenu(root, self.algorithm_var, "KNN", "Logistic Regression", "Decision Tree", "SVM").grid(row=1, column=1)

        # Train Model Button
        Button(root, text="Train Model", command=self.train_model).grid(row=1, column=2, pady=10)

        # Input fields for water properties
        self.entries = {}
        features = ["pH", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity",
                    "Organic Carbon", "Trihalomethanes", "Turbidity"]
        for i, feature in enumerate(features):
            Label(root, text=feature).grid(row=i+2, column=0)
            entry = Entry(root)
            entry.grid(row=i+2, column=1)
            self.entries[feature] = entry

        # Predict Button and result display
        Button(root, text="Predict", command=self.predict).grid(row=len(features) + 2, column=0, pady=10)
        self.result_label = Label(root, text="Prediction result will appear here")
        self.result_label.grid(row=len(features) + 2, column=1, columnspan=2)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(title="Select file", filetypes=[("CSV files", "*.csv")])
        self.file_label.config(text=self.file_path.split("/")[-1] if self.file_path else "No file selected")

    def train_model(self):
        if not self.file_path:
            self.result_label.config(text="Please select a file first")
            return

        data = pd.read_csv(self.file_path)
        data.dropna(inplace=True)

        X = data.drop('Potability', axis=1)
        y = data['Potability']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        algorithm = self.algorithm_var.get()
        if algorithm == 'KNN':
            self.model = KNeighborsClassifier()
        elif algorithm == 'Logistic Regression':
            self.model = LogisticRegression(max_iter=1000)
        elif algorithm == 'Decision Tree':
            self.model = DecisionTreeClassifier()
        elif algorithm == 'SVM':
            self.model = SVC()
        else:
            self.result_label.config(text="Invalid algorithm selected")
            return

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        self.result_label.config(text=f"{algorithm} Model Accuracy: {accuracy:.2f}")

    def predict(self):
        if not self.model:
            self.result_label.config(text="Please train the model first")
            return

        # Collect input values for prediction
        input_data = []
        for feature, entry in self.entries.items():
            try:
                value = float(entry.get())
                input_data.append(value)
            except ValueError:
                self.result_label.config(text=f"Invalid value for {feature}")
                return

        prediction = self.model.predict([input_data])[0]
        self.result_label.config(text=f"Prediction: {'Potable' if prediction == 1 else 'Not Potable'}")

# Initialize the GUI application
root = Tk()
app = WaterPotabilityApp(root)
root.mainloop()
