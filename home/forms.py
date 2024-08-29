from django import forms
from .models import Plantao


class FormularioPlantao(forms.forms):
        medicos = forms.ChoiceField(
                choices=[('0','--Selecione--')] + [(medico.id, medico.medico_responsavel) for medico in Plantao.objects.all()]
        )


#
#class FormularioPlantao(forms.ModelForm):
#    class Meta:
#        model= Plantao
#        fields =['data_inicio','hora_inicio','data_termino','hora_termino','especialidade','tipo_plantao','quantidade_horas','valor','status','contato_emergencia','equipamentos_necessarios','cargos_auxiliares','substituto','observacoes','medico_responsavel']