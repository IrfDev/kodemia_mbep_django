# Relationship fields:

There are some keys you can use in the python ORM:

1. 1-N = ForeignKey 
The foreign key needs to be assing to N
1. N-N = Many to many field
The f-key is being assigned hierarchically
The lowest class in the hierarchy will be the foreign key

1. 1-1 = OneToOneField


## ForeignKey and ManyToMany
The foreign key is the N

``````python
models.ForeignKey(Model,on_delete,related_name)
``````

### on_delete
models.CASCADE
1. Cascade: Delete all the relationships
   1. This is not recommended under any circunstance
2. Protect: If the entity is related, it won't delete other relationships
   1. Most used
   2. Is hard to use on many to many relationships
3. Restrict: If there is no relationship it'll let you delete the information

### related_name
How you're going to know the relationship name from the primary_key

EG: Class A. Class B. Row B.b=A.a If the related_name is 'bs'. Then you can call A.bs to bring all the B related to A



# Tweaking the terminal with iPython

