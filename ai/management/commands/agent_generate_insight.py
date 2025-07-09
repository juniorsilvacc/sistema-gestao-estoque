from django.core.management.base import BaseCommand
from ai.agent import SGEAgent


class Command(BaseCommand):

    def handle(self, *args, **options):
        agent = SGEAgent()
        agent.generate_insight()

        self.stdout.write(
            self.style.SUCCESS("AGENT DE IA CHAMADO COM SUCESSO!")
        )