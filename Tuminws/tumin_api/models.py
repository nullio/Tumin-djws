# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IxConConfiguracion(models.Model):
    con_id = models.SmallIntegerField(primary_key=True)
    con_nombre = models.CharField(max_length=50)
    con_valor = models.SmallIntegerField(blank=True, null=True)
    con_valor_fecha = models.DateTimeField(blank=True, null=True)
    con_valor_texto = models.CharField(max_length=100, blank=True, null=True)
    con_habilitado = models.SmallIntegerField()
    con_descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ix_con_configuracion'


class NkltCmvCreditoMov(models.Model):
    cmv_id = models.AutoField(primary_key=True)
    cmv_cre = models.ForeignKey('NkltCreCredito', models.DO_NOTHING)
    cmv_monto = models.DecimalField(max_digits=10, decimal_places=0)
    cmv_fmovimiento = models.DateTimeField()
    cmv_tip_mov = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nklt_cmv_credito_mov'


class NkltCreCredito(models.Model):
    cre_id = models.AutoField(primary_key=True)
    cre_codigo = models.CharField(max_length=45)
    cre_cli = models.ForeignKey('OlshCliCliente', models.DO_NOTHING)
    cre_cue_id = models.IntegerField(blank=True, null=True)
    cre_ext_id = models.CharField(max_length=10, blank=True, null=True)
    cre_ext_sist = models.IntegerField(blank=True, null=True)
    cre_fon_id = models.IntegerField()
    cre_prd_id = models.IntegerField()
    cre_principal = models.DecimalField(max_digits=10, decimal_places=2)
    cre_frec_tipo = models.IntegerField()
    cre_frecuencia = models.IntegerField()
    cre_num_cuotas = models.IntegerField()
    cre_cuota_cada = models.IntegerField()
    cre_cuota_frectipo = models.IntegerField()
    cre_tasa_interes_per = models.DecimalField(max_digits=5, decimal_places=5)
    cre_interes_frectipo = models.IntegerField()
    cre_gracia_principal = models.IntegerField(blank=True, null=True)
    cre_gracia_interes = models.IntegerField(blank=True, null=True)
    cre_gracia_interes_cargo = models.IntegerField(blank=True, null=True)
    cre_gracia_atraso = models.IntegerField(blank=True, null=True)
    cre_carga_interes_desde = models.DateField(blank=True, null=True)
    cre_primer_desembolso = models.DateField(blank=True, null=True)
    cre_sol_id = models.IntegerField()
    cre_tipo_amort = models.IntegerField()
    cre_tipo_interes = models.IntegerField()
    cre_per_calc_int = models.IntegerField()
    cre_tolerancia_atraso = models.DecimalField(max_digits=5, decimal_places=2)
    cre_fecha_ini_recalc_int = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nklt_cre_credito'


class OlshCliCliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_per = models.ForeignKey('OlshPerPersona', models.DO_NOTHING)
    cli_fcrea = models.DateField()
    cli_fmod = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'olsh_cli_cliente'


class OlshCuuCuentaUsuario(models.Model):
    cuu_id = models.AutoField(primary_key=True)
    cuu_tip_ident = models.IntegerField()
    cuu_cusuario = models.CharField(max_length=50)
    cuu_cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING)
    cuu_pass_pin = models.CharField(max_length=300, blank=True, null=True)
    cuu_fvencimiento = models.DateTimeField(blank=True, null=True)
    cuu_fcreacion = models.DateTimeField()
    cuu_ucreacion = models.IntegerField(blank=True, null=True)
    cuu_fmodificaion = models.DateTimeField(blank=True, null=True)
    cuu_umodificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'olsh_cuu_cuenta_usuario'


class OlshGrcGrupoCliente(models.Model):
    grc_id = models.AutoField(primary_key=True)
    grc_grp = models.ForeignKey('OlshGrpGrupo', models.DO_NOTHING)
    grc_cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING)
    grc_fcreacion = models.DateTimeField()
    grc_ucreacion = models.IntegerField(blank=True, null=True)
    grc_fmodificacion = models.DateTimeField(blank=True, null=True)
    grc_umodificacion = models.IntegerField(blank=True, null=True)
    grc_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'olsh_grc_grupo_cliente'
        unique_together = (('grc_grp', 'grc_cli'),)


class OlshGrpGrupo(models.Model):
    grp_id = models.AutoField(primary_key=True)
    grp_nombre = models.CharField(max_length=50)
    grp_descripcion = models.CharField(max_length=200)
    grp_estado = models.IntegerField()
    grp_fcreacion = models.DateTimeField()
    grp_ucreacion = models.IntegerField()
    grp_fmodificacion = models.DateTimeField(blank=True, null=True)
    grp_umodificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'olsh_grp_grupo'


class OlshPerPersona(models.Model):
    per_id = models.AutoField(primary_key=True)
    per_codigo = models.CharField(max_length=45)
    per_1nombre = models.CharField(max_length=100)
    per_2nombre = models.CharField(max_length=100, blank=True, null=True)
    per_1apellido = models.CharField(max_length=100)
    per_2apellido = models.CharField(max_length=100, blank=True, null=True)
    per_fnacimiento = models.DateField()
    per_docnum = models.CharField(max_length=50)
    per_doctip = models.IntegerField()
    per_tipo = models.CharField(max_length=1)
    per_estado = models.IntegerField()
    per_fcreacion = models.DateTimeField()
    per_ucreacion = models.IntegerField()
    per_fmodificacion = models.DateTimeField(blank=True, null=True)
    per_umodificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'olsh_per_persona'
        unique_together = (('per_docnum', 'per_doctip'),)


class TumnCtsCatServicio(models.Model):
    cts_id = models.AutoField(primary_key=True)
    cts_nombre = models.CharField(max_length=45)
    cts_descripcion = models.CharField(max_length=100)
    cts_estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tumn_cts_cat_servicio'


class TumnCueCuenta(models.Model):
    cue_id = models.AutoField(primary_key=True)
    cue_numero = models.CharField(unique=True, max_length=45)
    cue_fapertura = models.DateField()
    cue_saldo = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    cue_ultimomov = models.DateField(blank=True, null=True)
    cue_prd_id = models.IntegerField(blank=True, null=True)
    cue_sol_fcrea = models.DateField(blank=True, null=True)
    cue_interes = models.CharField(max_length=45, blank=True, null=True)
    cue_int_comp_pertip = models.IntegerField(blank=True, null=True)
    cue_int_cap_pertip = models.IntegerField(blank=True, null=True)
    cue_int_calc_tip = models.IntegerField(blank=True, null=True)
    cue_int_calc_diastip = models.IntegerField(blank=True, null=True)
    cue_min_req = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cue_block_frec = models.IntegerField(blank=True, null=True)
    cue_block_frec_tip = models.IntegerField(blank=True, null=True)
    cue_sobregiro = models.IntegerField(blank=True, null=True)
    cue_sobregiro_lim = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cue_retencion = models.IntegerField(blank=True, null=True)
    cue_cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tumn_cue_cuenta'


class TumnFonFondo(models.Model):
    fon_id = models.IntegerField(primary_key=True)
    fon_cli_id = models.IntegerField(blank=True, null=True)
    fon_cue = models.ForeignKey(TumnCueCuenta, models.DO_NOTHING)
    fon_monto_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fon_monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fon_est_id = models.CharField(max_length=45, blank=True, null=True)
    fon_prd_id = models.IntegerField(blank=True, null=True)
    cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tumn_fon_fondo'


class TumnFrecFrecuenciaT(models.Model):
    frec_id = models.IntegerField(primary_key=True)
    frec_descripcion = models.CharField(max_length=50, blank=True, null=True)
    frec_numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tumn_frec_frecuencia_t'


class TumnMovMovimiento(models.Model):
    mov_id = models.AutoField(primary_key=True)
    mov_cue = models.ForeignKey(TumnCueCuenta, models.DO_NOTHING)
    mov_monto = models.DecimalField(max_digits=5, decimal_places=2)
    mov_deb_cred = models.SmallIntegerField()
    mov_fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'tumn_mov_movimiento'


class TumnSclServicioCliente(models.Model):
    scl_id = models.AutoField(primary_key=True)
    scl_ser_id = models.IntegerField()
    scl_cli_id = models.IntegerField()
    scl_finicio = models.DateField()
    scl_ffin = models.DateField(blank=True, null=True)
    scl_param1 = models.CharField(max_length=45)
    scl_id_listaval = models.IntegerField(blank=True, null=True)
    cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING)
    ser = models.ForeignKey('TumnSerServicio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tumn_scl_servicio_cliente'


class TumnSerServicio(models.Model):
    ser_id = models.AutoField(primary_key=True)
    ser_cts_id = models.IntegerField()
    ser_nombre = models.CharField(max_length=100)
    ser_descripcion = models.CharField(max_length=100)
    ser_estado = models.CharField(max_length=1)
    ser_metodo_validacion = models.CharField(max_length=100, blank=True, null=True)
    ser_metodo_ejecucion = models.CharField(max_length=100, blank=True, null=True)
    ser_nombre_lista_param = models.CharField(max_length=45, blank=True, null=True)
    ser_finicio = models.DateField()
    ser_ffin = models.DateField(blank=True, null=True)
    cts = models.ForeignKey(TumnCtsCatServicio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tumn_ser_servicio'


class TumnSimSmsIn(models.Model):
    sim_id = models.IntegerField(primary_key=True)
    sim_telefono = models.CharField(max_length=25)
    sim_fecha = models.DateTimeField()
    sim_raw_sms = models.CharField(max_length=200)
    sim_estado = models.CharField(max_length=1, blank=True, null=True)
    sim_tipo_tx = models.IntegerField(blank=True, null=True)
    sim_tx_id = models.IntegerField(blank=True, null=True)
    sim_sou_id = models.IntegerField(blank=True, null=True)
    sim_cli_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tumn_sim_sms_in'


class TumnTerTercero(models.Model):
    ter_id = models.AutoField(primary_key=True)
    ter_cli_id = models.IntegerField()
    ter_cue_id_dest = models.ForeignKey(TumnCueCuenta, models.DO_NOTHING, db_column='ter_cue_id_dest')
    ter_fcrea = models.DateField()
    ter_descripcion = models.CharField(max_length=100)
    ter_ffin = models.DateField(blank=True, null=True)
    ter_estado = models.CharField(max_length=1, blank=True, null=True)
    cli = models.ForeignKey(OlshCliCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tumn_ter_tercero'


class TumnTrcTransferenciaCue(models.Model):
    trc_id = models.AutoField(primary_key=True)
    trc_cli_id = models.IntegerField()
    trc_fecha = models.DateTimeField()
    trc_monto = models.DecimalField(max_digits=10, decimal_places=2)
    trc_cue = models.ForeignKey(TumnCueCuenta, models.DO_NOTHING, related_name='trc_cue_id')
    trc_cue_id_des = models.ForeignKey(TumnCueCuenta, models.DO_NOTHING, db_column='trc_cue_id_des')
    trc_mov = models.ForeignKey(TumnMovMovimiento, models.DO_NOTHING, related_name='trc_mov_id')
    trc_mov_id_dest = models.ForeignKey(TumnMovMovimiento, models.DO_NOTHING, db_column='trc_mov_id_dest')

    class Meta:
        managed = False
        db_table = 'tumn_trc_transferencia_cue'



####################################################
