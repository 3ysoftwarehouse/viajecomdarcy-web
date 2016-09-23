from django.db import models

class StatusReserva(models.Model):

    id_status_reserva = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return self.descricao


class StatusReservaPassageiro(models.Model):

    id_status_reserva_passageiro = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return self.descricao


class Reserva(models.Model):

	id_reserva = models.AutoField(primary_key=True)
	id_cliente = models.ForeignKey('cliente.Cliente', on_delete=models.DO_NOTHING)
	id_emissor = models.ForeignKey('emissor.Emissor', on_delete=models.DO_NOTHING)
	id_agencia = models.ForeignKey('agencia.Agencia', on_delete=models.DO_NOTHING)
	id_status_reserva = models.ForeignKey('StatusReserva', on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.id_status_reserva


class ReservaPassageiro(models.Model):

    id_reserva_passageiro = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey('Reserva', on_delete=models.DO_NOTHING)
    id_passageiro = models.ForeignKey('cliente.Cliente', on_delete=models.DO_NOTHING)
    id_pacote = models.ForeignKey('pacote.Pacote', on_delete=models.DO_NOTHING)
    id_status_reserva_passageiro = models.ForeignKey('StatusReservaPassageiro', on_delete=models.DO_NOTHING)
    id_escola = models.ForeignKey('escola.Escola', on_delete=models.DO_NOTHING)
    reserva_passageiro_preco =  models.DecimalField(max_digits=10, decimal_places=2)
    id_moeda = models.ForeignKey('moeda.Moeda', on_delete=models.DO_NOTHING)
    reserva_passageiro_cambio = models.DecimalField(max_digits=5, decimal_places=4)
    reserva_passageiro_obs = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.reserva_passageiro_obs



