# 🤖 Bot Automático de Instagram - MakerStudios

Bot inteligente que responde automáticamente mensajes directos (DMs) de Instagram para tu emprendimiento de impresión 3D, usando **Claude AI** y **Meta Graph API**.

## ✨ Características

- ✅ **Respuestas Automáticas 24/7** - Funciona sin parar, mientras duermes
- 🧠 **Powered by Claude Sonnet** - Respuestas naturales y coherentes
- 📧 **Notificaciones por Email** - Alerta cuando un cliente necesita atención humana
- 💬 **Memoria de Conversación** - Mantiene contexto de chats anteriores
- 📊 **Logging Completo** - Registro de todas las conversaciones en `conversations.json`
- 🎯 **Detección de Escalado** - Reconoce palabras clave urgentes (reclamos, llamadas, etc.)
- 🔐 **Seguro** - Valida firmas HMAC de Meta para evitar requests no autorizados

## 🏗️ Arquitectura

```
Instagram DM (Meta Graph API)
         ↓
    Webhook Flask (app.py)
         ↓
    Detección de Escalado
         ├─→ Escalado Detectado → Email + Respuesta de escalado
         │
         └─→ Conversación Normal → Claude AI (claude_agent.py)
              ↓
              Meta Graph API → Respuesta a Instagram
              ↓
              Log (conversations.json)
```

## 📁 Estructura del Proyecto

```
makerstudios-bot/
├── app.py                          # Servidor Flask + webhook
├── config.json                     # Configuración del negocio
├── requirements.txt                # Dependencias Python
├── .env.example                    # Template de credenciales
├── .env                           # ⚠️ Credenciales (no subir a git)
├── .gitignore                     # Git ignore
├── conversations.json             # Log de conversaciones (auto-creado)
│
├── bot/
│   ├── __init__.py
│   ├── instagram.py               # Cliente Meta Graph API
│   ├── claude_agent.py            # Integración Anthropic Claude
│   ├── email_notifier.py          # Notificaciones por email
│   └── conversation_log.py        # Sistema de logging
│
├── README.md                      # Este archivo
├── SETUP.md                       # Guía detallada de configuración
└── venv/                          # Virtual environment (local)
```

## 🚀 Quick Start (5 minutos)

### 1. Clonar / Descargar el Proyecto

```bash
cd /Users/Escritorio/makerstudios-bot
```

### 2. Crear Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Credenciales

```bash
cp .env.example .env
# Edita .env con tus credenciales de:
# - Meta for Developers (Instagram)
# - Anthropic (Claude API)
# - Gmail (para escalados)
nano .env
```

📖 Ver **SETUP.md** para instrucciones detalladas de cómo obtener cada credencial.

### 5. Exponer Webhook (Desarrollo)

En otra terminal:

```bash
# Instalar ngrok si no lo tienes
brew install ngrok

# Exponer tu servidor local
ngrok http 5000
```

Usa la URL de ngrok en Meta for Developers → Webhook.

### 6. Ejecutar el Bot

```bash
python3 app.py
```

Deberías ver:
```
🚀 Bot de MakerStudios iniciando...
Puerto: 5000
```

### 7. Probar

Envía un DM a tu Instagram (@makerstudios.cl) - ¡el bot responderá automáticamente!

## 🔑 Credenciales Necesarias

| Variable | Origen | Descripción |
|----------|--------|-------------|
| `INSTAGRAM_ACCESS_TOKEN` | Meta for Developers | Token para enviar mensajes |
| `INSTAGRAM_APP_SECRET` | Meta for Developers | Secret para validar webhook |
| `WEBHOOK_VERIFY_TOKEN` | Tú lo creas | Token personalizado para webhook |
| `INSTAGRAM_PAGE_ID` | Tu página de Facebook | ID de la página |
| `ANTHROPIC_API_KEY` | https://console.anthropic.com | API key de Claude |
| `EMAIL_SENDER` | Tu Gmail | tu_email@gmail.com |
| `EMAIL_PASSWORD` | Gmail App Password | Contraseña especial para apps |

Ver **SETUP.md** para obtener cada uno.

## 📝 Configuración del Negocio

Edita `config.json` para personalizar:

```json
{
  "negocio": {
    "nombre": "MakerStudios",
    "descripcion": "...",
    "instagram": "@makerstudios.cl",
    "horario_atencion": "24/7"
  },
  "tono": {
    "estilo": "profesional y formal",
    "instrucciones": "Responder siempre de 'usted'..."
  },
  "precios": {
    "materiales_disponibles": ["PLA", "PETG", "TPU", "ABS"],
    "tiempo_cotizacion": "Respondemos en menos de 24 horas"
  },
  "escalado": {
    "trigger_palabras": ["hablar con alguien", "llamar", "urgente", "reclamo"],
    "notificar_a": "makerstudios.cl@gmail.com"
  }
}
```

## 🧠 Cómo Funciona Claude

El bot:

1. Lee tu `config.json` para entender tu negocio
2. Construye un system prompt profesional basado en tu info
3. Mantiene historial de conversaciones por usuario
4. Usa Claude Sonnet para generar respuestas contextuales
5. Responde en español, profesional y conciso

Ejemplo de conversación:

```
Cliente: "Hola, cuánto cuesta una pieza en PLA?"
Bot: "Buen día. Los precios en PLA dependen del tamaño y complejidad.
      Por favor, envíanos un archivo STL o foto de lo que necesitas
      y te haremos una cotización en menos de 24 horas. ¿Cuál es tu proyecto?"
```

## 📧 Escalado y Notificaciones

Si un cliente escribe palabras como "reclamo", "urgente", "llamar", etc.:

1. El bot responde con: *"Entendido. Le paso con nuestro equipo..."*
2. Se envía un email a `makerstudios.cl@gmail.com` con:
   - ID del cliente
   - Palabra clave detectada
   - Mensaje completo
   - Historial de conversación

Así sabes que necesita atención humana inmediata.

## 📊 Historial de Conversaciones

Todas las conversaciones se guardan en `conversations.json`:

```json
{
  "conversaciones": {
    "123456789": [
      {
        "timestamp": "2025-03-08T10:30:00",
        "rol": "usuario",
        "texto": "Hola, cuánto cuesta una pieza?"
      },
      {
        "timestamp": "2025-03-08T10:30:15",
        "rol": "bot",
        "texto": "Buen día. Los precios dependen de..."
      }
    ]
  }
}
```

Útil para:
- Revisar conversaciones
- Entrenar mejores prompts
- Analizar patrones de clientes
- Auditoría

## ⚙️ Variables de Entorno

```bash
# Meta Instagram
INSTAGRAM_ACCESS_TOKEN=EA1234...
INSTAGRAM_APP_SECRET=a1b2c3...
WEBHOOK_VERIFY_TOKEN=abc123
INSTAGRAM_PAGE_ID=1234567890

# Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-v0...

# Email (Gmail)
EMAIL_SENDER=tu_email@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop

# Flask
FLASK_PORT=5000
FLASK_DEBUG=True
```

## 🛠️ Comandos Útiles

```bash
# Crear virtual environment
python3 -m venv venv

# Activar virtual environment
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el bot
python3 app.py

# Ver logs en tiempo real
tail -f *.log

# Ver conversaciones guardadas
cat conversations.json | python3 -m json.tool

# Instalar ngrok para testing
brew install ngrok

# Exponer servidor local
ngrok http 5000
```

## 📚 Estructura de Código

### `app.py` - Servidor Flask
- `GET /webhook` - Verifica webhook con Meta
- `POST /webhook` - Procesa DMs entrantes
- Valida firmas HMAC-SHA256
- Coordina flujo: Instagram → Claude → Email → Log

### `bot/instagram.py` - Meta Graph API
```python
client = InstagramAPI(token, page_id)
client.enviar_mensaje(recipient_id, "Hola!")
```

### `bot/claude_agent.py` - Anthropic Claude
```python
agent = ClaudeAgent()
respuesta = agent.generar_respuesta(sender_id, "Tu pregunta")
```

### `bot/email_notifier.py` - Notificaciones
```python
notifier = EmailNotifier(email, password)
notifier.enviar_alerta_escalado(...)
```

### `bot/conversation_log.py` - Logging
```python
guardar_mensaje(sender_id, "usuario", "Hola")
historial = obtener_historial(sender_id)
```

## 🔒 Seguridad

- ✅ Validación de firma HMAC-SHA256 (Meta no puede falsificarse)
- ✅ Credenciales en `.env` (nunca en código)
- ✅ `.gitignore` protege archivos sensibles
- ✅ Rate limiting en Meta (configurable)
- ✅ Logs limpios (sin datos sensibles)

## 🚨 Troubleshooting

### "ConnectionError: Webhook no responde"
- Verifica que ngrok está corriendo
- Usa la URL correcta: `https://tu-ngrok.ngrok.io/webhook`

### "Firma HMAC inválida"
- Verifica que `INSTAGRAM_APP_SECRET` es correcto
- Meta puede tomar unos segundos en sincronizar

### "El bot no responde"
- Revisa los logs en Meta for Developers
- Verifica que `ANTHROPIC_API_KEY` es válido
- Asegúrate que el webhook está verificado en Meta

### "Email no llega"
- Para Gmail: usa **App Password**, no tu contraseña normal
- Verifica que habilitaste "Verificación en 2 pasos"

## 📈 Escalabilidad

Para producción:

1. **Hosting**: Railway, Render, Heroku, AWS
2. **Database**: Guardar conversations.json en PostgreSQL o MongoDB
3. **Queue**: Celery para procesar mensajes en background
4. **Monitoring**: Sentry para errores, DataDog para logs
5. **CI/CD**: GitHub Actions para tests automáticos

## 📞 Soporte & Contacto

Si tienes problemas:
1. Lee **SETUP.md** para configuración detallada
2. Revisa los logs de la aplicación
3. Verifica las credenciales en `.env`
4. Prueba con ngrok durante desarrollo

## 📄 Licencia

Este proyecto es para MakerStudios. Úsalo libremente para tu emprendimiento.

---

**Hecho con ❤️ para MakerStudios**

Responde 24/7, concentra en crecer tu negocio de impresión 3D. El bot se encarga de los DMs. 🚀
