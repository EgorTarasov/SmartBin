from django.db import models


class Bin(models.Model):
    name = models.CharField(
        max_length=50,
        default=''
    )
    ip_address = models.CharField(
        max_length=15,
        default='192.168.0.33'
    )
    filled_data = models.IntegerField(
        default=0,
    )

    def check_ip(self):
        # TODO: Улучшить проверку ip
        ip = self.ip_address
        ip = list(ip.split('.'))
        correct = True
        for num in ip:
            if 0 < int(num) < 255:
                correct = False
                break
        if correct:
            self.save()
        else:
            self.ip_address = '192.168.0.1'
            self.save()
