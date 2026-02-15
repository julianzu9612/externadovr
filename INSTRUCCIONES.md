# Instrucciones para la Experiencia AR (Externado VR)

Para que la experiencia funcione mañana en la ponencia, sigue estos pasos:

## 1. Generar los Marcadores (.mind)
La cámara necesita saber qué buscar. Sigue estos pasos exactos:
1.  Ve a: [https://hiukim.github.io/mind-ar-js-doc/tools/compile](https://hiukim.github.io/mind-ar-js-doc/tools/compile)
2.  Arrastra las fotos de los rectores que me pasaste.
3.  Asegúrate de que el orden sea:
    *   **Foto 1**: Rector del escritorio (será `targetIndex: 0`)
    *   **Foto 2**: Rector del fondo rojo (será `targetIndex: 1`)
4.  Haz clic en **"Export"**. Obtendrás un archivo llamado `targets.mind`.
5.  Copia ese archivo en: `assets/targets/targets.mind`.

## 2. Preparar los Videos
1.  Busca o crea los videos que quieres que se vean sobre los cuadros.
2.  Guárdalos en la carpeta `assets/videos/`.
3.  Nómbralos como `rector1.mp4` y `rector2.mp4` (o ajusta los nombres en el `index.html`).

## 3. Probar Localmente
Para probar en tu computadora:
1.  Abre una terminal en esta carpeta.
2.  Activa el venv: `.\venv\Scripts\activate`
3.  Corre el servidor: `python -m http.server 8000`
4.  Abre en tu navegador: `http://localhost:8000`

## 4. Para la Ponencia (Crucial) 🚨
Para que los asistentes lo vean en sus móviles, el sitio **DEBE estar en HTTPS**.
*   **Opción A (Recomendada y rápida)**: Sube esta carpeta a un repositorio de **GitHub** y activa **GitHub Pages**. Es gratis, rápido y tiene HTTPS.
*   **Opción B**: Usa **Vercel** o **Netlify** (solo arrastras la carpeta y ya).

## 5. Diseño de los QRs
En la entrada del museo, coloca un QR que apunte a la URL de tu sitio (ej. `https://tuusuario.github.io/externadovr`).
