from django.db import models
import agent.models
# Create your models here.
class Balance(models.Model):
    account_id = models.CharField(max_length=250,unique=True)
    agent_user_id = models.ForeignKey("agent.Agent", on_delete=models.CASCADE)
    btc_address = models.TextField(max_length=300,null=True,blank=True)
    agent_transaction_id = models.CharField(max_length=250,unique=True)
    sending_amount = models.IntegerField(default=0)  
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=0)
    def __str__(self):
        return self.account_id 
class TransferBalance(models.Model):
    profile_id = models.ForeignKey("user_profile.Profile", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0) 
    agents_id = models.ForeignKey("agent.Agent", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=0)
    def __str__(self):
        return self.profile_id
class BalanceWithdraw(models.Model):

    withdraw_type = models.CharField(max_length=200, default='' )
    payment_method = models.CharField(max_length=250,default='')
    Marchant_Method = models.CharField(max_length=250,default='')
    transaction_pin = models.CharField(max_length=250,default='')
    
    agents_user_id = models.ForeignKey("agent.Agent", on_delete=models.CASCADE)
    transaction_amount = models.IntegerField(default=0) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=0)
    def __str__(self):
        return self.agent_id

class BalanceExchange(models.Model):
    sender_id = models.ForeignKey("user_profile.Profile", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0) 
    receiver_id = models.ForeignKey("agent.Agent", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=0)

    def __str__(self):
        return self.sender_id