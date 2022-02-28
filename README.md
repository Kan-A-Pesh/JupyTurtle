# JupyTurtle

Une intégration de Turtle simple et rapide pour JupyterHub.\
***⚠ Remarque:* JupyTurtle est en phase de développement et donc n'est pas optimisé!**\
Notez que JupyTurtle fonctionne à base d'images SVG, et nécéssite les modules `IPython` et `math` pour fonctionner correctement.

## Installation
Pour utiliser JupyTurtle,

### 1️⃣ Téléchargez le fichier suivant: [jupyTurtle.py](https://raw.githubusercontent.com/Kan-A-Pesh/JupyTurtle/master/jupyTurtle.py)

### 2️⃣ Déposer ce fichier dans le dossier de votre projet

### 3️⃣ Importez JupyTurtle
```python
from jupyTurtle import Turtle
```
Et utilisez une tortue:
```python
maTortue = Turtle()
```

### 4️⃣ Bravo! 🎉
Vous pouvez désormais utiliser JupyTurtle
Pour plus d'information, veuillez consulter la documentation de JupyTurtle

**Voici quelques petits exemples:**

*🛑 Un octogone:*
```python
from jupyTurtle import Turtle

t = Turtle(size = 300)
t.color("purple")
for i in range(8):
    t.forward(30)
    t.right(45)
```
![octogone](https://user-images.githubusercontent.com/74819837/156070386-340c9dff-dfe9-452b-8fc6-7f5b57187f4f.png)


*✨ Une étoile:*
```python
from jupyTurtle import Turtle

t = Turtle(size = 300)
t.color("red")
for i in range(5):
    t.forward(30)
    t.backward(30)
    t.right(72)
```
![image](https://user-images.githubusercontent.com/74819837/156070551-eeeb072a-c563-49cd-a160-0df1b947b565.png)
