# 9s3mb6ec — Customer Churn Prediction

Guion paso a paso para grabar la tarea **9s3mb6ec**: armar en **Google Colab**, con **pandas** y un **árbol de decisión** (*Decision Tree*) de **scikit-learn**, un flujo de predicción de abandono de clientes (*churn*). Usa un dataset sintético de 200 clientes. El trabajo incluye preparar los datos, entrenar el modelo, hacer predicciones, evaluarlas y sacar ideas para retener clientes. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **26 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

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
| `tenure_months` | Meses que lleva como cliente (de 1 a 72) |
| `monthly_charges` | Cuánto paga por mes, en dólares (de 20 a 120) |
| `contract` | Tipo de contrato: `Month-to-month` (101), `Two year` (53) o `One year` (46) |
| `support_calls` | Llamadas a soporte (de 0 a 7) |
| `churn` | Si se dio de baja: `Yes` o `No`. **Es lo que queremos predecir** |

**Lo que hay que preparar** (lo encontrás y lo arreglás durante la grabación):

| Problema | Dónde | Cómo se arregla |
| -------- | ----- | --------------- |
| Valores faltantes | 6 clientes sin `monthly_charges` | `fillna()` con la mediana (69,67) |
| Texto en la variable objetivo | `churn` dice `Yes` / `No` | `map({"Yes": 1, "No": 0})` |
| Texto en una variable | `contract` tiene tres categorías de texto | `pd.get_dummies()` |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá. Comprobá que los números del modelo coinciden con la tabla de **Valores de referencia**.
3. Pegá el Goal en un documento de **Google Docs** y borrá el **Approval ID** y cualquier dato personal. Agrandá el texto hasta que se lea completo.
4. Dejá tres pestañas abiertas en Firefox, en este orden: el documento del **Goal**, Colab (https://colab.research.google.com) y el sitio de scikit-learn (https://scikit-learn.org). En Colab dejá a la vista el cuadro **Open notebook**, sin crear todavía el notebook. Tené `customers.csv` en una carpeta fácil de encontrar, como el Escritorio. Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini), no las uses. Cerrá este guion si está en la misma pantalla.

---

## 0:00–1:30 — El Goal y el plan

Empezás en la primera pestaña, la del **Goal**, con el texto completo y legible. La introducción dura menos de 20 segundos: la frase de apertura y el objetivo.

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind.
>
> (Voy a empezar mi tarea en breve. Este es el flujo de trabajo que tengo en mente.)
>
> 🖱️ I'm on the Goal document, in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst for a customer retention team, I'll build a churn prediction workflow in Google Colab. I'll prepare 200 customer records, train a Decision Tree, evaluate its predictions, and find customers who may be at risk of leaving.
>
> (Como analista de datos de un equipo de retención de clientes, voy a armar un flujo de predicción de abandono en Google Colab. Voy a preparar 200 registros de clientes, entrenar un árbol de decisión, evaluar sus predicciones y encontrar clientes que podrían estar en riesgo de irse.)

Ajustá esta frase a lo que diga tu Goal. Después contás el plan, paso por paso:

> 🟢 Here's the plan. First, I'll load the customer data in Google Colab and inspect it, to find any problems before building the model.
>
> (Este es el plan. Primero, voy a cargar los datos de los clientes en Google Colab e inspeccionarlos, para encontrar los problemas antes de armar el modelo.)
>
> 🟢 Second, I'll prepare the data: fill the missing values and turn the text columns into numbers, because a model only works with numbers.
>
> (Segundo, voy a preparar los datos: completar los valores faltantes y convertir las columnas de texto en números, porque un modelo solo trabaja con números.)
>
> 🟢 Third, I'll split the customers into a training set and a testing set, train a Decision Tree, and evaluate it on customers it has never seen.
>
> (Tercero, voy a dividir a los clientes en un conjunto de entrenamiento y uno de prueba, entrenar un árbol de decisión y evaluarlo con clientes que nunca vio.)
>
> 🟢 Finally, I'll list the customers most likely to leave, and write down ideas for the retention team.
>
> (Por último, voy a listar a los clientes con más probabilidad de irse y anotar ideas para el equipo de retención.)

---

## 1:30–3:00 — Colab y scikit-learn

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código se ejecuta en la nube de Google, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official scikit-learn website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de scikit-learn.)
>
> 🟢 Churn means a customer stops using a service. Keeping a customer is usually cheaper than finding a new one, so predicting churn helps a company act in time.
>
> (Churn significa que un cliente deja de usar un servicio. Retener a un cliente suele ser más barato que conseguir uno nuevo, así que predecir el abandono ayuda a una empresa a actuar a tiempo.)
>
> 🟢 This is scikit-learn, the most popular Python library for machine learning. I'll use its Decision Tree classifier. A decision tree learns simple yes-or-no questions from the data, like "is the contract month-to-month?", and follows them to a prediction. That makes it easy to explain to a business team. scikit-learn and pandas come already installed in Colab.
>
> (Esto es scikit-learn, la librería de machine learning más popular de Python. Voy a usar su clasificador de árbol de decisión. Un árbol de decisión aprende preguntas simples de sí o no a partir de los datos, como "¿el contrato es mensual?", y las sigue hasta llegar a una predicción. Eso lo hace fácil de explicar a un equipo de negocio. scikit-learn y pandas vienen ya instaladas en Colab.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 3:00–6:30 — Notebook nuevo y cargar los datos

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing churn_prediction.ipynb, to identify this project.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo churn_prediction.ipynb, para identificar este proyecto.)

Subís el CSV:

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing customers.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo customers.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso de que los archivos se borran al reiniciar el entorno: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Customer Churn Prediction
Dataset: 200 synthetic customer records. Goal: train a Decision Tree to predict which customers may leave, evaluate it, and find customers at risk.
```

**What each line does:**

- 🟢 `# Customer Churn Prediction`: the hash sign makes this the main title of the notebook.
- 🟢 `Dataset: ... Goal: ...`: this line says what the data is and what I want to find out.

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

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data, with its usual short name, pd.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot, the part of Matplotlib that draws charts, as plt.
- 🟢 `from sklearn.model_selection import train_test_split`: sklearn is the name of scikit-learn in code. This imports the function that splits the data into a training set and a testing set.
- 🟢 `from sklearn.tree import DecisionTreeClassifier, plot_tree`: this imports the Decision Tree model and a function to draw it.
- 🟢 `from sklearn.metrics import accuracy_score, confusion_matrix, classification_report`: these three functions measure how good the predictions are.
- 🟢 `df = pd.read_csv("customers.csv")`: read_csv reads the file I uploaded and stores it in a DataFrame called df. A DataFrame is a table with rows and columns, like a spreadsheet.
- 🟢 `df.head()`: head shows the first five customers, to check that the data loaded correctly. I don't need print, because Colab always shows the result of the last line of a cell.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the libraries and the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar las librerías y los datos.)
>
> 🟢 This is a synthetic dataset I generated for this analysis: 200 invented customers of a subscription company. So there's no real personal information here.
>
> (Este es un dataset sintético que generé para este análisis: 200 clientes inventados de una empresa de suscripción. Así que acá no hay información personal real.)

Señalás cada columna con el mouse, de izquierda a derecha, mientras la nombrás:

> 🟢 Each row is one customer, and there are six columns. customer_id is the code of the customer. tenure_months is how many months they've been a customer. monthly_charges is how much they pay each month, in dollars.
>
> (Cada fila es un cliente, y hay seis columnas. customer_id es el código del cliente. tenure_months es cuántos meses lleva como cliente. monthly_charges es cuánto paga cada mes, en dólares.)
>
> 🟢 contract is the type of contract: month-to-month, one year, or two years. support_calls is how many times they called customer support. And churn says if they left: Yes or No. That's the column we want to predict.
>
> (contract es el tipo de contrato: mensual, de un año o de dos años. support_calls es cuántas veces llamó a soporte. Y churn dice si se fue: Yes o No. Esa es la columna que queremos predecir.)

---

## 6:30–10:00 — Inspeccionar y preparar los datos

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

- 🟢 `df.info()`: info lists every column with how many values it has and its data type. info prints by itself, so I don't need print.
- 🟢 `print(df.isna().sum())`: isna marks each empty cell as True, and sum counts them in each column.
- 🟢 `print(df["churn"].value_counts())`: value_counts counts how many customers churned and how many stayed.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)

Señalás cada resultado con el mouse mientras lo nombrás:

> 🟢 We have 200 customers and 6 columns. monthly_charges has only 194 values, and the missing-values count confirms it: 6 customers have no monthly charge.
>
> (Tenemos 200 clientes y 6 columnas. monthly_charges tiene solo 194 valores, y el conteo de faltantes lo confirma: 6 clientes no tienen cargo mensual.)
>
> 🟢 Also, contract and churn are stored as text. The model needs numbers, so I'll have to convert them.
>
> (Además, contract y churn están guardadas como texto. El modelo necesita números, así que las voy a tener que convertir.)
>
> 🟢 And 82 customers churned while 118 stayed, so about 41 percent churned. The two groups are not perfectly balanced, which I'll keep in mind when I split the data.
>
> (Y 82 clientes se dieron de baja mientras que 118 se quedaron, así que cerca del 41 por ciento abandonó. Los dos grupos no están perfectamente equilibrados, y lo voy a tener en cuenta al dividir los datos.)

Según la versión de pandas, el texto aparece como `object` o como `str`.

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

- 🟢 `df["monthly_charges"] = df["monthly_charges"].fillna(df["monthly_charges"].median())`: fillna fills the 6 missing charges with the median charge, the middle value. I use the median because it isn't affected by very high or very low values. And I fill instead of removing, because with only 200 records, every customer counts.
- 🟢 `df["churn"] = df["churn"].map({"Yes": 1, "No": 0})`: models work with numbers, not words, so map turns Yes into 1 and No into 0.
- 🟢 `print(df.groupby("contract")["churn"].mean().round(2))`: groupby puts together the customers of each contract type. Since churn is now 1 or 0, its average is the share of customers who left: the churn rate of each group.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to prepare the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para preparar los datos.)
>
> 🟢 This is already a strong insight, even before the model: about 70 percent of month-to-month customers churned, but only about 15 percent of one-year customers and 8 percent of two-year customers.
>
> (Esto ya es un hallazgo fuerte, incluso antes del modelo: cerca del 70 por ciento de los clientes con contrato mensual se dieron de baja, pero solo cerca del 15 por ciento de los de contrato anual y el 8 por ciento de los de dos años.)
>
> 🟢 It makes sense: a month-to-month customer can leave at any time, without a penalty.
>
> (Tiene sentido: un cliente con contrato mensual se puede ir en cualquier momento, sin penalización.)

---

## 10:00–13:30 — Variable objetivo, variables y división de los datos

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
- 🟢 `X = pd.get_dummies(df.drop(columns=["customer_id", "churn"]), columns=["contract"])`: X holds the features, the information the model uses to predict. drop removes customer_id, because an ID says nothing about behavior, and churn, because that's the answer: if the model saw it, it would be cheating. get_dummies turns the contract text into three yes-or-no columns, one for each contract type, because the model needs numbers.
- 🟢 `X.head()`: this shows the first rows of the features.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to build the features.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para armar las variables.)
>
> 🖱️ I'm scrolling right in the table under the cell, to show the three new contract columns.
>
> (Me desplazo a la derecha en la tabla debajo de la celda, para mostrar las tres columnas nuevas de contrato.)
>
> 🟢 Now we have six features: tenure, monthly charges, support calls, and the three contract columns, with True or False. For example, the first customer has True only in contract Two year.
>
> (Ahora tenemos seis variables: antigüedad, cargo mensual, llamadas a soporte y las tres columnas de contrato, con True o False. Por ejemplo, el primer cliente tiene True solo en contract Two year.)

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

- 🟢 `X_train, X_test, y_train, y_test = train_test_split(...)`: this splits the customers into two groups, and returns four parts: the features and the answers for training, and the features and the answers for testing.
- 🟢 `test_size=0.25`: the model learns from 75 percent of the customers, the training set, and I test it on the other 25 percent, which it has never seen. That's how we know if it works on new customers.
- 🟢 `random_state=42`: this fixes the random split, so I get the same result every time I run it.
- 🟢 `stratify=y`: this keeps the same share of churners in both groups, about 41 percent, because the groups are not balanced.
- 🟢 `print(X_train.shape, X_test.shape)`: this shows the size of each group.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to split the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dividir los datos.)
>
> 🟢 150 customers for training and 50 for testing, each with 6 features.
>
> (150 clientes para entrenar y 50 para probar, cada uno con 6 variables.)

---

## 13:30–19:00 — Entrenar, predecir y evaluar

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

- 🟢 `model = DecisionTreeClassifier(max_depth=3, random_state=42)`: this creates the Decision Tree. max_depth equals 3 means it can ask at most three questions in a row. A small tree is easier to explain and is less likely to memorize the training data, which is called overfitting. random_state makes the result repeatable.
- 🟢 `model.fit(X_train, y_train)`: fit trains the model. It looks only at the training customers and learns the questions that best separate churners from customers who stay.
- 🟢 `plt.figure(figsize=(14, 6))`: this makes the chart wide, so the tree is easy to read.
- 🟢 `plot_tree(...)`: this draws the tree, with the feature names and the two answers, Stay and Churn. filled equals True colors the boxes: orange when most customers in that box stay, and blue when most churn.
- 🟢 `plt.show()`: this displays the tree.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to train the model and draw the tree.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para entrenar el modelo y dibujar el árbol.)

Señalás con el mouse la primera caja de arriba:

> 🖱️ I'm pointing at the first box, at the top of the tree, to explain the first question.
>
> (Señalo la primera caja, arriba del árbol, para explicar la primera pregunta.)
>
> 🟢 The first question is contract month-to-month less than or equal to 0.5. Since that column is 1 for month-to-month customers and 0 for the others, this really asks: is the contract not month-to-month? So the contract type is the feature that best separates the two groups. The box also shows samples equals 150, the training customers, and value, 89 who stayed and 61 who churned.
>
> (La primera pregunta es contract month-to-month menor o igual a 0,5. Como esa columna vale 1 para los clientes con contrato mensual y 0 para los demás, en realidad pregunta: ¿el contrato no es mensual? Así que el tipo de contrato es la variable que mejor separa a los dos grupos. La caja también muestra samples igual a 150, los clientes de entrenamiento, y value, 89 que se quedaron y 61 que se fueron.)
>
> 🖱️ I'm pointing at the right branch of the tree, the month-to-month customers, to follow the next questions.
>
> (Señalo la rama derecha del árbol, los clientes con contrato mensual, para seguir las preguntas siguientes.)
>
> 🟢 On the right are the month-to-month customers. The next question is tenure: if they've been a customer for 25 months or less, the box turns blue, so most of them churn. And among those, the ones with three or more support calls all churned. So new month-to-month customers who call support a lot are the highest risk.
>
> (A la derecha están los clientes con contrato mensual. La siguiente pregunta es la antigüedad: si llevan 25 meses o menos, la caja se pone azul, así que la mayoría se va. Y entre ellos, los que tienen tres llamadas a soporte o más se fueron todos. Así que los clientes nuevos con contrato mensual que llaman mucho a soporte son los de mayor riesgo.)
>
> 🟢 On the left are the customers with one-year or two-year contracts, and almost all of those boxes are orange: most of them stay.
>
> (A la izquierda están los clientes con contrato de uno o dos años, y casi todas esas cajas son naranjas: la mayoría se queda.)

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
- 🟢 `print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))`: accuracy compares the predictions with the real answers. It's the share of predictions that were correct.
- 🟢 `print(confusion_matrix(y_test, y_pred))`: the confusion matrix is a two-by-two table. The rows are the real answers and the columns are the predictions. The top-left corner counts customers who stayed and were predicted to stay, and the bottom-right corner counts churners the model caught.
- 🟢 `print(classification_report(...))`: this shows precision and recall for each group. For churn, precision is how many of the predicted churners really left, and recall is the share of real churners the model found. Recall is the most important number for a retention team.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to evaluate the model.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para evaluar el modelo.)

Señalás cada número mientras lo nombrás:

> 🟢 The accuracy is 0.8, so the model was right for 40 of the 50 test customers.
>
> (La accuracy es 0,8, así que el modelo acertó con 40 de los 50 clientes de prueba.)
>
> 🖱️ I'm pointing at the confusion matrix, below the accuracy, to read each corner.
>
> (Señalo la matriz de confusión, debajo de la accuracy, para leer cada esquina.)
>
> 🟢 In the first row, 23 customers stayed and the model predicted it, and 6 stayed but the model predicted they would leave. In the second row, the model missed 4 churners, and it caught 17 of the 21 customers who really left.
>
> (En la primera fila, 23 clientes se quedaron y el modelo lo predijo, y 6 se quedaron pero el modelo predijo que se irían. En la segunda fila, el modelo no detectó a 4 clientes que se fueron, y detectó a 17 de los 21 que realmente se fueron.)
>
> 🟢 In the report, the recall for churn is 0.81, so the model found about 8 out of 10 real churners. The precision for churn is 0.74: about 3 out of 4 customers it flagged really left.
>
> (En el reporte, el recall de churn es 0,81, así que el modelo encontró unos 8 de cada 10 clientes que realmente se fueron. La precisión de churn es 0,74: cerca de 3 de cada 4 clientes que marcó realmente se fueron.)

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

- 🟢 `importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()`: feature_importances_ says how much each feature helped the tree make its decisions. The values add up to one. I put them in a Series with the feature names, sorted from lowest to highest.
- 🟢 `importance.plot(kind="barh", title="Feature Importance")`: this draws a horizontal bar chart, with the most important feature at the top.
- 🟢 `plt.xlabel("Importance")`: this names the horizontal axis.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the feature importance chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de importancia de variables.)
>
> 🟢 The most important feature, by far, is the month-to-month contract, with about 63 percent of the importance. Tenure is second, with about 22 percent, then support calls and monthly charges.
>
> (La variable más importante, por lejos, es el contrato mensual, con cerca del 63 por ciento de la importancia. La antigüedad es la segunda, con cerca del 22 por ciento, y después las llamadas a soporte y el cargo mensual.)
>
> 🟢 The one-year and two-year columns show zero. That doesn't mean they don't matter: once the tree knows if a contract is month-to-month or not, those two columns add no new information. That matches what we saw before: the contract type and how long a customer has been with us matter most.
>
> (Las columnas de uno y dos años muestran cero. Eso no significa que no importen: una vez que el árbol sabe si un contrato es mensual o no, esas dos columnas no agregan información nueva. Eso coincide con lo que vimos antes: el tipo de contrato y cuánto tiempo lleva el cliente con nosotros son lo que más importa.)

---

## 19:00–21:00 — Clientes en riesgo y observaciones

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

- 🟢 `at_risk = df.loc[X_test.index, [...]]`: loc selects rows and columns by their labels. This takes the test customers from the original table, with their ID and a few readable columns, like the contract as text.
- 🟢 `at_risk["churn_probability"] = model.predict_proba(X_test)[:, 1]`: predict_proba gives the probability of each answer for each customer. The colon means all rows, and index 1 is the second column: the probability of churn.
- 🟢 `at_risk.sort_values("churn_probability", ascending=False).head(10)`: this sorts the customers from most to least likely to churn and shows the top ten.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to list the customers at risk.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para listar a los clientes en riesgo.)
>
> 🟢 This is the list the retention team can use. The first seven customers have a churn probability of 1, which means 100 percent. They all have a month-to-month contract, 25 months or less with the company, and three or more support calls: exactly the riskiest branch of the tree. The team could contact these customers first.
>
> (Esta es la lista que puede usar el equipo de retención. Los primeros siete clientes tienen una probabilidad de abandono de 1, o sea 100 por ciento. Todos tienen contrato mensual, 25 meses o menos con la empresa y tres llamadas a soporte o más: justo la rama más riesgosa del árbol. El equipo podría contactar primero a estos clientes.)
>
> 🟢 A probability of 100 percent doesn't mean they will surely leave. It means that every training customer in that branch left. With more data, the number would be less extreme.
>
> (Una probabilidad de 100 por ciento no significa que seguro se vayan. Significa que todos los clientes de entrenamiento de esa rama se fueron. Con más datos, el número sería menos extremo.)

Mirá la tabla antes de decirlo. Los empates en 1,0 pueden salir en otro orden en tu Colab: por eso no nombres un ID en particular.

**Valores de referencia** (los calculé directamente del CSV, con scikit-learn 1.9). Compará con tu resultado antes de decirlos:

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 200 filas, 6 columnas; `monthly_charges` con 194 valores (6 vacíos); `churn`: 118 `No` y 82 `Yes` |
| Preparación | Mediana usada para completar: 69,67. Tasa de churn: Month-to-month 0,70; One year 0,15; Two year 0,08 |
| Variables | 6 columnas: `tenure_months`, `monthly_charges`, `support_calls` y 3 de `contract_` |
| División | `(150, 6) (50, 6)`; en la prueba hay 21 clientes que se fueron y 29 que se quedaron |
| Árbol | Primera caja: `contract_Month-to-month <= 0.5`, `samples = 150`, `value = [89, 61]`. Rama derecha: `tenure_months <= 25.5`, después `support_calls <= 2.5` |
| Evaluación | Accuracy **0,8**. Matriz `[[23 6] [4 17]]`. Churn: precision 0,74, recall 0,81. Stay: precision 0,85, recall 0,79 |
| Importancia | Month-to-month 0,631 · tenure 0,215 · support_calls 0,097 · monthly_charges 0,056 · One year y Two year 0 |
| Clientes en riesgo | 7 clientes con probabilidad 1,0 (todos mensuales, ≤ 25 meses y ≥ 3 llamadas). Los siguientes, con 0,69 |
| Otros datos | Antigüedad promedio: 15,5 meses en los que se fueron y 35,3 en los que se quedaron |

> 🖱️ I'm clicking the plus Text button in the toolbar, to add my observations and retention insights.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar mis observaciones e ideas de retención.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 8. Observations and retention insights
- **Data:** 200 customers, 82 of them churned (41%). 6 customers had no monthly charge, so we filled it with the median.
- **Contract:** month-to-month customers churn far more (about 70%) than one-year (about 15%) and two-year customers (about 8%).
- **Model:** a Decision Tree with depth 3 reached an accuracy of 0.8 on the 50 test customers. It caught 17 of the 21 churners in the test set (recall 0.81).
- **Most important features:** month-to-month contract (about 63%), tenure (about 22%), and support calls (about 10%).
- **Retention ideas:** offer month-to-month customers a discount to move to a yearly contract, follow up with new customers in their first months, and contact customers who call support many times.
```

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the conclusion at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar la conclusión al final del notebook.)

```markdown
## 9. Conclusion
We loaded and prepared 200 customer records, trained a Decision Tree, and evaluated it on customers it had never seen. The model and the at-risk list help the retention team decide which customers to contact first.
```

> 🟢 For the retention team, there are three clear actions: move month-to-month customers to longer contracts, take extra care of new customers in their first months, and contact customers who call support a lot, before they leave.
>
> (Para el equipo de retención hay tres acciones claras: pasar a los clientes con contrato mensual a contratos más largos, cuidar especialmente a los clientes nuevos en sus primeros meses y contactar a los que llaman mucho a soporte, antes de que se vayan.)

---

## 21:00–26:00 — Epílogo (4–5 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)

### Resumen paso a paso

Subís hasta el principio del notebook y vas bajando: cada frase va cuando la sección correspondiente está en pantalla. Señalá con el mouse lo que nombrás.

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, to go over everything we did, step by step.
>
> (Subo hasta el principio del notebook con la rueda del mouse, para repasar todo lo que hicimos, paso a paso.)
>
> 🟢 Let me summarize the whole project. We started with the title and the goal, imported pandas, Matplotlib, and scikit-learn, and loaded 200 customers with six columns.
>
> (Les resumo todo el proyecto. Empezamos con el título y el objetivo, importamos pandas, Matplotlib y scikit-learn, y cargamos 200 clientes con seis columnas.)
>
> 🖱️ I'm scrolling down to sections 1 and 2, Inspect the data and Prepare the data.
>
> (Bajo hasta las secciones 1 y 2, Inspect the data y Prepare the data.)
>
> 🟢 In sections 1 and 2, we found 6 missing charges and filled them with the median, turned churn into ones and zeros, and saw that month-to-month customers churn the most, about 70 percent.
>
> (En las secciones 1 y 2 encontramos 6 cargos faltantes y los completamos con la mediana, convertimos churn en unos y ceros, y vimos que los clientes con contrato mensual son los que más abandonan, cerca del 70 por ciento.)
>
> 🖱️ I'm scrolling down to sections 3 and 4, the features and the split.
>
> (Bajo hasta las secciones 3 y 4, las variables y la división.)
>
> 🟢 In sections 3 and 4, we separated the target from the features, turned the contract into three number columns, and split the customers: 150 for training and 50 for testing.
>
> (En las secciones 3 y 4 separamos la variable objetivo de las variables, convertimos el contrato en tres columnas numéricas y dividimos a los clientes: 150 para entrenar y 50 para probar.)
>
> 🖱️ I'm scrolling down to sections 5 and 6, the tree and the evaluation.
>
> (Bajo hasta las secciones 5 y 6, el árbol y la evaluación.)
>
> 🟢 In sections 5 and 6, we trained a tree with three levels. Its first question is the contract type. On the test customers, it reached an accuracy of 0.8, and it caught 17 of the 21 churners.
>
> (En las secciones 5 y 6 entrenamos un árbol de tres niveles. Su primera pregunta es el tipo de contrato. Con los clientes de prueba llegó a una accuracy de 0,8, y detectó a 17 de los 21 que se fueron.)
>
> 🖱️ I'm scrolling down to sections 7, 8, and 9, at the end of the notebook.
>
> (Bajo hasta las secciones 7, 8 y 9, al final del notebook.)
>
> 🟢 And finally, we listed the customers at risk, and wrote down our observations, the retention ideas, and the conclusion.
>
> (Y por último, listamos a los clientes en riesgo y anotamos las observaciones, las ideas de retención y la conclusión.)

### Decisiones y próximos pasos

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
> 🟢 Accuracy alone can be misleading. If a model predicted "stay" for everyone, it would still be right for about 58 percent of the test customers. That's why I also looked at the confusion matrix and the recall for churn: missing a customer who leaves costs more than contacting one who would have stayed.
>
> (La accuracy sola puede engañar. Si un modelo predijera "se queda" para todos, igual acertaría con cerca del 58 por ciento de los clientes de prueba. Por eso también miré la matriz de confusión y el recall de churn: no detectar a un cliente que se va cuesta más que contactar a uno que se habría quedado.)
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
