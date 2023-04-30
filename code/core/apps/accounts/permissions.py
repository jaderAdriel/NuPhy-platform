from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Usuario

# Obtém o content_type para o model Usuario
content_type = ContentType.objects.get_for_model(Usuario)



def set_permissions(user):
    
    tipo = user.tipo

    grupo_nome = {
        "A": "Administrador",
        "C": "Cliente",
        "P": "Profissional",
    }.get(tipo, "default")

    grupo, _ = Group.objects.get_or_create(name=grupo_nome)

    nome_perm = grupo_nome.replace(" ", "_").upper()

    try:
        permission, _ = Permission.objects.get_or_create(
            codename=grupo_nome,
            name=nome_perm,
            content_type=content_type,
        )
    except Exception as e:
        raise Exception(f"Erro ao criar/recuperar permissão {nome_perm}: {e}")

    # Adiciona a permissão ao grupo
    try:
        grupo.permissions.add(permission)
    except Exception as e:
        raise Exception(f"Erro ao adicionar permissão {nome_perm} ao grupo {grupo_nome}: {e}")

    # Adiciona o usuário ao grupo
    try:
        user.groups.add(grupo)
    except Exception as e:
        raise Exception(f"Erro ao adicionar usuário {user.nome} ao grupo {grupo_nome}: {e}")

    return user