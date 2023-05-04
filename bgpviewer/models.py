from django.db import models


class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    local_timezone =  models.CharField(max_length=200, null=True,)
    site = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    path = models.IntegerField()
    bgp_as_path = models.CharField(max_length=200)
    bgp_as_path_length = models.IntegerField()
    origin= models.CharField(max_length=200)
    best_path_selection_reason = models.CharField(max_length=200)
    metric = models.CharField(max_length=200)
    localpref = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    valid = models.CharField(max_length=200)
    last_update = models.CharField(max_length=300)
    next_hop = models.CharField(max_length=500)
    next_hope_accessible = models.CharField(max_length=200)
    next_hope_metric = models.CharField(max_length=200)
    next_hope_used = models.CharField(max_length=200)
    next_hope_peerId = models.CharField(max_length=200)
    next_hope_routerId = models.CharField(max_length=200)
    next_hope_hostname = models.CharField(max_length=200)
    next_hope_peer_type = models.CharField(max_length=200)
    

    def __str__(self):
        return(f"{self.site} {self.prefix}")
