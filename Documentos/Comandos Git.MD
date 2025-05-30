# Comandos de Git y GitHub (Explicados Fácil)

Este archivo explica los comandos más usados de Git y GitHub, con ejemplos simples y explicaciones fáciles de entender.

---

## 📌 Configuración inicial

### `git config --global user.name "Tu Nombre"`
Guarda tu nombre para que se vea en los cambios que hagas.

### `git config --global user.email "tu@email.com"`
Guarda tu correo para identificarte en los cambios.

---

## 🛠️ Crear y manejar repositorios

### `git init`
Crea un repositorio Git en la carpeta actual.

> Es como decir: “Voy a empezar a guardar los cambios de este proyecto”.

### `git clone URL`
Copia un repositorio de GitHub a tu computadora.

> Es como descargar una carpeta con todo el proyecto y su historial.

---

## 💾 Guardar cambios

### `git status`
Muestra los archivos que cambiaste o agregaste.

> Sirve para ver qué archivos están listos para guardar y cuáles no.

### `git add archivo.txt`
Marca un archivo especifico para guardarlo.

> Es como decir: “Quiero guardar este archivo”.

### `git add .`
Agrega **todos** los archivos modificados para guardarlos.

### `git commit -m "Mensaje"`
Guarda los archivos con un mensaje que explique qué cambiaste.

> Es como tomar una foto del proyecto con una nota explicando qué hiciste.

---

## 🔄 Ver cambios y deshacer

### `git log`
Muestra la historia de todos los commits (cambios guardados).

### `git diff`
Muestra las diferencias entre lo que cambiaste y lo que está guardado.

### `git checkout archivo.txt`
Deshace los cambios de un archivo y lo deja como estaba antes.

### `git checkout`
Deshace  **todos** los cambios de un archivo y lo deja como estaba antes.

---

## 🚀 Subir y bajar cambios

### `git remote add origin URL`
Le dice a Git dónde está el repositorio en GitHub.

> Solo se hace una vez, al principio.

### `git push origin main` ##LOS PUSH no siempre van al  MAIN sino a la rama que queres PUSHEAR
Sube tus cambios a GitHub.

> Es como mandar tu trabajo a la nube.

### `git pull origin main` ##LOS PULL no siempre van al  MAIN sino a la rama que queres PUSHEAR
Descarga los cambios desde GitHub a tu computadora.

> Útil si otra persona trabajó en el mismo proyecto.

---

## 🌿 Ramas (branches)
### `git branch -m nuevo-nombre`
Cambia el nombre de la rama en la que estás.

### Si cambiaste el nombre de la rama y ya la habías subido, hace esto: 
### `git push origin -u nuevo-nombre`
### `git push origin --delete viejo-nombre`
Sube la nueva rama y borra la vieja de GitHub.

### `git branch`
Muestra todas las ramas.

### `git branch nombre-rama`
Crea una nueva rama (una copia del proyecto para hacer pruebas sin dañar lo principal).

### `git checkout nombre-rama` tambien `git switch nombre-rama`
Cambia de una rama a otra.

### `git merge nombre-rama`
Une una rama con otra. Generalmente se hace desde `main`.

### VER EL CODIGO DE UN COMMIT
### `git checkout <id_del_commit>`
Esto te lleva a ese commit, pero entras en modo "detached HEAD" (no puedes guardar nuevos commits en esa rama).

### Salir de modo DEACHED HEAD
### `git checkout nombre-de-la-rama`
Esto vuelve tu HEAD a la rama principal y ya puedes seguir trabajando normalmente.

### Apuntar a un HEAD y Crear una nueva rama de ese HEAD
### `git checkout -b nombre-nuevo <id_del_commit>`
Crea una rama nueva desde ese commit y te mueve ahí. Esto es conveniente en el caso de que quieras seguir trabajando con un commit viejo


### Apuntar el HEAD a un commit y borrar los cambios arriba de ese HEAD
### `git reset --hard <id_del_commit>`
⚠️ Borra los commits más nuevos. NO CONVENIENTE. Esto es solamente util, cuando ya no te interesa los cambios que se produjeron después de este commit

---

## 🗑️ Eliminar cosas

### `git rm archivo.txt`
Elimina un archivo y lo marca para que se borre en el próximo commit.

### `git branch -d nombre-rama`
Elimina una rama (solo si ya fue fusionada).

---

## 🆘 Ayuda

### `git help`
Muestra ayuda de Git en la terminal.

---

