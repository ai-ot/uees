from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
def train_svm(X_train, y_train):
return SVC(kernel='rbf', C=1.0, gamma='scale', class_weight='balanced', random_state=42).fit(X_train, y_train)
def train_tree(X_train, y_train):
return DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
def train_logistic(X_train, y_train):
return LogisticRegression(class_weight='balanced', random_state=42).fit(X_train, y_train)
def evaluate_model(model, X_test, y_test, model_name, save_path=None):
y_pred = model.predict(X_test)
print(f"\n=== {model_name} ===")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
if save_path:
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Matriz de Confusión - {model_name}')
plt.ylabel('Real')
plt.xlabel('Predicho')
plt.savefig(save_path, bbox_inches='tight')
plt.close()
