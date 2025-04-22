from django.db import models
from django.contrib.auth.models import User

class Relato(models.Model):

    TIPOS_PROBLEMA = [
        ('A', 'Alagamento'),
        ('B', 'Buraco'),
        ('L', 'Lixo'),
        ('I', 'Iluminação'),
        ('S', 'Saneamento'),
        ('O', 'Outro'),
    ]
    tipo_problema = models.CharField(
        max_length=1,
        choices=TIPOS_PROBLEMA,
        default='O'
    )

    descricao = models.TextField(help_text="Descrição detalhada do problema")
    foto = models.ImageField(upload_to='relatos_fotos/', null=True, blank=True, help_text="Foto do local do relato")
    poligono = models.JSONField(help_text="Formato: lista de pares [lat, lng] ou GeoJSON")
    data_relato = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relatos')

    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Em Análise'),
        ('R', 'Resolvido'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
    )

    def __str__(self):
        return f"{self.get_tipo_problema_display()} - {self.data_relato.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Relato"
        verbose_name_plural = "Relatos"
        ordering = ['-data_relato']
