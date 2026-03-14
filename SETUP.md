# 🚀 Guía de Configuración - Bot MakerStudios

## 1. Obtener Credenciales en Meta for Developers

### Paso 1.1: Crear una App en Meta
1. Ve a https://developers.facebook.com/
2. Haz click en **My Apps** (arriba a la derecha)
3. Click en **Create App**
4. Elige **Business** como tipo de app
5. Completa los datos y crea la app

### Paso 1.2: Obtener Page Access Token
1. En tu app, ve a **Messenger** → **Settings**
2. En la sección **Access Tokens**, selecciona tu página de Facebook
3. Se mostrará tu **Page Access Token** - cópialo (largo string que empieza con `EA...`)
4. Este es tu `INSTAGRAM_ACCESS_TOKEN`

### Paso 1.3: Obtener APP SECRET
1. Ve a **Settings** → **Basic** en tu app
2. Busca **App Secret** (necesitarás verificar tu identidad)
3. Cópialo - este es tu `INSTAGRAM_APP_SECRET`

### Paso 1.4: Obtener PAGE ID
1. Ve a tu página de Facebook
2. Abre la URL, el número al final es tu PAGE ID
3. O usa https://www.whatsmypageid.com/
4. Este es tu `INSTAGRAM_PAGE_ID`

### Paso 1.5: Configurar el Webhook
1. En tu app, ve a **Messenger** → **Settings**
2. Scroll a **Webhooks**
3. Click en **Add Callback URL**
   - **Callback URL**: Tu URL pública (ej: https://tu-dominio.com/webhook)
   - **Verify Token**: Un token que tú crees (ej: "abc123XYZ")
4. En Meta, se enviará un GET request - tu app debe responder con el challenge
5. Una vez verificado, selecciona:
   - **Subscribe to events**: Messages

## 2. Obtener API Key de Anthropic

1. Ve a https://console.anthropic.com/
2. Haz login o crea una cuenta
3. Click en **API Keys** en el sidebar
4. Click en **Create Key**
5. Copia la clave generada - este es tu `ANTHROPIC_API_KEY`

## 3. Configurar Email para Notificaciones

### Opción A: Usar Gmail (Recomendado)

1. Abre tu cuenta Gmail
2. Ve a **Seguridad** (https://myaccount.google.com/security)
3. Busca **Contraseñas de aplicación**
   - Si no la ves, primero activa **Verificación en 2 pasos**
4. Selecciona **Mail** y **Windows Computer** (o tu dispositivo)
5. Gmail generará una contraseña especial - cópiala
6. Este es tu `EMAIL_PASSWORD` (NO tu contraseña normal de Gmail)
7. Tu `EMAIL_SENDER` es tu email de Gmail (ej: tu_email@gmail.com)

### Opción B: Usar Otro Email SMTP
Modifica `bot/email_notifier.py` con:
```python
self.smtp_server = "tu-servidor-smtp.com"  # Ej: smtp.outlook.com
self.smtp_port = 587  # O el puerto de tu proveedor
```

## 4. Crear el Archivo .env

Copia `.env.example` a `.env` y llena todos los valores:

```bash
cp .env.example .env
```

Luego edita `.env` con tus credenciales:

```
INSTAGRAM_ACCESS_TOKEN=EA1234567890...
INSTAGRAM_APP_SECRET=a1b2c3d4e5f6...
WEBHOOK_VERIFY_TOKEN=abc123XYZ
INSTAGRAM_PAGE_ID=1234567890
ANTHROPIC_API_KEY=sk-ant-v0-...
EMAIL_SENDER=tu_email@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
```

⚠️ **IMPORTANTE**: Nunca compartas tu `.env` - agrégalo a `.gitignore`

## 5. Instalar Dependencias

```bash
cd /Users/Escritorio/makerstudios-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 6. Exponer el Webhook Localmente (Para Testing)

Para probar localmente, necesitas exponer tu servidor Flask a internet:

### Opción A: ngrok (Fácil)

```bash
# Instalar ngrok (si no lo tienes)
brew install ngrok

# Exponer tu servidor
ngrok http 5000
```

Esto te dará una URL como: `https://abc123.ngrok.io`

Usa `https://abc123.ngrok.io/webhook` en Meta for Developers

### Opción B: Usar un VPS (Producción)

Despliega en un servidor con Python 3.11+:
- Heroku (gratis con limitaciones)
- Railway
- Render
- DigitalOcean
- AWS EC2

## 7. Ejecutar el Bot

```bash
# Activar el virtual environment
source venv/bin/activate

# Ejecutar la app
python3 app.py
```

Deberías ver:
```
============================================================
🚀 Bot de MakerStudios iniciando...
============================================================
Puerto: 5000
Debug: True
Negocio: MakerStudios
============================================================

✓ Componentes inicializados correctamente
 * Running on http://0.0.0.0:5000
```

## 8. Probar el Bot

1. Abre Instagram (móvil o web)
2. Busca @makerstudios.cl
3. Envía un DM de prueba
4. El bot debería responder automáticamente

Revisa `conversations.json` para ver el log de la conversación.

## 🔧 Troubleshooting

### Error: "INSTAGRAM_ACCESS_TOKEN es requerido"
- Verifica que creaste el archivo `.env`
- Asegúrate de que copiaste el token completo desde Meta

### Error: "ANTHROPIC_API_KEY es requerido"
- Verifica que creaste una API key en console.anthropic.com
- Actualiza `.env` con la clave

### No recibe mensajes
- Verifica que el webhook está verificado en Meta
- Comprueba que usaste la URL correcta (con `/webhook`)
- Revisa los logs en Meta for Developers → Logs

### Email no se envía
- Para Gmail: verifica que usaste una **App Password**, no tu contraseña
- Comprueba que habilitaste "Verificación en 2 pasos" en Gmail
- Revisa el archivo `bot/email_notifier.py` para ver el error

### El bot responde lentamente
- Claude puede tardar 5-10 segundos en generar respuestas
- Esto es normal - es un trade-off entre calidad y velocidad
- Para respuestas instantáneas, podrías usar respuestas pre-escritas

## 📚 Archivos Importantes

- `config.json` - Configuración del negocio (precios, materiales, tono, etc.)
- `conversations.json` - Log de todas las conversaciones
- `.env` - Credenciales (NO SUBIR A GIT)
- `app.py` - Servidor Flask principal
- `bot/claude_agent.py` - Integración con Anthropic Claude
- `bot/instagram.py` - Cliente Meta Graph API
- `bot/email_notifier.py` - Notificaciones por email
- `bot/conversation_log.py` - Sistema de logging

## 🚀 Producción (Deploying)

Para lanzar en producción, considera:


1. Usar un servicio de hosting (Railway, Render, etc.)
2. Cambiar `FLASK_DEBUG=False` en `.env`
3. Usar un servidor WSGI como `gunicorn`:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
4. Proteger tus credenciales usando secrets manager del hosting
5. Configurar logs centralizados para debugging
6. Agregar rate limiting para evitar abuso

## 📞 Soporte

Si hay problemas:
1. Revisa los logs de la aplicación
2. Verifica las credenciales en `.env`
3. Comprueba que el webhook está verificado en Meta
4. Prueba enviando un mensaje de prueba desde Instagram

¡Buena suerte! 🎉


