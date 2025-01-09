from django.db.models.signals import post_migrate, pre_delete
from .models import PreguntasMChatR, RespuestasMchtR
from django.dispatch import receiver


@receiver(post_migrate)
def crear_preguntas_qchat(sender, **kwargs):
    if sender.name=="mchatr":
        if not PreguntasMChatR.objects.exists():
            preguntas = [
                {
                    "contenido": "Si usted señala algo al otro lado de la habitación, ¿su hijo/a lo mira? (POR EJEMPLO, Si usted señala a un juguete, un peluche o un animal, ¿su hijo/a lo mira?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Alguna vez se ha preguntado si su hijo/a es sordo/a?",
                    "respuesta_riesgo": "SI",
                },
                {
                    "contenido": "¿Su hijo/a juega juegos de fantasía o imaginación? (POR EJEMPLO, ¿hace como que bebe de una taza vacía, habla por teléfono o da de comer a una muñeca o peluche,…?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿A su hijo le gusta subirse a cosas? (POR EJEMPLO, a una silla, escaleras, o tobogán,…)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Hace su hijo/a movimientos inusuales con sus dedos cerca de sus ojos? (POR EJEMPLO, ¿mueve sus dedos cerca de sus ojos de manera inusual?)",
                    "respuesta_riesgo": "SI",
                },
                {
                    "contenido": "¿Su hijo/a señala con un dedo cuando quiere pedir algo o pedir ayuda? (POR EJEMPLO, ¿señala un juguete o algo de comer que está fuera de su alcance?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "Su hijo/a señala con un dedo cuando quiere mostrarle algo que le llama la atención? (POR EJEMPLO, ¿señala un avión en el cielo o un camión muy grande en la calle)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a se interesa en otros niños? (POR EJEMPLO, ¿mira con atención a otros niños, les sonríe o se les acerca?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a le muestra cosas acercándolas o levantándolas para que usted las vea – no para pedir ayuda sino solamente para compartirlas con usted? (POR EJEMPLO, ¿le muestra una flor o un peluche o un coche de juguete?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a responde cuando usted le llama por su nombre? (POR EJEMPLO, ¿se vuelve, habla o balbucea, o deja de hacer lo que estaba haciendo para mirarle?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Cuándo usted sonríe a su hijo/a, él o ella también le sonríe?",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Le molestan a su hijo/a ruidos cotidianos? (POR EJEMPLO, ¿la aspiradora o la música, incluso cuando está no está excesivamente alta?)",
                    "respuesta_riesgo": "SI",
                },
                {
                    "contenido": "¿Su hijo/a camina solo?",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a le mira a los ojos cuando usted le habla, juega con él o ella, o lo viste?",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a imita sus movimientos? (POR EJEMPLO, ¿decir adiós con la mano, aplaudir o algún ruido gracioso que usted haga?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "Si usted se gira a ver algo, ¿su hijo/a trata de mirar hacia lo que usted está mirando?",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a intenta que usted le mire/preste atención? (POR EJEMPLO, ¿busca que usted le haga un cumplido, o le dice “mira” o ”mírame”?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "¿Su hijo/a le entiende cuando usted le dice que haga algo? (POR EJEMPLO, si usted no hace gestos, ¿su hijo/a entiende “pon el libro encima de la silla” o “tráeme la manta”?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "Si algo nuevo pasa, ¿su hijo/a le mira para ver como usted reacciona al respecto? (POR EJEMPLO, ¿si oye un ruido extraño o ve un juguete nuevo, ¿se gira a ver su cara?)",
                    "respuesta_riesgo": "NO",
                },
                {
                    "contenido": "Le gustan a su hijo/a los juegos de movimiento? (POR EJEMPLO, ¿le gusta que le balancee, o que le haga “el caballito” sentándole en sus rodillas?)",
                    "respuesta_riesgo": "NO",
                },
                
                
            ]
            for pregunta in preguntas:
                PreguntasMChatR.objects.create(contenido=pregunta["contenido"],respuesta_riesgo=pregunta["respuesta_riesgo"])
                
@receiver(pre_delete, sender=RespuestasMchtR)
def eliminar_respuestas(sender, instance, **kwargs):
    respuestas = instance.respuestas.all()
    print(f"Eliminando respuestas asociadas con {respuestas}")
    for respuesta in respuestas:
        if RespuestasMchtR.objects.filter(respuestas=respuesta).count() == 1:
            print(f"Eliminando respuesta {respuesta}")
            respuesta.delete()