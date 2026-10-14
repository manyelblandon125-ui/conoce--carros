# Garaje

Sitio web de muestra para explorar carros, consultar sus piezas y probar una personalización visual. La aplicación usa Flask para servir la página.

## Ejecutar localmente

Requiere Python 3.9 o superior.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

Abre <http://127.0.0.1:5000>.

## Publicar con GitHub y Render

1. Crea un repositorio **público** en GitHub y súbele los archivos de este proyecto.
2. En Render, elige **New + → Blueprint** y conecta ese repositorio.
3. Render leerá `render.yaml`, instalará las dependencias y publicará el servicio web en el plan gratuito. Al terminar, mostrará la dirección pública del sitio. En el plan gratuito, el servicio puede tardar unos segundos en despertar si estuvo inactivo.
4. Los siguientes cambios enviados a la rama conectada se podrán desplegar automáticamente.

La ruta `/healthz` permite que Render compruebe que el servicio está respondiendo.

## Alcance actual

El catálogo y los precios son datos de ejemplo que viven en `index.html`. El personalizador funciona en el navegador, pero todavía no guarda configuraciones en una base de datos ni recibe anuncios de vendedores. Las imágenes y fuentes se cargan desde servicios externos.
