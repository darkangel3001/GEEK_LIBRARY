from django import forms
from . import models, paser_manas


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('manas', 'manas'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type"
        ]

    def parser_data(self):
        if self.data['media_type'] == 'manas':
            manas_file = paser_rezka.parsing()
            for i in manas_file:
                models.ManasModel.objects.create(**i)
