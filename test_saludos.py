"""
Test para verificar la detección de saludos.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from bot.claude_agent import crear_agent_claude
from dotenv import load_dotenv

load_dotenv()

def test_saludos():
    """Test detección de saludos."""

    print("\n" + "="*60)
    print("🧪 TEST: Detección de Saludos")
    print("="*60 + "\n")

    claude_agent = crear_agent_claude()

    saludos_positivos = [
        "Hola",
        "Buenos días",
        "Buenos tardes",
        "Hola, ¿cómo estás?",
        "Hey, qué tal",
        "Buen día, necesito información",
        "Buenos días, tengo una pregunta",
    ]

    no_saludos = [
        "¿Cuánto cuesta una pieza?",
        "Necesito una cotización",
        "¿Qué materiales tienen?",
        "Tengo un reclamo",
        "Quiero hablar con alguien",
    ]

    print("Pruebas POSITIVAS (deben detectar saludo):")
    print("-" * 60)
    for texto in saludos_positivos:
        es_saludo = claude_agent.detectar_saludo(texto)
        status = "✓" if es_saludo else "✗"
        print(f"  {status} '{texto}' → es_saludo={es_saludo}")
        assert es_saludo, f"Debería detectar saludo en: {texto}"

    print("\nPruebas NEGATIVAS (NO deben detectar saludo):")
    print("-" * 60)
    for texto in no_saludos:
        es_saludo = claude_agent.detectar_saludo(texto)
        status = "✓" if not es_saludo else "✗"
        print(f"  {status} '{texto}' → es_saludo={es_saludo}")
        assert not es_saludo, f"NO debería detectar saludo en: {texto}"

    print("\n" + "="*60)
    print("✅ TODOS LOS TESTS PASARON")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        test_saludos()
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
