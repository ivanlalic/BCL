# BCL 900 — Carbón Activado Líquido para Cultivo

Sitio web y herramienta interactiva de simulación de rendimientos para **BCL 900** de Biocharg.

## Características

* **Inicio**: Información general del producto, su naturaleza orgánica no biológica y mitigación de estrés abiótico.
* **Mapa de Ensayos**: Mapa interactivo con Leaflet.js mostrando la ubicación y el rinde de los ensayos 2026.
* **Planilla de Ensayos**: Tabla completa de rendimientos con comparativa de Testigo vs. BCL 900 y visualización de gráficos dinámicos con Plotly.js.
* **Simulador de Resultados**: Calculadora interactiva que estima el margen neto del productor y el retorno de inversión (ROI) en base al dólar oficial, precio de soja, costo y rinde extra.
* **Guía de Uso**: Instrucciones paso a paso para la correcta aplicación del producto.

## Tecnologías Utilizadas

* HTML5 + CSS3 (diseño responsivo móvil/escritorio con estética bento y modo oscuro premium)
* JavaScript Vanilla
* [Leaflet.js](https://leafletjs.com/) para mapas interactivos
* [Plotly.js](https://plotly.com/javascript/) para gráficos estadísticos
* Google Fonts (Plus Jakarta Sans) & FontAwesome Icons

## Desarrollo Local

Para correr el proyecto de forma local:

```bash
python -m http.server 8000
```

Luego ingresar a `http://localhost:8000`.

---
Creado por Edgardo Lalic - Biocharg - Carbosur SRL.
