# qa-project-Urban-Routes-es - Automatización de Pruebas (QA)

Este proyecto contiene una suite de pruebas automatizadas para la aplicación web **Urban Routes**, enfocada en verificar el correcto funcionamiento del flujo de creación de viajes, selección de dirección, método de pago y validación de elementos UI utilizando **Selenium** y **pytest**.

## 🚀 Descripción del Proyecto

La aplicación **Urban Routes** permite a los usuarios crear rutas de transporte urbano de manera rápida. Este proyecto automatiza las pruebas end-to-end del flujo principal de la app, incluyendo:

- Selección de dirección de origen y destino
- Validación del método de pago
- Comprobación de elementos visuales y comportamiento del botón "Solicitar viaje"
- Validación de mensajes y notificaciones

## 🛠️ Tecnologías y técnicas utilizadas

- **Lenguaje:** Python 3
- **Framework de pruebas:** `pytest`
- **Automatización web:** `Selenium WebDriver`
- **Gestión de dependencias:** `pip`
- **Buenas prácticas de QA:** 
  - Uso del patrón **Page Object Model (POM)**
  - Separación de datos de prueba en un archivo de configuración
  - Uso de `setup_class` y `setup_method` para preparar el entorno de prueba
  - Validación con `assert` de elementos clave de la aplicación

## 📂 Estructura del Proyecto

```
qa-project-Urban-Routes-es
├── data.py # Archivo con datos de prueba (números, URLs, direcciones)
├── localizadores.py  # Selectores y localizadores usados en las pruebas
├── main.py # Script principal con las pruebas automatizadas
└── README.md # Documentación del proyecto (este archivo)
```

## ▶️ Instrucciones para ejecutar las pruebas

1. Clonar el repositorio o descargar el proyecto.
2. Asegurarse de tener instalado Python 3 y las librerías necesarias:
   ```bash
   pip install selenium pytest
   ```
3. Descargar y configurar el ChromeDriver compatible con tu versión de Chrome y agregarlo al PATH.
4. Configurar el archivo `data.py` con los datos requeridos, como URLs, números telefónicos y datos de tarjetas.
5. Ejecutar las pruebas con:
   ```bash
   pytest
   ```
6. Observar el reporte en consola con los resultados de las pruebas.

## 🧪 Requisitos previos

- Tener instalado Python 3.8 o superior
- Tener instalado Google Chrome
- Tener el controlador `chromedriver` compatible con tu versión de navegador