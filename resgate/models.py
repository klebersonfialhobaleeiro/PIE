from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    TIPO_ANIMAL = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
    )
    
    especie = models.CharField(max_length=50, choices=TIPO_ANIMAL)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='animais/', blank=True, null=True)

    resgatado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_resgatou')
    data_resgate = models.DateTimeField(auto_now_add=True)

    adotado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_adotou')
    data_adocao = models.DateTimeField(blank=True, null=True)
    adotado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.especie}'