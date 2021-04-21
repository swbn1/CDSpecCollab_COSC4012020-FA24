from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.validators import FileExtensionValidator

#from cd_spec_viewer_web.users import User
# Create your models here.

class SpecRun(models.Model):
    #upload_user = models.ForeignKey("Upload User", User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField("Upload Date", auto_now_add=True)
    run_date = models.DateTimeField("Run Date")
    run_user = models.CharField("Run by:", max_length=64)
    run_title = models.CharField("Title", max_length=64)
    run_description = models.TextField("Description (Character Limit: 2000)", max_length=2000)
    data = JSONField("Raw Data")
    data_points = models.IntegerField("Data Points")
    visible_student = models.BooleanField("Visible to Students", default=False)
    visible_public = models.BooleanField("Visible to Public", default=False)
    source_file = models.FileField(upload_to='cdspecruns', validators=[FileExtensionValidator(allowed_extensions=['csv'])])

    #Calculation variables
    protein_concentration = models.DecimalField("Protein Concentration", max_digits=50, decimal_places=20)
    pathlength = models.DecimalField("Curvette Pathlength", max_digits=50, decimal_places=20)
    number_of_amino_acids = models.IntegerField("Number of amino acids")
    
    #Header names for x/y units
    x_units = models.CharField("XUNITS", null=True, max_length=64)
    y_units = models.CharField("YUNITS", null=True, max_length=64)
    y2_units = models.CharField("Y2UNITS", null=True, max_length=64)
    y3_units = models.CharField("Y3UNITS", null=True, max_length=64)

    def __str__(self):
        return self.run_title + "[" + str(self.pk) + "]"
    
    #class Meta:
    #     app_label = 'cd_spec_viewer_web.cdspec'
