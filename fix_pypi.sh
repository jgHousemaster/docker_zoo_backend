#!/bin/bash



function config_pip() {
    pypi_source=$1

    if [[ ! -f ~/.pydistutils.cfg ]]; then
cat > ~/.pydistutils.cfg << EOF
[easy_install]
index-url=http://$pypi_source/pypi/simple/
EOF
    else
        sed -i "s#index-url.*#index-url=http://$pypi_source/pypi/simple/#" ~/.pydistutils.cfg
    fi

    if [[ ! -f ~/.pip/pip.conf ]]; then
    mkdir -p ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
index-url=http://$pypi_source/pypi/simple/

[install]
trusted-host=$pypi_source
EOF
    else
        sed -i "s#index-url.*#index-url=http://$pypi_source/pypi/simple/#" ~/.pip/pip.conf
        sed -i "s#trusted-host.*#trusted-host=$pypi_source#" ~/.pip/pip.conf
    fi
}

config_pip $1
