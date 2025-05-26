# qa-project-Urban-Routes-es - Automatización de Pruebas (QA)

Este proyecto contiene una suite de pruebas automatizadas para la aplicación web **Urban Routes**, enfocada en verificar el correcto funcionamiento del flujo de creación de viajes, selección de direcciones, autenticación por SMS, método de pago, y validación de elementos de interfaz de usuario utilizando **Selenium** y **pytest**.

## 🚀 Descripción del Proyecto

La aplicación **Urban Routes** permite a los usuarios crear rutas de transporte urbano de manera rápida. Este proyecto automatiza las pruebas *end-to-end* del flujo principal de la app, incluyendo:

* Selección de dirección de origen y destino
* Validación del método de pago con tarjeta
* Autenticación por número de teléfono (SMS)
* Envío de mensajes al conductor
* Selección de artículos adicionales (como frazadas o helado)
* Comprobación de elementos visuales y comportamiento del botón "Solicitar viaje"
* Validación de mensajes y confirmaciones de UI

## 🛠️ Tecnologías y técnicas utilizadas

* **Lenguaje:** Python 3
* **Framework de pruebas:** `pytest`
* **Automatización web:** `Selenium WebDriver`
* **Gestión de dependencias:** `pip`
* **Buenas prácticas de QA:**

  * Uso del patrón **Page Object Model (POM)**
  * Separación de datos de prueba en archivos dedicados
  * Uso de `setup_class` y `teardown_class` para preparar y cerrar el entorno de prueba
  * Validaciones mediante `assert` para elementos clave de la aplicación

## 📂 Estructura del Proyecto

```
qa-project-Urban-Routes-es
├── data.py               # Datos de prueba: URL, direcciones, teléfono, tarjeta, mensajes
├── localizadores.py      # Localizadores (XPaths, CSS Selectors) de elementos de la app
├── selector.py           # Definición de la clase Page Object Model (UrbanRoutesPage)
├── phone_code.py         # Utilidad para extraer el código SMS desde los logs del navegador
├── TestUrbanRoutes.py    # Archivo principal con todos los casos de prueba organizados
└── README.md             # Documentación del proyecto (este archivo)
```

## ▶️ Instrucciones para ejecutar las pruebas

1. Clonar el repositorio o descargar el proyecto.
2. Asegúrate de tener instalado Python 3 y las librerías necesarias:

   ```bash
   pip install selenium pytest
   ```
3. Descarga y configura el ChromeDriver compatible con tu versión de Google Chrome y agrégalo al PATH del sistema.
4. Edita el archivo `data.py` con tus datos de prueba personalizados (direcciones, número telefónico, tarjeta, etc.).
5. Ejecuta las pruebas con:

   ```bash
   pytest TestUrbanRoutes.py
   ```
6. Observa el reporte en consola con los resultados de las pruebas.

## 🧪 Requisitos previos

* Tener instalado **Python 3.8** o superior
* Tener instalado **Google Chrome**
* Tener el ejecutable `chromedriver` compatible con tu versión de Chrome

## 📝 Notas adicionales

* El proyecto utiliza capacidades del navegador para acceder a los logs de red y obtener el código de confirmación SMS, por lo que es importante **no modificar la configuración de Chrome en `setup_class`**.
* Se recomienda ejecutar las pruebas en un entorno de prueba o staging.

---
