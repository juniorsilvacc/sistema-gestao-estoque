import json
from django.core import serializers
from django.conf import settings
from openai import OpenAI
from ai import prompts, models
from products.models import Product
from outflows.models import Outflow


class SGEAgent:

    def __init__(self):
        self.use_fake = getattr(settings, 'USE_FAKE_OPENAI', False)

        # Após iniciar a classe ele já faz a criação do client
        if not self.use_fake:
            self.__client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()
        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows),
        })

    def generate_insight(self):
        if self.use_fake:
            result = self.__fake_response()
        else:
            response = self.__client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {'role': 'system', 'content': prompts.SYSTEM_PROMT},
                    {'role': 'user', 'content': prompts.SYSTEM_USER.replace('{{data}}', self.__get_data())}
                ]
            )
            result = response.choices[0].message.content

        models.APIResult.objects.create(result=result)

    def __fake_response(self):
        return "⚠️ [RESPOSTA FAKE] Resultado gerado para simulação no ambiente de desenvolvimento."