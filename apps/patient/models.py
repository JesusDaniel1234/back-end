from django.db import models


# Create your models here.
class PatientData(models.Model):
    patient_name = models.CharField(max_length=100)

    CI = models.CharField(max_length=11, unique=True, null=False)

    age_in_month = models.PositiveIntegerField()

    tutor_name = models.CharField(max_length=100)

    @property
    def valoration(self):
        has_mr = False

        response_groups = [
            self.mchatrresponses_responses.all(),
            self.qchatresponses_responses.all(),
            self.qchat10responses_responses.all(),
        ]

        for responses in response_groups:
            for response in responses:
                if response.valoration == "AR":
                    return "AR"

                if response.valoration == "MR":
                    has_mr = True

        return "MR" if has_mr else "BR"

    class Meta:
        verbose_name = "Paciente"

        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.patient_name + " " + self.CI
