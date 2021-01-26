# Generated by Django 2.2.4 on 2021-01-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0108_auto_20210114_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='binance_payout_address',
            field=models.CharField(blank=True, default='0x0', help_text='The binance wallet address where subscription funds will be sent.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='checkout_type',
            field=models.CharField(blank=True, choices=[('eth_std', 'eth_std'), ('eth_zksync', 'eth_zksync'), ('zcash_std', 'zcash_std'), ('celo_std', 'celo_std'), ('zil_std', 'zil_std'), ('polkadot_std', 'polkadot_std'), ('harmony_std', 'harmony_std'), ('binance_std', 'binance_std')], help_text='The checkout method used while making the contribution', max_length=30, null=True),
        ),
    ]
