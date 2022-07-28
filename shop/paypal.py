import sys
from django.conf import settings
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AW7Tl5AJ26bMhj7PR2eUtj0Kr4JD5q6GVqaDqq_D7YPQUeOAIbHledkYtDsiKcrbv1hFS9nkFVc3VG6_"
        self.client_secret = "EM7d4tAHMr0Tz4VOrOKqDDqnQXka8VwX_lnmgRPdDYwfrzDPCuLdHc1c1DQ7CGvMpC_FA78vBWB4VjjG"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
