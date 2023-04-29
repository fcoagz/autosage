# auto-sage 🧙
Es un sabio automatizado que se ejecuta en el navegador Chrome en segundo plano. Utiliza el modelo de lenguaje GPT-3 que emplea un aprendizaje profundo.

Este proyecto está destinado únicamente a fines educativos. Este es solo un pequeño proyecto personal que he querido hacer ya un tiempo. He creado una API terciaria que me pueda automatizar la tarea desde el navegador y me retorne la promesa.

## Requerimientos
- Descarga las dependencias `pip install -r requeriments.txt`
- Navegador Chrome con una version superior de `112.0.5615.138`
- Python 3.10

No es necesario instalar Chrome Driver ya que el sabio lo hace por ti!

## Pagina web 
| Sito Web                  | Modelo  |
| --------------------------| ------- |
|[poe.com](https://poe.com) | GPT-3.5 |

## Uso
Crea una instancia de la clase Poe y establece una conexión con el chatbot. Luego, solicita al usuario que ingrese el código de verificación enviado por correo electrónico y lo envía al chatbot para verificar la sesión. Después de la verificación, inicia un bucle while que permite al usuario enviar mensajes al chatbot y recibir respuestas.

```python
from colorama import Fore
from autosage import Poe

if __name__ == '__main__':
    mychat = Poe(
        name_session='my_account',
        email='hi@outlook.es'
    )
    mychat.connect()

    code = input('Send the code receive in email: ')
    mychat.send_verification_code(code)

    while True:
        prompt = str(input(Fore.BLUE + 'Me: ' + Fore.RESET))
        answer = mychat.sage(prompt=prompt)

        print(Fore.GREEN + 'AutoSage: ' + answer + Fore.RESET)
```
### Funciones
- `mychat`: Una instancia de la clase Poe que se utiliza para interactuar con el chatbot.
- `code`: Una cadena que contiene el código de verificación enviado por correo electrónico al usuario.
- `mychat.send_verification_code(code)`: Una función que envía el código de verificación al chatbot para verificar la sesión.
- `prompt`: Una cadena que contiene el mensaje enviado por el usuario al chatbot.
- `mychat.sage(prompt=prompt)`: Una función que envía el mensaje del usuario al chatbot y devuelve la respuesta del chatbot.
- `answer`: Una cadena que contiene la respuesta del chatbot al mensaje del usuario.

### Ejecucion
```yaml
$ python autosage_chatbot.py
Send the code receive in email: ******
Me: Hola
AutoSage: ¡Hola! ¿En qué puedo ayudarte hoy?
Me: ¿Qué tiempo hace?
AutoSage: Lo siento, no puedo ayudarte con eso. ¿Hay algo más en lo que pueda ayudarte?
Me: ¿Cuál es tu nombre?
AutoSage: Me llamo Sage. ¿Y tú?
Me: Me llamo Cisco
AutoSage: ¡Hola Cisco! ¿En qué puedo ayudarte hoy?
```

El parametro `name_session` guardara las cookies una vez que hayas ingresado exitosamente, por lo tanto cuando vuelvas a ejecutar, hazlo de la siguiente manera:

```python
from colorama import Fore
from autosage import Poe

if __name__ == '__main__':
    mychat = Poe(
        name_session='my_account'
    )
    mychat.connect()

    while True:
        prompt = str(input(Fore.BLUE + 'Me: ' + Fore.RESET))
        answer = mychat.sage(prompt=prompt)

        print(Fore.GREEN + 'AutoSage: ' + answer + Fore.RESET)
```