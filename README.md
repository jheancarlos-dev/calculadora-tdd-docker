# 🧮 Calculadora TDD - Proyecto Final

Aplicación web de una calculadora interactiva desarrollada como proyecto final para la asignatura de **Construcción de Software**. Implementa una suite de pruebas completa con TDD, un flujo de trabajo profesional con Git y GitHub, contenerización con Docker e integración continua.

---

## ✨ Características

- **Interfaz visual e intuitiva**: Una calculadora con botones como la de un dispositivo real.
- **Operaciones básicas**: Suma, resta, multiplicación y división.
- **Manejo de errores**: Validación para evitar la división por cero.
- **Desarrollo Guiado por Pruebas (TDD)**: 6 pruebas unitarias documentadas.
- **GitFlow**: Ramas `main`, `develop` y colaboración mediante Pull Requests.
- **Docker**: Contenedor listo para ejecutar en cualquier entorno.
- **CI/CD**: GitHub Actions ejecuta los tests automáticamente.

---

## 🛠️ Tecnologías

- Python 3.13
- Flask
- Pytest
- Docker
- GitHub Actions

---

## 🚀 Cómo ejecutar el proyecto

### Opción 1: Local con Python
1. Clona el repositorio y entra en él:
   git clone https://github.com/jheancarlos-dev/calculadora-tdd-docker.git
   cd calculadora-tdd-docker
2. Instala las dependencias:
   pip install -r requirements.txt
3. Inicia la app:
   python app.py
4. Abre tu navegador en `http://127.0.0.1:5000`.

### Opción 2: Usando Docker
1. Construye la imagen:
   docker build -t calculadora-tdd .
2. Ejecuta el contenedor:
   docker run -p 5000:5000 calculadora-tdd
3. Abre tu navegador en `http://127.0.0.1:5000`.

---

## 🧪 Pruebas y TDD

El proyecto sigue estrictamente el ciclo Red-Green-Refactor. Para ejecutar las pruebas:

pytest -v

### Pruebas incluidas
- Suma de positivos
- Suma de negativos
- Resta
- Multiplicación
- División
- División por cero (manejo de error)

---

## 🤖 CI/CD

Cada Push y Pull Request activa GitHub Actions, que ejecuta las pruebas automáticamente para garantizar la calidad del código.

---

## 👥 Equipo

| Integrante | Rol |
|------------|-----|
| Jhean Carlos | Líder de Proyecto / DevOps |
| Alejandro | Desarrollador de pruebas |
| Higler | Desarrollador Frontend |
| Jorge | Desarrollador Backend |

---

## 📄 Licencia

Proyecto académico. Universidad Continental, 2026.
