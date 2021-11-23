from django.db import models
from polymorphic.models import PolymorphicModel

# Bug Description:
# Consider the following example. A simple inheritance where the child model has a M2M relation to some other model.
# I have altered migration 0001 manually to mimic the create behaviour prior to Django 3.2 (AutoField instead of BigAuto for PK)
# The second migration correctly picks up that this needs to be changed.
# 
# The resulting sql query for 0002 is:
# --
# -- Alter field id on basemodel
# --
# ALTER TABLE `sample_derivedmodel` DROP FOREIGN KEY `sample_derivedmodel_basemodel_ptr_id_a3110b27_fk_sample_ba`;
# ALTER TABLE `sample_basemodel` MODIFY `id` bigint AUTO_INCREMENT NOT NULL;
# ALTER TABLE `sample_derivedmodel` MODIFY `basemodel_ptr_id` bigint NOT NULL; <------------- FAILS
# ALTER TABLE `sample_derivedmodel` ADD CONSTRAINT `sample_derivedmodel_basemodel_ptr_id_a3110b27_fk` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `sample_basemodel` (`id`);
# --
# -- Alter field id on somemodel
# --
# ALTER TABLE `sample_derivedmodel_relation` DROP FOREIGN KEY `sample_derivedmodel__somemodel_id_31aa39d5_fk_sample_so`;
# ALTER TABLE `sample_somemodel` MODIFY `id` bigint AUTO_INCREMENT NOT NULL;
# ALTER TABLE `sample_derivedmodel_relation` MODIFY `somemodel_id` bigint NOT NULL;
#
# The marked line fails with the following message:
# Error Code: 3780. Referencing column 'derivedmodel_id' and referenced column 'basemodel_ptr_id' in foreign key constraint 'sample_derivedmodel__derivedmodel_id_9f9fbb1f_fk_sample_de' are incompatible.
#
# And this FK constraint is the one in the sample_derivedmodel_relation, I suspect because the relation table is not modified to use bigints for the foreign ids.
#
#



class SomeModel(models.Model):
    some_field = models.IntegerField(default=5)


class BaseModel(models.Model):
    some_other_base_field = models.IntegerField(default=5)

    class Meta:
        abstract = False

class DerivedModel(BaseModel):
    relation = models.ManyToManyField(SomeModel, related_name='+')


