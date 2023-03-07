# DICOM Tutorial

# DICOM Basics



# Loading a DICOM Dataset

## What is it? Series, Study,Image,...

## Using Python

```{Python}
from os import listdir
from pydicom import dcmread
from pydicom.fileset import FileSet

ds = []
path = 'example-dicom-structural/dicoms'

for filename in listdir(path):
    with dcmread(f"{path}{filename}") as f:
        ds.append(f)
```

## Loading the first object

```{python}

dir(dicom_list[0])

# Pick a field to list


dicom_list[0].PatientName
'Jane Doe'

dicom_list[0].PatientID
'02'


```

## Let's see all of the data :-)


