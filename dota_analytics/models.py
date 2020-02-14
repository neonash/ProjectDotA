from django.db import models


class TestData(models.Model):
    """Test Data Model."""

    match_id_hash = models.CharField(primary_key=True, max_length=40)
    r1_hero_id = models.FloatField()
    r1_gold = models.FloatField()
    r1_xp = models.FloatField()
    r1_health = models.FloatField()
    r1_level = models.FloatField()
    r2_hero_id = models.FloatField()
    r2_gold = models.FloatField()
    r2_xp = models.FloatField()
    r2_health = models.FloatField()
    r2_level = models.FloatField()
    r3_hero_id = models.FloatField()
    r3_gold = models.FloatField()
    r3_xp = models.FloatField()
    r3_health = models.FloatField()
    r3_level = models.FloatField()
    r4_hero_id = models.FloatField()
    r4_gold = models.FloatField()
    r4_xp = models.FloatField()
    r4_health = models.FloatField()
    r4_level = models.FloatField()
    r5_hero_id = models.FloatField()
    r5_gold = models.FloatField()
    r5_xp = models.FloatField()
    r5_health = models.FloatField()
    r5_level = models.FloatField()
    d1_hero_id = models.FloatField()
    d1_gold = models.FloatField()
    d1_xp = models.FloatField()
    d1_health = models.FloatField()
    d1_level = models.FloatField()
    d2_hero_id = models.FloatField()
    d2_gold = models.FloatField()
    d2_xp = models.FloatField()
    d2_health = models.FloatField()
    d2_level = models.FloatField()
    d3_hero_id = models.FloatField()
    d3_gold = models.FloatField()
    d3_xp = models.FloatField()
    d3_health = models.FloatField()
    d3_level = models.FloatField()
    d4_hero_id = models.FloatField()
    d4_gold = models.FloatField()
    d4_xp = models.FloatField()
    d4_health = models.FloatField()
    d4_level = models.FloatField()
    d5_hero_id = models.FloatField()
    d5_gold = models.FloatField()
    d5_xp = models.FloatField()
    d5_health = models.FloatField()
    d5_level = models.FloatField()

    class Meta:
        db_table = 'test_data'


class TrainData(models.Model):
    """Train Data Model."""

    match_id_hash = models.CharField(primary_key=True, max_length=40)
    r1_hero_id = models.FloatField()
    r1_gold = models.FloatField()
    r1_xp = models.FloatField()
    r1_health = models.FloatField()
    r1_level = models.FloatField()
    r2_hero_id = models.FloatField()
    r2_gold = models.FloatField()
    r2_xp = models.FloatField()
    r2_health = models.FloatField()
    r2_level = models.FloatField()
    r3_hero_id = models.FloatField()
    r3_gold = models.FloatField()
    r3_xp = models.FloatField()
    r3_health = models.FloatField()
    r3_level = models.FloatField()
    r4_hero_id = models.FloatField()
    r4_gold = models.FloatField()
    r4_xp = models.FloatField()
    r4_health = models.FloatField()
    r4_level = models.FloatField()
    r5_hero_id = models.FloatField()
    r5_gold = models.FloatField()
    r5_xp = models.FloatField()
    r5_health = models.FloatField()
    r5_level = models.FloatField()
    d1_hero_id = models.FloatField()
    d1_gold = models.FloatField()
    d1_xp = models.FloatField()
    d1_health = models.FloatField()
    d1_level = models.FloatField()
    d2_hero_id = models.FloatField()
    d2_gold = models.FloatField()
    d2_xp = models.FloatField()
    d2_health = models.FloatField()
    d2_level = models.FloatField()
    d3_hero_id = models.FloatField()
    d3_gold = models.FloatField()
    d3_xp = models.FloatField()
    d3_health = models.FloatField()
    d3_level = models.FloatField()
    d4_hero_id = models.FloatField()
    d4_gold = models.FloatField()
    d4_xp = models.FloatField()
    d4_health = models.FloatField()
    d4_level = models.FloatField()
    d5_hero_id = models.FloatField()
    d5_gold = models.FloatField()
    d5_xp = models.FloatField()
    d5_health = models.FloatField()
    d5_level = models.FloatField()

    class Meta:
        db_table = 'train_data'


class TrainTargets(models.Model):
    """Train Target Model."""

    match_id_hash = models.CharField(primary_key=True, max_length=40)
    radiant_win = models.IntegerField()

    class Meta:

        db_table = 'train_targets'
