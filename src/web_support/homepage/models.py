from django.db import models

# Create your models here.
    
class PhanQuyen(models.Model):
    MaPQ = models.CharField(max_length=10, primary_key=True)
    TenPQ = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Phân Quyền'
        verbose_name_plural = 'Phân Quyền'

    def _str_(self):
        return self.MaPQ
    
class Admin(models.Model):
    MaAD = models.CharField(max_length=10, primary_key=True)
    TaiKhoanAD = models.CharField(max_length=50)
    MatKhauAD = models.CharField(max_length=50)
    phanquyen = models.ForeignKey(PhanQuyen, on_delete= models.CASCADE, related_name = 'admins')

    class Meta:
        verbose_name = 'Quản Trị'
        verbose_name_plural = 'Quản Trị'

    def _str_(self):
        return self.MaAD