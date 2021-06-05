from django.db import models
from hashlib import sha256
import json
import time

# Create your models here.


from django.db import models

class b(models.Model):
    text= models.CharField(max_length=500,null=True)

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # difficulty de l'algorithme PoW
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []  # transactions non encore validées
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):

        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):

        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):

        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index















class Conseille(models.Model):
    nom=models.CharField(max_length=50, null= True)
    prenom= models.CharField(max_length=50, null=True)
    cni= models.CharField(max_length=50, null=True, unique= True)
    phone = models.CharField(max_length=50, null=True, unique=True)
    address= models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.cni
    class meta:
        db_table= ['Conseiller']

class Use(models.Model):
    TYPE=(
        ('Particulier', 'Particulier'),
        ('Etudiant', 'Etudiant')
    )
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    cne = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    phone = models.CharField(max_length=50, null=True)
    solde = models.FloatField(null=True)
    age = models.IntegerField()
    adress= models.CharField(max_length=50, null=True)
    dotationE= models.CharField(max_length=50, null=True, default="Bloquer")
    dotationT= models.CharField(max_length=50, null=True, default="Bloquer")
    dotationT= models.CharField(max_length=50, null=True, default="Bloquer")
    Adate= models.CharField(max_length=50, null=True)
    cheque = models.CharField(max_length=50, null=True, default="non")
    idC = models.ForeignKey(Conseille,  on_delete=models.CASCADE,related_name="idC",null="True")
    def __str__(self):
        return self.cne
    class meta:
        db_table= ['User']
        unique_together = ('cne', 'phone')

class Reclamation(models.Model):
    text=models.CharField(max_length=500, null=True)
    Adate=models.CharField(max_length=500, null=True)
    idU = models.ForeignKey(Use,  on_delete=models.CASCADE,related_name="idU",null="True")