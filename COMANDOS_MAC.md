# 🍎 Comandos para Ejecutar en Mac

## Paso 1: Preparar el Proyecto

```bash
# Navegar a la carpeta del proyecto
cd /Users/Escritorio/makerstudios-bot

# Crear un virtual environment
python3 -m venv venv

# Activar el virtual environment
source venv/bin/activate

# Deberías ver (venv) en tu terminal ahora

# Instalar las dependencias
pip install -r requirements.txt

# Esto tardará unos segundos
```

## Paso 2: Configurar Credenciales

```bash
# Copiar el template de .env
cp .env.example .env

# Abrir el archivo en el editor de texto
nano .env

# Ahora edita cada línea con tus credenciales:
# INSTAGRAM_ACCESS_TOKEN=...
# INSTAGRAM_APP_SECRET=...
# etc.

# Para salir de nano: Ctrl+X, luego Y, luego Enter
```

**Necesitas obtener las credenciales de:**
1. **Meta for Developers** (Instagram Token, App Secret, Page ID)
2. **Anthropic** (Claude API Key)
3. **Gmail** (Email y App Password)

Ver el archivo **SETUP.md** para instrucciones detalladas.

## Paso 3: Probar la Configuración (Opcional pero Recomendado)

```bash
# Verificar que todo está correctamente configurado
python3 test_bot.py

# Deberías ver ✓ en todo
# Si hay ✗, revisa el error y ajusta tu .env
```

## Paso 4: Exponer el Webhook (Necesario para Testing)

En una **NUEVA terminal** (sin cerrar la que tienes):

```bash
# Instalar ngrok si no lo tienes (una sola vez)
brew install ngrok

# Exponer tu servidor local al internet
ngrok http 5000

# Deberías ver algo como:
# Forwarding https://abc123.ngrok.io -> http://localhost:5000
```

**Copia esa URL (abc123.ngrok.io)** y úsala en Meta for Developers → Webhook → Callback URL.

## Paso 5: Ejecutar el Bot

En tu terminal original (donde hiciste `source venv/bin/activate`):

```bash
# Iniciar el servidor Flask
python3 app.py

# Deberías ver:
# 🚀 Bot de MakerStudios iniciando...
# ✓ Componentes inicializados correctamente
# * Running on http://0.0.0.0:5000
```

**¡El bot está corriendo!** 🎉

## Paso 6: Probar el Bot

1. Abre **Instagram** (web o app móvil)
2. Busca **@makerstudios.cl**
3. Envía un mensaje: *"Hola, cuánto cuesta una pieza en PLA?"*
4. El bot debería responder automáticamente en 5-10 segundos

Revisa `conversations.json` para ver el log:
```bash
cat conversations.json
```

## 🛑 Para Detener el Bot

En la terminal donde corre `python3 app.py`:
```
Presiona: Ctrl+C
```

Esto detiene el servidor Flask.

## ⚙️ Comandos Útiles

```bash
# Si necesitas volver a activar el venv en una nueva terminal:
source venv/bin/activate

# Ver las dependencias instaladas:
pip list

# Ver los últimos mensajes guardados:
tail -f conversations.json

# Desactivar el virtual environment:
deactivate

# Ver los logs en tiempo real:
tail -f app.log
```

## 🚀 Para Producción (Más Adelante)

Cuando quieras que el bot esté permanentemente en línea:

1. **Opción A: Usar un hosting gratuito**
   - Railway.app
   - Render.com
   - Heroku

2. **Opción B: Tu propio servidor**
   - DigitalOcean ($5/mes)
   - AWS EC2
   - Linode

3. **Opción C: VPS en Chile**
   - NiCDC
   - AXARNET

Para producción, cambia en `.env`:
```
FLASK_DEBUG=False
```

## 📱 Mantener el Bot Corriendo 24/7 en Mac

Si quieres que el bot corra todo el tiempo en tu Mac (sin cerrar la terminal):

### Opción 1: Usar `screen` (Simple)

```bash
# Abre una nueva sesión en background
screen -S makerstudios

# Luego:
cd /Users/Escritorio/makerstudios-bot
source venv/bin/activate
python3 app.py

# Para salir sin cerrar el proceso:
Ctrl+A, luego D

# Para volver a la sesión:
screen -r makerstudios

# Para ver todas las sesiones:
screen -ls
```

### Opción 2: Usar `nohup`

```bash
cd /Users/Escritorio/makerstudios-bot
source venv/bin/activate

# Ejecutar en background
nohup python3 app.py > bot.log 2>&1 &

# Ver el log:
tail -f bot.log

# Para detener:
pkill -f "python3 app.py"
```

### Opción 3: Crear un Launch Agent (Recomendado para Mac)

Crea un archivo `~/Library/LaunchAgents/com.makerstudios.bot.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.makerstudios.bot</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/Users/Escritorio/makerstudios-bot/app.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>/Users/Escritorio/makerstudios-bot</string>

    <key>StandardOutPath</key>
    <string>/Users/Escritorio/makerstudios-bot/bot.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/Escritorio/makerstudios-bot/error.log</string>

    <key>KeepAlive</key>
    <true/>

    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

Luego:
```bash
# Habilitar el agente
launchctl load ~/Library/LaunchAgents/com.makerstudios.bot.plist

# El bot iniciará automáticamente cuando enciendas tu Mac

# Para detenerlo:
launchctl unload ~/Library/LaunchAgents/com.makerstudios.bot.plist

# Ver logs:
tail -f /Users/Escritorio/makerstudios-bot/bot.log
```

## 🔍 Troubleshooting

### "command not found: python3"
```bash
# Instala Python via Homebrew
brew install python3
```

### "venv: command not found"
```bash
# Actualiza pip y venv
python3 -m pip install --upgrade pip
python3 -m venv venv
```

### "ModuleNotFoundError: No module named 'flask'"
```bash
# Asegúrate que el venv está activado
source venv/bin/activate

# Instala las dependencias de nuevo
pip install -r requirements.txt
```

### El bot no responde en Instagram
1. Verifica que ngrok está corriendo en otra terminal
2. Comprueba que usaste la URL de ngrok en Meta Webhook
3. Verifica que ANTHROPIC_API_KEY es válido
4. Mira los logs: `tail -f conversations.json`

### Puerto 5000 ya está en uso
```bash
# Cambiar el puerto en .env
FLASK_PORT=5001

# O ver qué proceso usa el puerto 5000
lsof -i :5000

# Y matarlo si es necesario
kill -9 <PID>
```

---

## ✅ Resumen de Configuración

1. ✓ Descargar código
2. ✓ `python3 -m venv venv`
3. ✓ `source venv/bin/activate`
4. ✓ `pip install -r requirements.txt`
5. ✓ `cp .env.example .env` → Editar con credenciales
6. ✓ En otra terminal: `ngrok http 5000`
7. ✓ `python3 app.py`
8. ✓ Enviar DM a Instagram
9. ✓ ¡El bot responde automáticamente!

**¡Listo! Tu bot está corriendo. 🚀**
