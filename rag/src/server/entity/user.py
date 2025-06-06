from src.server.entity.common import Table, fields


class UserModel(Table):
    """
    用户模型类 > user table
    """

    username = fields.CharField(max_length=16, description="账号", unique=True)
    password = fields.CharField(max_length=128, description="密码")

    class Meta:
        table = "sys_user"
        table_description = "用户表"
