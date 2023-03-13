{ pkgs ? import <nixpkgs> {} }:

let
 pythonEnv = with pkgs.python310Packages; [
    # Data Science Basics
    ipython
    jupyter
    pandas
    numpy
    matplotlib


    # Database Tools
    sqlalchemy
    neo4j

    # Data Query tools
    # pm4py
    # gnuhealth
   # Testing and CLI

    #DICOM
    pydicom

    garminconnect
   # fhir tools
   # fhir.resources
   # fhirclient
   # orjson
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pytest

    # CLI
    rich

    # Custom Derivations
    ( buildPythonPackage rec {
      pname = "fastapi-sqlmodel-crud";
      version = "0.2.0";
      src = fetchPypi {
        inherit pname version;
        sha256 = "307b20eaf92ad767473b7f2998d34e6efbf775679dced4b5092cb03704efcf34";
      };
      doCheck = false;
      propagatedBuildInputs = [
        fastapi
      ];
    })
    ( buildPythonPackage rec {
      pname = "sqlmodel";
      version = "0.0.8";
      src = fetchPypi {
        inherit pname version;
        sha256 = "3371b4d1ad59d2ffd0c530582c2140b6c06b090b32af9b9c6412986d7b117036";
      };
      doCheck = false;
      propagatedBuildInputs = [
        sqlalchemy2-stubs
        pydantic
        sqlalchemy
        setuptools
      ];
    })
    ( buildPythonPackage rec {
      pname = "rdftools";
      version = "0.2.0a";
      src = fetchPypi {
        inherit pname version;
        sha256 = "0c398154c86de1e29fe3916dd26397ebbd7101c05672459b13124e6bc4e674b1";
      };
      doCheck = false;
      propagatedBuildInputs = [
        python-i18n
        rdflib
        pyyaml
      ]; })
    ( buildPythonPackage rec {
      pname = "fhir.resources";
      version = "6.5.0";
      src = fetchPypi {
        inherit pname version;
        sha256 = "1d02ff2547e5b6323543c8ce9916e0c9e5536847b3b2171acb1f51a86efba16e";
      };
      doCheck = false;
      propagatedBuildInputs = [
        pydantic
        setuptools
      ];
    })
  ];
in pkgs.mkShell {
  buildInputs = with pkgs; [
    pythonEnv
    redis
    neo4j
    docker
    postgresql
    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
