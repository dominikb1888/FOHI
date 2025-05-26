{ pkgs ? import <nixpkgs> {} }:

let
 pythonEnv = with pkgs.python311Packages; [
    # Data Science Basics
    ipython
    jupyterlab
    matplotlib
    numpy
    pandas

    # Database Tools
    # sqlalchemy
    # alembic
    # neo4j

   fastapi
   uvicorn
   pytest
   pillow

    # # Custom Derivations
    # ( buildPythonPackage rec {
    #   pname = "fastapi-sqlmodel-crud";
    #   version = "0.2.0";
    #   src = fetchPypi {
    #     inherit pname version;
    #     sha256 = "307b20eaf92ad767473b7f2998d34e6efbf775679dced4b5092cb03704efcf34";
    #   };
    #   doCheck = false;
    #   propagatedBuildInputs = [
    #     fastapi
    #   ];
    # })
    # ( buildPythonPackage rec {
    #   pname = "sqlmodel";
    #   version = "0.0.8";
    #   src = fetchPypi {
    #     inherit pname version;
    #     sha256 = "3371b4d1ad59d2ffd0c530582c2140b6c06b090b32af9b9c6412986d7b117036";
    #   };
    #   doCheck = false;
    #   propagatedBuildInputs = [
    #     sqlalchemy2-stubs
    #     pydantic
    #     sqlalchemy
    #     setuptools
    #   ];
    # })
    # ( buildPythonPackage rec {
    #   pname = "rdftools";
    #   version = "0.2.0a";
    #   src = fetchPypi {
    #     inherit pname version;
    #     sha256 = "0c398154c86de1e29fe3916dd26397ebbd7101c05672459b13124e6bc4e674b1";
    #   };
    #   doCheck = false;
    #   propagatedBuildInputs = [
    #     python-i18n
    #     rdflib
    #     pyyaml
    #   ]; })
    # ( buildPythonPackage rec {
    #   pname = "wfdb";
    #   version = "4.1.2";
    #   src = fetchPypi {
    #     inherit pname version;
    #     sha256 = "6acef3ab2759f60cf911a57d9e5214ea15bd17b5ad4b3c66e4a57a7690e16024";
    #   };
    #   doCheck = false;
    #   propagatedBuildInputs = [
    #     pydantic
    #     setuptools
    #   ];
    #   # Disable pytest-runner if it tries to use it
    # nativeBuildInputs = [ ];
    # installCheckPhase = ''
    #   echo "Skipping tests as they require pytest-runner."
    # '';
    #
    # # Use pipInstallHook to manage dependencies
    # buildInputs = [ pipInstallHook ];
    # })
    #
    #  ( buildPythonPackage rec {
    #   pname = "heartpy";
    #   version = "1.2.7";
    #   src = fetchPypi {
    #     inherit pname version;
    #     sha256 = "01f154f330b7d221f79b7378fb6519e3647573c4274627f29f99bb569d74491e";
    #   };
    #   doCheck = false;
    #   propagatedBuildInputs = [
    #     pydantic
    #     setuptools
    #   ];
    #   # Disable pytest-runner if it tries to use it
    # nativeBuildInputs = [ ];
    # installCheckPhase = ''
    #   echo "Skipping tests as they require pytest-runner."
    # '';
    #
    # # Use pipInstallHook to manage dependencies
    # buildInputs = [ pipInstallHook ];
    # })
    #
    ( buildPythonPackage rec {
      pname = "fhir.resources";
      version = "7.1.0";
      src = fetchPypi {
        inherit pname version;
        sha256 = "fae2d43c03dacf85a9f9fbce3b62148f3166fe297471cd43b74d91abbf69f818";
      };
      doCheck = false;
      propagatedBuildInputs = [
        pydantic
        setuptools
      ];
    # Disable pytest-runner if it tries to use it
    nativeBuildInputs = [ ];
    installCheckPhase = ''
      echo "Skipping tests as they require pytest-runner."
     '';

    # Use pipInstallHook to manage dependencies
    buildInputs = [ pipInstallHook ];
    })
  ];
in pkgs.mkShell {
  buildInputs = with pkgs; [
    pythonEnv
    # redis
    # neo4j
    # docker
    # postgresql
    # keep this line if you use bash
    pkgs.bashInteractive
    jdk
  ];
}
