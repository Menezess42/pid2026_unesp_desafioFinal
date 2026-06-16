{ pkgs, lib, config, inputs, ... }:

{
    packages = [
        pkgs.pyright
    ];

    languages.python = {
        enable = true;
        package = pkgs.python313.withPackages (p: with p; [
            kagglehub
            numpy
            scipy
            pandas
            matplotlib
            scikit-image
            pytest
            ipykernel
            ipython
            kaggle
            plotly
            nbformat
            (p.opencv4.override { enableGtk3 = true; enableFfmpeg = true; })
        ]);
        venv.enable = true;
    };

    enterShell = ''
    echo "$(python --version) — venv ativo"
    '';
}
