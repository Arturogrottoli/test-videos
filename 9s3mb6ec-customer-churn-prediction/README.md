# 9s3mb6ec — Customer Churn Prediction

Guion paso a paso para grabar la tarea **9s3mb6ec**: armar en **Google Colab**, con **pandas** y un **árbol de decisión** (*Decision Tree*) de scikit-learn, un flujo de predicción de abandono de clientes (*churn*). Usa un dataset sintético de 200 clientes. El trabajo incluye preparar los datos, entrenar el modelo, hacer predicciones, evaluarlas y sacar ideas para retener clientes. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **23 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.
- **[ENTRE CORCHETES]** van los números del modelo, que tenés que anotar al ensayar (ver "Antes de grabar").

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, comparalo con el campo **Describe your idea** de la tarea. El dataset lo generé yo: es sintético, con 200 clientes inventados.

---

## Archivos de la carpeta

```
9s3mb6ec-customer-churn-prediction/
├── README.md               ← este guion
├── customers.csv           ← dataset de partida: 200 clientes sintéticos
└── churn_prediction.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook** y seleccionás `churn_prediction.ipynb`. Después subís `customers.csv` desde el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`customers.csv` tiene 200 clientes **sintéticos** de una empresa de suscripción, con 6 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `customer_id` | Identificador del cliente (C001 a C200) |
| `tenure_months` | Meses que lleva como cliente |
| `monthly_charges` | Cuánto paga por mes, en dólares (6 valores vacíos a propósito) |
| `contract` | Tipo de contrato: `Month-to-month`, `One year` o `Two year` |
| `support_calls` | Llamadas a soporte |
| `churn` | Si se dio de baja: `Yes` o `No`. **Es lo que queremos predecir** |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. **Ejecutá el notebook de referencia en Colab y anotá los números del modelo**: accuracy, matriz de confusión, las dos o tres variables más importantes y el primer cliente de la lista de riesgo. Con `random_state=42` salen siempre iguales, así que los podés decir con seguridad. Completá los **[CORCHETES]** de este guion con esos números.
3. Practicá una vez entera en un notebook nuevo, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá.
4. Dejá tres pestañas abiertas en Firefox, en este orden: el documento **Goal**, el sitio de scikit-learn (https://scikit-learn.org) y Colab (https://colab.research.google.com). Tené `customers.csv` en una carpeta fácil de encontrar. Agrandá el zoom (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst for a customer retention team, I'll build a churn prediction workflow in Google Colab. I'll prepare 200 customer records, train a Decision Tree, evaluate its predictions, and find customers who may be at risk of leaving.
>
> (Como analista de datos de un equipo de retención de clientes, voy a armar un flujo de predicción de abandono en Google Colab. Voy a preparar 200 registros de clientes, entrenar un árbol de decisión, evaluar sus predicciones y encontrar clientes que podrían estar en riesgo de irse.)

---

## 0:45–4:30 — scikit-learn, Colab y cargar los datos

> 🖱️ I'm clicking the second browser tab, at the top of the window, to show the scikit-learn website.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para mostrar el sitio de scikit-learn.)
>
> 🟢 Churn means a customer stops using a service. Keeping a customer is usually cheaper than finding a new one, so predicting churn helps a company act in time.
>
> (Churn significa que un cliente deja de usar un servicio. Retener a un cliente suele ser más barato que conseguir uno nuevo, así que predecir el abandono ayuda a una empresa a actuar a tiempo.)
>
> 🟢 This is scikit-learn, the most popular Python library for machine learning. I'll use its Decision Tree classifier. A decision tree learns simple yes-or-no questions from the data, like "is the contract month-to-month?", and follows them to a prediction. That makes it easy to explain to a business team.
>
> (Esto es scikit-learn, la librería de machine learning más popular de Python. Voy a usar su clasificador de árbol de decisión. Un árbol de decisión aprende preguntas simples de sí o no a partir de los datos, como "¿el contrato es mensual?", y las sigue hasta llegar a una predicción. Eso lo hace fácil de explicar a un equipo de negocio.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab runs Python notebooks in the browser, in Google's cloud. pandas and scikit-learn are already installed, so there's nothing to set up.
>
> (Google Colab ejecuta notebooks de Python en el navegador, en la nube de Google. pandas y scikit-learn ya vienen instalados, así que no hay nada que configurar.)
>
> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing churn_prediction.ipynb, to identify this project.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo churn_prediction.ipynb, para identificar este proyecto.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing customers.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo customers.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Customer Churn Prediction
Dataset: 200 synthetic customer records. Goal: train a Decision Tree to predict which customers may leave, evaluate it, and find customers at risk.
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads the libraries and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que carga las librerías y los datos.)

Escribís la **celda 1**:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("customers.csv")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot to draw charts.
- 🟢 `from sklearn.model_selection import train_test_split`: this imports the function that splits the data into a training set and a testing set.
- 🟢 `from sklearn.tree import DecisionTreeClassifier, plot_tree`: this imports the Decision Tree model and a function to draw it.
- 🟢 `from sklearn.metrics import ...`: these three functions measure how good the predictions are.
- 🟢 `df = pd.read_csv("customers.csv")`: this reads the uploaded file into a DataFrame called df.
- 🟢 `df.head()`: this shows the first five customers, to check the data loaded correctly.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar los datos.)
>
> 🟢 Each row is one customer: how many months they've been a customer, their monthly charge, their contract type, how many times they called support, and whether they churned.
>
> (Cada fila es un cliente: cuántos meses lleva como cliente, su cargo mensual, su tipo de contrato, cuántas veces llamó a soporte y si se dio de baja.)

---

## 4:30–9:00 — Inspeccionar y preparar los datos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that checks the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que revisa los datos.)

Escribís la **celda 2**:

```python
df.info()
print(df.isna().sum())
print(df["churn"].value_counts())
```

**What each line does:**

- 🟢 `df.info()`: this lists every column with its number of values and its data type.
- 🟢 `print(df.isna().sum())`: isna marks each empty cell, and sum counts them per column.
- 🟢 `print(df["churn"].value_counts())`: value_counts counts how many customers churned and how many stayed.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)
>
> 🟢 We have 200 customers and 6 columns. monthly_charges has 6 missing values. And 82 customers churned while 118 stayed, so about 41 percent churned. The two groups are not perfectly balanced, which I'll keep in mind when I split the data.
>
> (Tenemos 200 clientes y 6 columnas. monthly_charges tiene 6 valores faltantes. Y 82 clientes se dieron de baja mientras que 118 se quedaron, así que cerca del 41 por ciento abandonó. Los dos grupos no están perfectamente equilibrados, y lo voy a tener en cuenta al dividir los datos.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for data preparation.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la preparación de datos.)

Escribís `## 2. Prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that prepares the data for the model.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que prepara los datos para el modelo.)

Escribís la **celda 3**:

```python
df["monthly_charges"] = df["monthly_charges"].fillna(df["monthly_charges"].median())
df["churn"] = df["churn"].map({"Yes": 1, "No": 0})
print(df.groupby("contract")["churn"].mean().round(2))
```

**What each line does:**

- 🟢 `df["monthly_charges"] = ...fillna(...median())`: fillna fills the 6 missing charges with the median charge. I use the median because it isn't affected by very high or very low values, and I keep all 200 customers.
- 🟢 `df["churn"] = df["churn"].map({"Yes": 1, "No": 0})`: models work with numbers, not words, so map turns Yes into 1 and No into 0.
- 🟢 `print(df.groupby("contract")["churn"].mean().round(2))`: since churn is now 1 or 0, its average per contract type is the churn rate of that group.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to prepare the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para preparar los datos.)
>
> 🟢 This is already a strong insight: about 70 percent of month-to-month customers churned, but only about 15 percent of one-year customers and 8 percent of two-year customers.
>
> (Esto ya es un hallazgo fuerte: cerca del 70 por ciento de los clientes con contrato mensual se dieron de baja, pero solo cerca del 15 por ciento de los de contrato anual y el 8 por ciento de los de dos años.)

---

## 9:00–12:30 — Variable objetivo, variables y división de los datos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the target and the features.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la variable objetivo y las variables.)

Escribís `## 3. Target and features`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that separates what we predict from what we use to predict it.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que separa lo que predecimos de lo que usamos para predecirlo.)

Escribís la **celda 4**:

```python
y = df["churn"]
X = pd.get_dummies(df.drop(columns=["customer_id", "churn"]), columns=["contract"])
X.head()
```

**What each line does:**

- 🟢 `y = df["churn"]`: y is the target variable, the answer we want to predict: did the customer churn?
- 🟢 `X = pd.get_dummies(df.drop(columns=["customer_id", "churn"]), columns=["contract"])`: X holds the features, the information the model uses to predict. drop removes customer_id, because an ID says nothing about behavior, and churn, because that's the answer. get_dummies turns the contract text into three yes-or-no columns, one for each contract type, because the model needs numbers.
- 🟢 `X.head()`: this shows the first rows of the features.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to build the features.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para armar las variables.)
>
> 🟢 Now we have six features: tenure, monthly charges, support calls, and the three contract columns, with True or False.
>
> (Ahora tenemos seis variables: antigüedad, cargo mensual, llamadas a soporte y las tres columnas de contrato, con True o False.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the split.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la división.)

Escribís `## 4. Split into training and testing sets`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that splits the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que divide los datos.)

Escribís la **celda 5**:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print(X_train.shape, X_test.shape)
```

**What each line does:**

- 🟢 `train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)`: this splits the customers into two groups. The model learns from 75 percent of them, the training set, and I test it on the other 25 percent, which it has never seen. That's how we know if it works on new customers. random_state fixes the random split, so I get the same result every time. stratify keeps the same share of churners in both groups.
- 🟢 `print(X_train.shape, X_test.shape)`: this shows the size of each group.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to split the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dividir los datos.)
>
> 🟢 150 customers for training and 50 for testing, each with 6 features.
>
> (150 clientes para entrenar y 50 para probar, cada uno con 6 variables.)

---

## 12:30–17:00 — Entrenar, predecir y evaluar

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for training.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el entrenamiento.)

Escribís `## 5. Train a Decision Tree`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that trains the model and draws it.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que entrena el modelo y lo dibuja.)

Escribís la **celda 6**:

```python
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
plt.figure(figsize=(14, 6))
plot_tree(model, feature_names=list(X.columns), class_names=["Stay", "Churn"], filled=True)
plt.show()
```

**What each line does:**

- 🟢 `model = DecisionTreeClassifier(max_depth=3, random_state=42)`: this creates the Decision Tree. max_depth=3 means it can ask at most three questions in a row. A small tree is easier to explain and is less likely to memorize the training data, which is called overfitting.
- 🟢 `model.fit(X_train, y_train)`: fit trains the model. It learns the questions that best separate churners from customers who stay.
- 🟢 `plt.figure(figsize=(14, 6))`: this makes the chart wide, so the tree is easy to read.
- 🟢 `plot_tree(...)`: this draws the tree. Each box shows a question, and filled=True colors the boxes by the most common answer: stay or churn.
- 🟢 `plt.show()`: this displays the tree.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to train the model.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para entrenar el modelo.)

Señalás con el mouse la primera caja de arriba:

> 🟢 The first question, at the top of the tree, is [FIRST QUESTION OF YOUR TREE]. That's the feature that best separates the two groups. Each box below asks another question, and the color shows whether most customers there stay or churn.
>
> (La primera pregunta, arriba del árbol, es [PRIMERA PREGUNTA DE TU ÁRBOL]. Esa es la variable que mejor separa a los dos grupos. Cada caja de abajo hace otra pregunta, y el color muestra si la mayoría de los clientes ahí se quedan o se van.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the evaluation.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la evaluación.)

Escribís `## 6. Predict and evaluate`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that makes predictions and measures them.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que hace predicciones y las mide.)

Escribís la **celda 7**:

```python
y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["Stay", "Churn"]))
```

**What each line does:**

- 🟢 `y_pred = model.predict(X_test)`: predict makes a prediction for each of the 50 test customers: 1 for churn, 0 for stay.
- 🟢 `print("Accuracy:", ...)`: accuracy is the share of predictions that were correct.
- 🟢 `print(confusion_matrix(y_test, y_pred))`: the confusion matrix is a two-by-two table. The rows are the real answers and the columns are the predictions. The top-left corner counts customers who stayed and were predicted to stay, and the bottom-right corner counts churners the model caught.
- 🟢 `print(classification_report(...))`: this shows precision and recall for each group. For churn, recall is the share of real churners the model found, which is the most important number for a retention team.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to evaluate the model.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para evaluar el modelo.)
>
> 🟢 The accuracy is [YOUR ACCURACY], so the model was right for about [X] out of 50 test customers. In the confusion matrix, it caught [BOTTOM-RIGHT NUMBER] churners and missed [BOTTOM-LEFT NUMBER]. The recall for churn is [CHURN RECALL].
>
> (La accuracy es [TU ACCURACY], así que el modelo acertó con unos [X] de los 50 clientes de prueba. En la matriz de confusión, detectó [NÚMERO ABAJO A LA DERECHA] clientes que se fueron y no detectó [NÚMERO ABAJO A LA IZQUIERDA]. El recall de churn es [RECALL DE CHURN].)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that shows which features matter most.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que muestra qué variables importan más.)

Escribís la **celda 8**:

```python
importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()
importance.plot(kind="barh", title="Feature Importance")
plt.xlabel("Importance")
plt.show()
```

**What each line does:**

- 🟢 `importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()`: feature_importances_ says how much each feature helped the tree make its decisions. I put the values in a Series with the feature names, sorted from lowest to highest.
- 🟢 `importance.plot(kind="barh", title="Feature Importance")`: this draws a horizontal bar chart, with the most important feature at the top.
- 🟢 `plt.xlabel("Importance")`: this names the horizontal axis.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the feature importance chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de importancia de variables.)
>
> 🟢 The most important features are [TOP FEATURES]. That matches what we saw before: the contract type and how long a customer has been with us matter most.
>
> (Las variables más importantes son [VARIABLES PRINCIPALES]. Eso coincide con lo que vimos antes: el tipo de contrato y cuánto tiempo lleva el cliente con nosotros son lo que más importa.)

Ajustá la segunda frase si tus variables principales son otras.

---

## 17:00–19:00 — Clientes en riesgo y observaciones

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for customers at risk.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los clientes en riesgo.)

Escribís `## 7. Customers at risk`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that lists the customers most likely to leave.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que lista a los clientes con más probabilidad de irse.)

Escribís la **celda 9**:

```python
at_risk = df.loc[X_test.index, ["customer_id", "tenure_months", "contract", "support_calls"]]
at_risk["churn_probability"] = model.predict_proba(X_test)[:, 1]
at_risk.sort_values("churn_probability", ascending=False).head(10)
```

**What each line does:**

- 🟢 `at_risk = df.loc[X_test.index, [...]]`: this takes the test customers from the original table, with their ID and a few readable columns.
- 🟢 `at_risk["churn_probability"] = model.predict_proba(X_test)[:, 1]`: predict_proba gives the probability of each answer. The second column, index 1, is the probability of churn.
- 🟢 `at_risk.sort_values("churn_probability", ascending=False).head(10)`: this sorts the customers from most to least likely to churn and shows the top ten.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to list the customers at risk.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para listar a los clientes en riesgo.)
>
> 🟢 This is the list the retention team can use. For example, customer [FIRST ID] has a churn probability of [PROBABILITY]. The team could contact these customers first.
>
> (Esta es la lista que puede usar el equipo de retención. Por ejemplo, el cliente [PRIMER ID] tiene una probabilidad de abandono de [PROBABILIDAD]. El equipo podría contactar primero a estos clientes.)

**Valores de referencia** (calculados del CSV, no dependen del modelo):

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 200 filas, 6 columnas; `monthly_charges` con 6 vacíos; `churn`: 118 `No` y 82 `Yes` |
| Preparación | Mediana usada para completar: 69,67. Tasa de churn: Month-to-month 0,70; One year 0,15; Two year 0,08 |
| Variables | 6 columnas: `tenure_months`, `monthly_charges`, `support_calls` y 3 de `contract_` |
| División | `(150, 6) (50, 6)` |
| Otros datos | Antigüedad promedio: 15,5 meses en los que se fueron y 35,3 en los que se quedaron |

> 🖱️ I'm clicking the plus Text button in the toolbar, to add my observations and retention insights.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar mis observaciones e ideas de retención.)

Completá los corchetes con tus números y, mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 8. Observations and retention insights
- **Data:** 200 customers, 82 of them churned (41%). 6 customers had no monthly charge, so we filled it with the median.
- **Contract:** month-to-month customers churn far more (about 70%) than one-year (about 15%) and two-year customers (about 8%).
- **Model:** a Decision Tree with depth 3 reached an accuracy of [YOUR ACCURACY] on the 50 test customers. It caught [N] of the [N] churners in the test set.
- **Most important features:** [TOP FEATURES].
- **Retention ideas:** offer month-to-month customers a discount to move to a yearly contract, follow up with new customers in their first months, and contact customers who call support many times.
```

```markdown
## 9. Conclusion
We loaded and prepared 200 customer records, trained a Decision Tree, and evaluated it on customers it had never seen. The model and the at-risk list help the retention team decide which customers to contact first.
```

> 🟢 For the retention team, there are three clear actions: move month-to-month customers to longer contracts, take extra care of new customers in their first months, and contact customers who call support a lot, before they leave.
>
> (Para el equipo de retención hay tres acciones claras: pasar a los clientes con contrato mensual a contratos más largos, cuidar especialmente a los clientes nuevos en sus primeros meses y contactar a los que llaman mucho a soporte, antes de que se vayan.)

---

## 19:00–22:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)
>
> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. I filled the missing charges with the median instead of removing the customers, because with only 200 records, every customer counts.
>
> (En este epílogo quiero repasar mi enfoque. Completé los cargos faltantes con la mediana en vez de quitar a esos clientes, porque con solo 200 registros cada cliente cuenta.)
>
> 🟢 I chose a Decision Tree because a retention team can read it: each branch is a simple rule. I limited it to three levels so it doesn't memorize the training data. And I tested it on customers it had never seen, because a model is only useful if it works on new customers.
>
> (Elegí un árbol de decisión porque un equipo de retención lo puede leer: cada rama es una regla simple. Lo limité a tres niveles para que no memorice los datos de entrenamiento. Y lo probé con clientes que nunca había visto, porque un modelo solo sirve si funciona con clientes nuevos.)
>
> 🟢 Accuracy alone can be misleading. If a model predicted "stay" for everyone, it would still be right for 59 percent of these customers. That's why I also looked at the confusion matrix and the recall for churn: missing a customer who leaves costs more than contacting one who would have stayed.
>
> (La accuracy sola puede engañar. Si un modelo predijera "se queda" para todos, igual acertaría con el 59 por ciento de estos clientes. Por eso también miré la matriz de confusión y el recall de churn: no detectar a un cliente que se va cuesta más que contactar a uno que se habría quedado.)
>
> 🟢 This analysis has some limits. The data is synthetic, there are only 200 customers, and the test set has just 50, so the results can change with a different split. A model also finds patterns, not causes.
>
> (Este análisis tiene algunos límites. Los datos son sintéticos, hay solo 200 clientes y el conjunto de prueba tiene apenas 50, así que los resultados pueden cambiar con otra división. Además, un modelo encuentra patrones, no causas.)
>
> 🟢 As next steps, I could use cross-validation to get a more stable score, try other depths or a Random Forest, and add more data, like customer complaints or usage. Then the retention team could test the actions, for example a discount for yearly contracts, and measure if churn goes down. Thanks for watching!
>
> (Como próximos pasos, podría usar validación cruzada para tener un resultado más estable, probar otras profundidades o un Random Forest y sumar más datos, como reclamos o uso del servicio. Después el equipo de retención podría probar las acciones, por ejemplo un descuento por contrato anual, y medir si baja el abandono. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: seguí explicando el árbol caja por caja.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
