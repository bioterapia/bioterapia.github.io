# Plantillas de Instagram · Bioterapia (@bioterapia.arg)

Plantillas HTML con las que se generan las placas. Se renderizan a PNG con Chrome headless (Playwright).

## Preparación
```
cp -r instagram/_plantillas /tmp/ig && cd /tmp/ig
mkdir fonts && cd fonts && npm pack @fontsource/great-vibes @fontsource/playfair-display && for f in *.tgz; do tar xzf $f --one-top-level=${f%.tgz}; done && cd ..
# render: python3 render2.py <nombre_sin_.html> ...  (1080x1080). Historias: viewport 1080x1920.
```
Montserrat se carga desde /usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf.

## Archivos
- `v2.css`: estilos base (crema, violeta #8E3B7E/#6B2E61, rosa #EE7F97, menta #8FCDB5; Playfair Display títulos, Great Vibes firmas, Montserrat texto). Placas cuadradas 1080x1080.
- `m4.html`: placa de serie (kicker, título 2 tonos, pill con 3 ítems, descripción, ilustración a la derecha). `m8.html`: placa resumen/cierre.
- `masks*.svg`: ilustraciones acuarela de máscaras (fondo rosa con turbulencia, hojas). `blob.svg`: mancha acuarela decorativa.
- `d02.html`, `d09.html`: placa firmada por profesional (con lista / sin lista), con WhatsApp e Instagram abajo.
- `eq1.html`, `eq2.html`: carrusel del equipo (portada / profesional con foto en arco). `foto_*.jpg`: fotos del equipo.
- `stories/historia_ejemplo.html`: historia 1080x1920 "Nueva publicación" con la placa en miniatura (ajustar rutas de imagen).

## Datos del equipo
- Ailen Pierucci · Psicóloga · M.P.R.N. 2389 · WhatsApp 299 405 0874 · @bioterapia.arg
- Carla Tanzi · Psicóloga · M.P.R.N. 1668 · WhatsApp 299 466 5738 · @tanziyoga
- Marcelo de los Santos · Biodescodificación e Hipnosis · WhatsApp 299 405 0874 · @bioterapia.arg
