# Generated by Django 4.2 on 2023-04-27 11:01

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0012_alter_user_first_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="Budget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("budget_name", models.CharField(max_length=40)),
            ],
            options={
                "verbose_name": "Presupuesto",
                "verbose_name_plural": "Presupuestos",
            },
        ),
        migrations.CreateModel(
            name="BudgetDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.DateField(auto_now_add=True)),
                ("total", models.IntegerField()),
            ],
            options={
                "verbose_name": "Detalle elemento prestamo",
                "verbose_name_plural": "Detalles Elementos Prestamos",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("año", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Element",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(blank=True, null=True)),
                ("stock", models.IntegerField()),
                ("price_usd", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(blank=True, upload_to="img-prod/")),
                ("ecommerce", models.BooleanField()),
            ],
            options={"verbose_name": "Elemento", "verbose_name_plural": "Elementos"},
        ),
        migrations.CreateModel(
            name="Laboratory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("laboratory", models.CharField(max_length=40)),
            ],
            options={
                "verbose_name": "Laboratorio",
                "verbose_name_plural": "Laboratorios",
            },
        ),
        migrations.CreateModel(
            name="Specialty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("specialty", models.CharField(max_length=40)),
            ],
            options={
                "verbose_name": "Especialidad",
                "verbose_name_plural": "Especialidades",
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={"verbose_name": "Estado", "verbose_name_plural": "Estados"},
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.course",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CustomUser",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "speciality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.specialty",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CustomUser",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subcategory", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "SubCategoria",
                "verbose_name_plural": "SubCategorias",
            },
        ),
        migrations.CreateModel(
            name="PurchaseLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchase_location", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True, null=True)),
                ("contact", models.CharField(max_length=40)),
                (
                    "elementos",
                    models.ManyToManyField(
                        related_name="lugares_de_compra", to="ElectroStockApp.element"
                    ),
                ),
            ],
            options={
                "verbose_name": "Lugar de compra",
                "verbose_name_plural": "Lugares de compra",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=40)),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.laboratory",
                    ),
                ),
            ],
            options={"verbose_name": "Ubicacion", "verbose_name_plural": "Ubicaciones"},
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_in", models.DateField()),
                ("date_return", models.DateField(blank=True, null=True)),
                ("observations", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.status",
                    ),
                ),
            ],
            options={"verbose_name": "Prestamo", "verbose_name_plural": "Prestamos"},
        ),
        migrations.AddField(
            model_name="laboratory",
            name="specialty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.specialty",
            ),
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("minimum_stock", models.IntegerField()),
                (
                    "elemento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.element",
                    ),
                ),
            ],
            options={
                "verbose_name": "Inventario",
                "verbose_name_plural": "Inventarios",
            },
        ),
        migrations.CreateModel(
            name="HistoryLoan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.loan",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Historial Prestamos Estados",
                "verbose_name_plural": "Historial Prestamos Estados",
            },
        ),
        migrations.CreateModel(
            name="HistoryInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("date", models.DateField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.inventory",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.location",
                    ),
                ),
            ],
            options={
                "verbose_name": "Historial Iventario Ubicacion",
                "verbose_name_plural": "Historial Iventario Ubicacion",
            },
        ),
        migrations.AddField(
            model_name="element",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.subcategory",
            ),
        ),
        migrations.CreateModel(
            name="Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("elective_cycle", models.DateField()),
                (
                    "budget",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.budget",
                    ),
                ),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.inventory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Detalles Presupuesto Inventario",
                "verbose_name_plural": "Detalles Presupuesto Inventario",
            },
        ),
        migrations.CreateModel(
            name="Destination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("destination", models.CharField(max_length=40)),
                ("allocated_budget", models.IntegerField()),
                (
                    "budget",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.budget",
                    ),
                ),
            ],
            options={"verbose_name": "Destino", "verbose_name_plural": "Destinos"},
        ),
        migrations.AddField(
            model_name="course",
            name="specialty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.specialty",
            ),
        ),
        migrations.AddField(
            model_name="budget",
            name="specialty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.specialty",
            ),
        ),
    ]
