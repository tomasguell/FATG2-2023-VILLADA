# Generated by Django 4.2 on 2023-08-17 20:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Box",
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
                ("minimumStock", models.IntegerField(verbose_name="Stock Minimo")),
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Box",
                "verbose_name_plural": "Boxes",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descripcion"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_categories",
                        to="ElectroStockApp.category",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
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
                ("grade", models.IntegerField(verbose_name="Año")),
            ],
            options={
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
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
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Laboratorio",
                "verbose_name_plural": "Laboratorios",
            },
        ),
        migrations.CreateModel(
            name="Speciality",
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
                ("name", models.CharField(max_length=40, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Especialidad",
                "verbose_name_plural": "Especialidades",
            },
        ),
        migrations.CreateModel(
            name="TokenSignup",
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
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Token",
                "verbose_name_plural": "Tokens",
            },
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
                    "specialties",
                    models.ManyToManyField(blank=True, to="ElectroStockApp.speciality"),
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
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Log",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AP", "Aprobado"),
                            ("DAP", "Desaprobado"),
                            ("CAR", "Carrito"),
                            ("PED", "Pedido"),
                            ("COM", "Comprado"),
                            ("DEV", "Devuelto"),
                            ("VEN", "Vencido"),
                            ("TAR", "Tardio"),
                            ("ROT", "Roto"),
                        ],
                        default="COM",
                        max_length=30,
                        verbose_name="Estado",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="Cantidad")),
                (
                    "observation",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Observaciones",
                    ),
                ),
                (
                    "dateIn",
                    models.DateField(auto_now=True, verbose_name="Fecha de ingreso"),
                ),
                (
                    "dateOut",
                    models.DateTimeField(
                        blank=True,
                        help_text="No es necesario si se carga como comprado",
                        null=True,
                        verbose_name="Fecha de devolucion",
                    ),
                ),
                (
                    "borrower",
                    models.ForeignKey(
                        blank=True,
                        help_text="Si se ingresa como comprado poner nombre de tu usuario",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="borrowed_logs",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Prestador/Comprador",
                    ),
                ),
                (
                    "box",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.box",
                    ),
                ),
                (
                    "lender",
                    models.ForeignKey(
                        blank=True,
                        help_text="No es necesario si se carga como comprado",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lender_logs",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Prestatario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Prestamo y movimientos",
                "verbose_name_plural": "Prestamos y movimientos",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.laboratory",
                        verbose_name="Laboratorio",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ubicacion",
                "verbose_name_plural": "Ubicaciones",
            },
        ),
        migrations.AddField(
            model_name="laboratory",
            name="speciality",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.speciality",
                verbose_name="Especialidad",
            ),
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
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descripcion"),
                ),
                (
                    "price_usd",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Ingrese el precio en dolares",
                        max_digits=10,
                        null=True,
                        verbose_name="Precio",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="img-prod/", verbose_name="Foto"
                    ),
                ),
                (
                    "ecommerce",
                    models.BooleanField(default=True, verbose_name="Prestable"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ElectroStockApp.category",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Elemento",
                "verbose_name_plural": "Elementos",
            },
        ),
        migrations.AddField(
            model_name="box",
            name="element",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.element",
                verbose_name="Elemento",
            ),
        ),
        migrations.AddField(
            model_name="box",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ElectroStockApp.location",
                verbose_name="Ubicacion",
            ),
        ),
        migrations.AddField(
            model_name="box",
            name="responsable",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
